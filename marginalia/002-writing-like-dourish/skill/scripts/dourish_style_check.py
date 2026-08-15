"""Dourish-style diagnostic: compare a manuscript's signature-pattern densities
against the Dourish corpus baseline (20 papers + The Stuff of Bits, ~408k words).

Usage:
    python dourish_style_check.py <draft.txt|.md|.tex> [--top N]

Output: per-pattern table (count, per-1000-words, Dourish baseline, ratio) and
the top patterns most under-used relative to the baseline ("opportunities").
Pure-regex, no dependencies. Works on English text; strips LaTeX commands.
"""
import sys, re, argparse, json

# Baseline: occurrences per 1000 words, measured on the Dourish corpus
# (20 papers 2004-2026, 324k words; verified 2026-08-15).
BASELINE = {
    "not simply/just/only/merely...but": 0.93,
    "rather than": 0.82,
    "but rather": 0.41,
    "ways in which / way in which": 1.05,
    "a set/range/variety/series of": 0.98,
    "sorts/kinds/forms/types of": 2.15,
    "in the course of": 0.13,
    "in other words": 0.19,
    "that is,": 0.34,
    "in terms of": 0.47,
    "in particular": 0.39,
    "at the same time": 0.23,
    "of course": 0.26,
    "indeed": 0.33,
    "in fact": 0.27,
    "encounter(s)": 0.71,
    "everyday": 1.00,
    "mundane": 0.09,
    "accountable/accountability": 0.16,
    "achieve/achievement": 0.47,
    "practice(s)": 3.22,
    "materiality/materialities": 0.18,
    "seamless": 0.06,
    "mess/messy": 0.12,
    "I (first person)": 1.73,
    "we": 7.07,
    "questions (?)": 1.02,
    "might/may hedge": 0.84,
    "perhaps/arguably": 0.63,
}

PATTERNS = {
    "not simply/just/only/merely...but": r"\bnot (?:simply|just|only|merely)\b[^.]*\bbut\b",
    "rather than": r"\brather than\b",
    "but rather": r"\bbut rather\b",
    "ways in which / way in which": r"\bways? in which\b",
    "a set/range/variety/series of": r"\ba (?:set|range|variety|series) of\b",
    "sorts/kinds/forms/types of": r"\b(sort|kind|form|type)s? of\b",
    "in the course of": r"\bin the course of\b",
    "in other words": r"\bin other words\b",
    "that is,": r"\bthat is( to say)?[,;]\s",
    "in terms of": r"\bin terms of\b",
    "in particular": r"\bin particular\b",
    "at the same time": r"\bat the same time\b",
    "of course": r"\bof course\b",
    "indeed": r"\bindeed\b",
    "in fact": r"\bin fact\b",
    "encounter(s)": r"\bencounters?(?:ing|ed)?\b",
    "everyday": r"\beveryday\b",
    "mundane": r"\bmundane\b",
    "accountable/accountability": r"\baccountab(le|ility)\b",
    "achieve/achievement": r"\bachiev(e|ed|es|ing|ement|ements)\b",
    "practice(s)": r"\bpractices?\b",
    "materiality/materialities": r"\bmaterialit(?:y|ies)\b",
    "seamless": r"\bseamless\b",
    "mess/messy": r"\bmess(?:y)?\b",
    "I (first person)": r"\bI\b",
    "we": r"\bwe\b",
    "questions (?)": r"\?",
    "might/may hedge": r"\b(might|may) (be|well|also|then|argu)\b",
    "perhaps/arguably": r"\b(perhaps|arguably)\b",
}

# patterns where being BELOW baseline is the actionable signal
SIGNATURE = {"not simply/just/only/merely...but", "rather than", "ways in which / way in which",
             "that is,", "in other words", "in the course of", "a set/range/variety/series of",
             "sorts/kinds/forms/types of", "in terms of", "encounter(s)", "achieve/achievement",
             "in particular", "indeed", "might/may hedge", "perhaps/arguably", "questions (?)"}


def read_text(path):
    t = open(path, encoding="utf-8", errors="ignore").read()
    if path.endswith(".tex"):
        t = re.sub(r"(?m)^%.*$", " ", t)
        t = re.sub(r"\\(cite|ref|label|eqref)\{[^}]*\}", " [X] ", t)
        t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", t)
        t = re.sub(r"[{}]", " ", t)
    if path.endswith(".md"):
        t = re.sub(r"^#+\s*", " ", t, flags=re.M)
        t = re.sub(r"`{1,3}[^`]*`{1,3}", " ", t)
    # auto-cut a References/Bibliography section if present in the latter half
    m = re.search(r"(?m)^\s*(references?|bibliography|works cited)\s*$", t, re.I)
    if m and m.start() > len(t) * 0.5:
        t = t[: m.start()]
    for k, v in {"\ufb01": "fi", "\ufb02": "fl"}.items():
        t = t.replace(k, v)
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--top", type=int, default=6)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    text = read_text(args.file)
    words = len(re.findall(r"[A-Za-z][A-Za-z'-]*", text))
    if words < 150:
        print(f"[warn] only {words} words - density estimates unreliable; use on >=1 page of text")

    rows = []
    for name, pat in PATTERNS.items():
        c = len(re.findall(pat, text, re.I))
        perkw = c / words * 1000 if words else 0
        base = BASELINE[name]
        rows.append({"pattern": name, "count": c, "perkw": round(perkw, 2),
                     "baseline": base, "ratio": round(perkw / base, 2) if base else None})

    if args.json:
        print(json.dumps({"words": words, "rows": rows}, indent=1))
        return

    print(f"file: {args.file}\nwords: {words}\n")
    print(f"{'pattern':38s} {'n':>4s} {'/kw':>6s} {'Dourish':>8s} {'ratio':>6s}")
    for r in sorted(rows, key=lambda r: -(r["ratio"] or 0)):
        print(f"{r['pattern']:38s} {r['count']:4d} {r['perkw']:6.2f} {r['baseline']:8.2f} {r['ratio']:6.2f}")

    print(f"\n=== TOP {args.top} OPPORTUNITIES (signature patterns furthest below baseline) ===")
    under = [r for r in rows if r["pattern"] in SIGNATURE]
    for r in sorted(under, key=lambda r: r["ratio"])[:args.top]:
        gap = r["baseline"] - r["perkw"]
        expected = max(gap * words / 1000, 0)
        shown = f"~{expected:.0f}" if expected >= 1 else f"~{expected:.1f}"
        print(f"- {r['pattern']}: {r['count']}x ({r['perkw']}/kw) vs Dourish {r['baseline']}/kw "
              f"-> {shown} more expected in a Dourish-density text of this length")
    print("\nNote: ratios >2.5 on hedges/I/we mean the draft may already be over-styled; scale back.")


if __name__ == "__main__":
    main()
