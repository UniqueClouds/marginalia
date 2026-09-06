# NOTUGLY-S: learning \"not ugly\" instead of \"beautiful\" — an NLP × program-analysis proposal

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> Language / 语言：[中文](003-notugly-s.zh.md) · **English**
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-15</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> proposal</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #2</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-003</td></tr><tr><td>title</td><td>NOTUGLY-S: learning \"not ugly\" instead of \"beautiful\" — an NLP × program-analysis proposal</td></tr><tr><td>date</td><td>2026-08-15</td></tr><tr><td>published</td><td>2026-08-15</td></tr><tr><td>kind</td><td>proposal</td></tr><tr><td>issue</td><td>2</td></tr></table></details>

> If ethnography says beauty is plural and undefined while ugliness is concrete and sanctioned, why keep training models to score beauty? This proposal inverts the objective — and the architecture is itself a test of the theory.

## The inversion

Musing [001](001-code-taste-discord.en.md) ended at Fedorova's finding: "beauty" is organizational and deliberately left undefined; "ugliness" is nameable, and enforced through review *sanctions* — negative comments followed by revision, revert, or request-changes. NOTUGLY-S (v1.1) takes that literally as a supervision signal.

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


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [阅读中文版](003-notugly-s.zh.md)

