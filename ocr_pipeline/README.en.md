# ocr_pipeline — High-fidelity "sandwich" OCR for scanned books

Overlay a **precisely selectable, copy-clean** text layer onto scanned academic books while
**preserving the original page images byte-for-byte**. Built for one concrete need: turning
scans of Putnam's *Reason, Truth and History* and Rorty's *Philosophy and the Mirror of
Nature* into PDFs that are visually identical to the original yet fully searchable.
Both books shipped; this directory is the complete, reusable pipeline.

## Three hard guarantees

1. **Zero image re-encoding** — the text layer is drawn on the original PDF pages
   (invisible, `render_mode=3`); verification compares per-page image-stream MD5s: 0 diffs,
   rendered pixels identical.
2. **No phantom spaces on copy** — the text layer places every character individually with
   `fontsize = its allocated advance` (glyph pitch equals character pitch, so viewers cannot
   infer spaces); model-inserted spaces between CJK characters are stripped at assembly time.
3. **GPU speedup 6–10×** — rapidocr_onnxruntime 1.2.3 only knows the CPU/CUDA EPs;
   `patch_session()` monkey-patches the ONNX Runtime session to use `DmlExecutionProvider`
   (works on any NVIDIA/AMD GPU via the already-installed onnxruntime-directml).
   Measured on an RTX 4060 Laptop: ~1.0 pages/s vs 0.10 pages/s on full-core CPU, results identical.

## Architecture: two phases + independent verification

```
build_ocr_pdf.py ocr    source pdf → grayscale render (long side 2400px) → RapidOCR (PP-OCRv3) → JSONL cache (resumable)
build_ocr_pdf.py apply  invisible per-char text layer on the ORIGINAL pages → save(garbage=3, deflate) → lossless edition
build_compressed.py     optional compressed edition for grayscale scans: background whitening → Otsu binarize → despeckle → 1-bit PNG
verify_output.py        verification: image-stream MD5 / rendered-pixel sampling / round-trip character comparison
```

- Cache and assembly are decoupled: retune typography without re-OCR; interrupted OCR runs resume.
- Blocks are reordered by visual-row clustering then left-to-right, fixing page numbers landing mid-paragraph.
- Font is PyMuPDF's built-in `china-s`, subsetted on save (rare glyphs may lack shapes but copied text stays correct via ToUnicode).

## Usage

```bash
PY=python  # deps: pymupdf rapidocr_onnxruntime onnxruntime-directml pillow opencv-python numpy

# 1) OCR (GPU; --pages is 1-based, e.g. "2,3,50-60"; reruns resume automatically)
python build_ocr_pdf.py ocr --pdf book.pdf --cache cache.jsonl --device dml
#   CPU fallback (thread-capped so the machine stays usable): --device cpu --threads 4

# 2) Assemble the text layer (seconds; rerun freely)
python build_ocr_pdf.py apply --pdf book.pdf --cache cache.jsonl --out book_OCR.pdf

# 3) Verify + quality report
python verify_output.py --src book.pdf --out book_OCR.pdf --cache cache.jsonl
python quality_report.py   # whole-book confidence report, flags low-confidence pages
```

## Lessons learned (every single one was hit for real)

1. **`extract_image()` ignores PDF `/Decode` arrays.** A source book's 1-bit images carried a
   `[1 0]` inverse decode; the reconstructed PNG came out inverted and re-embedding produced
   black-background pages. Iron rule: **never pass through `extract_image()` bytes** — judge
   polarity/encoding from a native `get_pixmap` render instead.
2. **Don't recompress bitonal sources.** The Rorty scan stores CCITT G4 (~12–38 KB/page);
   every re-encode we tried (PIL PNG, gray JPEG) was larger and softer. The lossless edition IS
   the optimal compression. Compressed editions only make sense for grayscale-JPEG scans
   (Putnam: 61 MB → 21.6 MB, whiter paper, darker crisper strokes).
3. **Don't fight PyMuPDF's low-level API.** Hand-copying raw CCITT streams via
   `update_stream(new=True)` gets `/Filter` rewritten to FlateDecode, double-encoding every page.
4. **Feeding bitonal scans straight into OCR wrecks accuracy.** 1-bit jaggies break detection;
   always render through antialiased grayscale first (long side 2400px).
5. **`--pages` is 1-based.** An earlier 0-based convention misaligned entire runs — the
   "blank compressed page" in a comparison crop was simply an unprocessed page.
6. **Cap CPU threads for long jobs** (`--threads`) or the machine becomes unusable; prefer DML when a GPU exists.
7. **Automated verification is non-negotiable.** Image-stream MD5 + rendered-pixel sampling +
   round-trip char comparison, plus box-overlay crops for eyeballing alignment — all four
   failures during development were caught by these.

## Battle record (2026-08-22)

| Book | Pages | Source | Shipped |
|---|---|---|---|
| Reason, Truth and History (Putnam, tr. Tong Shijun / Li Guangcheng) | 314 | 283 DPI gray JPEG, 61 MB | lossless 66 MB + compressed 21.6 MB, round-trip 313/313 |
| Philosophy and the Mirror of Nature (Rorty, tr. Li Youzheng) | 521 | CCITT G4 bitonal, 19.9 MB | lossless only 23.9 MB (see lesson 2), round-trip 515/515 |

Whole-book mean OCR confidence ≈ 0.88; occasional near-shape errors are the PP-OCRv3 mobile model's ceiling — the confidence report locates pages worth spot-checking.

## Known limitations

- Sideways (90°-rotated) page numbers / vertical text are not detected (cls supports 0°/180° only); body text unaffected.
- The `china-s` font has limited coverage: rare glyphs show no shape on-page, but copied text remains correct.

## License

Same as this repository: CC BY-NC 4.0.
