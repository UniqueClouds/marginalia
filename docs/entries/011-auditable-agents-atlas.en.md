# Awesome Auditable AI — reading note: 188 entries / 9 sections / 132 arXiv papers; how a curated list turns AI agent auditability from a slogan into reliability engineering

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> Language / 语言：[中文](011-auditable-agents-atlas.zh.md) · **English**
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-17</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> analysis (research-map compilation note)</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #26</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-011</td></tr><tr><td>title</td><td>Awesome Auditable AI — reading note: 188 entries / 9 sections / 132 arXiv papers; how a curated list turns AI agent auditability from a slogan into reliability engineering</td></tr><tr><td>date</td><td>2026-08-17</td></tr><tr><td>published</td><td>2026-08-17</td></tr><tr><td>kind</td><td>analysis (research-map compilation note)</td></tr><tr><td>issue</td><td>26</td></tr></table></details>

> Working name **Auditable Agents Atlas**. A "systematic reading of one open-source repo" musing: clone Yue Zhao's `awesome-auditable-ai`, read through all 188 entries by nine sections, run the self-shipped `inventory.py` and `LINK-AUDIT.md` to cross-check the figures, then write down what it establishes, the gaps it leaves open, and how those gaps mate with my own research agenda. Up-front conclusion: **this list turns "AI agent auditability" from a slogan into a synthesis of "reliability engineering + decision accountability"**, and it demonstrates that synthesis on itself — entries can be recounted, links can be re-run, evidence-level can be inspected row by row.

## Musings

"Auditability of AI agents" has been discussed for years, but it kept stalling at the conceptual level: agent identifier, activity logging, post-hoc review — each term used, none with an agreed ruler. Across 2025–2026 three events then arrived and forced the engineering turn:

1. **A failure-attribution baseline appeared** — *Who&When* (ICML 2025) puts numbers on 184 annotated failure tasks: the strongest of three attribution methods identified the responsible agent in **53.5%** of cases and the decisive error step in **14.2%**. Stuck just past half, with the decisive step under two in ten — meaning "when a multi-agent system fails, no one can afterwards explain who or which step". Those 53.5 / 14.2 are the opening figures of this list and the anchor for everything below.
2. **The capability–reliability gap was quantified** — *Towards a Science of AI Agent Reliability* (ICML 2026) uses twelve metrics across fifteen models to confirm that "agent capability is rising much faster than agent reliability". Capability grows fast, reliability barely moves; the cost surfaces after a run, not during it.
3. **Record quality actually closes that gap** — *TraceElephant* (ACL 2026) reports that complete execution traces lift step-level attribution from 17% to 30%, a **76% relative gain**. What matters is log thickness, not log presence.

These three add up to the maintainer's thesis: **reliability is the path, auditability is the destination; an unreliable agent cannot be audited even if it logs everything.** The list is titled "Auditable AI", the subtitle reads "auditing AI agents", and the opening NOTE breaks auditability into four questions — what an agent did, what it relied on, why it acted, whether the action was right. In reliability-engineering terms the first three rest on monitoring and failure attribution; the last rests on decision records. So the real skeleton of the list is reliability engineering + decision accountability; auditability is its reader-facing interface.

## A research map, a dataset, or both

It is both.

- **Research map**: nine sections from surveys down to standards; each row carries a venue field and a one-sentence factual summary. The venue field is honest — 69 rows name a venue, 65 are marked Preprint; a workshop is never upgraded to its host conference, and "accepted" is never abused to fence-post-blur a non-archival venue (see CONTRIBUTING.md's venue rules).
- **An auditable artifact in its own right**: `tools/check_links.py` runs an arXiv title-vs-link audit on every PR with threshold = 1.0; even "Part I" vs "Part II" at 0.995 similarity is treated as a disagreement. The 2026-08-17 run crossed 262 destinations, 129 arXiv titles, 132 arXiv IDs — zero disagreements. It even parks its own four status badges and the pages behind them in "Repository Chrome Not Audited", so a rate-limit on the list's own pages cannot make the audit of everyone else false-pass. This detail is a paradigm: a curated list built as a research artifact.

To reproduce the authoritative entry counts:

```console
$ python tools/inventory.py README.md
entries (occurrences)      188
  across sections          9
    Surveys and Foundations                          8
    Failure Attribution and Diagnosis                25
    Reliability and Robustness                       11
    Runtime Monitoring and Guardrails                28
    Audit Trails and Decision Records                19
    Security Auditing and Scanners                   23
    Datasets and Benchmarks                          29
    Tools and Platforms                              21
    Standards and Governance                         24
table rows                 134
  venue named              69
  labelled Preprint        65
arXiv links (occurrences)  133
arXiv papers (unique)      132
  repeated arXiv URL       1 ['2601.06112']
cross-listed papers        5
GitHub repositories        87
Standards section labels   {'Standard': 16, 'Framework': 1, 'Tool': 1}
```

The numbers match the README's front-matter claims word for word. This "author claim → script recompute → citation check" three-layer architecture is itself a structural version of [[corpus-first-research-approach]] — fetch the raw content (a repository clone) first, then synthesize; never write from a second-hand summary.

## Going through the nine sections

Each section below records the count, the thesis, the 3–5 most representative entries, and the gaps it leaves.

### 1. Surveys and Foundations (8 entries)

The foundation section. Eight surveys / position papers from 2024 onward — "auditability" as term, engineering goal, accountability framework is built here.

Three worth keeping:

- *Visibility into AI Agents* (FAccT 2024): earliest to put agent identifier + real-time monitoring + activity logging on equal footing as measures to make agent behaviour accountable. This is where the list begins equating auditability with visibility.
- *TrustAgent* (KDD 2025): splits trustworthy-agent components into intrinsic (brain, memory, tool) and extrinsic (user, other agents, environment), mapping attacks and defenses onto each. This intrinsic–extrinsic decomposition scaffolds the later sections where "tool-chain poisoning vs agent's own reasoning failure" is classified.
- *AgentOps: Enabling Observability of LLM Agents* (Preprint 2024): maps observability for agents, listing the artifacts and trace data to record across the lifecycle. Note "observability" is not "auditability" — the former targets debugging and control, the latter emphasises post-hoc reconstruction and accountability. The two overlap but are not identical; the list covers both by extension.

### 2. Failure Attribution and Diagnosis (25 entries, joint-largest)

The attribution section — this list's genuinely heavyweight contribution: 25 entries around "something went wrong, who did it, which step".

Three pivotal numbers:

- *Who&When* (ICML 2025): the original 184 annotated failure tasks across 127 multi-agent system logs; strongest method 53.5% responsible agent / 14.2% decisive error step. The baseline.
- *Who&When Pro* (Preprint 2026) scales to **12,326 failed trajectories** with golden labels constructed by "exactly replaying a successful prefix and injecting a single failure", crossing 26 source benchmarks × 3 modalities. **This is the turning point that pushes ground truth from a few hundred manually annotated trajectories into the tens of thousands.** Note the list's own honesty in the open-gaps paragraph: "manually annotated sets remain in the low hundreds of trajectories and scale now comes from construction rather than annotation." For my research agenda this directly validates [[corpus-first-research-approach]] — even data scaling is now construction-driven, not annotation-driven.
- *TraceElephant* (ACL 2026): benchmark + conclusion — full execution traces lift attribution from 17% to 30% (**76% relative gain**).

Method lineage (the 25 entries sort into four generations):

| Generation | Representative | Philosophy |
|---|---|---|
| 1st (manual annotation) | Who&When, MAST, TRAIL | 100–150 expert-examined traces; from failure taxonomy back to attribution |
| 2nd (construction-scale) | Aegis (9,533) / Who&When Pro (12,326) | Replay a successful prefix, inject a single-point failure, build controllable ground truth |
| 3rd (automation & consistency) | AgenTracer (ICLR 2026, 8B attribution model) / StepFinder (KDD 2026, temporal-semantic encoding) / ErrorProbe (ACL Findings 2026, annotation-free self-improvement) | No human labels; rely on structure, context, executable evidence |
| 4th (controlled guarantees & long-horizon) | Conformal Agent Error Attribution (finite-sample coverage step set) / SAFARI (short-memory long-horizon attribution, +20% at 1M token budget) | With mathematical guarantees and breaking the long-context limit |

This lineage exposes at least two things: (i) data exists but is still nowhere wide enough — MP-Bench already argues "model weakness is benchmark single-root-cause design, not capability"; (ii) attribution on long / branching traces still undershoots practice — the list preface flatly says "accuracy on long, branching, multi-agent traces stays below what practice needs".

Entries worth a closer look:

- *Failure as a Process: An Anatomy of CLI Coding Agent Trajectories* (Preprint 2026): 1,794 CLI coding trajectories / 63,000 steps / 7 models / 3 scaffolds; conclusion: **most failures are epistemic, begin early, stay hidden until recovery is impossible**. This pairs naturally with [[transformer-teaching-workspace]] — students should read trajectory, not stdout.
- *Tracing Agentic Failure from the Flow of Success* (Preprint 2026): trains a one-class neural controlled differential equation on 100 successful trajectories only and scores deviation; +20% in-domain F1, 200–5000× faster than prompting baselines. "Successful flow" used as a negative prior.
- *GRADE* (one of the maintainer's own components): one graph per run, two edge layers — execution (what ran in what order) and dependency (what each step relied on); across six corpora **run size carries little signal; the dependency layer is what predicts failure**. This technique likely applies to [[research-citation-network-ai]]: is a highly cited paper constraining follow-on research to its dependency layer?

### 3. Reliability and Robustness (11 entries)

Only 11, but they establish that **reliability is decomposable and measurable**.

- *ReliabilityBench* (Preprint 2026): three axes — repeated runs at the same task under the same conditions (pass^k consistency), robustness to semantically equivalent perturbations, fault tolerance under injected tool/API failures. The list's minimal measurable reliability set.
- *τ-bench* (ICLR 2025) introduces **pass^k**: does the agent solve the same task on all of k independent trials. "Succeed once" and "succeed every time" are different things — a recurring list point from the engineering angle.
- *Towards a Science of AI Agent Reliability* (ICML 2026) decomposes reliability into 12 metrics across consistency / robustness / predictability / safety — the core evidence for the capability–reliability scissors in the list preface.
- *Beyond pass@1* (Preprint 2026) proposes four new long-horizon reliability metrics: reliability decay curve, variance amplification, graceful degradation, meltdown onset; 10 models × 23,392 episodes. The **"meltdown onset"** metaphor likens long-horizon agents to a reactor going supercritical — useful beyond traditional pass@1.
- *PALADIN* (AAAI 2026 Workshop): trains agents to detect and recover from tool malfunctions themselves — the first explicit evaluation of "recovery".
- *Atomix* (Preprint 2026): wraps tool use in progress-aware transactions that commit only after per-resource frontiers rule out earlier conflicting work, at microsecond-scale overhead. ACID for agentic tool calls.
- *ACRFence* (ASPLOS 2026 Workshop): names **semantic rollback attacks** — an agent re-synthesises a slightly different request after restore and the server treats it as new, enabling duplicate payments and credential reuse. A new attack surface against an otherwise safe checkpoint-restore mechanism.
- *ProtocolBench* (ICML 2026) compares A2A / ACP / ANP / Agora on success / latency / message overhead / failure robustness; completion time varies up to 36.5% across protocols in the Streaming Queue scenario; end-to-end latency differs by 3.48 s. "Multi-agent" is not "pick one framework and done".

Section gap: **recovery evaluation lacks a protocol**. ReliabilityBench evaluates injected faults, PALADIN reports recovery metrics, but there is no cross-system shared recovery protocol or metric suite. The list flags this as an open gap.

### 4. Runtime Monitoring and Guardrails (28 entries, the largest section)

Monitoring and guardrails — the largest section, and the one with the sharpest reversal: **the monitor itself is becoming the new attack surface**.

Classical cluster (monitoring the agent):

- *Llama Guard* (Preprint 2023): input / output two-side safety-taxonomy filter.
- *GuardAgent* (ICML 2025): reads safety requirements → generates a check plan → compiles it into guardrail code that checks the target agent's actions at runtime with no retraining.
- *G-Safeguard* (ACL 2025) / *GUARDIAN* (NeurIPS 2025) / *SentinelAgent* / *AgentSentinel* (CCS 2025): model multi-agent collaboration as a graph and use GNN / temporal graph encoder to find anomalous nodes.
- *ProbGuard* (ASE 2026): discrete-time Markov chain estimates the probability of reaching an unsafe future state, warn / intervene before a violation.
- *AgentSpec* (ICSE 2026): trigger + predicate + enforcement-action rule language; prevents 90%+ unsafe code-agent executions at millisecond overhead.

What actually stuns this section is the three papers where monitors are the target:

- *Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols* (ICLR 2026): an untrusted model that knows the control protocol and the monitor embeds prompt injections in its own outputs to evade language-model monitors; the Defer-to-Resample protocol even amplifies that injection into a best-of-n attack. **Monitor "visibility" becomes its attack entry point.**
- *Reliable Weak-to-Strong Monitoring of LLM Agents* (ICLR 2026): tests monitoring of a stronger agent for covert misbehavior on SHADE-Arena and CUA-SHADE-Arena — conclusion: **monitor scaffolding matters more than monitor awareness**; escalating only pre-flagged cases to human reviewers raises the true-positive rate ~15% at a 0.01 false-positive rate.
- *Classifier Context Rot* (Preprint 2026): the closest kin to "context grows long and the model drifts", and this one quantifies it: **Opus 4.6 / GPT 5.4 / Gemini 3.1 miss dangerous actions 2–30× more often after 800K tokens of benign activity.** Monitors have the "long-context can't hold nuance" bug too — a new monitor-side critical-data problem, the inverse face of the same coin as [[nuance-in-scientific-writing-seed]].
- *SLEIGHT-Bench* (Preprint 2026): 40 covert attacks across 11 evasion categories; an Opus 4.6 monitor with extended thinking catches 32% overall and 20 of 40 are never caught at 1% false-positive across 10 trials.

Plus abstention:

- *AgentAbstain* (Preprint 2026): 263 act-vs-abstain task pairs across 42 executable environments; the best of 17 frontier models reaches 59.5% paired accuracy, and **some agents execute irreversible actions before recognising a reason to stop**. This measures "knows when not to act" as a reliability dimension — the "calibrated abstention" open gap.
- *HiL-Bench* (Preprint 2026): human-in-loop, hides human-validated blockers in SE and text-to-SQL tasks and scores selective escalation with an Ask-F1 metric. When to ask for help?

Two guardrail tools worth flagging:

- *NeMo Guardrails* (NVIDIA): Colang-defined policies run before and after the LLM call.
- *LlamaFirewall*: PromptGuard 2 (jailbreak / injection detection) + AlignmentCheck (CoT goal-hijack auditor) + CodeShield (static analysis across 8 languages). License is Llama 3.2 Community License, **not OSI open source** — the list notes this directly in the description.

Sharp reversal of the section: **monitor success depends on whether the attacked object holds information about the monitor**. This shifts the research question from "build a good monitor" to "how does a monitor survive an adversary who has read its source?" It is the natural junction between RT-13 "AI slop governance" and critical-data studies.

### 5. Audit Trails and Decision Records (19 entries)

The thesis: **records are not logs; they are post-hoc reconstructable action credentials**.

Three keepers + one framework:

- The maintainer's own *Auditable Agents* (ACM AI Leadership Summit 2026) defines **5 auditability dimensions + an Auditability Card**:
  1. **action recoverability**
  2. **lifecycle coverage**
  3. **policy checkability**
  4. **responsibility attribution**
  5. **evidence integrity**
  
  These five are the list's core abstraction — the syllabus of an "AUDITABLE" course.

- *auditable* (tool): records the inputs a committed action relied on, re-evaluates it against current state, and reverses it through a pluggable rail when supporting conditions no longer hold. The framework's "recover" mechanism instantiated.
- *GRADE* (graph representation): execution layer + dependency layer in one graph; predicts failure and localises the faulting step. The framework's "represent" mechanism instantiated.

Around these three, the rest of the section fills out the framework's missing pieces:

- *Agent-BOM*: a unified hierarchical attributed graph that captures capability bindings / cognitive-state evolution / memory contamination / cross-agent risk propagation. Extends the graph representation to security audit.
- *ActiveGraph* / *The Log is the Agent*: append-only event log as canonical record, the working graph derived from the log. Supports replay and forks. This is close to [[marginalia-repo-workflow]]'s "issue → PR → squash commit + provenance frontmatter" — append-only-event-log thinking is already in yunqi's git workflow.
- *MemLineage* (Preprint 2026): each memory entry signed per principal over an RFC 6962 Merkle log; refuses sensitive actions whose active justification descends from external content. Drives attack success to zero on three memory-poisoning workloads and six AgentDojo banking pairs at sub-millisecond overhead. **This is Certificate Transparency's Merkle pattern applied to agent memory** — a beautifully clean research contribution.
- *TRACE* (watermark): two-channel complementary embedding — the action selection channel is distortion-free, the tally channel is keyed on log structure alone, so a reseller who rewrites the log cannot erase attribution; detection survives deletion of 70% of steps. **Defends against "the reseller rewrites the log to erase attribution"** — treats the user record itself as an adversary in the threat model.

Tools subsection, 8 by license / stack:

| Tool | Lang | Key tech | License |
|---|---|---|---|
| MakerChecker | TypeScript | role-based + human approval gates + Ed25519 hash-chained log | AGPL-3.0 |
| aegis | TypeScript | runtime policy enforcement + kill switch | MIT |
| halo-record | Python | dependency-free SHA-256 hash-chained JSONL + RFC 3161 timestamp | Apache-2.0 |
| Agent Governance Toolkit | Python | Microsoft; control mappings to OWASP Agentic Top 10 / NIST AI RMF / EU AI Act / SOC 2 | MIT |
| TRACE | Python | hardware attestation + TEE; offline-verifiable | CC BY 4.0 spec + Apache-2.0 tooling |
| AgentLens | TS / Py | MCP-native + append-only SHA-256 hash-chained | MIT |
| auditable | Python | maintainer's own; reversible committed action | Apache-2.0 |
| Proofline | Python | content-addressed proof packet + human approval gate | MIT |

What is worth flagging: **no tool implements a cross-vendor schema**. Each has its own hash chain / Merkle / Decision BOM structure, none mutual-align across tools. The list names this in the open gaps: "no widely adopted cross-vendor schema captures decisions, dependencies, rationale, integrity, and responsibility together." Concept clear, tools scattered, schema missing. This junction flows directly into RT-13 "AI slop governance" in [[se-topics-from-aihero-discord]] — the lowest layer of governing AI slop is "first, have a verifiable decision-record schema".

### 6. Security Auditing and Scanners (23 entries)

Treat the agentic system as a software system; do static analysis + dynamic scanning.

Main subsection (11) covers attack surface / injection / memory poisoning:

- *Agent Audit* (CAIS 2026): static security analysis of agent code and config, tool-boundary taint tracking + MCP config audit; the companion tool `agent-audit` lives in Scanners.
- *InjecAgent* (ACL Findings 2024) / *AgentDojo* (NeurIPS 2024 Datasets Track): injection benchmark foundations — 1,054 cases / 97 tasks + 629 security tests.
- *Agent Security Bench (ASB)* (ICLR 2025): 10 injection attacks + memory poisoning + Plan-of-Thought backdoor + 4 mixed attacks + 11 defenses across 13 backbones × 10 scenarios × 400+ tools; peak average ASR **84.30%**.
- *MINJA* (NeurIPS 2025): **query-only** injection of malicious memory records, success above 90% in most configurations — poisoning memory without direct write access.
- *MemSecBench* (Preprint 2026): follows 310 memory-poisoning cases from persistence to consequence to repair, across 24 harness / backend / model combinations — **84.2% persistence / 50.3% full-chain success / 56.1% selective repair among successfully poisoned cases**.
- *StepJack* (Preprint 2026): decomposes an adversarial goal into innocuous sub-steps along the navigation path; raises ASR on 3 of 6 computer-use agents by up to 31.2 points across 480 examples.
- *StakeBench* (Preprint 2026): scores prompt-injection harm by stakeholder (user / seller / platform) over 264 executable cases from 22 templates on a live e-commerce environment — indirect injection succeeds 41.67–68.16% and the **same agent shows a distinct failure profile per stakeholder**. **"Who can be hurt" becomes a new dimension** — matches [[research-agenda-proposals]] direction on AI and inequality.
- *Defeating Prompt Injections by Design* (SaTML 2026): extracts control / data flow from the trusted query so untrusted retrieved data cannot affect program flow, with capability-based tool-call policy. Solves 77% of AgentDojo tasks with provable security vs 84% for an undefended system.
- *SoK: The Attack Surface of Agentic AI* / *Design Patterns for Securing LLM Agents against Prompt Injections* (six patterns): exports "trust boundary" as a pattern language.

MCP / Skill Supply Chain subsection — 8 entries, given its own subsection because supply chain risk sits above agent reasoning risk:

- *Rethinking MCP Security* (Preprint 2026): builds **MCPZoo from 64,611 unique MCP servers** (37,288 support dynamic analysis); **existing scanners flag 96.89% of servers as risky at 45.53% average alert precision** — almost half the alerts are false positives.
- *Description-Code Inconsistency in Real-World MCP Servers* (Preprint 2026): structure-aware static analysis on 19,200 description-code pairs from 2,214 real servers; **9.93% of descriptions misstate what the tool code does**.
- *A First Measurement Study on Authentication Security in Real-World Remote MCP Servers* (Preprint 2026): 7,973 live remote servers, **40.55% expose tools with no authentication**; 325 flaws and 9 CVE identifiers from 119 OAuth-enabled servers.
- *SkillTrace* (Preprint 2026): audits marketplace-skill reuse across expression / implementation / operational traces — AUROC 0.938, F1 0.898 (820 transformed positives × 751 negative controls), auditing **36,446 marketplace skills**.
- *Cloak and Detonate* (Preprint 2026): self-extracting skill packing bypasses all 8 tested scanners at >90% across 1,613 in-the-wild malicious skills; the same author's sandbox auditor detects 97% of benchmark attacks at 2% FPR and 87% of real-world malicious skills. **Scanner and bypass are already racing**.
- *OpenSkillRisk* (Preprint 2026): 263 marketplace skills across 7 threat categories; the safest of 3 frameworks / 13 models still executes unsafe actions ~17% of the time.

Scanners subsection — 4 tools: `agent-audit` / `garak` (NVIDIA) / `Agentic Radar` (splx-ai) / `Snyk Agent Scan`. `Snyk Agent Scan` is explicitly marked "an open-source client to a commercial service" — requires a Snyk API token. This "honest flag of closed-source backend" is the list enforcing its inclusion bar.

The whole section is a nuclear arsenal: MCPZoo 64,611 servers, 9.93% description-code inconsistency, 40.55% unauthenticated, 9.5 in 10 malicious skills slip past 8 scanners. RT-12 "agent skills" no longer lacks a threat model.

### 7. Datasets and Benchmarks (29 entries, tie-largest with #2)

The dataset section. One important faceting decision: the list splits **Evaluation Integrity** as its own subsection, acknowledging **the measuring instrument itself deserves an audit**.

Common subsection (23) covers SWE-bench (ICLR 2024), SWE-agent (NeurIPS 2024), AgentBench (ICLR 2024), GAIA (ICLR 2024), WebArena (ICLR 2024), OSWorld (NeurIPS 2024), Terminal-Bench 2.0 (ICLR 2026), AppWorld (ACL 2024), ToolEmu (ICLR 2024), τ²-Bench (ICML 2026), AgentBoard (NeurIPS 2024), WildClawBench, ClawBench, MemoryAgentBench (ICLR 2026), HINTBench, OS-Harm, R-Judge, TelemetrySuffBench.

Two worth singling out:

- *TelemetrySuffBench* (Preprint 2026): compares metadata, OpenTelemetry-compatible, and OpenInference-compatible views — **detection F1 99.5–100% but fault-origin step accuracy ≤0.5%**. "Can detect that something went wrong" and "Can localise where it went wrong" are decoupled by telemetry granularity, and telemetry sufficiency is far below intuition. Combined with Classifier Context Rot, this declares today's telemetry + classifier nowhere near an adequate audit base.
- *HINTBench* (Preprint 2026): 629 trajectories (523 risky / 106 safe) averaging 33 steps, a **benign-condition** risk benchmark; strong models detect trajectory-level risk but fall below 35 Strict-F1 at locating the risky step. **Localising risk under benign conditions is a new problem class.**

Evaluation Integrity subsection (5 entries) — the list's meta-audit layer:

- *BenchJack* (Preprint 2026): red-teams 10 agent benchmarks, **surfaces 219 distinct reward-hacking flaws across 8 recurring classes, scores near-perfectly on most benchmarks without solving a single task**, then patches four below a 10% hackable-task ratio and fully repairs WebArena and OSWorld in three iterations. **Benchmark gaming quantified for the first time** — connects to "evaluation integrity" in [[chi-acl-storytelling-quantification]]; AI slop is not only in paper writing but also in evaluation systems gaming.
- *AgentRewardBench* (COLM 2025): 1,302 web agent trajectories × 5 benchmarks × 4 models, expert-reviewed; **12 LM judges scored; the rule-based evaluation of common benchmarks under-reports agent success**. Neither LM judges nor rule-based ones are reliable.
- *AgentAuditor* (NeurIPS 2025): training-free, memory-augmented; lifts LM safety evaluators toward human-expert accuracy. Ships ASSEBench (2,293 annotated records / 15 risk types / 29 scenarios).
- *SpecBench* (Preprint 2026): separates visible validation tests from held-out compositional tests across 30 systems-level tasks; **pass-rate gap grows 28 points per tenfold increase in code size** — the more code, the less visible tests reflect true capability.
- *AI Agents That Matter* (TMLR 2025): predates the other four by years; a foundational call — cost-aware evaluation, adequate holdout, reproducibility alongside accuracy. The most-cited source among the rest.

HF / GitHub output datasets:

- *TRAIL* (HF): 148 trajectories / 841 errors.
- *Aegis* (HF): 9,533 trajectories, constructive injection.
- *Who&When* (GitHub): 127 multi-agent system logs.

Section gap: **benchmark attack surface, evaluation integrity, and cost × Pareto converge into one cluster.** The list's separately naming them signals that the maintainer expects "benchmark integrity research" to graduate into its own section.

### 8. Tools and Platforms (21 entries)

Observability + sandbox. Three observations:

1. **OTel is the de facto substrate** — Langfuse, Arize Phoenix, OpenInference, OpenLLMetry, Helicone, TruLens, Laminar all use OpenTelemetry. This matches Section 9's OpenTelemetry GenAI Semantic Conventions as a de facto standard; telemetry standardisation is engineering fact, not research question.
2. **Sandbox as standalone category** — E2B, Microsandbox. Wraps high-risk execution in microVMs. Microsandbox: average boot under 100 ms, in-process spawn, hardware-level isolation. Useful for the [[yunqi-learning-style]] first-principles teaching track: why microVM isolation is stronger than a container.
3. **Audit engine as a new class** — AgentDebugX (Who&When: 28.8% exact agent-and-step accuracy vs 21.7% for the strongest single-pass baseline), Docent, AgentRunProof (deterministic runtime-conformance harness for the OpenAI Agents SDK, writes content-addressed evidence re-checkable without re-running the SDK), A2E (multi-dimensional: execution efficiency / tool use / task planning / error recovery). **"Agent audit engine" is branching off from "observability tool"** — the same process as Section 5's "audit trail is not a log", reflected on the tool side.

LangSmith is explicitly marked `[Managed]` and described as "Commercial product, not open source." CONTRIBUTING.md explains: a closed-source managed service is listed only when wide-adopted enough that omitting it would falsify the field's picture, and then it must be marked `[Managed]`. This is the list using engineering ethics to enforce its inclusion bar.

### 9. Standards and Governance (24 entries)

Governance: 6 papers, 16 Standards, 1 Framework, 1 Tool (Rekor, included as the transparency-log pattern source that agent trails reuse).

The six governance papers; **Black-Box Access is Insufficient for Rigorous AI Audits** (FAccT 2024) flatly argues that meaningful third-party AI audits need more than query access — comparing black-box, white-box, and outside-the-box methods. This is the list's theoretical warrant for broadening auditability from "logs visible" to "source / model / training data inspectable".

16 Standards by issuing body:

| Category | Entries |
|---|---|
| Protocol | MCP / A2A / AP2 (FIDO Alliance, payment authorisation) |
| Telemetry | OpenTelemetry GenAI Semantic Conventions (`gen_ai.*` deprecated in the core semantic-conventions repo at v1.42.0 and moved to a dedicated repo) |
| Risk framework | NIST AI RMF 1.0 / NIST AI 600-1 GenAI Profile |
| Regulation | EU AI Act Art. 12 record-keeping (≥6-month retention); Digital Omnibus on AI (Regulation (EU) 2026/1744, in force 27 July 2026) moves high-risk application to 2 Dec 2027 for Annex III areas, 2 Aug 2028 for AI embedded in regulated products |
| Management system | ISO/IEC 42001:2023 — first certifiable AI management system standard |
| Threat landscape | MITRE ATLAS v2026.07 — 16 tactics / 101 techniques / 77 sub-techniques / 37 mitigations / 68 case studies; adds AML.T0110.000/.001/.002 AI Agent Tool Poisoning and AML.T0115 |
| Risk lists | OWASP Top 10 for LLM Applications / OWASP Top 10 for Agentic Applications 2026 + Securing Agentic Applications Guide 1.0 |
| Software weakness | CWE-1427 (Improper Neutralization of Input Used for LLM Prompting) |
| Threat modelling | MAESTRO (CSA) Framework — **note the list flags it as "single-author blog rather than a ratified standard"**; lower evidence register than NIST / ISO / MITRE / OWASP — the list's first explicit evidence-register grading on a framework |
| Content provenance | C2PA / Content Credentials v2.2 |

The list also groups the "origin standards for verifiable-log and attestation patterns": Certificate Transparency (RFC 6962 / 9162), in-toto Attestation Framework, SLSA, DSSE, Rekor. These five are the source techniques that Section 5's tools build on (MemLineage uses RFC 6962, halo-record uses RFC 3161, Agent Governance Toolkit uses a Merkle chain). **This group is necessary to truly understand Section 5**: agent decision records are not invented from nothing, they inherit from software supply-chain provenance.

Biggest observation: **governance is well-stocked on protocols, risk frameworks, threat landscapes, certifiable management systems; only the cross-vendor decision-record schema is missing**. Same gap, viewed from the other side of Section 5.

## The 8-dimensional Reliability Map

Alongside the framework's 5 auditability dimensions, the list's `assets/reliability-map.png` fragments reliability into 8 dimensions. The 5 + 8 together are this list's two-layer skeleton.

| Dimension | Starting sections | Current coverage |
|---|---|---|
| Consistency and Determinism | Reliability / Datasets | **Weakest**: only 8 direct resources |
| Robustness | Reliability / Security | 76 |
| Fault Tolerance and Recovery | Reliability / Tools | data from PALADIN / Atomix / ACRFence; no protocol |
| Runtime Monitoring | Monitoring / Tools | monitor-as-attack-surface is the focal reversal |
| Failure Attribution and Diagnosis | Failure Attribution / Datasets | generations 1–4 complete |
| Decision Records and Accountability | Audit Trails / Standards | concept clear, schema scattered |
| Security Review | Security / Monitoring | 76 entries — the largest dimension |
| Evaluation and Benchmarks | Datasets / Tools | includes an Evaluation Integrity meta-layer |

The list notes explicitly: "Consistency and Determinism is the least represented dimension here, with eight direct resources against 76 for Security Review. That gap reflects where the field has put its effort, not a deliberate editorial choice." **Low coverage = research opportunity** — the list's plain statement of a gap.

## Eight open gaps (research entry points)

The list consolidates an "Open gaps" list of 11; I merge adjacent ones and order by tractability (existing tools / conceptual seeds / connection to my agenda):

1. **Cross-vendor decision-record schema.** OpenTelemetry GenAI only covers traces; Agent-BOM / ActiveGraph / GRADE each ship their own structure; none unites decision + dependency + rationale + integrity + responsibility into one schema. **Double-blank between Section 5's end and Section 9's governance papers.** Immediately tractable — union the four existing representations into a reference schema.
2. **MCP / skill supply-chain security.** SkillTrace already reaches AUROC 0.938 in production audit; marketplaces have no in-toto / SLSA-style provenance requirement at listing; Description-Code Inconsistency 9.93% is already material. **Directly maps to RT-12 "agent skills";** next step is research on the "three marketplace gates" (description-code consistency / sandbox replay / provenance signature) and whether 9.93 can be pushed down to 1.
3. **Monitor adversarial robustness.** Adaptive Attacks + Classifier Context Rot + SLEIGHT three-pronged attack on monitors; no independent benchmark or test protocol validates "the monitor itself still works under adversarial conditions". Research task: **monitoring the monitor — a red-team benchmark for monitors + a monitor-side decision record**. Overlaps with [[chi-acl-storytelling-quantification]]'s "evaluation integrity" layer.
4. **Multi-cause failure attribution.** MP-Bench argues single-cause benchmarks underestimate model capability; Conformal Agent is nascent; the finite-sample coverage step set is worth nurturing. Next step: **compute multi-cause subset statistical power on Who&When Pro / TraceElephant and propose a guaranteed multi-cause localisation**.
5. **Evaluation integrity / benchmark gaming.** BenchJack surfaces 219 reward-hacking flaws across 10 benchmarks; SpecBench pass-rate gap +28 points per 10× code; AgentRewardBench shows rule-based and human-evaluation both unreliable. Research task: **benchmark the benchmark** — automated discovery of "near-perfect score but task unsolved" exploit classes, with patches. Connects to [[dourish-style-analysis]]'s downstream critical-data research. The critical vs empirical seam is one I would push toward critical-data studies, leaning on the BDS baseline of [[discipline-style-analysis]].
6. **Cost × Reliability Pareto.** *AI Agents That Matter* calls for cost-aware evaluation; the 12 + 4 long-horizon metrics lack a cost dimension. Research task: **define a cost-adjusted reliability metric and recompute all 8 sections' benchmarks.** This is the work that sews Section 3 and Section 7 together.
7. **Detect–locate half-step problem.** HINTBench + Classifier Context Rot + TelemetrySuffBench jointly signal that **existing telemetry gives detection F1 99.5–100% but localisation accuracy ≤0.5% / Strict-F1 <35**. Research task: a new intermediate representation between the OTel span and the GRADE graph for "half-step localisation." Closest to the engineering landing point of [[se-ai-ccfb-survey-2026]].
8. **Calibrated abstention as a new dimension.** AgentAbstain: best of 17 frontier models at 59.5% paired accuracy; HiL-Bench's Ask-F1. Propose "when to stop / when to ask for help" as the 9th reliability dimension. Cleanest task: combine the two existing benchmarks into a cross-scenario abstain benchmark and push the Reliability Map to a 9th dimension.

## Connections to my own research agenda

Mapping my own agenda handles to the hits in this list:

| My agenda | List section / row hit | Leverage point |
|---|---|---|
| [[research-citation-network-ai]] AI and knowledge flows | Failure-attribution GRADE dependency layer; *Tracing Agentic Failure from the Flow of Success* | lift the "successful flow" controlled-ODE idea to "guided-successful paths" — is a highly cited paper constraining follow-on research to its dependency layer? |
| [[se-topics-from-aihero-discord]] RT-4 AI-ready codebase | SWE-bench / SWE-agent / Terminal-Bench / SpecBench / BenchJack | benchmark gaming is RT-4's mirror threat — AI-ready code may include training to hack the benchmark |
| [[se-topics-from-aihero-discord]] RT-12 agent skills | MCP / skill supply chain submodule (8 entries) + SkillTrace / Cloak and Detonate / OpenSkillRisk | RT-12's threat model is ready-made; next step is research on the three gates (description-code consistency / sandbox replay / provenance signature) |
| [[se-topics-from-aihero-discord]] RT-13 AI slop governance | §5 missing decision-record schema; §7 Evaluation Integrity 5 entries | the lowest layer of governing AI slop is "verifiable decision record + gaming-resistant evaluation" |
| [[chi-acl-storytelling-quantification]] | Evaluation Integrity subsection / Classifier Context Rot | "storytelling" expands to "benchmark storytelling" — AgentRewardBench and BenchJack give critical-data research a numerical window |
| [[nuance-in-scientific-writing-seed]] | Classifier Context Rot (monitor nuance rises and falls) | the monitor losing nuance under long context is the monitor-side instance of AI nuance rises / falls — the same coin, the other face |
| [[abbott-fractal-vs-benz-homology-seed]] | multi-cause failure attribution + MP-Bench argument | "single-cause" as a benchmark design assumption is the seam between Abbott's "fractal distinction" critique of treating analysis as the object itself |
| [[dourish-style-analysis]] / [[discipline-style-analysis]] | evidence register wording | the maintainer flagging MAESTRO as "single-author blog rather than a ratified standard" is an instance of evidence-register academic-writing style |
| [[transformer-teaching-workspace]] | *Failure as a Process* — 1,794 CLI trajectories | the "from-scratch Transformer" course should have students read trajectory, not stdout |
| [[marginalia-repo-workflow]] | ActiveGraph — "the log is the agent" | yunqi's git workflow (append-only event log + provenance frontmatter) is already an instance of this |
| [[research-agenda-proposals]] CSS direction | StakeBench — stakeholder-centric | AI-and-inequality research connects directly with "same agent, distinct failure profile per stakeholder" |

## One meta-observation

The list itself does four things beyond a normal awesome list, jointly treating the curated list as an audit artifact:

1. **Claims and products are synchronised.** Every quantity in the README preface (188 entries / 9 sections / 132 unique arXiv / 87 GitHub / 5 cross-listed / 16 standards) is recomputed by `tools/inventory.py`; the author claim equals script output.
2. **Link / title three-layer verification.** `tools/check_links.py` checks (a) link accessibility, (b) agreement between the arXiv page's `citation_arxiv_id` and the URL, (c) agreement between the arXiv page's `citation_title` and the list's title — threshold = 1.0, even "Part I" vs "Part II" at 0.995 similarity is scored as disagreement. `tools/test_check_links.py` turns every "audit might false-pass" path into a test, run on every PR.
3. **Destinations refusing automated clients are named explicitly.** `LINK-AUDIT.md` separates "unresolved" from "known bot wall" — pages that refuse bots are flagged, not silently counted as passing. **Audit honesty**: report not only pass but also "unable to verify", and separates the latter from the former.
4. **The list's own badges are not audited.** The list's four own status badges and the pages behind them sit in "Repository Chrome Not Audited" — the list's own pages' rate-limit cannot fail the audit of everyone else's links; the badge reporting the audit result cannot decide that result. This is the methodological separation of "measuring instrument" and "measured object".

These four together make the abstract topic of "auditable agent" concrete on the list itself. My research-method preference is [[corpus-first-research-approach]] — take raw content first, synthesize second, never write from a second-hand summary. The list's maintainer is plainly the same kind — so reading this list is reading not only the content but also a model of "how to make a research artifact".

## Citation and reproducibility

- List main link: <https://github.com/yzhao062/awesome-auditable-ai>
- Maintainer: Yue Zhao, USC-FORTIS lab; author of [PyOD](https://github.com/yzhao062/pyod) and co-author of [ADBench](https://github.com/Minqi824/ADBench). Google Scholar page: [zoGDYsoAAAAJ](https://scholar.google.com/citations?user=zoGDYsoAAAAJ&hl=en).
- Framework paper: Nian, Yuan, Zhang, Li, Zhao. *Auditable Agents*. arXiv:2604.05485. ACM AI Leadership Summit 2026.
- Self-audit scripts: `python tools/inventory.py README.md` / `python tools/check_links.py README.md --out LINK-AUDIT.md`; standard library only, Python 3.12.
- License: CC0-1.0 (list and code together in the public domain); individual tools may carry their own licenses (each row has a license field).
- CONTRIBUTING.md lays out the inclusion bar: an entry must be "directly useful for auditing an AI agent"; tools must have an inspectable public source repository; a closed-source managed service is listed only when wide-adopted enough that omitting it would falsify the field picture, and then it is marked `[Managed]`; the venue field records what the venue is, not its strength; a workshop is never upgraded to its host conference.

My local clone is at `/tmp/aaa-audit/` (machine-local temp); to re-reproduce this audit, `git clone --depth 1 https://github.com/yzhao062/awesome-auditable-ai` then run `inventory.py` and `check_links.py`.

## Next steps (optional follow-up)

1. **Concretise the missing Section 5 schema.** Synthesise Agent-BOM, ActiveGraph, GRADE, Auditable Agents framework, Agent Governance Toolkit into a cross-vendor reference schema; track in a marginalia entry 012.
2. **MCP supply chain three-gate experiment design document.** Description-code consistency detection (push 9.93% → ?); sandbox-replay risk (Cloak and Detonate, 87% real-world malicious detection); provenance signature (use the in-toto Attestation Framework across marketplaces).
3. **Monitor adversarial benchmark.** Synthesise Adaptive Attacks / SLEIGHT / Classifier Context Rot / Reliable Weak-to-Strong Monitoring / Adaptive Attacks on Trusted Monitors into a single monitor red-team suite; propose a monitor-side decision-record requirement.
4. **Add "calibrated abstention" as the 9th Reliability Map dimension.** Pair AgentAbstain + HiL-Bench into a cross-scenario combined test. The list marks this "emerging" in the open gaps — somebody should graduate it to "existing".

— End. Companion summary card: [artifact.en.md](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/011-auditable-agents-atlas/artifact.en.md).


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [阅读中文版](011-auditable-agents-atlas.zh.md)

