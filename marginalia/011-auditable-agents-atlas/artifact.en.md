---
id: marginalia-011-artifact
title: "Artifact: a 10-minute read of `awesome-auditable-ai`"
date: 2026-08-17
published: 2026-08-17
kind: artifact (companion summary card)
sources:
  - "note.zh.md in this folder — the full systematic compilation (~12 k characters, with section-by-section scans, eight open gaps, and the bridge to my own research agenda)"
  - "https://github.com/yzhao062/awesome-auditable-ai — curated list maintained by Yue Zhao (USC-FORTIS, author of PyOD / ADBench); 2026-08-17 clone snapshot"
initial-prompt: "A new musing note: summarize, distill, and systematically aggregate this link — existing progress, what remains to research, and so on."
agent: ZCode CLI
model: GLM (Zhipu)
issue: 26
---

# Artifact: a 10-minute read of `awesome-auditable-ai`

> Companion to the long-form note: [note.zh.md](note.zh.md) (Chinese) / [note.en.md](note.en.md) (English). This card gives only the "what / a few numbers / how to read / the holes it leaves".

## What it is

A curated list maintained by Yue Zhao (USC-FORTIS, father of [PyOD](https://github.com/yzhao062/pyod) and co-author of [ADBench](https://github.com/Minqi824/ADBench)), titled **Awesome Auditable AI**. It recasts "auditability of AI agents" as a synthesis of "reliability engineering + decision accountability". The one-sentence thesis: **logging is not enough; only a record that lets you afterwards reconstruct what happened, who is responsible, and whether it can be undone counts as auditable — and an unreliable agent cannot be audited even if it keeps logs**.

2026-08-17 snapshot: **188 entries / 9 sections / 132 arXiv papers / 87 GitHub repositories / 16 standards / 1 framework / 5 cross-listed papers**. The README is 565 lines; the self-shipped `tools/check_links.py` runs a title-vs-link audit on every PR with threshold 1.0 — "Part I" vs "Part II" at 0.995 similarity still counts as a disagreement; the 2026-08-17 run crossed 262 destinations with zero disagreements, and even caught a dataset repository that went 404 three days after it last resolved.

## Numbers that cannot be ignored (from the README preface)

- *Towards a Science of AI Agent Reliability* (ICML 2026): **agent capability is rising much faster than agent reliability** — 12 metrics across 15 models confirm the scissors.
- *Who&When* (ICML 2025): the strongest of three attribution methods, on 184 annotated failure tasks drawn from 127 multi-agent systems, identifies the responsible agent in **53.5%** of cases and the decisive error step in **14.2%**.
- *TraceElephant* (ACL 2026): full execution traces lift step-level attribution from 17% to 30% — a **76% relative gain** over output-only traces.
- *MITRE ATLAS* v2026.07 adds three AI Agent Tool Poisoning sub-techniques (AML.T0110.000/.001/.002) and AML.T0115; total 16 tactics / 101 techniques / 77 sub-techniques.
- *Cloak and Detonate*: self-extracting packing bypasses all 8 scanners at >90%; its sandbox auditor catches 97%.
- *Classifier Context Rot*: Opus 4.6 / GPT 5.4 / Gemini 3.1 miss dangerous actions **2–30×** more often after 800K tokens of benign activity.

## Nine sections at a glance (counts re-verified against `tools/inventory.py`)

| # | Section | Count | Main thesis |
|---|---|---|---|
| 1 | Surveys & Foundations | 8 | Establishes the terms of art: agent identifier / monitoring / activity logging |
| 2 | Failure Attribution & Diagnosis | 25 | Attribution scales from 100–200 annotated traces to 12,326 constructed ones (Who&When Pro) |
| 3 | Reliability & Robustness | 11 | pass^k consistency + transactional tool use + anti-rollback; recovery evaluation has no protocol |
| 4 | Runtime Monitoring & Guardrails | 28 | The monitor itself becomes the attack surface — Adaptive Attacks + Classifier Context Rot + SLEIGHT |
| 5 | Audit Trails & Decision Records | 19 | Framework: 5 dimensions (recoverability / coverage / checkability / responsibility / integrity); **cross-vendor schema still missing** |
| 6 | Security Auditing & Scanners | 23 | MCP / skill supply chain gets its own subsection: MCPZoo 64,611 servers, 9.93% inconsistency, 40.55% unauthenticated |
| 7 | Datasets & Benchmarks | 29 | Includes an Evaluation Integrity sub-cluster: BenchJack's 219 reward-hacking flaws |
| 8 | Tools & Platforms | 21 | Observability + sandbox + audit engines; LangSmith transparently flagged `[Managed]` as closed-source |
| 9 | Standards & Governance | 6 papers + 16 standards + 1 framework + 1 tool = 24 | Governance is largely in place (NIST / ISO / EU AI Act / MITRE ATLAS / OWASP / MCP / A2A / C2PA) |

## Eight open gaps (research entry points, ordered by tractability and fit with my agenda)

1. **Cross-vendor decision-record schema** — OpenTelemetry only covers traces; Agent-BOM / ActiveGraph / GRADE each go their own way; no shared schema captures decisions + dependencies + rationale + integrity + responsibility together. Maps to RT-13 AI slop governance.
2. **MCP / skill supply-chain security** — SkillTrace is already at AUROC 0.938, but marketplaces have no in-toto / SLSA-style provenance bar at listing. Maps to RT-12 agent skills.
3. **Monitor adversarial robustness** — Adaptive Attacks + Context Rot + SLEIGHT attack the monitor from three angles; no independent benchmark or monitor-side decision record.
4. **Multi-cause failure attribution** — MP-Bench already shows single-cause benchmarks underestimate model capability; Conformal Agent is nascent; the finite-sample coverage step set is worth nurturing.
5. **Evaluation integrity / benchmark gaming** — BenchJack scored near-perfectly on most benchmarks without solving the task; the natural pivot toward AB-slop / critical-data-studies.
6. **Cost × Reliability Pareto** — *AI Agents That Matter* (TMLR 2025) calls for cost-aware evaluation; the 12 + 4 long-horizon metrics do not include a cost dimension.
7. **Detect-vs-locate half-step problem** — TelemetrySuffBench confirms OTel views retain 99.5–100% detection F1 but fault-origin step accuracy ≤0.5%; HINTBench shows strong models detecting risk but Strict-F1 <35 at locating it. Detection is enough; localisation isn't — the next bottleneck for auditing.
8. **Calibrated abstention as a new dimension** — AgentAbstain: 17 frontier models, best at 59.5% paired; HiL-Bench's Ask-F1. Propose making "when to stop / when to ask" the 9th reliability dimension.

## One meta-observation

The list itself is a self-demonstration of auditability: 188 entries, 9 sections, 5 cross-listed papers made transparent; the audit run names every destination that refuses automated clients (rather than silently treating it as passing); the 4 unaudited destinations (the list's own badges and the pages behind them) are themselves named. Treating the curated list as an "audit artifact for the agent era" is itself a research method, and matches my own [[corpus-first-research-approach]]: take the raw content first (the cloned repository), then synthesize.

## How to use this list

- Find representative papers / tools for a topic: scan the table per section; every row carries a venue + links.
- Reproduce the link audit: `python tools/check_links.py` → writes to `LINK-AUDIT.md`.
- Recount the list: `python tools/inventory.py`.
- Contribute a new entry: `CONTRIBUTING.md` sets the inclusion bar; every entry must have a working link and pass the same audit.

For the full analysis, section-internal branches, and the more precise bridge into my own research agenda, see [note.zh.md](note.zh.md) (Chinese) / [note.en.md](note.en.md) (English).
