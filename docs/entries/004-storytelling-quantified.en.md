# Is CHI/ACL a storytelling festival? From community gripe to measurable construct

<div class="lang-switch" markdown>
🌐 Language / 语言：[中文](004-storytelling-quantified.zh.md) · **English**
</div>

<details><summary style='cursor:pointer;color:#888;'>Provenance（来源与元数据）</summary><table style='border:1px solid #eee;border-radius:8px;'><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>id</td><td style='padding:3px 10px;'>marginalia-004</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>title</td><td style='padding:3px 10px;'>Is CHI/ACL a storytelling festival? From community gripe to measurable construct</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>date</td><td style='padding:3px 10px;'>2026-08-15</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>published</td><td style='padding:3px 10px;'>2026-08-15</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>kind</td><td style='padding:3px 10px;'>survey + proposal</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>issue</td><td style='padding:3px 10px;'>7</td></tr></table></details>


# Is CHI/ACL a storytelling festival?

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

> 🌐 [阅读中文版](004-storytelling-quantified.zh.md)

