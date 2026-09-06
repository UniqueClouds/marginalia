# Do coding agents have taste? What 29,787 Discord messages say about beautiful vs. ugly code

<div class="lang-switch" markdown>
🌐 Language / 语言：[中文](001-code-taste-discord.zh.md) · **English**
</div>

<div class='marg-meta'><span>📅 2026-08-15</span><span>🏷️ analysis</span><span>🐙 issue #1</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-001</td></tr><tr><td>title</td><td>Do coding agents have taste? What 29,787 Discord messages say about beautiful vs. ugly code</td></tr><tr><td>date</td><td>2026-08-15</td></tr><tr><td>published</td><td>2026-08-15</td></tr><tr><td>kind</td><td>analysis</td></tr><tr><td>issue</td><td>1</td></tr></table></details>

> A corpus-first survey of how practitioners actually talk about "beautiful" and "ugly" code in the AI-coding era: 550+ mined hits from four communities, read against Fedorova's ethnography of coding beauty.

Two questions started it. **RQ1:** can coding agents judge elegant vs. ugly code, and learn aesthetic standards that vary *per repository*? **RQ2:** are agents making codebases systematically more complex — and can they be steered to *subtract* (simplify) rather than append?

## Data & method

Corpus-first, as always here: read the raw talk before the literature.

- **Corpus** — my local Discord archive: four AI-engineering communities (Matt's AI Heroes, Latent Space, EleutherAI, Cursor), 51 channels, **29,787 messages** with body text, **2024-11 → 2026-08**.
- **Extraction** — two regex families: RQ1 terms (beautiful / elegant / ugly / aesthetic / clean code / readable) and RQ2 terms (simplify / complex / bloat / verbose / slop / over-engineer / minimal diff / refactor). **550 raw hits**, each rebuilt with a ±6–9 message thread window; a second-pass filter required both a code word and an AI-writing word; then a full manual read of ~15k lines of extracted context.
- **Triangulation** — GitClear's 211M-line change analysis, CodeRabbit's 470-PR audit, METR's randomized controlled trial, and ICLR 2025/2026 evidence on model-side biases.

## Findings

**Six bloat phenotypes** recur across all four communities: test verbosity (2–5× longer than necessary), needless abstraction, comment floods, concept proliferation, entanglement of concerns, and "ticket closed ≠ intent met".

The macro numbers agree:

- **GitClear** (211M changed lines): duplicated code **×4 in five years**; copy/paste overtook "moved" lines for the first time; churn rose from ~3.3% to **5.7% (2024)** and **7.1% (2025)**.
- **CodeRabbit** (470 PRs): AI-authored PRs carry **~1.7× the issue density** of human PRs (10.83 vs 6.45 per PR).
- **METR** (RCT): experienced developers were **19% slower** with AI assistance.

Model-side: self-preference (ICLR 2025), sycophancy, and an RLHF verbosity bias. AesCode-358K (ICLR 2026) shows aesthetics *can* serve as a reward signal — but so far only at the artifact's visual layer.

Reconciling granularities: single-generation quality is passable; the entropy accumulates at the *evolution* granularity.

Voices from the corpus:

> "It's all-over ugly! ... So dirty, I'm surprised it runs." — Yandex interviewee, on foreign code

> "There, it works like this. Just do the same." — imitation as the default norm

> "I've seen LLMs do this in our codebase... we get a swamp of entangled concerns." — KBall

## The Fedorova lens

Fedorova et al., *"Coding Beauty and Decoding Ugliness"* (Science, Technology, & Human Values 50(1):69–93, 2025; three-month field study at Yandex, 26 developer interviews): code aesthetics are not intrinsic properties but locally produced organizational norms. "Beauty" stays plural and deliberately undefined; "ugliness" is concrete, nameable, and *sanctioned* — anything that fails to imitate the existing codebase is ugly. Newcomers are socialized into "not ugly" by imitation; the codebase itself is the teacher.

## Five doors it opened

1. **RepoBench-Aesthetic** — benchmark repo-contextual aesthetic consistency.
2. **MinimalityReward** — diff minimality as an explicit reward.
3. **SimplifyBench** — simplification under functional-equivalence constraints.
4. **Controlled agent-socialization loop** — first controlled test of positive exemplars + cross-model negatives + norm write-back.
5. **The microeconomics of bloat** — does falling regeneration cost depress the marginal value of quality?

Door #0, already taken: → [NOTUGLY-S, musing 003](003-notugly-s.en.md), which formalizes sanction / imitation / not-ugly into a machine-learning objective.

## Provenance

| field | value |
|---|---|
| Data | `discord_workflow/raw/` (4 communities · 51 channels · 29,787 msgs · 2024-11→2026-08); `code_beauty_simplification/corpus_out/` (25 hit files, 550 hits); `fedorova2025.txt` |
| Initial prompt | "Can coding agents judge elegant vs. ugly code — and learn repo-local standards? Are agents making codebases systematically more complex; can they subtract?" |
| Time | analysis 2026-08-15 · note published 2026-08-15 |
| Agent / model | ZCode CLI · GLM (Zhipu) |
| Issue | [#1](https://github.com/UniqueClouds/marginalia/issues/1) |


---

> 🌐 [阅读中文版](001-code-taste-discord.zh.md)

