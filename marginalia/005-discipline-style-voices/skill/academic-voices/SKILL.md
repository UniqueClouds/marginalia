---
name: academic-voices
description: Polish and revise English academic manuscripts in one of five measured academic voices — Paul Dourish (critical HCI/STS essayist) and four discipline registers: Big Data & Society (critical data studies), HCI (CHI/CSCW), Sociology (AJS/ASR/BJS), Software Engineering (ICSE/FSE/TSE). Use whenever the user mentions Dourish or any of these venues/fields, asks to make a draft sound like a CHI paper / an AJS paper / a BDS article / an ICSE paper, wants a draft diagnosed for which academic voice it currently sounds like, or has a Chinese draft to render in one of these registers. Supersedes the earlier dourish-style skill (Dourish is now voice #1 of five).
---

# Academic Voices: Five-Register Manuscript Polishing

You are revising the user's own manuscript toward one of **five measured voices**, each grounded in a corpus analysis: **dourish** (21 texts, 400k words, 2004–2026), **bds** (27 papers, *Big Data & Society*/*New Media & Society*), **hci** (94 papers, CHI/CSCW), **soc** (79 papers, AJS/ASR/BJS), **se** (114 papers, ICSE/FSE/TSE) — 3.7M words of baselines total. Reports: `C:\Users\yunqi\ZCodeProject\Dourish_语言特征分析报告.md` and `ZCodeProject\学科风格分析_1..5_*.md`. The goal is a manuscript that belongs in the venue's neighborhood — **not** parody, never plagiarism.

## Non-negotiable guardrails

1. **Never copy distinctive sentences from any corpus into the user's manuscript.** Patterns and templates only; sentences marked 原文例证 are calibration, not quotable stock.
2. **Never change claims, evidence, citations, or terminology** unless asked. If a rewrite would change what a sentence asserts, flag it instead.
3. **Never fabricate anecdotes, quotes, participants, or numbers.** Anecdote/news-hook/epigraph recipes only use material already in the user's draft or data.
4. **One voice per manuscript** (user's choice or inferred target venue). Mixing registers mid-paper — e.g. an ICSE liturgy with BDS manifesto openings — produces sludge; only the user can request hybridization.
5. Intensity scales with section: intro/discussion carry the voice's rhetoric; methods/results stay plainer in every register.

## Workflow

### Step 1 — Pick the voice
- User names it (Dourish / BDS / CHI / AJS-ASR / ICSE…) → use it.
- User names a target venue → map: STS/critical→bds or dourish; CHI/CSCW/TOCHI→hci; sociology journals→soc; ICSE/FSE/TSE/MSR/EMSE→se.
- Unknown → run Step 2 in `auto` mode and **propose** the nearest voice plus runner-up; let the user confirm before deep revision.

### Step 2 — Diagnose (whole sections or full drafts)

```bash
python C:/Users/yunqi/.zcode/skills/academic-voices/scripts/voice_check.py <draft>            # classify
python C:/Users/yunqi/.zcode/skills/academic-voices/scripts/voice_check.py <draft> --voice se # full table
```

`auto` ranks the draft against all five baselines. Honest accuracy on held-out corpus papers: **~60% top-1, ~90% top-2**; HCI drafts often rank se/bds adjacent because CHI itself is internally hybrid — read the ranking, not just the winner. Keep output for the change report; skip for single paragraphs.

### Step 3 — Revise with the voice's guide
- **dourish** → read `references/dourish-style-guide.md` (registers A/B), apply recipes P1–P12 in `references/dourish-patterns.md`; deep mode restructures around `references/dourish-motifs.md` (M1–M8).
- **bds / hci / soc / se** → read `references/voices/<voice>.md` and apply its recipes in the listed priority order; respect its anti-patterns list (deleting anti-patterns is half the work).
- Chinese-draft input: translate into the chosen voice in one pass — never translate literally then style separately.

### Step 4 — Report
1. Revised text (full paragraphs; unchanged text elided `...`).
2. Change table: `original → revised → recipe/basis`, one row per substantive change (recipe codes like P1/B2/H3 so the user learns the moves).
3. If Step 2 ran: re-run `--voice X` on the revision; report before/after densities of the top opportunities.
4. Flag anything left unchanged because it would alter meaning, and where the user's phrasing beat the template.

## Calibration cheat-sheet (per 1000 words; full tables in each guide)

| | dourish | bds | hci | soc | se |
|---|---|---|---|---|---|
| avg sentence | 23.9w | **26.8w** | 23.7w | 23.6w | **18.8w** |
| we | 6.8 | 3.8 (lowest) | 9.1 | 5.2 | **10.3** |
| not-simply-but | **0.93** | 0.29 | 0.15 | 0.16 | 0.08 |
| rather than | 0.82 | **0.51** | 0.36 | 0.33 | 0.20 |
| semicolon | 4.2 | **4.6** | 2.3 | 4.4 | 2.3 |
| em-dash | 3.3 | 1.7 | 1.4 | **3.5** | **0.7** |
| contractions | 0.15 | **0.00** | 0.27 | **0.74** | 0.12 |
| this article / this paper | journal voices say *article* (bds 0.32/kw, soc 0.23); conference voices say *paper* (hci 0.38, se 0.37) ||||

Over-styling rule: exceeding any baseline by >2.5× means dial back — these are corpus *averages*, and a good paper sits near them, not far above.

## Title clinic (all voices)
Offer 3–5 candidates per the voice's title formula (dourish: chiasmus/allusion; bds: "The X of Y" lever; hci: hook+colon, quotes allowed; soc: metaphor + dated-mechanism subtitle; se: short noun phrase or pain-point question). Reject "A Study of / An Investigation of / Towards+another-hedge" in every voice.
