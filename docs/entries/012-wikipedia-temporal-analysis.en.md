# Large-Scale Temporal Analysis of Wikipedia Edit History and Talk Pages — survey: the pieces are ready, the joint study is missing

<div class="lang-switch" markdown>
🌐 Language / 语言：[中文](012-wikipedia-temporal-analysis.zh.md) · **English**
</div>

<div class='marg-meta'><span>📅 2026-08-18</span><span>🏷️ survey (literature survey)</span><span>🐙 issue #28</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-012</td></tr><tr><td>title</td><td>Large-Scale Temporal Analysis of Wikipedia Edit History and Talk Pages — survey: the pieces are ready, the joint study is missing</td></tr><tr><td>date</td><td>2026-08-18</td></tr><tr><td>published</td><td>2026-08-18</td></tr><tr><td>kind</td><td>survey (literature survey)</td></tr><tr><td>issue</td><td>28</td></tr></table></details>

> A survey note. The question: how do existing studies analyse, at scale, the temporal change of individual Wikipedia entries (edit history) and their long-term change — including Discussion/Talk pages? And are there scholars already doing it? The answer, up front: **yes — this is a mature field dating back to CHI 2004, and each of its three research lines has already reached "whole-site scale"**. What is genuinely scarce is not "has anyone done it", but joint modelling of three things — per-entry text evolution, talk-page interaction, and editor careers — in a **single multi-year, whole-site dataset**: **the pieces are ready; the joint study is missing.**

## 1. Three research lines, each already whole-site scale

### 1.1 Entry level: temporal evolution of a single article (words, revisions, lifecycle)

- **History flow** (Viégas, Wattenberg, Dave, CHI 2004) opened the visualisation line: colour-tracking how each author's contribution grows and shrinks across revisions, making "who wrote it, who deleted it, and when" visible for the first time. Early work was case studies of controversial articles; it became the seed of a whole family of visualisation tools.
- **Token-level "value survival"** (Priedhorsky et al., GROUP 2007, DOI 10.1145/1316624.1316663): parsed the **entire English-Wikipedia revision history** of its time, tracked per-word "did this word survive 90 days in the page", and quantified the dynamics of vandalism and repair. One of the earliest and best-known whole-site word-level studies.
- **WikiWho, token-level authorship attribution** (Flöck & Acosta, WWW 2014, DOI 10.1145/2566486.2568026): a chain diff-attribution algorithm — "who wrote this sentence (or even this token)". A live whole-site REST API exists.
- **Edit-war measurement**: Sumi et al. (IEEE SocialCom 2011) automatically detected and clustered "war-like rewriting"; Yasseri et al. (PLoS ONE 2012) turned revert events into time series and derived the bursty timescales of conflicted articles; Chhabra et al. (OpenSym 2020) moved to the **temporal structure** of edit-war sequences.

### 1.2 Long-term / whole-site: multi-year evolution

- **Slowing growth** (Suh, Convertino, Chi, Pirolli, WikiSym 2009): monthly aggregates from 2001–2008 showed that edit growth is not unbounded.
- **"The Rise and Decline of an Open Collaboration Community"** (Halfaker, Geiger, Morgan, Riedl, *American Behavioral Scientist* 2013, DOI 10.1177/0002764212469365): editor-cohort survival analysis over the full 2001–2011 edit history — why newcomers could no longer stay, and why the platform rose then contracted. The benchmark paper for long-term editor research.
- **Edit sessions** (Geiger & Halfaker, CSCW 2013, DOI 10.1145/2441776.2441873): segmenting activity into "edit sessions" by time gaps to unify participation measurement; the dataset (2001–2011) was released with the paper.
- Same lineage: Panciera et al. 2009 (*Wikipedians are born, not made*); Halfaker et al. 2011 (*Don't bite the newbies*, how reverts drive newcomers away); Yasseri et al. 2012 (**circadian patterns** across tens of millions of edit timestamps, decomposed by region); Wagner et al. 2016 (gender asymmetries).
- **Systematic review**: Mesgari et al. (JASIST 2015, DOI 10.1002/asi.23172) reviewed 400+ studies of Wikipedia content — proof that this is an institutionalised field.

### 1.3 Talk pages: the "other half" that is actually the most systematised

- **Reply-structure reconstruction** (Laniado, Tasso, Volkovich, Kaltenbrunner, ICWSM 2011, DOI 10.1609/icwsm.v5i1.14100): text alignment rebuilds talk pages as **reply networks/trees** — "who replied to whom" became computable.
- **Temporal dynamics of discussions** (Kaltenbrunner & Laniado, WikiSym 2012, DOI 10.1145/2462932.2462941): roughly a decade of full-scale talk-page time series, arguing that discussions evolve with "no deadline" pacing.
- **The conversational-computing school** (Danescu-Niculescu-Mizil and collaborators): computational politeness (ACL 2013), predicting conversational failure early (ACL 2018), "Anyone Can Become a Troll" (CSCW 2017) — all built on Wikipedia's Request for Comments corpus.
- **WikiConv** (Hua et al., EMNLP 2018, DOI 10.18653/v1/D18-1305): **replays** the revision history to reconstruct the complete conversational trees of all English talk pages — including deleted and edited comments. Talk pages went from "text" to "queryable conversation graphs".
- **Harassment at scale** (Wulczyn, Thain, Dixon, WWW 2017, DOI 10.1145/3038912.3052591): ~100k personally-attacked talk-page comments with human toxicity labels (WikiDetox / Talk Corpus).
- In 2024 a whole corpus-linguistics volume, *Investigating Wikipedia* (John Benjamins, SCL 121, DOI 10.1075/scl.121), was devoted to talk-page interaction and reply strategies.

## 2. How the scale is achieved (an inventory of methods)

| Method family | Representative work | Granularity / coverage | Scale (as stated in the papers) |
|---|---|---|---|
| Revert detection and edit-war metrics (3RR, revert graphs) | Kittur et al. CHI 2007; Sumi et al. 2011; Yasseri et al. PLoS ONE 2012 | revision-stream level, per-article revert graphs | full English-Wikipedia revision stream, focused on high-revert articles; multilingual extensions |
| Token survival / token attribution | Priedhorsky et al. 2007; Flöck & Acosta 2014 | token level | full English history already in 2007; WikiWho whole-site API |
| Edit sessions and edit sequences | Geiger & Halfaker 2013 | per-editor activity sequences | full 2001–2011 edit sequences |
| Survival analysis / editor retention | Panciera et al. 2009; Halfaker et al. 2013; Morgan & Halfaker 2018 (Teahouse) | editor-cohort level | monthly/annual survival curves over the full editor population, 2001–2011 |
| Reply networks and discussion trees | Laniado et al. 2011; Kaltenbrunner & Laniado 2012; Hua et al. 2018 (WikiConv) | talk-page reply relations | all / tens of thousands of EN talk pages, tree structure + timing |
| Time series / burstiness | Yasseri et al. 2012 (circadian); Keegan et al. 2011/2013 (breaking news) | timestamp distributions, article-level bursts | tens of millions of edit timestamps; clusters of breaking-news articles |
| Quality / vandalism ML models | Potthast & Holfeld PAN@CLEF 2010; Blumenstock 2008; Dang & Ignat 2016; **Halfaker & Geiger 2020 (ORES)** | revision-level / page-quality level | ORES in production across 300+ language editions |

The common thread: nearly every line starts from the **official Wikimedia full-revision dumps** (XML) and cuts the problem into time series, graphs, or conversations. The norm is the whole, not a sample.

## 3. Data and infrastructure (all real, all usable today)

| Tool / dataset | What it is |
|---|---|
| [Wikimedia XML dumps](https://dumps.wikimedia.org/) | full revision text and metadata for all languages; where everything starts |
| MediaWiki API + Pageviews API | per-article / per-user revision history online; site metrics |
| [WikiWho](https://wikiwho-api.wmcloud.org/) | token-level authorship and change data, live REST API |
| ORES / LiftWing | quality / vandalism / revert-risk scoring API (wp10 model family, 300+ languages, programmable) |
| Wikipedia Talk Corpus / WikiDetox | ~100k manually toxicity-labelled talk-page comments |
| ConvoKit (wiki_politeness module) | Wikipedia RfC conversational corpus with politeness annotations |
| WikiConv | complete talk-page conversation structure (including history restoration) |
| PAN-WVC (Webis) | manually labelled vandalism-revision corpus (PAN@CLEF 2010) |
| Wikipedia Edit Sessions dataset | ready-made edit-session segmentation (released with Geiger & Halfaker) |

## 4. Key scholars: who has been doing this for the long run

- **Wikimedia Foundation Research**: Aaron Halfaker (long-term retention, edit sessions, ORES first author), Jonathan Morgan (Teahouse / RfC social dynamics), Dario Taraborelli (WikiConv co-author, former research lead), Leila Zia, Diego Saez-Trumper, Miriam Redi, Isaac Johnson, Martin Gerlach. Their hallmark is turning research directly into **production** systems — ORES, LiftWing, and public data pipelines.
- **The editor/caretaker lineage**: the Minnesota GroupLens school (John Riedl† and Loren Terveen trained Priedhorsky/Panciera/Halfaker); R. Stuart Geiger (bots, edit sessions); Aniket Kittur (CMU).
- **Edit wars and long-run dynamics**: Taha Yasseri (Oxford), János Kertész, András Kornai.
- **Talk pages and conversational computing**: Cristian Danescu-Niculescu-Mizil (Cornell), David Laniado and Andreas Kaltenbrunner (Eurecat, Barcelona).
- **Token attribution and visualisation**: Fernanda Viégas & Martin Wattenberg (history flow), Fabian Flöck (KIT/GESIS) and Maribel Acosta (WikiWho).

## 5. 2020–2026: what the AI era changed (directly on-topic)

- **Post-ChatGPT editing behaviour is now quantified**: the MIT group (Acemoglu / Huttenlocher / Ozdaglar et al.), *Wikipedia Contributions in the Wake of ChatGPT* (WWW 2025, DOI 10.1145/3701716.3715543), measures structural changes in the edit stream since late 2022.
- **LLM-text detection has moved into real edit streams**: the KCL/TU Berlin group (Quaremba, Black, **Denny Vrandečić** (Wikidata founder), Simperl) released WETBench (WikiNLP@ACL 2025) and TSM-Bench (2026, arXiv 2605.31113), detection benchmarks built on real Wikipedia revision streams.
- **Governance history**: Froneman (*AI & Society* 2026) documents Wikipedia's three-year struggle (2022–2025) to govern AI-generated content (pragmatism vs. outright ban).
- **Derived ecosystems**: Grokipedia (an AI encyclopedia derived from Wikipedia content) has begun to be studied (arXiv 2512.03337); the "discussion/controversy analysis" methodology is being migrated to knowledge-graph editing (Wikidata; arXiv 2306.11766).

## 6. The gap: pieces ready, joint study missing

**Back to the original question: has anyone jointly modelled per-entry time-series + talk pages + long-term change at scale?**

- Each line alone is whole-site: article text evolution (Priedhorsky 2007; WikiWho), talk-page structure (Laniado 2011; WikiConv 2018), editor long-run retention (Halfaker 2013) — **but joint modelling on a single dataset is rare**.
- The closest template is Keegan, Gergle & Contractor's breaking-news research (*Hot Off the Wiki*, ABS 2013): on the same set of articles they put **articles + editors + discussions** together in a multi-layer analysis. Everything else is mostly pairwise (article×editor, discussion×article).
- There is no recognised "whole-site × all articles × (text | discussion | editors) × 20 years" joint benchmark or long-panel study — this is the clear gap.

**Ready-to-use starter kit** (all sourced, see §2): revert detection and edit-war metrics (Sumi/Yasseri line); token survival (Priedhorsky; WikiWho API directly); edit-session segmentation (Geiger & Halfaker's released data); cohort survival analysis (replicable from Halfaker 2013); talk-page reply-tree reconstruction (Laniado 2011; WikiConv methodology); quality/vandalism scoring out of the box (ORES/LiftWing); and, from 2025–2026, an additional LLM-generation detection layer (WETBench/TSM-Bench).

**Verification boundary (honest statement)**: all 18 seed papers were confirmed real via Semantic Scholar / arXiv / Crossref; the "VOSS talk-page corpus project" could not be found in any first-party source; Miquel-Ribé et al. 2021 has no DOI (S2 record only); the "Liang & Cao 2024-style Wikipedia AI-text detection" paper the prompt alluded to was not found — the closest verified works are WETBench / TSM-Bench / M4.

## Reference index (selection; DOI / arXiv-resolvable)

1. 10.1145/985692.985765 — Viégas, Wattenberg, Dave, CHI 2004 (History flow)
2. 10.1145/1316624.1316663 — Priedhorsky et al., GROUP 2007 (token survival)
3. 10.1145/1641309.1641322 — Suh et al., WikiSym 2009 (slowing growth)
4. 10.1177/0002764212469365 — Halfaker, Geiger, Morgan, Riedl, ABS 2013 (Rise and Decline)
5. 10.1145/2441776.2441873 — Geiger & Halfaker, CSCW 2013 (edit sessions)
6. 10.1145/2566486.2568026 — Flöck & Acosta, WWW 2014 (WikiWho)
7. 10.1609/icwsm.v5i1.14100 — Laniado et al., ICWSM 2011 (talk-page reply trees)
8. 10.1145/2462932.2462941 — Kaltenbrunner & Laniado, WikiSym 2012 (discussion timing)
9. 10.18653/v1/D18-1305 — Hua et al., EMNLP 2018 (WikiConv)
10. 10.1145/3038912.3052591 — Wulczyn et al., WWW 2017 (Ex Machina, personal attacks)
11. 10.1371/journal.pone.0038869 — Yasseri et al., PLoS ONE 2012 (conflict dynamics)
12. 10.1109/PASSAT/SocialCom.2011.47 — Sumi et al., 2011 (Edit Wars)
13. 10.1145/3415219 — Halfaker & Geiger, PACM HCI 2020 (ORES)
14. 10.1002/asi.23172 — Mesgari et al., JASIST 2015 (systematic review)
15. 10.1145/3701716.3715543 — Lyu et al., WWW 2025 (post-ChatGPT contributions)
16. 10.18653/v1/2025.wikinlp-1.6 — Quaremba et al., 2025 (WETBench); arXiv 2605.31113 — TSM-Bench 2026
17. 10.1007/s00146-026-03046-1 — Froneman, AI & Society 2026 (AI-content governance history)
18. 10.1075/scl.121 — *Investigating Wikipedia*, John Benjamins 2024
19. arXiv 1306.6078 — Danescu-Niculescu-Mizil et al., ACL 2013 (politeness)
20. 10.1145/2998181.2998213 — Cheng et al., CSCW 2017 (Anyone Can Become a Troll)

---

> 🌐 [阅读中文版](012-wikipedia-temporal-analysis.zh.md)

