---
id: marginalia-027
title: "How rhetoric amplifies knowledge in networks — selective citation, social media promotion, and weak foundations"
date: 2026-10-08
published: 2026-10-08
kind: proposal
sources:
  - "Peng, Qiu, Fosse & Uzzi (2024), doi:10.1073/pnas.2320066121; PMC full text"
  - "Qiu, Chen & Li (2026), Counterfactual LLM-based Framework for Measuring Rhetorical Style; official ICLR paper"
  - "Fang et al. (2022), doi:10.1145/3510003.3510121; author-lab full text"
  - "Stavrova et al. (2025), doi:10.1038/s44271-025-00293-8; publisher full text"
  - "Chen, Teplitskiy & Jurgens (2025), doi:10.18653/v1/2025.acl-long.1534; ACL Anthology"
  - "Gilbert (1977), doi:10.1177/030631277700700112; publisher record"
  - "Small (1978), doi:10.1177/030631277800800305; publisher abstract and original scan"
  - "Latour (1987), Science in Action; author bibliography and scanned first part"
  - "Cozzens (1989), doi:10.1007/BF02017064; publisher abstract"
  - "Mizruchi & Fein (1999), doi:10.2307/2667051; publisher abstract"
  - "Greenberg (2009), doi:10.1136/bmj.b2680; PubMed abstract and PMC full text"
  - "Teplitskiy et al. (2022), doi:10.1016/j.respol.2022.104484; publisher full text"
  - "Boutron et al. (2010), doi:10.1001/jama.2010.651; PubMed/publisher abstract and metadata"
  - "Meyer & Rowan (1977), doi:10.1086/226550; publisher abstract and metadata"
  - "Bromley & Powell (2012), doi:10.1080/19416520.2012.684462; author-hosted full text"
  - "Weiss (1979), doi:10.2307/3109916; JSTOR metadata and university-hosted scan"
  - "Carlile (2004), doi:10.1287/orsc.1040.0094; INFORMS abstract and metadata"
  - "Szulanski (1996), doi:10.1002/smj.4250171105; Wiley abstract and metadata"
  - "Leung et al. (2017), doi:10.1056/NEJMc1700150; author institution ICES research record"
  - "Beers et al. (2023), doi:10.1126/sciadv.adh1933; original paper and UW author bibliography"
  - "Bagchi, Malmi & Grabowicz (2025), doi:10.1609/icwsm.v19i1.35809; official record and author-preprint full text"
  - "Luc et al. (2021), doi:10.1016/j.athoracsur.2020.04.065; original research abstract"
  - "Branch et al. (2024), doi:10.1371/journal.pone.0292201; PLOS full text"
initial-prompt: "overclaim in academic research paper; overclaim and 形式上 或者 名义上的 知识流动 而非实质上的流动. Find a few foundational readings and update my website."
agent: Codex
follow-up-prompt: "Are there related investigations in the sociology of knowledge and science studies? Connect Sophie Qiu's promotional-language research, Hong Chen's Counterfactual LLM-based Framework for Measuring Rhetorical Style, and Hongbo's This Is Damn Slick to whether rhetorical papers, including overclaim, are more likely to be cited."
clarification-prompt: "Focus on papers with weak foundations that attract a wave of citations through overclaim or oververbose presentation, leading to knowledge chains whose foundations are problematic."
extension-prompt: "Connect the UW pandemic selective-citation study, rhetoric in papers and promotional tweets, tweet visibility, later academic citations, and network prominence; retain weak foundations as one risk pathway."
updated: 2026-10-09
model: GPT-6
issue: 75
---

# How rhetoric amplifies knowledge in networks — selective citation, social media promotion, and weak foundations

> Research seed: how do paper presentation, social media promotion, and citers’ selection and interpretation amplify knowledge’s visibility and network prominence? Is that prominence accompanied by independent evidence and substantive contribution, or mainly by rhetoric and support for positions? Dependency chains rooted in weak evidence are one risk pathway. These are questions to test.

## Core idea

The current overarching question is **how rhetoric changes knowledge’s position in communication and citation networks**. Separately measure source-paper rhetoric, promotional-post rhetoric, and which papers citers select and how they restate or use claims. Rhetorical citation can legitimately organize arguments and acknowledge knowledge; unsupported amplification requires separate assessment.

One previously proposed risk pathway is **an insufficiently supported claim being treated as a reliable premise by later work**. Other parts of the source paper may be sound. Assess what makes the particular claim insufficiently grounded—design, measurement, controls, inference, or scope—independently of citation counts and writing style.

The proposed mechanism is **weak evidence + overclaim/verbose packaging → an early wave of citations → adoption as an established premise → repeated citations appearing to provide multiple sources of support → further research depending on the same weak foundation**. Citation counts may grow without corresponding growth in independent evidence for the claim. Each transition requires testing; neither packaging-induced uptake nor a problematic entire chain is an established conclusion.

Trace **how apparent authority forms and how later work depends on it**. Downstream authors can accurately reproduce the source, substantively adopt its methods, or build studies around it while inheriting an insufficiently verified premise. Nominal citation, citation distortion, and substantive use are distinct features of the chain: **faithful transmission does not establish a reliable foundation, and substantive use does not guarantee a sound knowledge chain**. Independent validation, refutation, or narrower scope may repair or interrupt the dependency.

## Closest literature anchor and the links still to test

**Greenberg (2009)** is the core anchor: [How Citation Distortions Create Unfounded Authority](https://pmc.ncbi.nlm.nih.gov/articles/PMC2714656/). Its claim-specific network identifies neglected contrary evidence, amplification without new relevant data, and hypotheses becoming facts through citation. It motivates studying how citations generate unsupported authority but does not directly test verbose source presentation as the trigger for early uptake. The proposed connection joins **source evidential gaps, presentation, early reception, and dependencies across generations**.

A related case is **Leung, P. T. M., Macdonald, E. M., Stanbrook, M. B., Dhalla, I. A., & Juurlink, D. N. (2017). _A 1980 Letter on the Risk of Opioid Addiction._ NEJM, 376(22), 2194–2195.** [DOI](https://doi.org/10.1056/NEJMc1700150) · [Author institution record](https://www.ices.on.ca/publications/journal-articles/a-1980-letter-on-the-risk-of-opioid-addiction/). Examines how a brief letter was widely invoked to support low addiction risk in chronic-pain treatment without sufficient evidence for that extension. It illustrates the need to trace original support and downstream uses. A problematic chain does not require a verbose source; overextension may arise downstream.

**Measure overclaim and oververbose presentation separately.** Overclaim exceeds evidence; oververbose provisionally means repetition, redundancy, or elaborate packaging relative to actual information added. Such presentation might obscure evidential gaps or create an impression of thorough support, but it might instead reduce citations by increasing reading costs. Both are hypotheses. Length can reflect necessary technical detail and is not itself evidence of packaging or poor quality. The two features can occur together or independently.

## Connecting promotional language, rhetorical measurement, and OSS promotion

1. **Peng, H., Qiu, H. S., Fosse, H. B., & Uzzi, B. (2024). _Promotional language and the adoption of innovative ideas in science._ PNAS, 121(25), e2320066121.** [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11194578/) · [DOI](https://doi.org/10.1073/pnas.2320066121). Sophie Qiu's co-first-authored study examines promotional language in **grant proposals**, relating it to funding, innovativeness, and subsequent publication output and citations. It connects rhetoric to scientific resource allocation, without directly measuring paper-abstract rhetoric or equating promotion with unsupported exaggeration. Its word-substitution exercise concerns model predictions, not a randomized experiment on real citations.

2. **Qiu, J., Chen, H., & Li, Z. (2026). _Counterfactual LLM-based Framework for Measuring Rhetorical Style._ ICLR 2026.** [Official record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/085b4b5d1f81ad9e057ad2b3de922ad4-Abstract-Conference.html) · [Official paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/085b4b5d1f81ad9e057ad2b3de922ad4-Paper-Conference.pdf). Generates persona-based abstracts from identical substantive content and measures rhetoric through pairwise comparisons and a Bradley–Terry model. Across 8,485 ICLR submissions, rhetorical strength positively predicts citations and media attention after controls for review scores, subfield, and year. This directly addresses the citation-association question. **Counterfactuals measure style; they do not randomize real papers' exposure.** Review scores are also only a quality proxy, so the association does not establish a causal effect.

3. **Fang, H., Lamba, H., Herbsleb, J., & Vasilescu, B. (2022). _“This Is Damn Slick!” Estimating the Impact of Tweets on Open Source Project Popularity and New Contributors._ ICSE 2022, 2116–2129.** [Author paper](https://cmustrudel.github.io/papers/fang2022twitter.pdf) · [DOI](https://doi.org/10.1145/3510003.3510121). Hongbo's study uses matching and difference-in-differences to estimate effects of tweet bursts: approximately 7% more new stars and 2% more new commit authors on average. Its useful connection is **measuring popularity separately from actual participation**. Treatment is tweet exposure, not the title quotation's rhetorical intensity; promotional classification primarily uses link destinations. Stars/contributors and citations/knowledge use offer a mechanism analogy, not interchangeable measures.

4. **Stavrova, O., Kleinberg, B., Evans, A. M., & Ivanović, M. (2025). _Scientific publications that use promotional language in the abstract receive more citations and public attention._ Communications Psychology, 3, 118.** [Full text](https://www.nature.com/articles/s44271-025-00293-8). Analyzes 136,615 abstracts from Nature, Science, and PNAS. A **one-percentage-point** increase in promotional-word share predicts approximately 9–14% more citations per year, or 9% with covariate controls. Another direct study of the association, without causal identification. See existing [023 · Journal mediatization](../023-journal-mediatization/note.en.md).

5. **Chen, H., Teplitskiy, M., & Jurgens, D. (2025). _The Noisy Path from Source to Citation: Measuring How Scholars Engage with Past Research._ ACL 2025, 31786–31802.** [Official record and paper](https://aclanthology.org/2025.acl-long.1534/). Hong Chen's related work matches source claims to citation sentences to measure **citation fidelity** and investigate distortion along citation chains. This offers a tool for connecting source rhetoric with downstream changes in claims. Fidelity and substantive use still require separate coding: accurate repetition may not change research, while an adapted method may be substantively used.

**Role of these studies:** Sophie's work provides background on rhetoric, reception, and resource allocation; the ICLR paper provides rhetorical measurement and citation associations; Hongbo's study offers a design analogy connecting early exposure to later participation. None establishes the complete mechanism of weak source claims gaining uptake through packaging and creating dependencies across generations. The ACL study helps track distortion, but source evidential support still requires separate assessment: faithful repetition of a weak claim can also sustain a problematic foundation. This is a proposed integration, not an established novelty claim.

## Further connection: selective citation and social media promotion

### The UW study: shared evidence, competing perceived consensuses

**Beers, A., Nguyễn, S., Starbird, K., West, J. D., & Spiro, E. S. (2023). _Selective and deceptive citation in the construction of dueling consensuses._ Science Advances, 9(38), eadh1933.** [DOI](https://doi.org/10.1126/sciadv.adh1933) · [Open paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10516490/). Closely matches the remembered UW study, with **masks** as its case. Comparing academic citations with scientific commentary circulated via Twitter, it shows how selection and interpretation construct opposing perceived consensuses; misleading citation is especially prominent in anti-mask commentary. It does not establish equivalent polarization within academia or measure citation-induced changes in political attitudes.

Extend this question to academic groups selecting work consistent with their methods, theories, or arguments, examining **what is selected, how it is cited, and how relevant contrary evidence is treated**. Differences may reflect legitimate scope or methodological choices; selection does not automatically imply distortion. Distinguish reliable source papers being misused from weak source claims being faithfully transmitted.

### Three textual locations and three outcome levels

| Location/stage | Measure separately | Outcomes |
|---|---|---|
| Source paper | Abstract/discussion rhetoric, claim–evidence alignment, necessary detail versus redundancy | Original claims and their evidential support |
| Author promotion and third-party retelling | Contribution framing, expanded implications, certainty, and retained limitations; distinguish authors, institutions, and third parties | Spread, discussion, clicks/reading, and audience composition |
| Later academic citations | Background, endorsement/criticism, concrete use, selective quotation, and dependency on source claims | Citation growth, endorsement-based centrality, concentration within groups, multi-generation dependencies, and new independent evidence |

**The proposed connection is paper/claim → promotional post → social circulation and selective retelling → academic citations and their uses → position in the knowledge network.** Test each transition; social and academic communities are not necessarily the same. Existing academic status may also increase social circulation, requiring chronology and possible feedback to be retained.

“Undeservedly large prominence” requires an explicit benchmark: among comparable topics, paper ages, and evidence levels, does presentation or alignment with a group's position accompany greater endorsement and network prominence without corresponding independent validation? This measures relative prominence, not an algorithmically determined citation entitlement. Operationalize “unnecessary networks” as repeated referencing or dependencies on a specifically unsupported premise, assessed individually. Centrality, topical popularity, or being a citation descendant alone cannot establish a problematic network.

### Research directly connecting arXiv, Twitter, and citations

**Bagchi, C., Malmi, E., & Grabowicz, P. A. (2025). _Effects of Research Paper Promotion via ArXiv and X._ ICWSM, 19(1), 160–177.** [Official paper](https://ojs.aaai.org/index.php/ICWSM/article/view/35809) · [Author preprint](https://arxiv.org/abs/2401.11116). Links preprints, social mentions, and subsequent citations, estimating promotion effects from observational data with confounding adjustment and distinguishing author from other accounts. Promotion and citation growth already have direct research. Extend this to **specific promotional wording, claim expansion relative to the original, and types and communities of subsequent citation**. Adjustment does not guarantee removal of unmeasured confounding.

Experimental results suggest keeping the outcomes separate: **Luc et al. (2021), _Does Tweeting Improve Citations? One-Year Results From the TSSMN Prospective Randomized Trial_** ([Study](https://pubmed.ncbi.nlm.nih.gov/32504611/)) reports greater one-year citation growth in the randomized promotion group. **Branch et al. (2024), _Controlled experiment finds no detectable citation bump from Twitter promotion_** ([Paper](https://doi.org/10.1371/journal.pone.0292201)) finds increased downloads and online attention without a statistically significant three-year citation increase. These test promotion schemes, not isolated rhetorical wording. Visibility, discussion, and citations are separate outcomes.

### Two separable pilot studies

1. **Original paper–tweet–later citations:** within one field, link arXiv IDs, versions, and publication DOIs into one work identity. Retain pre-promotion text and tweet timestamps; annotate claims added and conditions removed in promotion. Measure circulation/discussion and subsequent citations and uses within fixed windows. Record impressions only when available; likes and reposts are not actual exposure, and missing impressions are not zero. Multiple tweets about one paper enable comparisons of wording and circulation, but paper-level citation growth cannot be attributed directly to a particular tweet.
2. **Groups–literature selection–claim use:** define groups from prior collaboration, methods, or explicit theoretical positions, avoiding circular definition from the citation outcomes to be explained. Build a candidate pool of relevant literature available at the time. Compare selection of supporting and opposing findings, manually checking applicability. Separate endorsement, criticism, method use, and background reference. Examine whether different groups quote different parts of the same paper and infer different conclusions, then test how these selections shape endorsement networks and claim prominence.

Retain paper rhetoric, tweet rhetoric, and citation interpretation as separate measurements, inspecting claim expansion between them. Account for pre-promotion author status, account audience, topic popularity, open access, and paper age. Circulation may mediate the effect of rhetoric, so distinguish estimation of a total effect from analysis of the pathway. High-quality papers can also gain citations, and criticism can raise total counts; extra citations are not automatically unsupported amplification. The weak-foundation question remains a stratified branch: **do weak claims made easier to promote and select become shared premises without independent support?**

## Separate foundations, presentation, and downstream dependency

| Concept | Working definition | Evidence to examine |
|---|---|---|
| Weak evidential foundation | Insufficient design, measurement, controls, or inference for a particular claim; not a judgment that the entire paper is invalid | Assess source support and uncertainty; low citations, negative findings, or non-replication alone do not establish weakness |
| Oververbose presentation | Redundancy, repetition, or elaborate packaging relative to information added; a provisional definition | Human assessment of redundancy and new information, accounting for necessary technical detail and genre; length alone is insufficient |
| Dependency on a weak foundation | Later work uses the claim as a premise while its support traces back to the same evidential gap | Distinguish independent evidence from repeated citation; assess dependency in reasoning, design, or methods and subsequent validation or repair |
| Overclaim | Claim strength or scope exceeds evidential support | Compare abstract/discussion claims with methods, results, and limitations; e.g., causality inferred from correlation or unrestricted generalization from a limited sample |
| Formal / nominal knowledge flow | Papers, terms, or contribution narratives enter downstream texts, but observed evidence establishes only acknowledgment, repetition, or legitimation | Background citations, contribution labels, repeated conclusions; when concrete use is not observed, record “substantive use unconfirmed” |
| Substantive knowledge flow | Knowledge enters downstream reasoning or work and changes problem framing, methods, explanations, or practice | Method adaptation, theoretical derivation, treatment of boundary conditions, replication or refutation, traceable design/decision changes |

Citation counts establish visible connections. Separately assess foundations, presentation, fidelity, downstream use, and new independent support. Citing a paper does not imply dependence on its weak claim; criticism, correction, and successful independent validation should not count as perpetuating the weak foundation.

## More direct foundations: sociology of knowledge and science studies

This question has an established intellectual history and should not be situated only in organizational decoupling or general knowledge transfer. Relevant research examines **citation rhetoric, papers as concept symbols, selective interpretation of knowledge, the transformation of claims into facts, and differences between citations and influence**. These concepts are related but do not all denote overclaim or jointly establish that more citations imply emptier knowledge flow.

1. **Gilbert, G. N. (1977). _Referencing as Persuasion._ Social Studies of Science, 7(1), 113–122.** [DOI](https://doi.org/10.1177/030631277700700112). Citations participate in persuasion and argument, rather than merely documenting intellectual debts. A classic starting point for distinguishing citation circulation from knowledge use. A rhetorical function does not itself imply deception or absence of intellectual contribution.

2. **Small, H. G. (1978). _Cited Documents as Concept Symbols._ Social Studies of Science, 8(3), 327–340.** [DOI](https://doi.org/10.1177/030631277800800305) · [Original scan](https://garfield.library.upenn.edu/small/hsmallsocstudsciv8y1978.pdf). Examines citation contexts in chemistry to show how documents become standard symbols for concepts, methods, or data. Closely related to the circulation of names and labels. Symbols can also efficiently condense and communicate knowledge, so symbolic use is not automatically nominal use.

3. **Latour, B. (1987). _Science in Action: How to Follow Scientists and Engineers Through Society._ Harvard University Press.** [Author bibliography](https://www.bruno-latour.fr/node/130.html) · [First part of the original book](https://classes.matthewjbrown.net/teaching-files/hps/latour-SiA-pt1.pdf). Chapter 1, particularly original pp. 22–23 and 42–43, follows how downstream statements use **modalities** to move claims toward accepted facts or back toward their conditions of production and controversy. Useful for tracing the disappearance of qualifications and the stabilization of claims. Stabilization is not automatically overclaim: whether certainty is warranted requires a separate assessment of evidence.

4. **Cozzens, S. E. (1989). _What Do Citations Count? The Rhetoric-First Model._ Scientometrics, 15, 437–447.** [DOI](https://doi.org/10.1007/BF02017064). Proposes understanding citations first as rhetoric and second as reward or recognition. Equal citation counts can represent different argumentative functions and influence intensities; they cannot simply be treated as quantities of substantive knowledge flow.

5. **Mizruchi, M. S., & Fein, L. C. (1999). _The Social Construction of Organizational Knowledge: A Study of the Uses of Coercive, Mimetic, and Normative Isomorphism._ Administrative Science Quarterly, 44(4), 653–683.** [DOI](https://doi.org/10.2307/2667051). Traces selective appropriation of DiMaggio and Powell's classic paper: mimetic isomorphism receives disproportionate attention, and operationalizations blur distinctions among concepts. A direct social-science case of theory being cited while its content and distinctions are reconstructed through use.

6. **Greenberg, S. A. (2009). _How Citation Distortions Create Unfounded Authority: Analysis of a Citation Network._ BMJ, 339, b2680.** [DOI](https://doi.org/10.1136/bmj.b2680). Examines a specific biomedical claim's citation network, identifying bias against contrary evidence, amplification without new relevant data, and conversion of hypotheses into facts through citation alone. A direct empirical anchor for **overclaim and epistemic distortion during circulation**. Demonstrates a possible mechanism, not its prevalence across all networks.

7. **Teplitskiy, M., Duede, E., Menietti, M., & Lakhani, K. R. (2022). _How Status of Research Papers Affects the Way They Are Read and Cited._ Research Policy, 51(4), 104484.** [DOI](https://doi.org/10.1016/j.respol.2022.104484) · [Institutional full text](https://knowledge.uchicago.edu/record/5150/files/How-status-of-research-papers-affects-the-way-they-are-read-and-cited.pdf). Surveys 17,154 randomly sampled citations supplied by 9,380 corresponding authors across 15 fields. Authors report little or no influence for 54% of citations, but citations to the most highly cited papers are more likely to reflect substantive influence. Directly investigates rhetorical versus substantive citations while challenging an equation of high citation counts with empty prestige. Influence is self-reported, and the study does not directly test overclaim.

**Connection to the revised question:** these studies connect rhetorical citation and fact stabilization to unsupported authority. Focus on claim-level foundations and dependencies across generations: even when citations support substantive research, ask whether independent evidence is added or dependence on the same weak source grows.

## Supporting readings: organizational mechanisms, utilization, and transfer barriers

1. **Boutron, I., Dutton, S., Ravaud, P., & Altman, D. G. (2010). _Reporting and Interpretation of Randomized Controlled Trials With Statistically Nonsignificant Results for Primary Outcomes._ JAMA, 303(20), 2058–2064.** [DOI](https://doi.org/10.1001/jama.2010.651) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/20501928/). Examines **spin** in trial reports with nonsignificant primary outcomes: reporting that emphasizes favorable interpretations or redirects attention. A starting point for operationalizing claim–evidence mismatch. Its clinical-trial categories and prevalence cannot be assumed to apply to HCI, SE, or all disciplines.

2. **Meyer, J. W., & Rowan, B. (1977). _Institutionalized Organizations: Formal Structure as Myth and Ceremony._ American Journal of Sociology, 83(2), 340–363.** [DOI](https://doi.org/10.1086/226550). Formal structures can provide legitimacy while remaining decoupled from ongoing activity. This suggests asking whether citations, theoretical labels, or knowledge-transfer narratives perform legitimating work. Applying the organizational theory to papers and their uses is a proposed extension, not direct evidence for this mechanism.

3. **Bromley, P., & Powell, W. W. (2012). _From Smoke and Mirrors to Walking the Talk: Decoupling in the Contemporary World._ Academy of Management Annals, 6(1), 483–530.** [DOI](https://doi.org/10.1080/19416520.2012.684462) · [Author full text](https://patriciabromley.com/wp-content/uploads/2018/06/BromleyPowellDecoupling.pdf). Distinguishes **policy–practice** from **means–ends decoupling**: adoption may be claimed without implementation, or procedures may be implemented with weak connections to intended goals. This motivates separate questions about whether knowledge is used and whether that use realizes the claimed contribution.

4. **Weiss, C. H. (1979). _The Many Meanings of Research Utilization._ Public Administration Review, 39(5), 426–431.** [DOI](https://doi.org/10.2307/3109916) · [Original scan](https://sites.ualberta.ca/~dcl3/KT/Public%20Administration%20Review_Weiss_The%20many%20meanings%20of%20research_1979.pdf). Distinguishes uses including problem solving, political/tactical purposes, and gradual conceptual enlightenment. Offers a more nuanced account of nominal use and cautions against equating lack of immediate practical change with lack of influence. Accurate research use to support an existing position is not automatically overclaim.

5. **Carlile, P. R. (2004). _Transferring, Translating, and Transforming: An Integrative Framework for Managing Knowledge Across Boundaries._ Organization Science, 15(5), 555–568.** [DOI](https://doi.org/10.1287/orsc.1040.0094). Distinguishes syntactic, semantic, and pragmatic boundaries and transfer, translation, and transformation. Helps ask whether downstream actors receive information, address differences in meaning, or negotiate interests and change work. Substantive use need not require transformation: effective transfer or translation can also qualify.

6. **Szulanski, G. (1996). _Exploring Internal Stickiness: Impediments to the Transfer of Best Practice Within the Firm._ Strategic Management Journal, 17(S2), 27–43.** [DOI](https://doi.org/10.1002/smj.4250171105). Identifies barriers involving absorptive capacity, causal ambiguity, and source–recipient relationships. Provides an alternative explanation: limited substantive transfer may arise from recipient conditions or transfer barriers rather than overclaim in the source paper.

## Retained branch: weak foundations and multi-generation dependencies

**Among insufficiently supported source claims, does overclaim or verbose packaging increase early uptake and help the claim become a recurring premise for later research without independent validation?**

1. **Initiation:** assess evidential support independently, then examine early citation growth in relation to overclaim, verbosity, and their interaction. Compare different combinations of evidence and presentation strength; avoid selecting only highly cited papers that later proved problematic.
2. **Stabilization and branching:** trace when a claim shifts from a proposal to an established premise, whether later research actually depends on it, and whether multiple references share a single source. Record chain depth, dependent branches, and growth in independent evidence. A whole-paper citation graph cannot substitute for a claim-specific chain.
3. **Persistence and repair:** distinguish nominal repetition, unverified practical dependency, independent validation, refutation, and correction. Examine continued reliance after new evidence or corrections and identify branches that acquire reliable support.

Start within one field with a small set of source claims and two or three citation generations, tracing claim, direct evidence, citation purpose, and new evidence. Where feasible, hide citation counts and author identities during evidence assessment; record uncertainty and disagreements. Use source text predating the citations. Adapt content-conditioned rhetorical comparisons, assess verbosity separately, and manually verify technical content, dependency, and independence of evidence. Missing support does not prove a claim false, and citation descendants are not automatically problematic.

Use equal early observation windows and consider field, novelty, author status, open access, and paper age. The number of dependent studies is not automatically a measure of causal harm. Report associations separately from mechanism evidence. Randomized presentation of content-equivalent texts could test perceived credibility, verification behavior, and intended use, but would not establish the formation of long-term knowledge chains.

Connections to existing notes: [004 · Storytelling quantified](../004-storytelling-quantified/note.en.md) examines narratives as measurable constructs; [007 · Nuance rises and falls](../007-nuance-rises-and-falls/note.en.md) examines qualifications and limits; [023 · Journal mediatization](../023-journal-mediatization/note.en.md) examines amplification. This idea asks how an insufficiently supported premise becomes a shared foundation through presentation and citation.
