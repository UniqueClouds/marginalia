---
id:              marginalia-010-en
title:           "组织惰性:成功的副产品,抑或组织病症?——基于系统性审查方法的述评与展望 — the dichotomy, dissolved onto a relative-inertia index"
date:            2026-08-18
published:       2026-08-18
kind:            note (paper reading note + idea extension)
sources:
  - "Bai Jingkun (白景坤), Xun Ting (荀婷), Zhang Zhenzhen (张贞贞). 2016. 组织惰性:成功的副产品,抑或组织病症?——基于系统性审查方法的述评与展望 [Organizational Inertia: Byproduct of Success or Organizational Symptom? Review and Prospects Based on Systematic Examination]. Waiguo jingji yu guanli (《外国经济与管理》, Foreign Economy and Management) 38(12):113–128. doi:10.16538/j.cnki.fem.2016.12.009"
  - "Abstract, keywords, byline, and affiliation (School of Business Administration, Dongbei University of Finance and Economics) verified char-by-char against the CNKI abstract page: https://kns.cnki.net/kcms2/article/abstract?v=&uniplatform=NZKPT&language=CHS (DOI resolved via chndoi.org → CNKI)"
  - "OpenAlex + Crossref double-checked the paper's metadata; the English-deposited parallel title matches the user-provided one"
  - "Six 'first-priority' classic references cross-checked via Crossref; three of them needed author/venue corrections (see table below)"
  - "Yi-Knudsen-Becker 2016 abstract quoted verbatim from Crossref metadata"
  - "Song, Bo & Dinghong Peng. 2026. Research on a novel organizational anti-inertia evaluation method. *Decision* (Springer) 53(1):113–133. doi:10.1007/s40622-025-00458-8 — verified via OpenAlex (NSFC 72261020); one of the recent works asserting that no systematic 'anti-inertia / adaptability' evaluation method yet exists"
  - "Cheng Lu (程露), Su Jingqin (苏敬勤), Lyu Yibo (吕一博). 2019. 组织惯性：理论评述与研究框架构建 [Organizational inertia: theoretical review and research-framework construction]. A second Chinese-language review, the one after Bai et al., sorting the literature under ecology / rational-adaptation / hybrid. **Cited as the user supplied it from a working note; Crossref and OpenAlex searches in this session did not surface its venue/volume/issue/pages/DOI**, so those are left un-faked pending later verification."
  - "The revision added-body further down (the '## Annotation: … to a relative index' section) integrates a second-pass working note supplied by the user on 2026-08-18; the relative-inertia index `I_it = V^E_it / (V^O_it + ε)` is the user's own conceptual measurement framework in that note. This marginalia incorporates it as the user's original contribution, **not as a metric imported from any of the cited papers**."
initial-prompt: "Write a bilingual marginalia reading note on this 2016 Chinese systematic review; the user supplies six 'first-priority' classic references as anchors and bundles the project under the idea-name 'organizational-inertia research for enterprises (企业组织惯性的相关研究)'. On revision, the user supplied a second-pass systematic working note on the same construct — containing the relative-inertia index as a conceptual measurement framework plus two new references (Song & Peng 2026; Cheng et al. 2019); selectively merge its original parts — the index framework, the inertia/momentum/resistance distinctions, the two four-way taxonomies (dimensions and mechanisms), and the theoretical shift from 'does the org change' to 'does the org keep up with the environment' — without re-incorporating the introductory arc and the formula-derivation middle steps already covered in the main note."
agent:           ZCode CLI
model:           GLM (Zhipu)
issue:           22
---

# 组织惰性:成功的副产品,抑或组织病症?——基于系统性审查方法的述评与展望 — the dichotomy, dissolved onto a relative-inertia index

> A Chinese systematic review that stands the dichotomy "organizational inertia — byproduct of success or organizational symptom" on its own two feet. Its contribution is to *name* the mountain; its limitation is to leave it as two mountains. On revision, the note walks up the valley the review left standing — dissolving that dichotomy onto a *relative*-inertia index where **byproduct** and **symptom** become two asymptotes instead of two opponents.

## The paper itself

- **Source**: *Waiguo jingji yu guanli* (《外国经济与管理》, Foreign Economy and Management), vol. 38, no. 12, December 2016, pp. 113–128; doi:10.16538/j.cnki.fem.2016.12.009.
- **Authors**: Bai Jingkun (白景坤), Xun Ting (荀婷), Zhang Zhenzhen (张贞贞); **affiliation**: School of Business Administration, Dongbei University of Finance and Economics.
- **Chinese title verbatim**: 组织惰性:成功的副产品,抑或组织病症?——基于系统性审查方法的述评与展望. **English parallel title (deposited)**: "Organizational Inertia: Byproduct of Success or Organizational Symptom? Review and Prospects Based on Systematic Examination".
- **Keywords (as the paper tags itself)**: 组织惰性 · 组织变革 · 环境选择 · 组织适应 (organizational inertia · organizational change · environmental selection · organizational adaptation).
- **Tracing note**: the paper uses **组织惰性** (lazy/sluggish, with a pejorative hue) rather than the more neutral **组织惯性** (physics-flavoured inertia). The English-deposited title quietly collapses that distinction into "Inertia".

### Abstract (Chinese, quoted verbatim)

> 随着环境不确定性的增加，组织惰性日益成为组织理论研究的热点问题，然而学术界对组织惰性的理解存在明显分歧。通过文献梳理发现，不同视角对组织惰性研究的逻辑起点不同以及组织惰性本身的复杂性是导致分歧的主要原因。基于系统性审查方法，搜集整理近 40 年来国内外组织惰性研究文献后，本文选取 79 篇英文文献和 24 篇中文文献，以环境选择和组织适应两类视角及其融合为主线，对组织惰性的概念构成与测量、前因和后果等方面进行了系统地梳理与述评，最后指出现有研究存在的不足和未来的研究方向。本文对组织惰性研究成果进行系统性梳理在国内外尚属首次，可为推动理论与实证研究的深入展开提供依据。

One-paragraph translation pass-through: as environmental uncertainty rises, organisational inertia has become a hot topic in organisation theory, but understandings diverge sharply. Through a literature scan the authors trace the divergence to two sources — different perspectives have different logical starting points, and the construct itself is complex. Using a systematic-examination method, the authors gather forty years of domestic and international literature and select **79 English + 24 Chinese = 103 articles**, threading the review along **environmental selection and organisational adaptation *and their fusion***; they cover conceptual composition, measurement, antecedents, and consequences, and turn finally to shortcomings and future directions. The paper claims this is the **first systematic review of the construct anywhere in either the Chinese- or English-speaking literature**.

One-sentence compression: **thread 103 papers along a "selection–adaptation + fusion" spine, catalogue them under conceptual composition / measurement / antecedents / consequences, attribute the field's divergence to "different logical starting points" plus "construct complexity" — and leave that attribution as a classification rather than a resolution.**

### Method skeleton

- **Corpus**: 40 years of "组织惰性" research, narrowed to **79 English + 24 Chinese = 103 articles**. The paper's own "first-of-its-kind" claim pins it as a **fixation point in the construct's bibliographic chronology** — the moment a concept first becomes a shaped corpus rather than a scatter of articles.
- **Spine**: two perspectives — **environmental selection** and **organisational adaptation** — *and their fusion*. The paper's promise.
- **Four quadrants**: **conceptual composition · measurement · antecedents · consequences** — the standard concept-review template, orthogonal to the S/A axis: each quadrant further splits along S/A.

### Main findings (in the paper's own wording)

- **Meta-conclusion**: organisational inertia research diverges because **different perspectives have different logical starting points** + the **complexity of the construct itself**. The paper stops here — it names the source of divergence without mechanising it.
- **The dichotomy in the title falls directly onto the spine**:
  1. **Environmental selection / structural inertia lineage** (after Hannan & Freeman 1984): inertia is **a byproduct of success** — selection pressures favour reproducibility, structurally-reliable organisations win; the more successful the org, the more inert its structure becomes.
  2. **Organisational adaptation / strategic choice lineage** (traceable back to Child 1972 et al.; Gilbert, Colombo et al. in the paper): inertia is read as a **symptom** — drawable, decomposable, surgically targetable. Gilbert 2005's "resource vs routine rigidity" is the most-famous unboxing knife.
  3. **The fusion view**: the paper proposes future work to take the two starting points as complementary rather than oppositional — but it leaves "fusion" at the level of a label, never a mechanism.
- **Measurement, antecedents, consequences** are each unpacked across the S/A split in §§3–5 — dense enough that this layer is best read in the original.

## Reading note: the byproduct–symptom dichotomy, left standing

The pleasure of reading this paper is the same flavour as [009 — borrowed the boundary, not the fractal](../009-homology-without-fractal/note.en.md): a paper first **names** a dichotomy with care, and then **does not press** the switch that would dissolve it. Bai et al.'s "byproduct vs symptom" sits right at the highest-tension point of the entire inertia literature — they fill the table, attribute divergence to "different logical starting points", and stop. To actually dissolve the byproduct-symptom pair, you need a reverse proposition that simultaneously accepts "inertia is the byproduct of success" AND "inertia can be turned to use"; and **Yi-Knudsen-Becker 2016 already gave that reverse proposition** (the user's sixth "priority reference", below). Bai et al.'s review lets the reconciler sit on the shelf without being activated.

A cheap check on the side: of the six "priority references" the user listed, **only the last one (Yi-Knudsen-Becker 2016) can reconcile "byproduct vs symptom" — and that one is exactly the paper the user's casual paraphrase mangles hardest** (drops the lead author, gets the venue wrong). Itself a small metaphor: mis-remembering the most important reconciler costs more than missing an ally of secondary importance.

### A few tensions I kept circling

- **"Byproduct" and "symptom" are not opposites; they are two shadows the same construct casts under two measuring instruments.** Hannan & Freeman 1984 measures org structure-duration and naturally reads inertia as the harmless, predictable byproduct. Gilbert 2005 decomposes the org's malfunction under threat into resource rigidity and routine rigidity and naturally reads inertia as a symptom that can be operated on. Reading Bai et al. I kept coming back to: what divides the two propositions is not "inertia itself" but **the instrument used to measure it**.
- **"Selection vs adaptation" is a tilting-axis distinction, not a procedural one.** Hannan & Freeman give a population-evolution mechanism (external selection sieves organisations); the adaptation lineage gives an intentional strategic-adjustment mechanism (internal agents reorganise). Bai et al. neutralise the contrast into "selection + adaptation → fusion" — but "fusion" in the paper is a label, not an explanation, and never says whether "fusion" is *between mechanisms* (synthesis) or *between viewpoints* (parataxis).
- **Yi-Knudsen-Becker 2016 is the suspended reverse proposition.** Empirical finding: routine-level inertia *helps* organisation-level adaptation because lower change rates bring temporal reordering. In other words, **inertia is at once byproduct AND symptom AND asset**. That is precisely the third cell Bai et al.'s title-trichotomy quietly drops. The reconciling cell is on the same shelf as the citations the review collected; the review simply doesn't pick it up.
- **The Chinese rendition of "selection vs adaptation" does two quiet things**: (1) it translates Hannan-Freeman's *population ecology* into the softer "环境选择" / environmental selection, blunting its Darwinian edge; (2) it shrinks *strategic choice* into "组织适应" / organisational adaptation, dropping the political-actor dimension that goes back to Child 1972 — and both lines end up *easier to fuse*. That's the inverted effect of terminological softening: it smooths the review but covers the genuine tension under fusion rhetoric.

### Why we name this idea "enterprise organisational inertia research"

Bundling the project under **"企业组织惯性的相关研究" (research on enterprise organisational inertia)** — rather than the more direct "组织惰性研究" — is a deliberate tightening of the unit of analysis **to the enterprise**. Inertia has a branch in organisation theory (organisational ecology) whose unit is populations of *organisations-any-kind* — also universities, churches, NGOs; narrowing the radius to the enterprise pegs measurement, antecedents, and consequences onto "mature organisations with path-dependent routines" — the very unit that AI-deployment experience can illuminate concretely.

It plays a concrete role in yunqi's research agenda: a **more structured vocabulary than "the organisation resists"** for "why is AI deployment in enterprises so slow?" Gilbert 2005's resource vs routine rigidity is immediately operational — when an enterprise's AI hasn't spread, is the bottleneck GPU-budget / licence-cost (a *resource* rigidity) or workflow-lockin / documentation-inertia (a *routine* rigidity)? And Yi-Knudsen-Becker 2016's reverse proposition gives an unexpected flip: **routine inertia may turn out to be a precondition, not a bottleneck, for AI adoption** — only enterprises whose routines are already inert enough can host an AI's default behaviour as a stable runtime; enterprises whose routines are too active can't give the model a stable input representation, and each deployment has to re-align from scratch.

That is a real runnable research question, and it lands adjacent to yunqi's existing SE×AI corpus work (AIDev et al.; see the SE×AI CCF-B survey): pull routines out of a firm's dev teams, compute routine-level inertia, regress against actual AI-adoption rates, and you have a pair of competing, measurable hypotheses sitting across the Gilbert vs Yi-Knudsen-Becker axes.

### The six priority references, Crossref-verified

The user listed six "first-priority" classic references; what follows is the **errata-checked** version after Crossref — three of the six need author/venue fixes:

| As the user gave it | Crossref-verified canonical | Where the user's wording slips |
|---|---|---|
| Hannan & Freeman (1984), *Structural Inertia and Organizational Change* | Michael T. Hannan & John H. Freeman. 1984. "Structural Inertia and Organizational Change." *American Sociological Review* 49(2):149–164. doi:10.2307/2095567 | OK as given |
| Romanelli & Tushman (1986), *Inertia, Environments, and Strategic Choice* | Elaine Romanelli & Michael L. Tushman. 1986. "Inertia, Environments, and Strategic Choice: A Quasi-Experimental Design for Comparative-Longitudinal Research." *Management Science* 32(5):608–621. doi:10.1287/mnsc.32.5.608 | Venue is **Management Science**, not Admin Sci Quarterly; habitual-dropping of the subtitle |
| Gilbert (2005), *Unbundling the Structure of Inertia: Resource Versus Routine Rigidity* | Clark G. Gilbert. 2005. "Unbundling the Structure of Inertia: Resource Versus Routine Rigidity." *Academy of Management Journal* 48(5):741–763. doi:10.5465/amj.2005.18803920 | Venue is **Academy of Management Journal**, not Admin Sci Quarterly |
| Colombo et al. (2002), *The Determinants of Organizational Change and Structural Inertia* | Massimo G. Colombo & Marco Delmastro. 2002. "The Determinants of Organizational Change and Structural Inertia: Technological and Organizational Factors." *Journal of Economics & Management Strategy* 11(4):595–635. doi:10.1111/j.1430-9134.2002.00595.x | Actually **2 authors** (not "et al."); subtitle's last word is **Organizational**, not "Competitive" |
| Kelly & Amburgey, *A Dynamic Model of Strategic Change* | Dawn Kelly & Terry L. Amburgey. 1991. "Organizational Inertia and Momentum: A Dynamic Model of Strategic Change." *Academy of Management Journal* 34(3):591–612. doi:10.2307/256407 | Year is **1991** (the user omitted it); venue is **AMJ** |
| Becker & Knudsen (2016), *Inertia in Routines* | Sangyoon Yi, Thorbjørn Knudsen & Markus C. Becker. 2016. "Inertia in Routines: A Hidden Source of Organizational Variation." *Organization Science* 27(3):782–800. doi:10.1287/orsc.2016.1059 | **3 authors**, **Yi is lead author** (not "Becker & Knudsen"); venue is **Organization Science**, not ASQ |

**Why the errata itself matters**: it is precisely the sixth paper — the one that carries the reconciling reverse proposition — that the user's paraphrase drifts farthest from the canonical text (drops the lead author, gets the venue wrong). Bai et al.'s review cannot dissolve the byproduct-symptom dichotomy because, in essence, its "fusion" register is **missing the knife** that makes inertias and adaptation **mutually preconditioning** — and that knife is already ground in Yi-Knudsen-Becker 2016. Getting this chain whole (citation order, author order, venue) is the entry point if you want to move from "this is a review of a dichotomy" to "you can now mechanise the dichotomy".

### Yi-Knudsen-Becker 2016 abstract, quoted verbatim — what this card actually is

> Traditionally, routines have been perceived as a primary source of inertia, which slows down organizational change and hinders organizational adaptation ... routine-level inertia may help, rather than hinder, organization-level adaptation because reduced rates of routine-level changes may lead to temporal reordering. ... inertia acts as a source of variation that turns out to be useful for adaptation, helping explain why apparently inertial organizations keep surviving.

The flip is forceful: **routine-level inertia → temporal reordering → organisation-level adaptation** — inertia stops being an obstacle and becomes a timing device on the time axis. Bai et al.'s "fusion" narrative doesn't take this step, so "selection vs adaptation" stays a *spatial* dichotomy inside their review; Yi-Knudsen-Becker moves the dichotomy onto the **time axis and discharges it there**.

## Annotation: taking the suspended "fusion" over to a relative index

> A revision pass. Having finished Bai et al., the user delivered a same-construct systematic **working note** — plainer terminology, four-way taxonomies, and most importantly a *relative-inertia index* that turns Bai et al.'s label-level "fusion" into something computable. Below I bring in only the note's **original** parts: the "fusion" gets mechanically backfilled rather than just rhetoricised.

Bai et al.'s "fusion" is a *label, not a mechanism* — you can see where it sits, but not how it walks. The most natural way to end a marginalia closer than the review did is to **back-search for the device that lets "fusion" do work**: to flip organisational inertia out of an absolute noun and into a **relational concept** that puts "environmental change" and "organisational change" on the same metronome. That step turns out to answer Bai et al.'s two suspended threads at once — the byproduct/symptom pair becomes two asymptotes of one index, and the selection/adaptation pair becomes two cross-sections of one index. Across the Bai 2016 → Cheng et al. 2019 → Song & Peng 2026 ten-year window, the relative-inertia index is precisely the device that lets that label load-bear real structure.

### Tidying the construct boundary — three easy-to-conflate pairs

The user's note stresses that the *boundary confusion* across **organisational inertia / persistence / resistance / momentum** is itself one of Bai et al.'s "reasons for divergence." Three pairs matter most:

- **inertia ≠ momentum.** inertia = the organisation tends to hold its present state; momentum = the organisation tends to keep moving in whatever direction it was already moving. Ten years of an unchanged product portfolio = inertia; a firm that has spent a decade expanding internationally and keeps doing so = momentum. **Same family, not synonyms** — Kelly & Amburgey 1991 already drew this line, holding off the practice of treating "not moving" and "moving in the same direction" as the same phenomenon.
- **inertia ≠ resistance.** inertia can arise **without any agent actively resisting** (sunk cost + routine sedimentation suffice); resistance presupposes an agent actively blocking. This matters in management semantics: reading inertia as "the organisation resists" closes all of the cost-mechanical, cognitive-identity, and routine-sedimentation flanks in favour of a single one — the political one.
- **inertia ≠ "no change".** Treating `I = −ΔO` as the index privileges a firm that hasn't moved at all as max-inertia — which is illogical under a stable environment (where not moving may be locally optimal). **The absolute measurement must be replaced by a relative one.**

### Dimensions and mechanisms — two compact four-way tables

The working note's core architectural move is two orthogonal four-way taxonomies — **dimensions** (where inertia lives) and **mechanisms** (where inertia comes from). Together they backfill Bai et al.'s "measurement scatters" layer neatly:

| Dimension (where) | What persists |
|---|---|
| Structural inertia | hierarchy · departmental boundaries · power-reporting relations · formalisation level |
| Strategic inertia | product portfolio · target market · technology trajectory · R&D direction · business model |
| Resource rigidity | whether the firm changes its *existing allocation* — GPU budget, licences, supplier ties |
| Routine rigidity | whether the firm changes the *processes for using* those resources — decision mechanism, collaboration patterns, performance review |

| Mechanism (why) | Pathology |
|---|---|
| Sunk cost & adjustment cost | `Existing Structure → Investment → Switching Cost → Persistence` |
| Routine sedimentation | repeated behaviour → routine → routine reproduces itself → routine constrains future behaviour |
| Power structure | `Existing Structure → Power Distribution → Political Resistance → Inertia` |
| Cognition & org identity | `Past Success → Identity → Cognitive Commitment → Strategic Inertia` |

Two tables together explain why Bai et al.'s byproduct-vs-symptom pair **co-embeds**: dimensions read byproduct-flavoured, mechanisms read symptom-flavoured, and **they can sit at different addresses on the same organisation at the same time** — a firm can carry "byproduct" structural inertia while carrying "disease" routine inertia. Gilbert 2005's resource/routine split already touches that same diagonal, but Bai et al. do not set it back against the S/A contrast.

### Connecting "fusion" to a relative index: `I_it = V^E_it / (V^O_it + ε)`

The core backfill is to define organisational inertia as a **lag of organisational change behind environmental change**. Given org state `O_it` and environment state `E_it`, frame-to-frame velocity is

```
V^O_it  = ‖ O_it  – O_{i,t-1} ‖      # organisational-state velocity
V^E_it  = ‖ E_it  – E_{i,t-1} ‖      # environmental-state velocity
```

The relative-inertia index (ε avoids zero in the denominator)

```
        V^E_it
I_it = ─────────────
        V^O_it + ε
```

Reading the index:


- `I > 1`: environmental change outpaces organisational change → **high relative inertia** (adaptive lag)
- `I ≈ 1`: organisational change roughly matches environmental change
- `I < 1`: organisational change is outpacing environmental change; here the "symptom" reading of inertia dissolves on its own, byproduct-intuition is restored

The theoretical payoff dwarfs the form: this one index simultaneously parks every loose thread Bai et al. leave labelled but unresolved — byproduct vs symptom becomes the two asymptotes of the `V^O=0` and `V^O→∞` extremes; selection vs adaptation becomes two cross-sections of one index; and Yi-Knudsen-Becker's "routine-level inertia → temporal reordering → organisation-level adaptation" supplies the micro-foundation for *why* `I ≈ 1` is not a coincidence, i.e. why the organisation does not in fact need to chase the environment one-to-one frontier-tight.

The caveat is direct: **this is a conceptual measurement framework, not a metric that any of Bai et al. 2016 / Cheng et al. 2019 / Song & Peng 2026 has adopted as standard.** It answers "how should S/A fusion be mechanised" but leaves "what is the environment state `E_it`?" — a well-known no-default sub-problem — explicitly hanging; Bai et al.'s review hits exactly this wall after decades of arguing about measurement.

### How that backfill lands operationally — research cut

The minimum viable stack to run the "environment-to-org" relative measure is three things: a longitudinal firm-level panel (state `O_it`), a same-window environment-state proxy (`E_it`), and an explicit **choice of which environment-axis to take** (product mix? market? technology roadmap? one or several). That makes the backfill adjacent to yunqi's existing SE×AI panel work — the AIDev class of datasets has long enough firm-level dev-activity panels in fintech / manufacturing / recruiting services to sit as `O`; sector-level tech-adoption rates, M&A / rollups as product proxies, and so on can serve as `E`. Regressing AI adoption rates on this `I` is the operational form of the Gilbert-vs-Yi-Knudsen-Becker pair of competing hypotheses the main note already lays out.

One-line summary of the backfilling done: **under the relative index, Bai et al.'s "byproduct vs disease" is no longer a dichotomy but two asymptotes of the same index; "selection vs adaptation" is no longer a dichotomy but two cross-sections of the same index.** That backfill is the step Bai et al.'s review *did not* take, and the step a marginalia reading of the review *naturally* does.

### Provenance pins for the revision

- Consistent with `### Yi-Knudsen-Becker 2016 abstract, quoted verbatim`: the reverse proposition and the *relative index* are two forms of conceptual plug on the same reading path — the former moves inertias/adaptation onto the time axis, the latter moves the organisation's velocity to an environmental frame.
- Song & Peng 2026 (`doi:10.1007/s40622-025-00458-8`) supply one verifiable co-concurrent effort at an "**anti-inertia / adaptability**" evaluation method — a computational companion to this conceptual framework, not its warrant.

## Sentences I kept

- The title, intact: 组织惰性:成功的副产品,抑或组织病症?——基于系统性审查方法的述评与展望 — a single title-line already sets the research radius and the argumentative posture of the whole paper.
- Abstract: "以环境选择和组织适应两类视角**及其融合**为主线" — "**及其融合** / *and their fusion*" is the paper's promise, and also the hook it leaves for those who follow; the mechanism of fusion never lands.
- Abstract, last sentence: "本文对组织惰性研究成果进行系统性梳理在国内外尚属首次". This "first-of-its-kind" self-claim is a useful bibliometric signal (the moment a concept's literature set first takes a citable chronology-node shape) — but because the paper is in a **Chinese-language journal** published in 2016, it never enters the English-language citation flow; its "first" is unquoted, unknown in the English-language literature. This is a bibliometrically typical case of **silencing by language (语言遮蔽)**: the first-claim is real, but the publishing language keeps it out of the global citation network, and a particular language circle simply "does not see" it.
- Yi-Knudsen-Becker 2016, abstract: "inertia acts as a source of variation that turns out to be useful for adaptation" — flips inertias and adaptation from antagonists into temporal complements.

## Who it's for / limits

- **For**: people who want a joined-up map of the forty-year organisational-inertia literature (English + Chinese, in one); people who want to look back from inside the Chinese research world at how the Hannan-Freeman lineage and the strategic-choice lineage blur into each other; researchers doing "AI × organisation" empirical work who need **an already-collated concept lexicon** for design work.
- **Limits**: (1) Chinese-language venue; the paper's translation of the S/A split performs a terminological softening ("环境选择" softens population ecology; "组织适应" softens strategic choice), so an English-language reader working only from the SA literature won't map cleanly onto Bai et al.'s Chinese terminology; (2) the "first-of-its-kind" self-claim is real but bibliographically **unobservable** in the English-language literature — a silencing by language; (3) "fusion" is a label, not a mechanism, the most serious limit — especially after one reads Yi-Knudsen-Becker 2016 and notices that the reconciling card was already on the shelf but never played.

## Hooks with other marginalia

- **Isomorphic with [009 · borrowed the boundary, not the fractal](../009-homology-without-fractal/note.en.md)**: 009 is "the paper borrows Abbott's boundary but doesn't activate the fractal mechanism"; this one is "the review raises the S/A dichotomy but doesn't bring in Yi-Knudsen-Becker's reverse proposition." Both are the same shape — set up a dichotomy, then don't press the switch that would dissolve it. It seems to be a recurring motif in this notebook worth naming.
- **Sits with [005 · four academic voices](../005-discipline-style-voices/note.en.md)**: 005 measures disciplinary "voice" as computable distance; this note takes "citation silencing" (a Chinese first-claim being unobservable in English) as a scientometric phenomenon. Both treat "discipline-language difference" as a measurable context factor — exactly the kind of unit that ties into yunqi's science-of-science agenda.
- **Distant kin to [007 · nuance rises and falls](../007-nuance-rises-and-falls/note.en.md)**: 007 measures word-weakening over time; this note's meta-phenomenon is "concept first-claims get silenced by publishing language." Both are working different slices of the same scientometric asymmetry.
