# Is CHI/ACL a storytelling festival? From community gripe to measurable construct

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> Language / 语言：[中文](004-storytelling-quantified.zh.md) · **English**
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-15</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> survey + proposal</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #7</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-004</td></tr><tr><td>title</td><td>Is CHI/ACL a storytelling festival? From community gripe to measurable construct</td></tr><tr><td>date</td><td>2026-08-15</td></tr><tr><td>published</td><td>2026-08-15</td></tr><tr><td>kind</td><td>survey + proposal</td></tr><tr><td>issue</td><td>7</td></tr></table></details>

> A community gripe, a pile of quantitative studies nobody had connected, and a proposal that splits narrativism into what the *text* says and what the *figures* do.

## The claim, and where it comes from

"CHI/ACL 是故事会" — top-venue papers succeed by storytelling rather than substance. The gripe has named carriers: a Zhihu thread *"ACL 为什么叫故事汇"* (2023), Wobbrock's critique of CHI's rejection culture, Nacke openly teaching the CHI "narrative arc". What it has never had: a measurement. That gap is the musing.

## The evidence that already exists (once you squint)

- **Hillier et al. 2016** (PLOS ONE): 732 climate-science abstracts, crowdsourced scores on 6 narrative elements → composite index; PCA first component carries **76.5%** of variance; 4 elements correlate with citations (confounded with impact factor, **R² = 0.62**).
- **Qiu et al. 2024** (JAMA): 11,535 grant applications; promotional language predicts funding, **OR = 1.47**.
- **Peng 2024** (PNAS): high-promotion abstracts ≈ **2×** the odds of funding.
- **Stavrova 2025** (HSSC): 130k abstracts; hype predicts citations — with higher returns for men.
- Counter-evidence: **Vincent-Lamarre & Larivière 2021** (QSS) — accepted AI-conference papers are *less* readable.
- Context drift: **Vinkers 2015** — positive words in abstracts up **×9** over decades; **Kobak 2025** — **≥13.5%** of 2024 biomedical abstracts carry LLM traces.

## The proposal: explicit vs. implicit narrativism

- **Explicit** — the linguistic surface (v1 five dimensions: hook, first person, sensory language, appeal, connectives, hype words).
- **Implicit** — the structural-visual layer: impersonal CARS moves, master narratives, figure devices (teaser figure, hero chart, caption micro-narratives), **narrative denial** (denial gap = visual-rhetoric intensity − explicit explanation markers), and the artifact layer (benchmark casting, metrics-as-plot, baseline character tables, the ablation morality play). L3: field ideology.
- Unified construct: the **narrative depth gradient** — the deeper the narrative hides, the higher the return.

## Method sketch (v2)

RQ1–9: explicit/implicit separation · rhetorical drift · payoff decomposition · CHI-vs-ACL field contrast · LLM breakpoint · interviews · denial premium · artifact narrativity · stigma boundary. Hypotheses include: explicit narrativity peaks in introductions, implicit in results; the denial gap grows with technicality and carries an acceptance premium.

Dual-track: multimodal large-sample census + critical ethnography, with reflexivity. The figure pipeline is deliberately **local**: Docling + GROBID extraction → ArXivCap (6.4M figures) warm-up → ACL (~50k papers) + OpenReview + CHI; three-tier annotation (SigLIP figure typing → Qwen2.5-VL-7B structured pass → semantic VL pass) with a 500-figure gold set; DuckDB throughout; ~250k figures ≈ 3 GPU-days. Plus arXiv v1↔camera-ready diffs and community discourse as complementary signals.

## People worth remembering

**Sophie Qiu = Huilian Sophie Qiu (邱惠莲)** — CMU PhD 2022, now at Northwestern working with Brian Uzzi (JAMA 2024, IC2S2 2025). Theoretical anchor: **Dourish & Gómez Cruz 2018** — yes, the same Dourish whose prose is dissected in [musing 002](002-writing-like-dourish.en.md); small field. Also in the net: Birhane 2022; Espeland & Sauder 2007 (reactivity); Segel & Heer 2010 and Hullman & Diakopoulos 2011 (narrative visualization).

## Next

M1–M5: coding scheme + 500-figure gold set → 250k-figure census → payoff decomposition → interviews → writing. Three exits: P1 measurement (IC2S2 / QSS / Metascience), P2 main paper (CHI / CSCW), P3 critical (BD&S). Read DiagramBank to draw competitor boundaries.

## Provenance

The original source documents (verbatim, in Chinese) are published alongside this note in [`docs/`](docs/storytelling-survey.zh.md) — the full survey and the proposal v2, not just this summary.

| field | value |
|---|---|
| Data | `CHI_ACL_故事会量化_调研.md`; `AI论文显隐叙事主义_提案v2.md`; external chain as listed in frontmatter |
| Initial prompt | "Community wisdom says CHI/ACL papers are 'storytelling festivals'. Quantify it: has anyone measured narrative in papers? Then turn it into a research proposal." |
| Time | survey + proposal 2026-08-15 · note published 2026-08-15 |
| Agent / model | ZCode CLI · GLM (Zhipu) |
| Issue | [#7](https://github.com/UniqueClouds/marginalia/issues/7) |


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [阅读中文版](004-storytelling-quantified.zh.md)

