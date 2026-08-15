"""Academic-voice diagnostic: measure a manuscript's style-pattern densities and
compare them against five measured baselines — Paul Dourish (21 texts) and four
discipline corpora (Big Data & Society / HCI / Sociology / Software Engineering).

Usage:
    python voice_check.py <draft.txt|.md|.tex>                # classify: which voice does this sound like?
    python voice_check.py <file> --voice soc                  # full table vs one baseline + opportunities
    python voice_check.py <file> --voice dourish --top 8
    python voice_check.py <file> --json

Pure regex, no dependencies. English text; strips LaTeX/Markdown noise.
Baselines live in baselines.json (per-1000-word densities; provenance inside).
"""
import sys, re, argparse, json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
BASELINES = json.load(open(os.path.join(HERE, "baselines.json"), encoding="utf-8"))
VOICES = BASELINES["voices"]

PATTERNS = {
    "not simply...but": r"\bnot (?:simply|just|only|merely)\b[^.]*\bbut\b",
    "rather than": r"\brather than\b",
    "but rather": r"\bbut rather\b",
    "there is/are": r"\b[Tt]here (?:is|are|was|were)\b",
    "a set of": r"\ba (?:set|range|variety|series) of\b",
    "in other words": r"\bin other words\b",
    "that is,": r"\bthat is( to say)?[,;]\s",
    "in terms of": r"\bin terms of\b",
    "we": r"\b[Ww]e\b",
    "I": r"\bI\b",
    "our": r"\b[Oo]ur\b",
    "passive be+Ved": r"\b(?:is|are|was|were|be|been|being)\s+\w+ed\b",
    "contraction": r"\b\w+'(?:s|t|re|ve|ll|d|m)\b",
    "semicolon": ";",
    "em-dash": "\u2014",
    "open-curly-quote": "\u201c",
    "question marks": r"\?",
    "hedge may": r"\bmay\b",
    "hedge might": r"\bmight\b",
    "hedge suggest": r"\bsuggest(?:s|ed|ing)?\b",
    "increasingly": r"\bincreasingly\b",
    "consistent with": r"\bconsistent with\b",
    "this article": r"\bthis article\b",
    "this paper": r"\bthis paper\b",
    "In this paper, we": r"[Ii]n this (?:paper|article|study),?\s+we",
    "ways in which": r"\bways? in which\b",
    "in the course of": r"\bin the course of\b",
    "sorts/kinds of": r"\b(sort|kind|form|type)s? of\b",
    "practice(s)": r"\bpractices?\b",
    "everyday": r"\beveryday\b",
    "encounter(s)": r"\bencounters?(?:ing|ed)?\b",
    "achieve/achievement": r"\bachiev(e|ed|es|ing|ement|ements)\b",
    "materiality": r"\bmaterialit(?:y|ies)\b",
    "perhaps/arguably": r"\b(perhaps|arguably)\b",
    "net of": r"\bnet of\b",
}

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\u201c\u201d\u2018'\(\[]|\d)")

# patterns used for voice classification (shared across all five baselines)
CORE = ["not simply...but", "rather than", "there is/are", "a set of", "in other words",
        "we", "I", "our", "passive be+Ved", "contraction", "semicolon", "em-dash",
        "open-curly-quote", "question marks", "hedge may", "hedge might", "hedge suggest",
        "increasingly", "consistent with", "this article", "this paper", "In this paper, we",
        "in terms of"]

PORTRAIT = {
    "dourish": "critical essayist (Dourish 2004-2026): not-X-but-Y engine, practice register, teacherly asides",
    "bds": "Big Data & Society: long-sentence public intellectual, zero contractions, critical refutation",
    "hci": "CHI/CSCW: workshop host, 'We present...', heavy hedging, participant detail",
    "soc": "AJS/ASR/BJS: theoretical statistician, em-dashes, contractions OK, model ladders",
    "se": "ICSE/FSE/TSE: list-writing engineer, 16-word sentences, RQ + threats-to-validity",
}


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
    m = re.search(r"(?m)^\s*(references?|bibliography|works cited)\s*$", t, re.I)
    if m and m.start() > len(t) * 0.5:
        t = t[: m.start()]
    for k, v in {"\ufb01": "fi", "\ufb02": "fl"}.items():
        t = t.replace(k, v)
    return t


def measure(text):
    words = len(re.findall(r"[A-Za-z][A-Za-z'-]*", text))
    dens = {}
    for name, pat in PATTERNS.items():
        c = len(re.findall(pat, text, re.I))
        dens[name] = {"count": c, "perkw": c / words * 1000 if words else 0.0}
    sents = [s for s in SENT_SPLIT.split(text) if s and s.strip()]
    dens["avg_sent_len"] = {"count": len(sents),
                            "perkw": sum(len(s.split()) for s in sents) / max(1, len(sents))}
    return words, dens


def distance(dens, voice):
    """mean |log2 ratio| over core patterns + sentence length (smaller = closer)"""
    ds = []
    for name in CORE + ["avg_sent_len"]:
        base = VOICES[voice].get(name)
        if base is None:
            continue
        d = dens[name]["perkw"]
        eps = 0.05
        ds.append(abs(math.log2((d + eps) / (base + eps))))
    return sum(ds) / len(ds)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--voice", choices=list(VOICES) + ["auto"], default="auto")
    ap.add_argument("--top", type=int, default=6)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    text = read_text(args.file)
    words, dens = measure(text)
    if words < 150:
        print(f"[warn] only {words} words - densities unreliable; use on >=1 page of text")

    if args.json:
        print(json.dumps({"words": words, "densities": dens}, indent=1))
        return

    ranked = sorted(VOICES, key=lambda v: distance(dens, v))

    print(f"file: {args.file}\nwords: {words}")
    if args.voice == "auto":
        print("\n=== VOICE CLASSIFICATION (nearest measured baseline first) ===")
        for v in ranked:
            print(f"  {distance(dens, v):5.3f}  {v:8s} {PORTRAIT[v]}")
        voice = ranked[0]
        print(f"\n-> sounds most like: {voice}   (re-run with --voice {voice} for the full table)")
    else:
        voice = args.voice

    base = VOICES[voice]
    rows = []
    for name in PATTERNS:
        if name not in base:
            continue
        d = dens[name]
        rows.append({"pattern": name, "count": d["count"], "perkw": round(d["perkw"], 2),
                     "baseline": base[name], "ratio": round(d["perkw"] / base[name], 2) if base[name] else None})
    print(f"\n=== DENSITIES vs {voice.upper()} baseline ===")
    print(f"{'pattern':30s} {'n':>4s} {'/kw':>6s} {'base':>6s} {'ratio':>6s}")
    for r in sorted(rows, key=lambda r: -(r["ratio"] or 0)):
        print(f"{r['pattern']:30s} {r['count']:4d} {r['perkw']:6.2f} {r['baseline']:6.2f} {r['ratio']:6.2f}")
    sl = dens["avg_sent_len"]["perkw"]
    print(f"{'avg sentence length':30s} {'':4s} {sl:6.1f} {base['avg_sent_len']:6.1f}"
          f" {sl / base['avg_sent_len']:6.2f}")

    print(f"\n=== TOP {args.top} OPPORTUNITIES vs {voice} (signature patterns furthest below baseline) ===")
    SIGNATURE = {"not simply...but", "rather than", "there is/are", "a set of", "in other words",
                 "we", "passive be+Ved", "contraction", "semicolon", "em-dash",
                 "open-curly-quote", "hedge may", "hedge might", "increasingly",
                 "this article", "this paper", "In this paper, we", "question marks",
                 "ways in which", "in the course of", "practice(s)", "consistent with", "net of"}
    under = [r for r in rows if r["pattern"] in SIGNATURE]
    for r in sorted(under, key=lambda r: r["ratio"])[: args.top]:
        gap = r["baseline"] - r["perkw"]
        expected = max(gap * words / 1000, 0)
        shown = f"~{expected:.0f}" if expected >= 1 else f"~{expected:.1f}"
        print(f"- {r['pattern']}: {r['count']}x ({r['perkw']}/kw) vs {voice} {r['baseline']}/kw "
              f"-> {shown} more expected at this voice's density")
    print("\nNote: ratios >2.5 on hedges/we/I mean the draft may be over-styled; scale back.")


if __name__ == "__main__":
    main()
