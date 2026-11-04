#!/usr/bin/env python3
"""Export the selected NSF awards as a compact, public, browser-ready JSON.GZ."""
from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "marginalia" / "028-nsf-funding-rhetoric" / "data" / "nsf-awards-priority-2026-11-03.json.gz"

AWARD_FIELDS = (
    "title", "pi", "coPIs", "institution", "program", "officialTags",
    "directorate", "division", "programElements", "startDate", "endDate",
    "themeTags", "researchAreas", "awardUrl", "abstractEnglish", "abstractChinese",
)
PUBLICATION_FIELDS = ("title", "authors", "venue", "year", "url")


def dollars(value: Any) -> int | None:
    digits = re.sub(r"[^0-9]", "", str(value or ""))
    return int(digits) if digits else None


def compact_award(row: dict[str, Any]) -> dict[str, Any]:
    item: dict[str, Any] = {"awardId": str(row.get("id", ""))}
    for key in AWARD_FIELDS:
        value = row.get(key)
        if value not in (None, "", []):
            item[key] = value
    amount = dollars(row.get("amountDisplay"))
    obligated = dollars(row.get("obligatedDisplay"))
    if amount is not None:
        item["amountUSD"] = amount
    if obligated is not None:
        item["obligatedUSD"] = obligated
    publications = []
    for source_pub in row.get("publications") or []:
        pub = {key: source_pub.get(key) for key in PUBLICATION_FIELDS if source_pub.get(key) not in (None, "")}
        if pub.get("title"):
            publications.append(pub)
    if publications:
        item["publications"] = publications
    return item


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Path to nsf_funding_priority.json")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help=f"Output path (default: {DEFAULT_OUTPUT})")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"input not found: {args.input}")

    with args.input.open("r", encoding="utf-8-sig") as stream:
        rows = json.load(stream)
    awards = [compact_award(row) for row in rows]
    awards.sort(key=lambda item: (item.get("amountUSD") or 0, item.get("awardId", "")), reverse=True)
    package = {
        "schemaVersion": 1,
        "source": "NSF Award Search / NSF Awards API",
        "snapshotDate": "2026-11-03",
        "recordCount": len(awards),
        "description": "User-scoped filtered award universe; the full English abstract is retained where present. Existing Chinese translations are included where available.",
        "fieldNotes": {
            "themeTags": "Curated topic tags used for this research collection; not all tags are official NSF classifications.",
            "researchAreas": "Curated research-area labels used for the collection; not official NSF classifications.",
            "publications": "Bibliographic metadata listed by the NSF award record; listing does not establish exclusive support by that award.",
            "amountUSD": "Award total displayed in the NSF record, converted to an integer number of US dollars.",
        },
        "awards": awards,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=9, mtime=0) as compressed:
            import io
            with io.TextIOWrapper(compressed, encoding="utf-8", newline="") as text:
                json.dump(package, text, ensure_ascii=False, separators=(",", ":"))
    print(f"Exported {len(awards):,} awards to {args.output} ({args.output.stat().st_size:,} compressed bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
