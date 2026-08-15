---
id: marginalia-005-artifact-skill
title: "Artifact: the academic-voices five-register polishing skill"
date: 2026-08-16
published: 2026-08-16
kind: artifact
sources:
  - "C:/Users/yunqi/.zcode/skills/academic-voices/ — verbatim snapshot (SKILL.md + references/ + scripts/)"
initial-prompt: "Upgrade the paul-style skill into paul + these journal styles as one polishing skill."
agent: ZCode CLI
model: GLM (Zhipu)
issue: none (artifacts go straight to PR, per publisher's rule)
---

# Artifact: the `academic-voices` skill

> A verbatim snapshot of a live ZCode agent skill. [002's dourish-style skill](../002-writing-like-dourish/artifact.en.md) is hereby upgraded to five voices: Dourish plus four discipline registers — BDS / HCI / Sociology / SE — each with measured baselines.

## What it is

A polishing & diagnostic skill for academic prose. Each voice ships with:

- **a voice guide** (`references/voices/{bds,hci,soc,se}.md`): portrait, target density table (per-1000-words), lexicon, structural liturgy, rewrite recipes (B1–B6 / H1–H6 / S1–S6 / E1–E7, before→after), anti-patterns, title formulas. Dourish keeps his original three references (P1–P12, M1–M8).
- **`scripts/voice_check.py`**: multi-baseline diagnostics. `auto` mode is a discipline-camouflage detector — it ranks the draft against all five measured baselines (3.7M words of corpus, densities in `scripts/baselines.json`) by mean log-ratio distance; held-out accuracy 62% top-1 / 92% top-2. `--voice X` prints the full density table plus the most under-used signature patterns (opportunities).

## Red lines (same as 002)

Never copy corpus sentences into the user's manuscript; never alter claims, evidence, or citations; never fabricate anecdotes or participants; one voice per manuscript.
