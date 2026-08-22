# -*- coding: utf-8 -*-
"""
build_compressed.py — reading-optimized compressed variant of the sandwich-OCR pdf.

Per page routing:
  cover/photo (RGB source or high ink-ratio) -> original JPEG bytes passed through,
                                               or whitened gray JPEG q85
  already-bilevel source                     -> original bytes passed through
  normal text page                           -> flat-field whitening + Otsu binarize +
                                                speckle removal -> 1-bit PNG

Text layer is reused from the existing OCR cache (page geometry unchanged).
Usage:
  python build_compressed.py --pdf <src.pdf> --cache <cache.jsonl> --out <out.pdf>
                             [--pages 1-20]
"""
import argparse
import io
from pathlib import Path

import cv2
import numpy as np
import pymupdf as fitz
from PIL import Image

from build_ocr_pdf import load_cache, parse_pages, write_text_layer

INK_RATIO_PHOTO = 0.30     # >30% dark pixels => treat page as photo/halftone
BG_SIGMA = 25              # flat-field blur sigma (px at ~300dpi)
BG_TARGET = 245            # whitened paper level
JPEG_Q = 85                # fallback gray jpeg quality for photo pages
MIN_SPECKLE_AREA = 6       # connected components smaller than this are dust


def whiten(gray: np.ndarray) -> np.ndarray:
    """Divide by blurred background -> paper turns white, ink stays dark."""
    bg = cv2.GaussianBlur(gray, (0, 0), BG_SIGMA)
    bg = np.maximum(bg, 1)
    norm = gray.astype(np.float32) * (BG_TARGET / bg.astype(np.float32))
    return np.clip(norm, 0, 255).astype(np.uint8)


def despeckle(binary: np.ndarray, min_area: int = MIN_SPECKLE_AREA) -> np.ndarray:
    """Drop small black components (scanner dust). binary: True=ink."""
    n, labels, stats, _ = cv2.connectedComponentsWithStats(
        binary.astype(np.uint8), connectivity=8)
    mask = np.zeros_like(binary)
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] >= min_area:
            mask[labels == i] = True
    return mask


def png_1bit(binary: np.ndarray) -> bytes:
    """binary: True=ink -> optimized 1-bit PNG bytes."""
    img = Image.fromarray((~binary))          # PIL: False=black after invert? -> ensure
    img = img.convert("1")
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def gray_jpeg(gray: np.ndarray) -> bytes:
    buf = io.BytesIO()
    Image.fromarray(gray).save(buf, format="JPEG", quality=JPEG_Q, optimize=True)
    return buf.getvalue()


def rgb_jpeg_render(page, iw: int, ih: int) -> bytes:
    """Render the page in RGB at native resolution -> JPEG.

    Never pass extract_image() bytes through: reconstruction ignores PDF /Decode
    arrays, which inverted bitonal pages (black background) for one source book.
    Rendering always applies Decode correctly.
    """
    pm = page.get_pixmap(matrix=fitz.Matrix(iw / page.rect.width, ih / page.rect.height),
                         colorspace=fitz.csRGB, alpha=False)
    buf = io.BytesIO()
    Image.frombytes("RGB", (pm.width, pm.height), pm.samples).save(
        buf, format="JPEG", quality=88, optimize=True)
    return buf.getvalue()


def process_and_insert(src_doc, page, i: int) -> str:
    """Process src page i, insert the replacement image into `page`, return route kind."""
    imgs = src_doc[i].get_images(full=True)
    if not imgs:
        return "blank"
    im = imgs[0]
    iw, ih = im[2], im[3]
    info = src_doc.extract_image(im[0])

    # render at native resolution so decode arrays/polarity are applied correctly;
    # NEVER trust or pass through extract_image() bytes (it ignores PDF /Decode
    # arrays — bitonal pages came out inverted when we tried)
    zx, zy = iw / page.rect.width, ih / page.rect.height
    pm = page.get_pixmap(matrix=fitz.Matrix(zx, zy), colorspace=fitz.csGRAY, alpha=False)
    gray = np.frombuffer(pm.samples, dtype=np.uint8).reshape(pm.height, pm.width)

    vals = np.unique(gray)
    if len(vals) <= 4 and vals.min() <= 32 and vals.max() >= 224:
        # already bitonal: the source encoder (usually CCITT G4) beats any
        # re-encode we can do — skip compression entirely for such books
        raise SystemExit(
            f"page {i + 1} is already bitonal (CCITT G4-class source): "
            "compression variant pointless. Use the lossless pipeline "
            "(build_ocr_pdf.py) as the final edition.")

    try:
        pil = Image.open(io.BytesIO(info["image"]))
        pil.load()
    except Exception:
        page.insert_image(page.rect, stream=rgb_jpeg_render(page, iw, ih))
        return "cover-rgb-render(fail)"

    if pil.mode not in ("L", "I;16", "I", "1"):
        page.insert_image(page.rect, stream=rgb_jpeg_render(page, iw, ih))
        return "cover-rgb-render"               # covers etc.

    ink_ratio = float((gray < 128).mean())
    if ink_ratio > INK_RATIO_PHOTO:
        page.insert_image(page.rect, stream=gray_jpeg(whiten(gray)))
        return f"photo-gray-q{JPEG_Q}"

    normed = whiten(gray)
    thr, _bw = cv2.threshold(normed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    binary = normed < thr                       # True=ink
    binary = despeckle(binary)
    page.insert_image(page.rect, stream=png_1bit(binary))
    return "bilevel-png"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--cache", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--pages", default="")
    args = ap.parse_args()

    src = fitz.open(args.pdf)
    by_page = load_cache(args.cache)
    want = set(parse_pages(args.pages, src.page_count))

    out = fitz.open()
    kinds = {}
    for i in range(src.page_count):
        srect = src[i].rect
        page = out.new_page(width=srect.width, height=srect.height)
        if i in want or not want:
            kind = process_and_insert(src, page, i)
            kinds[kind] = kinds.get(kind, 0) + 1
        if (i + 1) % 50 == 0:
            print(f"  built {i+1}/{src.page_count}", flush=True)

    n = write_text_layer(out, by_page)
    out.save(args.out, garbage=4, deflate=True)
    print(f"pages={src.page_count} chars={n} routes={kinds} -> {args.out}")
    size_mb = Path(args.out).stat().st_size / 1048576
    src_mb = Path(args.pdf).stat().st_size / 1048576
    print(f"size: {src_mb:.1f}MB -> {size_mb:.1f}MB")


if __name__ == "__main__":
    main()
