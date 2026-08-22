# -*- coding: utf-8 -*-
"""Inspect source PDFs: pages, sizes, image encodings, DPI, text-layer presence."""
import sys, io
import fitz  # pymupdf

BOOKS = {
    "putnam": r"D:\Downloads\理性、真理与历史 (希拉里·普特南著, 童世骏, 李光程) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
    "rorty":  r"D:\Downloads\哲学和自然之镜 (理查德·罗蒂) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
}

def human(n):
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f}{u}"
        n /= 1024
    return f"{n:.1f}TB"

for key, path in BOOKS.items():
    doc = fitz.open(path)
    print(f"===== {key}: {path}")
    print(f"pages={doc.page_count}  size={human(doc.tobytes().__len__() if False else __import__('os').path.getsize(path))}  encrypted={doc.is_encrypted}  pdf_version={doc.metadata.get('format')}")
    # sample pages: first few, middle, last
    samples = sorted(set([0, 1, 2, doc.page_count // 4, doc.page_count // 2, 3 * doc.page_count // 4, doc.page_count - 1]))
    filt_stats = {}
    total_text_chars = 0
    for i in range(doc.page_count):
        page = doc[i]
        total_text_chars += len(page.get_text("text").strip())
        if i in samples:
            rect = page.rect
            imgs = page.get_images(full=True)
            print(f"  p{i+1}: rot={page.rotation} rect={rect.width:.0f}x{rect.height:.0f}pt images={len(imgs)}")
            for im in imgs[:3]:
                xref, smask, w, h, bpc, cs = im[0], im[1], im[2], im[3], im[4], im[5]
                info = doc.extract_image(xref)
                print(f"     img xref={xref} {w}x{h}px {bpc}bpc cs={cs} ext={info['ext']} bytes={human(len(info['image']))} dpi_hint={w / (rect.width / 72):.0f}")
        for im in page.get_images(full=True):
            info = doc.extract_image(im[0])
            k = (im[5], info["ext"])
            filt_stats[k] = filt_stats.get(k, 0) + 1
    print(f"  TOTAL text chars across all pages: {total_text_chars}")
    print(f"  image filter histogram: {filt_stats}")
    doc.close()
