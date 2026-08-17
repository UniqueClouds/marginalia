# Homologies in Fields of Cultural Production. Evidence from the European Scientific Field — a reading note: borrowed the boundary, not the fractal

<div class="lang-switch" markdown>
🌐 Language / 语言：[中文](009-homology-without-fractal.zh.md) · **English**
</div>

<details><summary style='cursor:pointer;color:#888;'>Provenance（来源与元数据）</summary><table style='border:1px solid #eee;border-radius:8px;'><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>id</td><td style='padding:3px 10px;'>marginalia-009-en</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>title</td><td style='padding:3px 10px;'>Homologies in Fields of Cultural Production. Evidence from the European Scientific Field — a reading note: borrowed the boundary, not the fractal</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>date</td><td style='padding:3px 10px;'>2026-08-17</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>published</td><td style='padding:3px 10px;'>2026-08-17</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>kind</td><td style='padding:3px 10px;'>note (paper reading note)</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>issue</td><td style='padding:3px 10px;'>17</td></tr></table></details>


# *Homologies in Fields of Cultural Production. Evidence from the European Scientific Field* — a reading note: borrowed the boundary, not the fractal

> Putting two "fields" side by side always brings you back to one question: is it resemblance, isomorphism, or homology; and at which scale does it run.

## The paper itself

- **Source**: *Poetics* vol. 107 (2024), article 101945; doi:10.1016/j.poetic.2024.101945. CC-BY open access; the LSE Research Online mirror hosts a clean published PDF.
- **Authors**: Pierre Benz (École de bibliothéconomie et des sciences de l'information, Université de Montréal), Kristoffer Kropp and Trine Cosmus Nobel (Department of Social Sciences and Business, Roskilde University), Thierry Rossier (LIVES, University of Lausanne; Sociology, LSE).
- **Keywords (as the paper tags itself)**: Disciplines · Fields · Homology · Autonomy · Topics · Culture.

### Abstract (quoted verbatim)

> This article suggests a comparative field analytical approach to fields of cultural production. Combining concepts from field analysis and focusing on homology with topic modeling and multiple correspondence analysis, we compare four scientific disciplines and show homological structures along both internal and external principles of differentiation. The empirical analysis suggests that despite major differences between the four disciplines (biology, chemistry, economics, and sociology), they are structured along similar principles. Moreover, cognitive distinctions in certain disciplines can be correlated with institutional properties and symbolic hierarchies. Despite the similarities, the analysis also shows important differences between the four disciplines related to internal organization and their relations to both other scientific disciplines and the field of power. The article shows how topic modeling and multiple correspondence analysis can cross-fertilize to understand how fields of cultural production differentiate and how cultural practices (here scientific knowledge production) relate to social structures (here academic hierarchies and prestige). The method hence allows for comparison between fields of cultural production while retaining a nuanced analysis of specific fields and the practices that constitute them.

One-sentence compression: **graft LDA topic modeling and multiple correspondence analysis (MCA) onto field analysis, compare four scientific disciplines, and show that they share structural form (homology) — but the depth and the weight of the "internal/external" principles of differentiation vary across disciplines.**

### Data and method skeleton

- **Data**: 12,206 ERC (European Research Council) grants + 200,576 associated publications. An ERC grant abstract is the PI declaring what they will do — used as a proxy for position-takings; publications are classified via Scopus's 27 major fields / 300+ minor fields.
- **Method**: **LDA topic modeling** grows a topic space; **MCA (multiple correspondence analysis, a branch of geometric data analysis)** projects topics alongside supplementary variables (journal discipline, ERC panel, high-ranked journal, supportive organisation, most-funded).
- **The three measurable principles of homology** (the paper's own operationalization):

  1. **position-takings ↔ positions** — whether the topic space is structured by disciplinary affiliations;
  2. **relative autonomy from neighbouring disciplines** — whether a discipline's main axis is dominated by its relation to adjacent ones;
  3. **interaction with the field of power** — whether external power-field pressures (funding priorities, recognition regimes of high-cited journals) are projected within the discipline.

  Once both main axes are computed for each discipline, the horizontal axis collapses onto the same pair everywhere: **autonomy ↔ heteronomy** — the hidden protagonist sitting in the middle of the paper.

### Empirical findings per discipline (§5.1–5.4)

**Biology §5.1**: the first axis is field-specific — functional biology on the left, evolutionary biology on the right (the Mayr 1961 dual), with high-ranked journals pinned to functional biology; strongest homology.

![Fig. 3 · space of topics in biology](/assets/entries/009-homology-without-fractal/fig3-biology.png)
*Fig. 3 · the space of topics in biology (taken from p. 8 of the paper)*

**Chemistry §5.2**: the first axis is *not* field-specific — left electronic / energy / semiconductor (PE8 engineering, PE3 condensed-matter physics), right cell / disease / protein (bleeding into biology); the disciplinary boundary is looser than biology's.

![Fig. 4 · space of topics in chemistry](/assets/entries/009-homology-without-fractal/fig4-chemistry.png)
*Fig. 4 · the space of topics in chemistry (taken from p. 9 of the paper)*

**Economics §5.3**: first axis = autonomous vs heteronomous — heteronomous pole productivity / growth / business / firm / inequality responds to political-economic demand; autonomous pole model / equilibrium / inference / contract is the microeconomic vocabulary; the topic axis does *not* correspond to disciplinary affiliation — captured by the field of power.

![Fig. 5 · space of topics in economics](/assets/entries/009-homology-without-fractal/fig5-economics.png)
*Fig. 5 · the space of topics in economics (taken from p. 10 of the paper)*

**Sociology §5.4**: first axis = autonomous vs heteronomous as well — left culture / global / social (autonomous), right citizen / party / opinion (political sociology / political science); but political-science and sociology journals are bundled together and spread evenly, so no stable hierarchy can be recovered — the paper's verdict is "dissolved."

![Fig. 6 · space of topics in sociology](/assets/entries/009-homology-without-fractal/fig6-sociology.png)
*Fig. 6 · the space of topics in sociology (taken from p. 11 of the paper)*

### Closing Table 2, made compact

| Discipline | Main axis | Second axis | homology status |
|---|---|---|---|
| Biology | topics↔disciplines | autonomy vs other disciplines | **strong** homology |
| Chemistry | autonomy vs other disciplines | topics↔disciplines | **moderate** homology |
| Economics | autonomy vs field of power | autonomy, no topics↔disciplines | **heteronomous** |
| Sociology | autonomy vs other disciplines | autonomy vs other disciplines | **dissolved** |

"Dissolved" is the paper's word for sociology floating in the topic space and never recovering a stable hierarchy. In Table 2, sociology's two columns are both autonomy-only — the discipline is compressed down to the single dimension "where it sits relative to the others."

## Reading note: borrowed the boundary, not the fractal

The pleasure of this paper is not in what it solves but in the small move it does not make. Benz et al. neatly hang Andrew Abbott's "boundary + disciplinary chaos" pair — the 1995 *Things of Boundaries* and the 2001 *Chaos of Disciplines* — on their reference shelf, yet in sixteen pages of body the **mechanism that is genuinely Abbott's, namely fractal distinction (the same cleavage reproducing itself across recursive scales), is never switched on.** I ran a cheap check: pulled the PDF into plain text and grepped the whole document for `fractal`, `recursive`, `self-similar`, `nested`, `linked ecolog` — **zero hits.**

That is not a sign the paper is wrong — it is a sign that they borrowed Abbott's "boundary" skin and left his "fractal" blade in its sheath. As a result the paper's verdict, "partial homology," sits frozen on a static ladder: four disciplines graded strong-to-dissolved, then a stop. So a marginalia entry is exactly the right shape for what I want to record: a switch that was already present, inside the paper, that no one pressed.

### A few tensions I kept circling

- **Borrowed the boundary, not the fractal.** Abbott 1995 and 2001 are in the reference list; in the body, Abbott is invoked in §1 only to the extent that "disciplines are bounded, transgressive objects" — a soft citation. The genuine Abbott mechanism — the same cleavage reproducing itself at recursive scales — is not present. The paper can only deliver "partial homology" as a static four-level grading because it does not engage the one mechanism that would explain *why depths differ*.
- **Wang 2016 is on the shelf, never cut.** Wang's piece doing the homology-vs-isomorphism cut is referenced, but the body never takes the theoretical consequence that cut implies — the paper's "homology" tilts toward "seeing similar principles across fields" and never walks down to the deeper, structurally-isomorphic institutional layer that the contrast would have opened up.
- **autonomy/heteronomy is the hidden protagonist.** The third principle measures it directly, but more importantly Table 2 puts it at the centre of all four disciplines' interpretations — only the paper never names it as Abbott would, as a "fractal depth." Reading this I kept hearing one line in my head: **homology runs on the horizontal axis; the fractal could have run on the vertical.**
- **Biology under the lens is an empirical specimen for Abbott.** Biology axis-1 is topics↔disciplines; axis-2 is autonomy; high-ranked journals are pinned to functional biology; the paper cites Mayr 1961 to make the "functional vs evolutionary" substructure explicit — this is already an empirical version of "the same cleavage recurs at lower scales," i.e. Abbott's fractal distinction. The paper is standing within half a step of the fractal framing and does not take that step.

## Sentences I kept

- Abstract: "we compare four scientific disciplines and show homological structures along both internal and external principles of differentiation." — the paper's own framing of "homology running on two cross-sections (internal/external)."
- §2: "homology may refer more broadly to the observation of similar principles of vision and division across different fields (Bourdieu, 1979, p.547; Bourdieu, 1989, p.384; Sapiro, 2002)." — the precise page citations to Bourdieu are more solid than second-hand retellings.
- Conclusion: "we observe partial homology. ... we cannot conclude on the existence of homologies between positions and position-takings in this case [sociology]." — the partial verdict lands on sociology being unresolvable.
- End of §6: "Proposing an advancement in comparative field theory for cultural production involves emphasizing two key features: the utility of field theory in comprehending relative autonomy and homology within and between fields, and the necessity for empirical consideration of the interplay between content and positions within a specific field." — the paper itself points its future-work sentence at "content × positions" within a specific field; that is precisely the slot where fractal depth could enter.

## Who it's for / limits

- **For**: scholars doing field analysis who want cross-discipline comparisons; people trying to wire LDA into geometric data analysis; readers of science-of-science who have read Bourdieu but not this particular operationalization of him.
- **Limits**: ERC grants + their publications are a proxy that only sees the position-takings of PIs who were funded and thus enfranchised — the periphery of each field is thinly sampled; ERC panels are not one-to-one with "discipline" (the paper itself concedes this when sociology spills across many panels); "Europe" is the bounded frame, which flattens national-level differences within the European field; finally, both isomorphism and fractal — two existing sociological mechanisms available alongside homology — are not invoked, a limit the paper openly names as its "conceptual refinement still imperative" (§6 end).

## Hooks with other marginalia

- Sits with [005 · discipline-style-voices](005-discipline-style-voices.en.md): 005 measures four disciplines' **rhetorical style** (counts, length, posture); this paper measures four disciplines' **cognitive/positional homology**. Both books take "four disciplines" as the comparative cell, but 005 reads language style off the surface of text, while this paper reads off a topic space whose axes are the standing-room — the former grabs how the discipline speaks, the latter grabs where it stands to speak. Read together, one irony surfaces: in 005 the four-disciplinary "voice" difference is computable and concrete; in Benz's eyes that same heterogeneity is a *symptom of homology failing* — the two measures give sociology frictionally different verdicts.
- Sits with [002 · writing like Dourish](002-writing-like-dourish.en.md): 002 takes a single scholar's corpus as the indicator of "one voice"; this paper takes a whole discipline's abstract corpus as the indicator of "one stance" — both lower the level of field analysis down to the text layer.
- And an oblique line to [008 · How to Scale Your Model note](008-llm-scaling-book.en.md): that technical book lives in the tension between the *mathematical correctness of an algorithm* and the *physical squeezability of hardware* — a horizontal axis of "is it squeezed onto the roofline." This paper lives in the tension between *horizontal homology across fields* and *recursive possibility at depth* — also a horizontal vs vertical choice of axis.


---

> 🌐 [阅读中文版](009-homology-without-fractal.zh.md)

