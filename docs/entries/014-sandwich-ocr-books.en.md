# Sandwich OCR for scanned books — making Putnam and Rorty pixel-identical and fully searchable

<div class="lang-switch" markdown>
🌐 Language / 语言：[中文](014-sandwich-ocr-books.zh.md) · **English**
</div>

<details><summary style='cursor:pointer;color:#888;'>Provenance（来源与元数据）</summary><table style='border:1px solid #eee;border-radius:8px;'><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>id</td><td style='padding:3px 10px;'>marginalia-014</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>title</td><td style='padding:3px 10px;'>Sandwich OCR for scanned books — making Putnam and Rorty pixel-identical and fully searchable</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>date</td><td style='padding:3px 10px;'>2026-08-22</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>published</td><td style='padding:3px 10px;'>2026-08-22</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>kind</td><td style='padding:3px 10px;'>analysis (engineering retrospective)</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>issue</td><td style='padding:3px 10px;'>37</td></tr></table></details>


# Sandwich OCR for scanned books

> Engineering retrospective. Problem: scanned academic books are neither searchable nor precisely copyable — how do you bolt on a text layer **without touching a single pixel**? Conclusion up front: use a *sandwich* architecture — a per-character invisible text layer (`render_mode=3`) drawn onto the original PDF pages, image streams never re-encoded (per-page MD5 verification shows zero diffs); recognition via RapidOCR behind a DirectML monkey-patch (~1.0 pages/s, 10× CPU); the key to phantom-space-free copying is setting each character's fontsize exactly equal to its allocated advance. Both books shipped and verified: Putnam in a lossless 66 MB edition plus a compressed 21.6 MB one; Rorty lossless-only at 23.9 MB (its CCITT G4 streams are already optimal — do not recompress). Along the way I hit seven real traps; the most expensive: `extract_image()` ignores PDF `/Decode` arrays, which turned inverted pages into black-background ones.

## 1. Requirements and constraints

The two books hurt differently:

- **Putnam**: 283 DPI grayscale JPEG, no text layer at all — unsearchable, uncopyable;
- **Rorty**: worse. The circulating old OCR edition has a garbage layer — copying yields fragments like `CET |AREA BG BAB)` riddled with fake word breaks.

Three goals that pull against each other: **visually identical to the original**, **precisely selectable/copyable text** (with no phantom spaces), and **as small as possible**. Any re-encoding breaks goal one; a sloppy text layer breaks goal two; fidelity and size naturally trade off — unless you treat each book according to what it is.

## 2. The sandwich architecture, decoupled in two phases

```
build_ocr_pdf.py ocr    source pdf → grayscale render (long side 2400px) → RapidOCR → boxes+text+scores → JSONL cache
build_ocr_pdf.py apply  invisible per-char text layer on the ORIGINAL pages (render_mode=3) → save(garbage=3) → lossless edition
```

Two decisions worth expanding:

**Zero image re-encoding.** Instead of generating a new PDF, append the text layer to the original page objects and save. `save(garbage=3, deflate=True)` tidies structure and recompresses metadata streams but **never touches image streams**. The verifier compares per-page image-stream MD5s (zero diffs) and samples rendered pixels (identical). "Identical to the original" stops being a slogan and becomes an assertable property.

**Cache decoupled from assembly.** OCR results land in JSONL (one record per page); assembly takes seconds and can be rerun freely — I retuned the layer's typography four times (spaces, reading order) without re-recognizing a single character. Resume after interruption comes free: cached pages are skipped.

## 3. Three key technical decisions

### 1. Per-character placement with fontsize = advance, killing phantom spaces

RapidOCR returns line-level boxes. To make selection character-exact, split each line into characters: allocate the line's width by weight (CJK full-width 1.0, Latin/digits 0.55, punctuation 0.45).

The first-version trap: fontsize was `min(box height × 0.72, …)`, so glyphs ended up narrower than their pitch, and **viewers inferred spaces from glyph gaps during extraction** — copies came out full of phantom spaces (found by the user). Fix: make **each character's fontsize exactly its allocated advance width**. CJK glyph advance equals fontsize, so glyph pitch equals character pitch, gaps are structurally zero, and no extractor can invent spaces. As a second guard, model-inserted spaces between CJK characters ("李幼 蒸译") are stripped at assembly time.

### 2. DirectML monkey-patch: 6–10× speedup

rapidocr_onnxruntime 1.2.3's session factory only knows CPU/CUDA EPs, so the RTX 4060 in this machine sat idle while onnxruntime-directml shipped `DmlExecutionProvider` all along. Rewriting `OrtInferSession.__init__` to swap the provider list fixes it:

| Device | Speed | Notes |
|---|---|---|
| Full-core CPU (default) | 0.10 pages/s | saturates every core; machine unusable |
| CPU capped at 4 threads | 0.18 pages/s | fallback |
| **DirectML** | **~1.0 pages/s** | CPU mostly idle; output identical char-for-char |

A 521-page book drops from ~87 to ~9 minutes, with the laptop usable throughout.

### 3. Bitonal scans must be rendered to antialiased grayscale first

Feeding the Rorty 1-bit scans straight into OCR wrecks accuracy (the root cause of the old edition's failure). Jagged edges break detection and recognition; rendering through PyMuPDF at long side 2400px produces antialiased grays as a side effect of upscaling, and quality snaps back to normal (mean confidence 0.71 → 0.88).

## 4. Seven traps, ranked by cost

1. **`extract_image()` ignores PDF `/Decode` arrays.** Some of Rorty's 1-bit images carry a `[1 0]` inverse decode; the reconstructed PNG comes out inverted and re-embedding yields **black-background pages** (caught by the user). Iron rule: never pass through `extract_image()` bytes — judge polarity/encoding only from native `get_pixmap` renders, which always apply Decode.
2. **Don't recompress bitonal sources.** First attempt at size relief: pass-through via PNG containers (~30 KB/page fatter than raw G4; 19.9 → 36 MB). Second: own re-encode (despeckle + PIL optimize, seemingly 0.65×) — until I noticed 0.65× was measured against extract_image's bloated containers; against true CCITT G4 streams PIL PNG is ~1.7× larger. G4 wins; the lossless edition IS the optimal compression. Compressed editions only make sense for grayscale-JPEG scans.
3. **Don't fight PyMuPDF's low-level API.** Hand-copying CCITT streams (`get_new_xref` + `update_object` + `update_stream(new=True)`) gets `/Filter` silently rewritten to FlateDecode, double-encoding every page into blankness.
4. **Mixing 0-/1-based `--pages` conventions misaligned entire runs.** A "blank compressed page" in a comparison crop was simply a page that had never been processed — suspect your indexing before suspecting the library.
5. **Saturating all CPU cores gets complained about.** Default posture for long jobs: GPU if available, else capped threads (`--threads`).
6. **Making detection thresholds more sensitive gained exactly zero on these books** — v1/v2 caches matched per-page, character for character. The real cause of "missing text" was the text layer's small font failing selection highlight coverage (see §3.1). Quantify before optimizing.
7. **Automated verification is non-negotiable.** Image-stream MD5 + rendered-pixel sampling + round-trip char comparison, plus box-overlay crops for eyeballing — every failure above was caught by these, including the polarity inversion (dark%=91% convicted instantly).

## 5. Battle record

| Book | Pages | Source | Shipped | round-trip |
|---|---|---|---|---|
| Reason, Truth and History (Putnam) | 314 | 283 DPI gray JPEG, 61 MB | lossless 66 MB + compressed 21.6 MB (whiter paper, darker crisper strokes) | 313/313 |
| Philosophy and the Mirror of Nature (Rorty) | 521 | CCITT G4 bitonal, 19.9 MB | lossless only 23.9 MB (trap 2) | 515/515 |

Whole-book mean OCR confidence ≈ 0.88. Residual errors are near-shape substitutions (肯→背), the PP-OCRv3 mobile model's ceiling; the confidence report locates pages worth proofreading.

## 6. Limitations and next steps

- Sideways (90°-rotated) page numbers go undetected (cls supports 0°/180° only); body text unaffected.
- Rare glyphs may lack shapes under the subsetted `china-s` font, but copied text stays correct (extraction uses ToUnicode).
- If smaller matters: JBIG2 would save ~30% over G4, but the Windows toolchain (jbig2enc) is awkward; swapping to PP-OCRv5 models should raise accuracy further.

The full pipeline lives in this repository at [`ocr_pipeline/`](https://github.com/UniqueClouds/marginalia/tree/main/ocr_pipeline) (PR #36), with bilingual READMEs and the engineering log of all seven traps.


---

> 🌐 [阅读中文版](014-sandwich-ocr-books.zh.md)

