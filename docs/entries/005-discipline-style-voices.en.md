# Four academic voices, measured: the language styles of Big Data & Society / HCI / Sociology / Software Engineering classics (314 papers, 3.3M words)

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> Language / 语言：[中文](005-discipline-style-voices.zh.md) · **English**
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-15</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> analysis</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #11</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-005</td></tr><tr><td>title</td><td>Four academic voices, measured: the language styles of Big Data & Society / HCI / Sociology / Software Engineering classics (314 papers, 3.3M words)</td></tr><tr><td>date</td><td>2026-08-15</td></tr><tr><td>published</td><td>2026-08-15</td></tr><tr><td>kind</td><td>analysis</td></tr><tr><td>issue</td><td>11</td></tr></table></details>

> After measuring one author's voice ([002: Dourish](002-writing-like-dourish.en.md)), measure a discipline: same Zotero library, same pipeline, four fields of classic papers. Can stylistic differences be *counted*? Yes — and each discipline turns out to run its own conceptual machine.

## Musing

Writing advice is usually given per author ("write like X"), but academic writing is shaped by **disciplinary ritual**: submit to a venue, inherit its syntax and move-set. I wanted to test how measurable this is — not the impressionistic "SE papers are dry, sociology papers are winding", but densities, rankings, and machine-verifiable example sentences. This is also the sequel to 002: Dourish's signature construction runs at 9.2 per 10k words. What does the *average* paper in his (or neighbouring) fields look like?

## Corpus

Four sub-collections of my Zotero "Classic Papers by Discipline" library — 347 items, 327 with PDFs; after cleaning (watermarks out, Chinese-translation blocks out, hopeless OCR out, monographs out): **314 papers / 3.3M words**.

| Discipline | Papers | Words | Home venues | Years |
|---|---|---|---|---|
| Big Data & Society | 27 | 211,858 | *Big Data & Society*, *New Media & Society* | 2004–2021 |
| Human-Computer Interaction | 94 | 817,868 | CHI, CSCW (ACM) | 2003–2025 |
| Sociology | 79 | 1,105,574 | AJS, ASR, BJS | 1975–2026 |
| Software Engineering | 114 | 1,166,765 | ICSE, FSE, TSE, MSR | 1987–2023 |

## Method

Same pipeline as 002: PyMuPDF block-level paragraph extraction → drop references/watermarks/CJK blocks → word frequencies and 2–5-gram document frequencies → **log-odds keyness (discipline vs the pooled other three)** → 60+ rhetorical-move regexes (RQ lists, threats-to-validity, we+verb collocations, the epistemology/power lexicon…) → title statistics → close reading. All **39 quotes were machine-verified** by `verify_quotes.py` (tolerant of ligature loss, line-broken words, and footnote digits).

## The four voices

**Big Data & Society: the long-sentence public intellectual.** Mean sentence 26.8 words; densest semicolons (46/10k); zero contractions across the whole library; the *not X but Y / rather than* refutation pattern ranks first — restate the mainstream understanding, then flip it; highest passive rate (agency suspended — precisely how the critiqued mechanisms operate); self-refers as "This article", opens with manifesto declarations ("Data are a form of power."), closes with an exhortation to the discipline; titles love the "The X of Y" concept lever.

**HCI: the excited workshop host.** "We present…" straight out of the gate; the richest we-verb repertoire (found/conducted/present/describe/argue); all three hedging markers rank first (may/might/suggest) — permanently honest about small samples; participant registration down to compensation amounts and handedness; interview quotes and p-values side by side; findings must be cashed out as *design implications*; the most playful titles of the four (first person, parody, participants' own words as titles).

**Sociology: the theoretical statistician in dialogue with both Weber and the GSS.** Longest papers (14k words); em-dashes, contractions, and scare quotes all rank first — the loosest prose texture; lowest passivity (the researcher is always actively operating on data); the evidence syntax is "consistent with / net of / Model 1 → Model 3"; juxtaposed epigraph openings (a Weber passage against a campaign attack ad); and a journal ritual found nowhere else — AJS abstracts forced into third-person "The authors" while the body says "we" throughout.

**Software Engineering: the engineer who writes in lists.** Median sentence just 16 words; em-dashes all but banned; we/our both rank first but "I" ranks last; verbs are all tool-verbs (use/found/present/describe); the noun-field is countable objects (bugs/commits/repositories); the heaviest fixed liturgy — "To understand X" opener → bulleted contributions → numbered RQs → a Threats-to-Validity confessional in three parts (construct/internal/external) → future work (70% of papers, guaranteed).

## Three findings I like most

1. **One pronoun betrays your genre**: journal papers self-refer as "this article" (BDS 21/27, SOC 53/79), conference papers as "this paper" (HCI 82/94, SE 103/114). One glance at the self-reference tells you which register you're in.
2. **Dourish is still an outlier**: even BDS, the closest discipline, averages only ~1/3 of his personal density of the not-simply construction (2.9 vs 9.2 per 10k). "Writing like the discipline" and "writing like Dourish" are different calibration targets.
3. **Style is a spectrum, not a border**: critical HCI (Bardzell/Irani/Keyes/Dourish line) forms a BDS-style enclave inside the HCI library (critique density 6.5 vs BDS 7.0); Zeller and Hindle are the rhetorical defectors inside SE; computational sociology is drifting toward SE's empirical liturgy.

## Cheat sheet

| | Syntax signature | Person | Evidence | Ending |
|---|---|---|---|---|
| BDS | not X but Y / rather than / increasingly | This article + I | author-date sparring | exhortation |
| HCI | We present / may-suggest / quotes+stats | we (the workshop) | N+pay+p-values+quotes | design implications |
| SOC | consistent with / net of / in other words | we (abstract: the authors) | model ladders vs hypotheses | limitations |
| SE | To understand X / a set of / 16-word sentences | we+our (the team) | dataset scale + tables | Threats → Future Work |

## Deliverables & limits

- **Five full reports** (Chinese, published verbatim): [BDS](reports/01-big-data-and-society.zh.md) · [HCI](reports/02-hci.zh.md) · [Sociology](reports/03-sociology.zh.md) · [SE](reports/04-software-engineering.zh.md) · [cross-discipline comparison](reports/05-cross-discipline.zh.md)
- The reusable pipeline stays local at `ZCodeProject/discipline_style_analysis/` (resolve → extract → metrics → keyness → clean → quote-verify); `paras.json` keys are `discipline_ZoteroKey`.
- Limits: the sub-collections are a hand-curated "my classics" list, not a random sample; SE lacks 19 papers that exist only as IEEE web snapshots; SOC includes 1970s–80s classics, so part of the difference is era, not field; paragraph-level statistics are affected by single/double-column layouts (sentence-level metrics are not).

**Possible next steps**: distill the four portraits into four polishing skills (mirroring 002's dourish-style), or turn the keyness word lists into a "discipline camouflage detector" — give it a passage, it tells you which field it most sounds like.


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [阅读中文版](005-discipline-style-voices.zh.md)

