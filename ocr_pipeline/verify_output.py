# -*- coding: utf-8 -*-
"""verify_output.py — sanity checks + debug overlay for sandwich OCR pdfs."""
import argparse
import json
import hashlib
import sys
import pymupdf as fitz


def img_hashes(doc):
    h = {}
    for i in range(doc.page_count):
        for im in doc[i].get_images(full=True):
            info = doc.extract_image(im[0])
            h[f"p{i}"] = hashlib.md5(info["image"]).hexdigest()
    return h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--cache", required=True)
    ap.add_argument("--pages", default="")   # pages (1-based) for overlay debug
    args = ap.parse_args()

    src, out = fitz.open(args.src), fitz.open(args.out)
    assert src.page_count == out.page_count, "page count mismatch"

    hs, ho = img_hashes(src), img_hashes(out)
    diff = [k for k in hs if hs[k] != ho.get(k)]
    print(f"[1] image-stream identity: {len(hs)} pages compared, {len(diff)} differ"
          f"{' -> ' + str(diff[:8]) if diff else '  (byte-identical)'}")

    # pixel-level render comparison on sample pages
    import random
    random.seed(42)
    samples = random.sample(range(src.page_count), 5)
    pix_diff = []
    for i in samples:
        z = fitz.Matrix(0.5, 0.5)
        a = src[i].get_pixmap(matrix=z, colorspace=fitz.csGRAY, alpha=False).samples
        b = out[i].get_pixmap(matrix=z, colorspace=fitz.csGRAY, alpha=False).samples
        pix_diff.append(a == b)
    print(f"[2] rendered-pixel equality on {len(samples)} random pages: {sum(pix_diff)}/{len(pix_diff)} identical "
          f"(text layer is invisible so renders must match)")

    # round-trip: cached OCR strings must survive into output text extraction
    by_page = {}
    with open(args.cache, encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            by_page[rec["p"]] = rec
    bad, checked = [], 0
    for p, rec in by_page.items():
        want = "".join(l["t"] for l in sorted(rec["lines"], key=lambda l: min(pt[1] for pt in l["box"])))
        got = out[p].get_text("text").replace("\n", "")
        want_clean = "".join(want.split())
        got_clean = "".join(got.split())
        if not want_clean:
            continue
        checked += 1
        inter = sum(1 for ch in want_clean if ch in got_clean)  # rough containment
        ratio = inter / len(want_clean)
        if ratio < 0.95:
            bad.append((p, ratio))
    print(f"[3] round-trip on {checked} OCR'd pages: {checked - len(bad)} pass (>=95% char containment)"
          + (f"; FAIL pages: {bad[:10]}" if bad else ""))

    # overlay debug images
    if args.pages:
        for spec in args.pages.split(","):
            p1 = int(spec) - 1
            rec = by_page.get(p1)
            if not rec:
                print(f"p{p1+1}: no cache"); continue
            page = out[p1]
            zx, zy = rec["z"]
            pm = page.get_pixmap(matrix=fitz.Matrix(0.55 * zx / (zx), 0), alpha=False)  # placeholder
            pm = page.get_pixmap(matrix=fitz.Matrix(0.55, 0.55), colorspace=fitz.csRGB, alpha=False)
            import numpy as np
            from PIL import Image, ImageDraw
            img = Image.frombytes("RGB", (pm.width, pm.height), pm.samples)
            dr = ImageDraw.Draw(img, "RGBA")
            for l in rec["lines"]:
                xs = [pt[0] / zx * 0.55 for pt in l["box"]]
                ys = [pt[1] / zy * 0.55 for pt in l["box"]]
                dr.rectangle([min(xs), min(ys), max(xs), max(ys)], outline=(255, 0, 0, 160), width=2)
            name = f"overlay_p{p1+1}.png"
            img.save(name)
            print(f"[4] wrote {name}")
    print("verify done.")


if __name__ == "__main__":
    main()
