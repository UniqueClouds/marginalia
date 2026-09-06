# Writing like Dourish: a 21-text corpus analysis of a critical HCI voice (2004–2026)

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> Language / 语言：[中文](002-writing-like-dourish.zh.md) · **English**
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-15</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> analysis</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #3</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-002</td></tr><tr><td>title</td><td>Writing like Dourish: a 21-text corpus analysis of a critical HCI voice (2004–2026)</td></tr><tr><td>date</td><td>2026-08-15</td></tr><tr><td>published</td><td>2026-08-15</td></tr><tr><td>kind</td><td>analysis</td></tr><tr><td>issue</td><td>3</td></tr></table></details>

> Can a scholarly *voice* be measured? Twenty-one Dourish texts and ~408k words later: yes — a signature you can count, stable for two decades.

## The musing

Style advice is usually vibes. I wanted the opposite: take one of critical HCI's most distinctive prose voices — Paul Dourish — and measure it from primary texts, with a pipeline where every quoted sentence is machine-verified against the corpus.

## Corpus

- **20 texts** pulled from my local Zotero (author search over ~5.6k journal articles; bilingual editions excluded; all with PDF attachments), 2004–2026, including two MIT Press monographs; ~**324k words** after cleaning.
- **+1**: *The Stuff of Bits* (2017), extracted from EPUB at the author's implicit invitation of completeness — 584 paragraphs, ~**83.5k words**.
- **Control**: 25 papers from other fields, same era, ~393k words — the baseline for keyness.

## Method

PyMuPDF layout-block extraction → reference stripping → paragraph corpus (`paras.json`) → word frequencies and 2–5-gram document frequencies → keyness by log-ratio against the control corpus → **60+ rhetorical-pattern regexes** → paragraph TF-IDF clustering into **8 recurring motifs (M1–M8)** → `verify_quotes.py` re-finding every quote cited in the report (ligatures/smart-quote normalized) and marking PASS/FAIL. A separate module scores *The Stuff of Bits* signatures (`sob_stats.py`: ~30 signature densities vs. baseline; `sob_sim.py`: paragraph-level TF-IDF similarity).

## The measurable signature

- Lexicon: **practice ×1,041**, **data ×1,022** lead the corpus.
- Negation-restatement: **"not simply/just/only/merely … but" 298× across 18 texts**, **"rather than" 267× across 19** — roughly **one every 350 words**.
- **"ways in which" ×252** (14 texts); quantified-plural constructions ×697; **"that is / in other words" ≈ ×172**.
- Rhetorical questions: about **one every 200 words** in solo theory texts.
- The same syntactic template — *not a property of X, but an achievement of interaction* — travels from **context (2004)** through *emotion* and *data* to *beauty*, two decades apart; sentence-level self-recycling reaches **0.97** TF-IDF similarity.
- *Stuff of Bits* signatures: "that is" **2.45×** baseline; *materiality* **14.98×**; *everyday* **0.12×**.

Two specimens (both 2004, verified in-corpus):

> "what I want to do here is to reconsider context, not as a representational problem but as an interactional problem."

> "Embodiment is not a property of systems, technologies, or artifacts; it is a property of interaction."

## What it produced

1. **The report** — `Dourish_语言特征分析报告.md` (~40KB), every quote verified.
2. **A reusable pipeline** — scripts + JSON intermediates + 12 motif quote files.
3. **A `dourish-style` skill** — polishing workflow with Register A/B and recipes P1–P10; red line: *never copy Dourish verbatim*, only reproduce the mechanism. Published as an artifact: [artifact.en.md](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/002-writing-like-dourish/artifact.en.md).
4. **A first experiment** — my own OSS position paper revised in that register (with a change log).

## Provenance

| field | value |
|---|---|
| Data | Zotero (`zotero.sqlite`, API :23119) → `zotero_copy.sqlite` (201MB); `dourish_analysis/`; skill at `~/.zcode/skills/dourish-style/` |
| Initial prompt | "Search my Zotero for Paul Dourish's papers and analyze his language/style features — quantitatively, and verifiably." |
| Time | analysis 2026-08-15, 20:56 → 21:35 · note published 2026-08-15 |
| Agent / model | ZCode CLI · GLM (Zhipu) |
| Issue | [#3](https://github.com/UniqueClouds/marginalia/issues/3) |


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [阅读中文版](002-writing-like-dourish.zh.md)

