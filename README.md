# Marginalia

> *mar·gin·a·li·a* (n.) — notes scribbled in the margins of a book; the traces a reader leaves behind.

Selective research & reading notes by [Yunqi Chen](https://github.com/UniqueClouds) — distilled musings from AI-assisted analyses, published bilingually (English / [中文](README.zh-CN.md)).

**This repo is deliberately sparse.** The workspace behind it holds raw corpora, private drafts and unfinished work; by default **everything is git-ignored**, and only explicitly whitelisted, curated notes are ever committed. Nothing lands here casually — each entry is published on purpose, as **one issue → one pull request → one squashed commit**.

## How an entry is born

1. **Issue** — the musing itself: what triggered it, where the data came from, what the original prompt/idea was.
2. **Pull request** — the distilled bilingual note (`note.en.md` + `note.zh.md`), cross-linked to the issue, plus one new row in the index below.
3. **Commit** — exactly one squashed commit on `main` per entry, so the history reads like a table of contents.

## Provenance format

Every note opens with full provenance — no orphan musings:

```yaml
---
id:              marginalia-NNN
title:           ...
date:            when the analysis was done
published:       when this note was committed
kind:            musing | analysis | proposal | survey
sources:         local corpora / files / tools the musing is grounded in
initial-prompt:  the request (idea) that started the conversation
agent:           ZCode CLI
model:           the LLM behind the conversation
issue:           N
---
```

## Index

| # | Entry | Date | Issue → PR |
|---|-------|------|------------|
| 001 | [Do coding agents have taste? What 29,787 Discord messages say about beautiful vs. ugly code](marginalia/001-code-taste-discord/note.en.md) · [中文](marginalia/001-code-taste-discord/note.zh.md) | 2026-08-15 | [#1](https://github.com/UniqueClouds/marginalia/issues/1) |
| 002 | [Writing like Dourish: a 21-text corpus analysis of a critical HCI voice (2004–2026)](marginalia/002-writing-like-dourish/note.en.md) · [中文](marginalia/002-writing-like-dourish/note.zh.md) | 2026-08-15 | [#3](https://github.com/UniqueClouds/marginalia/issues/3) |
| 003 | [NOTUGLY-S: learning "not ugly" instead of "beautiful" — an NLP × program-analysis proposal](marginalia/003-notugly-s/note.en.md) · [中文](marginalia/003-notugly-s/note.zh.md) | 2026-08-15 | [#2](https://github.com/UniqueClouds/marginalia/issues/2) |
| — | *(entries land here as they are published)* | | |

## Languages

Every document exists twice — `*.en.md` and `*.zh.md`, same content, neither an afterthought: switch to [中文版 README](README.zh-CN.md).

---

Personal research notes — no license granted yet; please ask before reuse.
