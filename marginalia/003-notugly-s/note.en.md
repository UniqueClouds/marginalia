---
id: marginalia-003
title: "NOTUGLY-S: learning \"not ugly\" instead of \"beautiful\" — an NLP × program-analysis proposal"
date: 2026-08-15
published: 2026-08-15
kind: proposal
sources:
  - "ZCodeProject/code_beauty_simplification/NOTUGLY-S_Proposal_NLP与程序分析融合训练.md (v1.1)"
  - "ZCodeProject/code_beauty_simplification/好代码的定量度量与跨源规范清单_调研报告.md — companion survey"
  - "ZCodeProject/code_beauty_simplification/notugly/ — notugly.py (rule-based, Python AST, L1–L3), notugly2.py (tree-sitter, cross-lingual), express/flask/gin repo profiles"
  - "upstream: musing 001 (Discord corpus + Fedorova et al. 2025)"
initial-prompt: "Turn the 'sanction / imitation / not-ugly' reading of Fedorova into a testable ML objective — NLP meets program analysis."
agent: ZCode CLI
model: GLM (Zhipu)
issue: 2
---

# NOTUGLY-S: learn "not ugly", not "beautiful"

> If ethnography says beauty is plural and undefined while ugliness is concrete and sanctioned, why keep training models to score beauty? This proposal inverts the objective — and the architecture is itself a test of the theory.

## The inversion

Musing [001](../001-code-taste-discord/note.en.md) ended at Fedorova's finding: "beauty" is organizational and deliberately left undefined; "ugliness" is nameable, and enforced through review *sanctions* — negative comments followed by revision, revert, or request-changes. NOTUGLY-S (v1.1) takes that literally as a supervision signal.

## The scorer

A repo-conditioned, cross-lingual **not-ugly scorer**:

```
s(x) = g_θ(d) + h_φ(d, c_r) + α·reviewer + ε
```

`g_θ` global (travels across repos), `h_φ` local (conditioned on repo card `c_r`), `α·reviewer` a human-in-the-loop term — per-axis "not-ugly" probabilities, never a single "beauty" score. Supervision comes from review sanctions, not static labels.

## Questions & hypotheses

- **RQ1** learnability · **RQ2** signal value · **RQ3** modality contribution · **RQ4** theory test.
- **H1** within-repo AUROC beats the global model by ≥0.05 · **H2** revision-pairs beat static labels · **H3** global+local decomposition works · **H4** dual-modal > single-modal · **H5** ecological validity (flags correlate with revert / 30-day churn) · **H6** invariance under author-identity permutation (KL below threshold) · **H7** cross-lingual transfer: `g` travels, `h` anchors at repo level.

## Three tracks

1. **Hierarchical interpretable model** — global GBM + per-repo model with Bayesian shrinkage.
2. **Graph-text fusion Transformer** — 7–14B open code LLM + LoRA; diff + repo card + linearized program graph; DPO.
3. **Preference-only track** — Bradley–Terry / DPO.

Program-analysis side: tree-sitter unified AST across **8 languages** + idiom tables; complexity / naming / clone / graph features, normalized to per-`(language, is_test)` percentiles. NLP side: review comments, commit/issue text, Snorkel-style weak supervision, PU learning.

## Evaluation

Within-repo temporal AUROC/AUPRC · 30-day churn survival (C-index, Cox HR) · revision-pair ranking · line-level attribution IoU · annotator agreement α≥0.7. Baselines: SonarQube, LLM zero-shot, LLM+repo-card, CodeReviewer DQE. Leave-one-language-out for cross-lingual claims; author-permutation probe for bias.

## Toy prototypes already exist

`notugly.py` — rule-based, Python AST, levels L1–L3. `notugly2.py` — tree-sitter, cross-lingual, with percentile fallback. Three repo profiles (express / flask / gin: files, naming style, distributions, commit size, hotspots, revert commits) act as "the repo's own distribution" — the baseline any deviation is judged against.

## The companion survey

Six layers of quantitative "good code" metrics — McCabe → ISO 5055 → LLM-as-judge — are, structurally, all *ugliness detectors*, constrained by Goodhart's law, collinearity, arbitrary thresholds, and level mismatch. A cross-source norms corpus (Google eng-practices, PEP 8, Rust API guidelines, Swift, Linux kernel, CISQ; thousands of clauses) coded with an 8-field schema (polarity, automatability, conflicts, enforcement…) yields three testable hypotheses: prohibitions dominate; consensus core + repo-local residue decomposes cleanly; threshold numbers have informative cross-source distributions.

## Where it stands

Proposal v1.1 (cross-lingual design + notugly2 validation), toy prototypes, and the survey — all 2026-08-15. Next: sanction mining on real review corpora, then Track A.

## Provenance

| field | value |
|---|---|
| Data | `code_beauty_simplification/` (proposal v1.1 + survey + notugly/ prototypes); upstream corpus of musing 001 |
| Initial prompt | "Turn the 'sanction / imitation / not-ugly' reading of Fedorova into a testable ML objective — NLP meets program analysis." |
| Time | proposal v1.1 2026-08-15 · note published 2026-08-15 |
| Agent / model | ZCode CLI · GLM (Zhipu) |
| Issue | [#2](https://github.com/UniqueClouds/marginalia/issues/2) |
