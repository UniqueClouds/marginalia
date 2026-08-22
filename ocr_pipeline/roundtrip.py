# -*- coding: utf-8 -*-
import json, sys
import pymupdf as fitz
from build_ocr_pdf import load_cache, sort_reading_order

out = fitz.open(sys.argv[1])
by_page = load_cache(sys.argv[2])
checked = passed = 0
fails = []
for p, rec in by_page.items():
    if not rec["lines"]:
        continue
    want = "".join(l["t"] for l in sort_reading_order(rec["lines"]))
    got = out[p].get_text("text")
    want_c = "".join(want.split()); got_c = "".join(got.split())
    if not want_c:
        continue
    checked += 1
    ratio = sum(1 for ch in want_c if ch in got_c) / len(want_c)
    if ratio >= 0.95:
        passed += 1
    else:
        fails.append((p + 1, round(ratio, 3)))
print(f"round-trip: {passed}/{checked} pages pass (>=95% char containment)")
if fails:
    print("FAIL pages:", fails[:15])
