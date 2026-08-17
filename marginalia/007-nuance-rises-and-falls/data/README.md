# Nuance / scalar-modifier density — data appendix

**For:** [`note.zh.md`](../note.zh.md) · [`note.en.md`](../note.en.md) of marginalia entry **007**.

This directory holds the **machine-countable empirical supplement** to the note. Both CSVs are derived solely from the local corpus (Yunqi's Zotero "Classic Papers" library for BDS / HCI / Sociology / SE) plus the Dourish baseline from entry [002](../../002-writing-like-dourish/note.en.md). No external data was fetched.

## Files

| file | rows | content |
|---|---|---|
| `paper_level_rates.csv` | 335 | One row per paper: discipline · year · word count · raw counts and per-10k-word rates for B1 weak-scalar, B2 mid-scalar, B3 strong-booster, epistemic-hedge bands. |
| `discipline_decade_rates.csv` | 16 | Aggregated rates: one `ALL` row per discipline (+ Dourish), plus one row per decade for the four disciplines with enough time depth. |

## Wordlists (reproducible)

Each band is the union of English surface regexes over the paragraph-merged text. Hyphenation was already de-broken during extraction in entry [005](../../005-discipline-style-voices/note.en.md); the regexes are case-insensitive, word-boundary anchored.

- **B1_weak_scalar** (the MASP target class) — `slightly / somewhat / partly / partially / relatively / mildly / a bit / a little / marginally / nominally / to some extent / to some degree / to a limited extent`
- **B2_mid_scalar** — `quite / rather / fairly / moderately / considerably / noticeably / substantially / meaningfully / to a large extent / to a great extent`
- **B3_strong_booster** — `very / highly / extremely / entirely / completely / fully / totally / utterly / strongly / clearly / obviously / significantly / indeed / in fact / demonstrate / prove / proven`
- **epistemic_hedge** — `may / might / could / suggest(+s|ed|ing) / appear(+s|ed|ing) / seem(+s|ed|ing) / likely / perhaps / possibly / arguably / plausibly / approximately / roughly`

Chinese scalar modifiers (稍微 / 略微 / 有点 / 有些 / 一些 / 部分 / 些许 / 多少) were also scanned but returned zero hits after CJK cleaning in [005]'s pipeline (the corpus contains only English-original papers; Chinese translation PDFs were filtered out in step `05_cjk_clean.py`).

## How the numbers were computed

The re-runnable script lives in the workspace behind this repo at `ZCodeProject/discipline_style_analysis/nuance_scan.py` (not checked into this repo — see entry [005]'s `sources`). It loads `paras.json` (paragraph-level text, 314 papers / 3.3M words after cleaning), runs the four band regexes over every paper, and aggregates by discipline and decade.

## Caveats (also printed in the note)

- **Surface-pattern counting** — not a parse. "rather" caught as B2 is mostly Dourish / BDS's "X, rather than Y" construction (a phrase-level rather than a degree reading). The note's top-items table shows this — `rather` dominates B2 in BDS / SOC / Dourish precisely because of that signature construction. The band rates are best read as **a first-pass measure**, not a semantic parse.
- **Sample size per cell** — the 1970s/1980s Sociology cells contain 1 paper each; the BDS 2020s cell is 1 paper / 4 052 words. Cell-level rates for these buckets are reported in the note but explicitly flagged as too thin for inference.
- **"Classic Papers" library** — the 314-paper corpus is a *curated* set of canonical papers per discipline, not a random sample of all papers in each field. The note's observations describe this corpus, not "the field as a whole".
- **No causal claims** — these are densities across discipline × decade cells. The note deliberately reports and quotes; it does not argue that social-media pressure is reducing nuance, or that LLM blind spots are affecting writing.
