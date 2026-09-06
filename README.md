# Marginalia

> *mar·gin·a·li·a* (n.) — notes scribbled in the margins of a book; the traces a reader leaves behind.

Selective research & reading notes by [Yunqi Chen](https://github.com/UniqueClouds) — distilled musings from AI-assisted analyses, published bilingually (English / [中文](README.zh-CN.md)).

> 🌐 **Website:** <https://uniqueclouds.github.io/marginalia/> — 全部内容物在线阅读（MkDocs 构建，push 自动部署）

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
| 004 | [Is CHI/ACL a storytelling festival? From community gripe to measurable construct](marginalia/004-storytelling-quantified/note.en.md) · [中文](marginalia/004-storytelling-quantified/note.zh.md) | 2026-08-15 | [#7](https://github.com/UniqueClouds/marginalia/issues/7) |
| 005 | [Four academic voices, measured: language styles of BDS/HCI/Sociology/SE classics (314 papers, 3.3M words)](marginalia/005-discipline-style-voices/note.en.md) · [中文](marginalia/005-discipline-style-voices/note.zh.md) | 2026-08-15 | [#11](https://github.com/UniqueClouds/marginalia/issues/11) |
| 006 | [Spotify Podcast Guide 2026 · 英文播客推荐清单（47 节目 / 77 集精选，全部官方链接）](marginalia/006-podcast-guide/artifact.zh.md) · [English](marginalia/006-podcast-guide/artifact.en.md) | 2026-08-17 | [#13](https://github.com/UniqueClouds/marginalia/issues/13) |
| 007 | [Nuance rising and falling in scientific writing: identification, measurement, and one local-corpus test (314 papers / 3.3M words)](marginalia/007-nuance-rises-and-falls/note.en.md) · [中文](marginalia/007-nuance-rises-and-falls/note.zh.md) | 2026-08-17 | [#14](https://github.com/UniqueClouds/marginalia/issues/14) |
| 008 | [How to Scale Your Model — reading note: LLM training taken from alchemy to a roofline accounting (JAX-ML scaling book)](marginalia/008-llm-scaling-book/note.en.md) · [中文](marginalia/008-llm-scaling-book/note.zh.md) | 2026-08-17 | [#15](https://github.com/UniqueClouds/marginalia/issues/15) |
| 009 | [Homologies in Fields of Cultural Production. Evidence from the European Scientific Field — borrowed the boundary, not the fractal](marginalia/009-homology-without-fractal/note.en.md) · [中文](marginalia/009-homology-without-fractal/note.zh.md) | 2026-08-17 | [#17](https://github.com/UniqueClouds/marginalia/issues/17) |
| 010 | [组织惰性:成功的副产品,抑或组织病症?——基于系统性审查方法的述评与展望 — a reading note: the byproduct–symptom dichotomy, left standing](marginalia/010-organizational-inertia/note.en.md) · [中文](marginalia/010-organizational-inertia/note.zh.md) | 2026-08-18 | [#22](https://github.com/UniqueClouds/marginalia/issues/22) |
| 011 | [Awesome Auditable AI — reading note: 188 entries / 9 sections / 132 arXiv papers; how a curated list turns AI agent auditability from a slogan into reliability engineering](marginalia/011-auditable-agents-atlas/note.en.md) · [中文](marginalia/011-auditable-agents-atlas/note.zh.md) | 2026-08-17 | [#26](https://github.com/UniqueClouds/marginalia/issues/26) |
| 012 | [Large-Scale Temporal Analysis of Wikipedia Edit History and Talk Pages — survey: the pieces are ready, the joint study is missing](marginalia/012-wikipedia-temporal-analysis/note.en.md) · [中文](marginalia/012-wikipedia-temporal-analysis/note.zh.md) | 2026-08-18 | [#28](https://github.com/UniqueClouds/marginalia/issues/28) |
| 013 | [Ethnomethodology — survey: origins, its relation to ethnography, and development](marginalia/013-ethnomethodology/note.en.md) · [中文](marginalia/013-ethnomethodology/note.zh.md) | 2026-08-21 | [#30](https://github.com/UniqueClouds/marginalia/issues/30) |
| 015 | [The Qualitative HCI Landscape of UC Irvine Informatics — survey: who does qualitative, STS, and health information work](marginalia/015-uci-informatics-qualitative/note.en.md) · [中文](marginalia/015-uci-informatics-qualitative/note.zh.md) | 2026-09-05 | [#39](https://github.com/UniqueClouds/marginalia/issues/39) |
| 014 | [Sandwich OCR for scanned books — making Putnam and Rorty pixel-identical and fully searchable](marginalia/014-sandwich-ocr-books/note.en.md) · [中文](marginalia/014-sandwich-ocr-books/note.zh.md) | 2026-08-22 | [#37](https://github.com/UniqueClouds/marginalia/issues/37) |
| 016 | [Amazon Desk Shopping for ZIP 92617 — survey: desktop depth and budget don't combine in standing desks](marginalia/016-apartment-desk-shopping/note.en.md) · [中文](marginalia/016-apartment-desk-shopping/note.zh.md) | 2026-09-05 | [#43](https://github.com/UniqueClouds/marginalia/issues/43) |
| 017 | [Ways of Knowing in HCI — reading note: eighteen ways of knowing and the accountabilities that govern them](marginalia/017-ways-of-knowing-in-hci/note.en.md) · [中文](marginalia/017-ways-of-knowing-in-hci/note.zh.md) | 2026-09-05 | [#45](https://github.com/UniqueClouds/marginalia/issues/45) |
| 018 | [The Spectacularization of SOTA — essay: model launches, aesthetic fatigue, and the politics of technological time](marginalia/018-sota-spectacle/note.en.md) · [中文](marginalia/018-sota-spectacle/note.zh.md) | 2026-09-06 | [#47](https://github.com/UniqueClouds/marginalia/issues/47) |
| 019 | [TokenMaxxing — essay: conspicuous consumption of compute and a three-month moral crusade](marginalia/019-tokenmaxxing/note.en.md) · [中文](marginalia/019-tokenmaxxing/note.zh.md) | 2026-09-06 | [#48](https://github.com/UniqueClouds/marginalia/issues/48) |
| 020 | [AI Blackouts — essay: outages, the compensatory politics of resets, and the grey reseller tier](marginalia/020-ai-as-utility/note.en.md) · [中文](marginalia/020-ai-as-utility/note.zh.md) | 2026-09-06 | [#49](https://github.com/UniqueClouds/marginalia/issues/49) |
| 021 | [Re-run the review and half the program changes — Best Paper randomness and the floor of 'not-ugly'](marginalia/021-best-paper-lottery/note.en.md) · [中文](marginalia/021-best-paper-lottery/note.zh.md) | 2026-09-06 | [#50](https://github.com/UniqueClouds/marginalia/issues/50) |
| 022 | [Dragged by the models — programme sketch: gravity, shifting ground, and the social isomorphism of 'Attention is all you need'](marginalia/022-gravity-of-models/note.en.md) · [中文](marginalia/022-gravity-of-models/note.zh.md) | 2026-09-06 | [#51](https://github.com/UniqueClouds/marginalia/issues/51) |
| 023 | [When Nature learns clickbait — essay: journal mediatization and the redirection of taste](marginalia/023-journal-mediatization/note.en.md) · [中文](marginalia/023-journal-mediatization/note.zh.md) | 2026-09-06 | [#52](https://github.com/UniqueClouds/marginalia/issues/52) |
| 024 | [Laying the track ahead of the train — essay: the political economy of release cycles, from CPU benchmarks to SOTA](marginalia/024-release-cycle-politics/note.en.md) · [中文](marginalia/024-release-cycle-politics/note.zh.md) | 2026-09-06 | [#53](https://github.com/UniqueClouds/marginalia/issues/53) |

## Artifacts

Companions to the entries above, published **verbatim** — live skills, original source documents, full reports — in whatever language they were born in. Each lives inside its entry's directory but arrives in its own PR; artifacts need no issue.

| Artifact | Entry | PR |
|---|---|---|
| `dourish-style` polishing skill (since superseded by `academic-voices`) | [002](marginalia/002-writing-like-dourish/artifact.en.md) | [#9](https://github.com/UniqueClouds/marginalia/pull/9) |
| Storytelling originals — survey + proposal v2 (中文) | [004](marginalia/004-storytelling-quantified/docs/storytelling-survey.zh.md) | [#10](https://github.com/UniqueClouds/marginalia/pull/10) |
| Five full discipline-style reports (中文) | [005](marginalia/005-discipline-style-voices/reports/05-cross-discipline.zh.md) | [#12](https://github.com/UniqueClouds/marginalia/pull/12) |
| `academic-voices` skill — five measured voices, density baselines + voice classifier | [005](marginalia/005-discipline-style-voices/artifact.en.md) | [#13](https://github.com/UniqueClouds/marginalia/pull/13) |
| `ocr_pipeline` — sandwich OCR for scanned books: byte-identical page images + per-character invisible text layer | [014](marginalia/014-sandwich-ocr-books/note.en.md) | [#36](https://github.com/UniqueClouds/marginalia/pull/36) |

## Languages

Every **note** exists twice — `*.en.md` and `*.zh.md`, same content, neither an afterthought. Verbatim **artifacts** (skills, original source documents) are published as-is, in whatever language they were born in: switch to [中文版 README](README.zh-CN.md).

## License

The contents of this repository and the [website](https://uniqueclouds.github.io/marginalia/) — the entry notes, reports, the podcast guide — are licensed under **[Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)**. You're free to share and adapt for any non-commercial purpose, as long as you credit the source; commercial use requires prior permission. The underlying data corpora are not redistributed here and remain governed by their original sources (each entry's `sources` field cites them).
