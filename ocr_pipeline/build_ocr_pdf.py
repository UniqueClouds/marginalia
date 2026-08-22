# -*- coding: utf-8 -*-
"""
build_ocr_pdf.py — sandwich-OCR pipeline that preserves original page images byte-for-byte.

Two phases:
  ocr    : render each page to grayscale (long side ~TARGET_PX), run RapidOCR,
           append results to a JSONL cache (resumable — done pages are skipped).
  apply  : reopen the ORIGINAL pdf, draw an invisible (render_mode=3) per-character
           text layer from the cache, save a new pdf. Image streams are never touched.

Usage:
  python build_ocr_pdf.py ocr   --pdf <src.pdf> --cache <cache.jsonl> [--pages 0-9,50]
  python build_ocr_pdf.py apply --pdf <src.pdf> --cache <cache.jsonl> --out <out.pdf>
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

import numpy as np

import pymupdf as fitz
from rapidocr_onnxruntime import RapidOCR

TARGET_LONG_SIDE = 2400          # px, OCR input raster long side (bilevel scans: try 3000)
MIN_SCORE = 0.35                 # drop lines below this confidence
ENGINE_KWARGS = {
    "Det.limit_type": "min",     # never downscale; small pages get upscaled to 736 min-side
    "Det.limit_side_len": 736,
    "Det.thresh": 0.25,          # default 0.3 — more sensitive pixel map
    "Det.box_thresh": 0.30,      # default 0.5 — keep fainter boxes
    "Global.text_score": MIN_SCORE,
}

PAGE_RANGE_RE = re.compile(r"^\d+$|^\d+-\d+$")

# space between two CJK chars in rec output is a model artifact -> strip at apply time
_CJK = r"\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef"
CJK_SPACE_RE = re.compile(rf"(?<=[{_CJK}])[ \t]+(?=[{_CJK}])")


def patch_session(device: str, threads: int | None):
    """Rebuild OrtInferSession.__init__: DirectML provider and/or capped CPU threads."""
    import onnxruntime as ort
    from rapidocr_onnxruntime.utils import OrtInferSession

    def __init__(self, config):
        sess_opt = ort.SessionOptions()
        sess_opt.log_severity_level = 4
        sess_opt.enable_cpu_mem_arena = False
        sess_opt.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        if threads:
            sess_opt.intra_op_num_threads = threads
            sess_opt.inter_op_num_threads = 1
        self._verify_model(config["model_path"])
        providers = {
            "dml": [("DmlExecutionProvider", {"device_id": 0}), "CPUExecutionProvider"],
            "cuda": [("CUDAExecutionProvider", {"device_id": 0}), "CPUExecutionProvider"],
            "cpu": ["CPUExecutionProvider"],
        }[device]
        self.session = ort.InferenceSession(config["model_path"], sess_options=sess_opt,
                                            providers=providers)

    OrtInferSession.__init__ = __init__


def parse_pages(spec: str, n: int):
    """Parse 1-based page spec ("5", "1-20", "2,3,50-60") -> sorted 0-based indices."""
    if not spec:
        return range(n)
    out = []
    for part in spec.split(","):
        part = part.strip()
        if PAGE_RANGE_RE.match(part):
            if "-" in part:
                a, b = part.split("-")
                out.extend(range(int(a), int(b) + 1))
            else:
                out.append(int(part))
        else:
            raise ValueError(f"bad page spec: {part}")
    return sorted(set(p - 1 for p in out if 1 <= p <= n))


def render_page(page: fitz.Page, long_side: int = TARGET_LONG_SIDE) -> tuple[np.ndarray, tuple[float, float]]:
    """Render page grayscale with long side ≈ long_side. Returns (BGR ndarray, (zx, zy))."""
    long_pt = max(page.rect.width, page.rect.height)
    z = long_side / long_pt
    pm = page.get_pixmap(matrix=fitz.Matrix(z, z), colorspace=fitz.csGRAY, alpha=False)
    arr = np.frombuffer(pm.samples, dtype=np.uint8).reshape(pm.height, pm.width)
    bgr = np.stack([arr] * 3, axis=-1)  # gray replicated; RapidOCR treats input as BGR
    return bgr, (z, z)


def char_width_weight(ch: str) -> float:
    o = ord(ch)
    if 0x4E00 <= o <= 0x9FFF or 0x3400 <= o <= 0x4DBF:      # CJK unified
        return 1.0
    if 0x3000 <= o <= 0x303F or 0xFF00 <= o <= 0xFFEF:      # CJK punct / fullwidth
        return 1.0
    if ch == " ":
        return 0.35
    if ch.isdigit() or ch.isalpha():
        return 0.55
    return 0.45


def sort_reading_order(lines):
    """Cluster detected blocks into visual rows (top-to-bottom), left-to-right within a row."""
    if len(lines) <= 1:
        return lines
    def geom(l):
        ys = [pt[1] for pt in l["box"]]; xs = [pt[0] for pt in l["box"]]
        return min(xs), min(ys), max(xs), max(ys)
    items = [(geom(l), l) for l in lines]
    heights = sorted(g[2] - g[1] + g[3] - g[1] for g, _ in items)
    med_h = max(heights[len(heights) // 2] / 2, 1e-6)
    items.sort(key=lambda t: ((t[0][1] + t[0][3]) / 2, t[0][0]))
    rows, cur, cur_y = [], [], None
    for g, l in items:
        cy = (g[1] + g[3]) / 2
        if cur_y is None or abs(cy - cur_y) <= med_h * 0.6:
            cur.append((g, l))
            cur_y = cy if cur_y is None else (cur_y * (len(cur) - 1) + cy) / len(cur)
        else:
            rows.append(cur); cur = [(g, l)]; cur_y = cy
    if cur:
        rows.append(cur)
    out = []
    for row in rows:
        out.extend(l for _, l in sorted(row, key=lambda t: t[0][0]))
    return out


def phase_ocr(args):
    patch_session(args.device, args.threads)
    engine = RapidOCR(**ENGINE_KWARGS)
    src = fitz.open(args.pdf)
    pages = parse_pages(args.pages, src.page_count)

    done = set()
    cache_path = Path(args.cache)
    if cache_path.exists():
        with cache_path.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    done.add(json.loads(line)["p"])
                except Exception:
                    pass
    todo = [p for p in pages if p not in done]
    print(f"pages total={src.page_count} requested={len(pages)} cached={len(done & set(pages))} todo={len(todo)}", flush=True)

    t0 = time.time()
    with cache_path.open("a", encoding="utf-8") as fout:
        for k, i in enumerate(todo):
            page = src[i]
            img, (zx, zy) = render_page(page, args.long_side)
            result, _elapse = engine(img)
            lines = []
            if result:
                for box, text, score in result:
                    score = float(score)
                    if score < MIN_SCORE or not text.strip():
                        continue
                    lines.append({"box": [[round(float(x), 2), round(float(y), 2)] for x, y in box],
                                  "t": text, "s": round(float(score), 4)})
            rec = {"p": i, "z": [zx, zy], "n": len(lines),
                   "mean_s": round(sum(l["s"] for l in lines) / len(lines), 4) if lines else 0.0,
                   "lines": lines}
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fout.flush()
            if (k + 1) % 10 == 0 or k == len(todo) - 1:
                rate = (k + 1) / (time.time() - t0)
                eta = (len(todo) - k - 1) / rate if rate > 0 else 0
                print(f"[{i+1}/{src.page_count}] done {k+1}/{len(todo)} "
                      f"lines={rec['n']} mean_score={rec['mean_s']:.3f} "
                      f"rate={rate:.2f}p/s eta={eta/60:.1f}min", flush=True)
    src.close()
    print("OCR phase complete.", flush=True)


def load_cache(cache_path: str) -> dict:
    by_page = {}
    with Path(cache_path).open("r", encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except Exception:
                continue
            by_page[rec["p"]] = rec  # last record wins (allows re-OCR by appending)
    return by_page


def write_text_layer(doc, by_page: dict) -> int:
    """Write invisible per-char text layer onto doc's pages from cache records."""
    font = fitz.Font("china-s")
    n_chars_total = 0
    for i in range(doc.page_count):
        rec = by_page.get(i)
        if not rec or not rec["lines"]:
            continue
        page = doc[i]
        zx, zy = rec["z"]
        tw = fitz.TextWriter(page.rect, color=(0, 0, 0))
        for line in sort_reading_order(rec["lines"]):
            xs = [pt[0] / zx for pt in line["box"]]
            ys = [pt[1] / zy for pt in line["box"]]
            left, right = min(xs), max(xs)
            top, bottom = min(ys), max(ys)
            h = bottom - top
            w = right - left
            text = CJK_SPACE_RE.sub("", line["t"])  # drop rec-internal spaces between CJK chars
            if h <= 0 or w <= 0 or not text:
                continue
            weights = [char_width_weight(c) for c in text]
            total_w = sum(weights)
            if total_w <= 0:
                continue
            # per-char fontsize == its allocated advance: glyph pitch then matches the
            # placed origins, so viewers don't infer spaces between characters
            baseline = top + h * 0.80
            x = left
            for ch, cw in zip(text, weights):
                adv = cw / total_w * w
                if not ch.isspace():
                    tw.append(fitz.Point(x, baseline), ch, font, max(adv, h * 0.4))
                    n_chars_total += 1
                x += adv
        tw.write_text(page, render_mode=3)  # invisible: selectable & copyable, not printed
    return n_chars_total


def phase_apply(args):
    src = fitz.open(args.pdf)
    by_page = load_cache(args.cache)

    missing = [i for i in range(src.page_count) if i not in by_page]
    if missing:
        print(f"WARNING: {len(missing)} pages missing from cache "
              f"(e.g. {missing[:10]}). They will get no text layer.", flush=True)

    n_chars_total = write_text_layer(src, by_page)
    out = Path(args.out)
    src.save(str(out), garbage=3, deflate=True)
    src.close()
    print(f"applied text layer: {n_chars_total} chars -> {out}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="phase", required=True)
    for name in ("ocr", "apply"):
        s = sub.add_parser(name)
        s.add_argument("--pdf", required=True)
        s.add_argument("--cache", required=True)
        if name == "ocr":
            s.add_argument("--pages", default="")
            s.add_argument("--device", default="cpu", choices=["cpu", "dml", "cuda"])
            s.add_argument("--threads", type=int, default=None,
                           help="cap ORT intra-op threads (CPU mode) so the machine stays usable")
            s.add_argument("--long-side", type=int, default=TARGET_LONG_SIDE)
        if name == "apply":
            s.add_argument("--out", required=True)
    args = ap.parse_args()
    if args.phase == "ocr":
        phase_ocr(args)
    else:
        phase_apply(args)


if __name__ == "__main__":
    main()
