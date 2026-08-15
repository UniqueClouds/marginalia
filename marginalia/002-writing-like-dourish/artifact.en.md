---
id: marginalia-002-artifact
title: "Artifact: the dourish-style polishing skill"
date: 2026-08-15
published: 2026-08-15
kind: artifact
sources:
  - "C:/Users/yunqi/.zcode/skills/dourish-style/ — verbatim snapshot (SKILL.md + references/ + scripts/)"
initial-prompt: "Same thread as musing 002: after the corpus analysis, package the findings as a reusable polishing skill."
agent: ZCode CLI
model: GLM (Zhipu)
issue: none (artifact PR, by publisher's choice)
---

# Artifact: the `dourish-style` skill

> A verbatim snapshot of the working ZCode agent skill distilled from the [21-text corpus analysis](note.en.md) — publish-the-tool, not just the findings.

## What it is

A skill that revises English academic manuscripts toward Paul Dourish's critical HCI/STS/CSCW register, with hard guardrails:

1. **Never copy distinctive sentences from his corpus** — patterns and templates only; corpus examples are calibration, not material.
2. **Never alter claims, evidence, citations, or terminology** — style work on wording/rhythm/framing; if a rewrite changes what a sentence asserts, flag it instead.
3. **Never fabricate anecdotes, quotes, or fieldwork details.**
4. Intensity matches venue (full style for STS/CSCW/CHI critical papers; sentence-level only for technical venues).

## What's inside

| file | role |
|---|---|
| [`skill/SKILL.md`](skill/SKILL.md) | workflow: scope → diagnose → revise → report; Register A (practice/everyday/encounter) vs B (materiality/format/infrastructure); intensity levels; title clinic |
| [`skill/references/patterns.md`](skill/references/patterns.md) | recipes P1–P10 (not-X-but-Y, ways-in-which, paraphrase pairs, plural quantifiers, hedge calibration…) |
| [`skill/references/motifs.md`](skill/references/motifs.md) | the eight recurring argument motifs for deep-mode restructuring |
| [`skill/references/style-guide.md`](skill/references/style-guide.md) | register vocabulary + anti-patterns to delete |
| [`skill/scripts/dourish_style_check.py`](skill/scripts/dourish_style_check.py) | diagnostic: ~29 signature-pattern densities vs. the corpus baseline; prints under-used patterns as "opportunities" |

## Calibration targets (from the corpus)

"not simply X but Y" ≈ 0.9 per 1000 words (~5–6 per 6000-word paper, in intro/contributions/discussion) · "rather than" ≈ 0.8 · "the ways in which" ≈ 1.0 · "that is," ≈ 0.3 · hedges ≈ 1.5 combined · rhetorical questions ~1 per 200 words in intro/discussion of theoretical papers, never methods/results · exceeding baseline by >2.5× = over-styled, dial back.

## How to use

Drop the `skill/` folder into a ZCode-compatible skills directory (e.g. `~/.zcode/skills/dourish-style/`) and mention "Dourish" or ask for HCI/STS-style polishing; or read `SKILL.md` as standalone prompt guidance for any agent. Paths inside the files are as-authored (this copy is a snapshot of the live skill; the local original may evolve).

## Provenance

| field | value |
|---|---|
| Data | verbatim copy of `~/.zcode/skills/dourish-style/` (40 KB, 5 files), built 2026-08-15 from the musing-002 corpus analysis |
| Initial prompt | "After the corpus analysis, package the findings as a reusable polishing skill." |
| Time | built 2026-08-15 21:28–21:35 · published 2026-08-15 |
| Agent / model | ZCode CLI · GLM (Zhipu) |
| Parent entry | [musing 002](note.en.md) · [issue #3](https://github.com/UniqueClouds/marginalia/issues/3) |
