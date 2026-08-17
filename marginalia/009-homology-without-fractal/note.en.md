---
id:              marginalia-009-en
title:           "Borrowed the Boundary, Not the Fractal — a reading note on Benz et al., Homologies in Fields of Cultural Production (Poetics 2024)"
date:            2026-08-17
published:       2026-08-17
kind:            note (paper reading note)
sources:
  - "Benz, Pierre, Kristoffer Kropp, Trine Cosmus Nobel, and Thierry Rossier. 2024. Homologies in Fields of Cultural Production. Evidence from the European Scientific Field. Poetics 107:101945. doi:10.1016/j.poetic.2024.101945"
  - "Open-access PDF (CC-BY, mirrored by LSE Research Online): http://eprints.lse.ac.uk/126061/1/1-s2.0-S0304422X24000846-main.pdf — all quotations and figures here were verified against this primary full text"
  - "Abbott, Andrew. 1995. Things of Boundaries. Social Research 62:857–882."
  - "Abbott, Andrew. 2001. Chaos of Disciplines. University of Chicago Press."
  - "Wang, Yingyao. 2016. Homology and Isomorphism: Bourdieu in Conversation with New Institutionalism. The British Journal of Sociology 67(2):348–370. doi:10.1111/1468-4446.12197"
  - "Semantic Scholar Graph API (x-api-key verified 200) — used to inspect the paper's reference set and citing edges"
initial-prompt: "New idea: bring this Benz et al. 2024 article into a reading relationship with Andrew Abbott's fractal distinction."
agent:           ZCode CLI
model:           GLM (Zhipu)
issue:           17
---

# Borrowed the Boundary, Not the Fractal — a reading note on Benz et al. (Poetics 2024)

> Putting two "fields" side by side always brings you back to one question: is it resemblance, isomorphism, or homology; and at which scale does it run.

## Musing

The pleasure of this paper is not in what it solves but in the small move it does not make. Benz et al. neatly hang Andrew Abbott's "boundary + disciplinary chaos" pair — the 1995 *Things of Boundaries* and the 2001 *Chaos of Disciplines* — on their reference shelf, yet in sixteen pages of body the **mechanism that is genuinely Abbott's, namely fractal distinction (the same cleavage reproducing itself across recursive scales), is never switched on.** I ran a cheap check: pulled the PDF into plain text and grepped the whole document for `fractal`, `recursive`, `self-similar`, `nested`, `linked ecolog` — **zero hits.**

That is not a sign the paper is wrong — it is a sign that they borrowed Abbott's "boundary" skin and left his "fractal" blade in its sheath. As a result the paper's verdict, "partial homology," sits frozen on a static ladder: four disciplines graded strong-to-dissolved, then a stop. So a marginalia entry is exactly the right shape for what I want to record: a switch that was already present, inside the paper, that no one pressed.

## The paper

- **Source**: *Poetics* vol. 107 (2024), article 101945; doi:10.1016/j.poetic.2024.101945. CC-BY open access; the LSE Research Online mirror hosts a clean published PDF.
- **Authors**: Pierre Benz (École de bibliothéconomie et des sciences de l'information, Université de Montréal), Kristoffer Kropp and Trine Cosmus Nobel (Department of Social Sciences and Business, Roskilde University), Thierry Rossier (LIVES, University of Lausanne; Sociology, LSE).
- **Method skeleton**: they treat ERC (European Research Council) grant abstracts as carriers of "disciplinary position-takings," run **LDA topic modeling** to grow a topic space, then **MCA (multiple correspondence analysis, a branch of geometric data analysis)** to project topics alongside supplementary variables (journal discipline, ERC panel, high-ranked journal, supportive organisation, most-funded); and finally compare the "axis 1 + axis 2" pair across four disciplines (biology, chemistry, economics, sociology).
- **Data scale**: 12,206 ERC grants + 200,576 associated publications. This is a genuine "field analysis × scientometrics" graft — not yet another LDA paper.

## What they make "homology" do

Two lines should be kept apart before reading on:

- **homology** — Bourdieu's usage (1979:547 / 1989:384): the same principle of vision and division recurring across different fields. It runs **horizontally**: discipline vs discipline;
- **isomorphism** — the new-institutionalist usage. Wang 2016 has carefully cut this conceptual pair apart, and the entry is clean on Benz's reference list, yet **the body text never cuts the term** — `isomorph` only appears in the body as a word inside the Wang 2016 reference entry; the prose of the paper does not use it.

This is a deliberate terminological narrowing: they want a *comparably empirical* operational concept (homology) without loading the structural-isomorphism baggage that comes with isomorphism. Worth marking.

Their operational "homology" is decomposed into three measurable principles:

1. **position-takings ↔ positions** — whether the topic space is structured by disciplinary affiliations (how strongly topics correspond to disciplines);
2. **relative autonomy from neighbouring disciplines** — whether a discipline's topic axis is dominated by its relation to adjacent ones;
3. **interaction with the field of power** — whether external power-field pressures (funding priorities, recognition regimes of high-cited journals) are projected within the discipline.

The two main axes that come out of measuring the three principles all collapse onto the same pair: **autonomy ↔ heteronomy.** That dichotomy is the never-named but always-there central axis of the paper.

## Translating their claims

1. **ERC abstracts are a legitimate vehicle for field analysis**: ERC is a common European arena, cross-comparable; abstracts are PIs declaring what they will do — a proxy for position-takings, not for the totality of a discipline.
2. **Which layer homology runs on is the question**: Bourdieu's homology in *Distinction* marks the correspondence of position ↔ position-taking; this paper stretches it into "shared vision/division across fields" — a use case of GDA that has been available but underused (Schmidt-Wellenburg & Lebaron 2018:26 already flagged this).
3. **The horizontal axis collapses to autonomy/heteronomy**: across all four disciplines, both axes of interpretation ultimately fall onto this same pair — differing only in which one sits at axis 1 and which at axis 2.
4. **Partial homology**: the four disciplines are not equally "homologous" but graded — biology strong, chemistry next, chemistry standardized, economics dragged off by the field of power, sociology "dissolved."
5. **Their clean closing table (Table 2)**:

   | Discipline | Main axis | Second axis | homology status |
   |---|---|---|---|
   | Biology | topics↔disciplines | autonomy vs other disciplines | **strong** homology |
   | Chemistry | autonomy vs other disciplines | topics↔disciplines | **moderate** homology |
   | Economics | autonomy vs field of power | autonomy, no topics↔disciplines | **heteronomous** |
   | Sociology | autonomy vs other disciplines | autonomy vs other disciplines | **dissolved** |

   "Dissolved" is the paper's word for sociology floating in the topic space and never recovering a stable hierarchy. In Table 2, sociology's two columns are both autonomy-only — the discipline is compressed down to the single dimension "where it sits relative to the others."

6. **Biology under the lens is an empirical specimen for Abbott**: the biology axis-1 is topics↔disciplines; axis-2 is autonomy; high-ranked journals are pinned to functional biology; the paper cites Mayr 1961 to make the "functional vs evolutionary" substructure explicit — this is already an empirical version of "the same cleavage recurs at lower scales," i.e. Abbott's fractal distinction. The paper is standing within half a step of the fractal framing and does not take that step.

## A few tensions I kept circling

This marginalia is not a polemic, but three tensions sat with me after the last page:

- **Borrowed the boundary, not the fractal.** Abbott 1995 and 2001 are in the reference list; in the body, Abbott is invoked in §1 only to the extent that "disciplines are bounded, transgressive objects" — a soft citation. The genuine Abbott mechanism — the same cleavage reproducing itself at recursive scales — is not present. The paper can only deliver "partial homology" as a static four-level grading because it does not engage the one mechanism that would explain *why depths differ*.
- **Wang 2016 is on the shelf, never cut.** Wang's piece doing the homology-vs-isomorphism cut is referenced, but the body never takes the theoretical consequence that cut implies — the paper's "homology" tilts toward "seeing similar principles across fields" and never walks down to the deeper, structurally-isomorphic institutional layer that the contrast would have opened up.
- **autonomy/heteronomy is the hidden protagonist.** The third principle measures it directly, but more importantly Table 2 puts it at the centre of all four disciplines' interpretations — only the paper never names it as Abbott would, as a "fractal depth." Reading this I kept hearing one line in my head: **homology runs on the horizontal axis; the fractal could have run on the vertical.**

## Sentences I kept

- Abstract: "we compare four scientific disciplines and show homological structures along both internal and external principles of differentiation." — the paper's own framing of "homology running on two cross-sections (internal/external)."
- §2: "homology may refer more broadly to the observation of similar principles of vision and division across different fields (Bourdieu, 1979, p.547; Bourdieu, 1989, p.384; Sapiro, 2002)." — the precise page citations to Bourdieu are more solid than second-hand retellings.
- Conclusion: "we observe partial homology. ... we cannot conclude on the existence of homologies between positions and position-takings in this case [sociology]." — the partial verdict lands on sociology being unresolvable.
- End of §6: "Proposing an advancement in comparative field theory for cultural production involves emphasizing two key features: the utility of field theory in comprehending relative autonomy and homology within and between fields, and the necessity for empirical consideration of the interplay between content and positions within a specific field." — the paper itself points its future-work sentence at "content × positions" within a specific field; that is precisely the slot where fractal depth could enter.

## Who it's for / limits

- **For**: scholars doing field analysis who want cross-discipline comparisons; people trying to wire LDA into geometric data analysis; readers of science-of-science who have read Bourdieu but not this particular operationalization of him.
- **Limits**: ERC grants + their publications are a proxy that only sees the position-takings of PIs who were funded and thus enfranchised — the periphery of each field is thinly sampled; ERC panels are not one-to-one with "discipline" (the paper itself concedes this when sociology spills across many panels); "Europe" is the bounded frame, which flattens national-level differences within the European field; finally, both isomorphism and fractal — two existing sociological mechanisms available alongside homology — are not invoked, a limit the paper openly names as its "conceptual refinement still imperative" (§6 end).

## Hooks with other marginalia

- Sits with [005 · discipline-style-voices](../005-discipline-style-voices/note.en.md): 005 measures four disciplines' **rhetorical style** (counts, length, posture); this paper measures four disciplines' **cognitive/positional homology**. Both books take "four disciplines" as the comparative cell, but 005 reads language style off the surface of text, while this paper reads off a topic space whose axes are the standing-room — the former grabs how the discipline speaks, the latter grabs where it stands to speak. Read together, one irony surfaces: in 005 the four-disciplinary "voice" difference is computable and concrete; in Benz's eyes that same heterogeneity is a *symptom of homology failing* — the two measures give sociology frictionally different verdicts.
- Sits with [002 · writing like Dourish](../002-writing-like-dourish/note.en.md): 002 takes a single scholar's corpus as the indicator of "one voice"; this paper takes a whole discipline's abstract corpus as the indicator of "one stance" — both lower the level of field analysis down to the text layer.
- And an oblique line to [008 · How to Scale Your Model note](../008-llm-scaling-book/note.en.md): that technical book lives in the tension between the *mathematical correctness of an algorithm* and the *physical squeezability of hardware* — a horizontal axis of "is it squeezed onto the roofline." This paper lives in the tension between *horizontal homology across fields* and *recursive possibility at depth* — also a horizontal vs vertical choice of axis.
