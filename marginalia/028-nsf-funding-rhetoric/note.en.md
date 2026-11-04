---
id: marginalia-028
title: "The Abstract Is a Small Proposal: Rhetorical Moves in NSF Award Abstracts Across Software Engineering, AI & Society, Science of Science, and Organization Studies"
date: 2026-11-04
published: 2026-11-04
kind: analysis
sources:
  - "NSF Award Search/API snapshot, 2026-11-03; local filtered corpus of 19,630 records (the raw database is not redistributed with this entry)"
  - "NSF Award Search Overview; scope of public abstracts, award data, and complete proposals"
  - "NSF CAREER Program; NSF 22-502 AI Research Institutes Solicitation"
  - "Public pages and abstracts for NSF awards 2404109, 2229885, 2116935, 1928608, 1231154, and 2339830"
  - "Peng, Qiu, Fosse & Uzzi (2024), Promotional language and the adoption of innovative ideas in science, PNAS, doi:10.1073/pnas.2320066121"
  - "Related publications listed as outcomes by award records or acknowledging an award; listing does not establish exclusive support"
initial-prompt: '我主要是希望能学习它们的修辞手法，你能不能想办法把这个内容用合适的办法 update 到我的 github repo 的 marginal 的那个 repo，这样我之后可以再看。'
agent: Codex
model: GPT-6
issue: 81
---

# The Abstract Is a Small Proposal: Rhetorical Moves in NSF Award Abstracts

> The point is not to copy a universal “winning formula.” It is to notice how researchers compress a consequential problem into a reviewable plan: why it matters now, what current knowledge cannot yet explain or do, how the project will proceed, why the team can do it, and who can use the results.

## What this material can and cannot show

The local filtered corpus contained **19,630 NSF award records** in the 2026-11-03 snapshot. Its scope reflects the filters developed earlier in this search: software engineering, computing, AI including AI and society, computational social science, science of science, innovation, and organization studies; generally excluding awards below $200,000 except student-specific funding; and excluding fellowships, conferences, and the subject areas removed in prior rounds. This entry offers close readings; it does not replace the local full dataset, and the public repository does not contain the entire abstract corpus.

Topic labels overlap, so the counts below should not be added together: Computing 18,687; Artificial Intelligence 12,493; Software Engineering 7,738; Innovation Research 1,443; AI & Society / Human-Centered AI 730; Computational Social Science 504; Science of Science / Science Policy 424; Organization Studies 270. Based on award totals displayed in the records, the median is about **$461,435** and the mean about **$722,141**; a few very large computing-infrastructure awards pull the mean upward. The corpus contains 2,950 awards with a CAREER tag (about 15%), with a median total of about $522,748; the median project duration is about four years. These are recorded award totals, not annual budgets, expenditures, or a PI's personal income. Summing total project amounts does not produce an annual NSF spending figure.

**These are public NSF award abstracts, not complete proposals.** NSF states that Award Search supplies award abstracts and that submitted proposals are confidential intellectual property of the submitting organizations. I did not locate the full funded applications for these examples. Each case links to its NSF record so you can read the full public abstract. Abstracts and linked research outputs cannot reconstruct the project description, budget justification, reviewer comments, or reviewers' actual judgments.

**Browse the full original abstracts:** [open the 19,630-award browser](docs/028-nsf-award-browser.en.md). Each record expands to show its English abstract, PI/institution/amount/field metadata, publications listed by NSF, and any Chinese translation already present in the source corpus. Search by title, PI, institution, area, and amount.

## A rhetorical chain to annotate

A recurring, though not universal, structure is:

**stakes / affected parties → a specific gap or tension → the project's claim and object of study → methods that answer the question in stages → team, site, and resources that make the plan credible → outputs, users, channels, and plausible impact.**

| Move | What a reader needs to see | A useful check |
|---|---|---|
| Establish stakes | Who or what is affected, and why the problem matters now | Would the problem remain clear if “transformative” were removed? |
| Name the gap as a tension | Why existing methods or explanations are insufficient, or why evidence conflicts with expectations | Is this a testable gap, or just “little research has been done”? |
| Make the object legible | A mechanism, capability, system, or theoretical object—not a string of grand nouns | Can the project be explained in one sentence? |
| Connect methods | What each method answers, what evidence it produces, and how that evidence feeds the next stage | Do interviews, models, and experiments each do different work? |
| Make feasibility visible | Data, sites, partners, interdisciplinary capacity, and preliminary work | Are these resources necessary to the project, or only listed? |
| Specify impact | Output → user → channel → observable change | Is broader impact tied to a course, tool, policy process, or community partnership? |
| Calibrate promises | Testable targets, boundaries, risks, and alternatives | What evidence would justify “causal,” “trustworthy,” “universal,” or “transformative”? |

## Six close readings, ordered by total award amount

The cases are **illustrative close readings** chosen to cover the requested research areas. They are not a complete rhetorical coding of the 19,630 records, and the wording below should not be read as having caused the funding decision. Amounts and PIs follow the NSF records.

| Amount | Award, PI, and institution | NSF / disciplinary placement | Rhetorical move to inspect |
|---:|---|---|---|
| $20,000,000 | [Global Observatory and Virtual Laboratory for Science and Technology Advance](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2404109) · James A. Evans · University of Chicago | APTO; science of science, technology innovation, and policy | Turn global competition into a research infrastructure: an “observatory + virtual laboratory” |
| $20,000,000 | [Institute for Trustworthy AI in Law and Society (TRAILS)](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2229885) · Hal Daumé · University of Maryland, College Park | CISE / AI Research Institutes; AI and society | Move from transparency and public trust to an integrated research architecture across technical, social, perceptual, and governance work |
| $1,299,701 | [Qualitative Data Repository 2021–2024](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2116935) · Sebastian Karcher · Syracuse University | SBE / Social and Economic Sciences; research infrastructure and methods | Present a repository as public infrastructure for transparency, accumulation, and ethical data sharing |
| $1,195,189 | [Understanding the Algorithmic Workplace](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=1928608) · H. C. Robinson · Northeastern University | SBE / Social and Economic Sciences; computational social science, organization, and work | Turn a multi-method plan into an evidence chain from worker experience to modeling and field tests |
| $1,085,570 | [Formal and Informal Boundary Spanning in Multiteam Systems](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=1231154) · John R. Hollenbeck · Michigan State University | Science of Organizations / Virtual Organizations; innovation and organization studies | Use the tension between formal and informal ties to focus a problem about knowledge and innovation across teams |
| $846,731 | [CAREER: Scientist-in-the-loop-software testing](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2339830) · Joshua S. Sunshine · Carnegie Mellon University | CISE / Software & Systems Foundations; software engineering, CAREER | Connect the consequences of faulty scientific software to testing tools, foundational research, and education |

### 1. Compress macro-level competition into an imaginable research instrument: APTO

The abstract uses “**global observatory and virtual laboratory**” to turn scientific and technological competition from an abstraction into a research instrument. Its sequence is: shifts in global leadership → a need to understand U.S. technological capacity, production, and use → cross-technology and organizational datasets → a large language model described as a “digital double” → simulated policy experiments → dashboards for funders, policymakers, and researchers.

The rhetorical strength is that **a complicated technical program becomes a repeatable infrastructure vision**, with methods and end users placed on one roadmap. The important questions are that “digital double” and “causal estimation” carry substantial inferential weight: how will the model be validated, and how will simulation be distinguished from actual policy effects? The abstract proposes this work; it does not demonstrate that the system can already do it.

One related paper listed by the NSF record is Wu, Esposito, and Evans's [“Shifting power asymmetries in scientific teams reveal China’s rising leadership in global science”](https://doi.org/10.1073/pnas.2414893122), published in *PNAS*. The award page's outcome listing indicates a recorded association, not that this award was the paper's sole funding source.

### 2. Expand a technical performance issue into social trust and governance: TRAILS

The abstract first recognizes AI's promise, then introduces a counter-tension: “**Current AI systems are not created in a way that is transparent**.” It connects opacity to public trust, potential harms, and adoption, then proposes a multi-institution research institute. Four thrusts—Society, Technical Design, Socio-Technical Perceptions, and Governance—organize the plan.

The transferable move is to **identify social conditions beyond the technology, then explain why a multidisciplinary and multi-institution structure is needed**. The abstract does not reduce trust to a single technical metric. In your own proposal, distinguish whether people trust a system, whether the system deserves trust, and which stakeholders are involved; otherwise, “promoting trust” becomes hard to evaluate.

A related paper by TRAILS team members is [“The epistemologies of trust: conflicting worldviews in the ‘Trustworthy AI’ discourse”](https://doi.org/10.1007/s43681-026-01087-2), in *AI and Ethics*. The NSF project record lists the paper; still distinguish a record association from exclusive support. The [NSF AI Research Institutes solicitation](https://www.nsf.gov/funding/opportunities/national-artificial-intelligence-research-institutes/nsf22-502/solicitation) is useful context: the abstract's architecture also responds to the solicitation's expectations for institute-scale work, interdisciplinary integration, and partnerships.

### 3. Describe research infrastructure as scientific capacity: QDR

The QDR abstract calls itself “**an open repository dedicated to the curation, preservation, and publication of data**,” but does not stop at promising a repository. It connects data sharing and reuse to research transparency, ethical and legal protections, cumulativeness, rigor, and efficiency.

This is a useful pattern for infrastructure proposals: **name the service, then explain the mechanism by which it changes research practice**. Instead of promising only a platform, QDR connects accessibility and compliant sharing to several downstream benefits. A proposal can make this chain even more concrete: who will use the service, what can be shared, how will ethics review and participant protection work, and what measures define success?

Related publications listed in the NSF record include [“Actually Accessible Data: An Update and a Call to Action”](https://doi.org/10.31274/jlsc.15449) and [“Teaching with shared data for learning qualitative data analysis”](https://doi.org/10.1080/1743727X.2024.2443935). The first is especially useful for distinguishing “open” from “accessible.”

### 4. Make a multi-method design read like an evidence production line: Algorithmic Workplace

The award names three constituencies: “**workers, business organizations, and government institutions**.” It then connects platform-worker experience, business data, a worker-behavior model, field experiments, and audience-specific outputs for employers, policymakers, and the U.S. workforce.

The rhetorical move is not merely to list interviews, surveys, modeling, and field experiments. It is to show **how evidence from one stage becomes an input to the next**. That makes the methods look like complementary evidence about one problem rather than a list of tools. The risk is that a broad label such as “comprehensive optimization” can outrun what a design can identify, so the abstract should say how predictions will be tested and what the field experiment can establish.

Some papers explicitly acknowledge NSF award 1928608, including Vallas and Schor's [“Labour platforms as mechanisms of class reproduction”](https://doi.org/10.1332/27324176Y2024D000000023), and Schor, Tirrell, and Vallas's [“Consent and Contestation: How Platform Workers Reckon with the Risks of Gig Labor”](https://doi.org/10.1177/09500170231199404). The second paper's own opening is rhetorically instructive: it turns a contradiction between algorithmic control and workers' support for platform work into a question about differentiated experiences of risk.

### 5. Organize organizational research around an observable theoretical tension: Boundary Spanning

The project title itself sets up a formal/informal contrast. The abstract explains why multiteam systems need cross-boundary coordination, then proposes that informal relationships outside formal structures may either reinforce or undermine those structures. It anchors this question in Michigan State's FRIB setting and names interviews, surveys, and network analysis.

The lesson is to align **theoretical tension, observable site, and method**. A site is not just a decorative highlight; it supports feasibility only if it makes the proposed mechanism observable. Guo and colleagues' related paper, [“When Discretionary Boundary Spanning Relationships Cease Becoming Discretionary”](https://doi.org/10.1037/apl0000911), acknowledges NSF award 1231154 and another NSF award, so it should not be described as an exclusive output of one grant.

### 6. How CAREER joins a research agenda to an education agenda: Scientist-in-the-loop testing

The abstract starts with a concrete consequence: scientists write code every day, and a software fault can invalidate a scientific result. It then identifies a training gap—“**scientists do not follow common testing practices**”—and narrows the response to an actionable research goal: help scientific programmers create effective test suites.

This CAREER case connects **problem consequence → technical research → courses and training for graduate students outside computer science**. NSF's CAREER program emphasizes integration of research and education for early-career faculty, so education is part of this project's plan rather than a separate promotional paragraph. See the [CAREER program description](https://www.nsf.gov/funding/opportunities/career-faculty-early-career-development-program).

The NSF record lists [“TestLoop: A Process Model Describing Human-in-the-Loop Software Test Suite Generation”](https://doi.org/10.1145/3765754) and [“TerzoN: Human-in-the-Loop Software Testing with a Composite Oracle”](https://doi.org/10.1145/3729359) as outcomes. For proposal writing, inspect how the abstract makes tool development and education part of one agenda; when reading the papers, check whether the project produced the corresponding models and tools.

## A writing exercise

Fill the outline in one paragraph, then check whether there is evidence for every arrow:

> Because **[documented problem]** affects **[specific people, system, or decision]**, current **[approach or explanation]** cannot yet **[specific limitation]**. This project studies **[one mechanism, capability, or problem]**. We will first use **[method A]** to identify **[evidence]**, then use **[method B]** to develop **[model, theory, or tool]**, and finally use **[method C]** to test **[an explicit result]**. The team has **[data, site, partners, or prior work]** to support this plan. We will provide **[deliverable]** to **[specific audience]** through **[channel]**, and assess progress using **[measure]**.

Then ask:

1. If “important,” “innovative,” “transformative,” and “unprecedented” are removed, does the problem and method still make sense? Replace adjectives with a comparison or a clear gap.
2. Does each method answer a research question? Do the methods provide complementary evidence?
3. Does the impact chain name actual users and settings, rather than only promising “broad impact”?
4. What can the project demonstrate, and what remains a future aspiration? Are future benefits written as established facts?
5. For CAREER, are education activities linked to research findings, with a course, audience, and evaluation plan specified?
6. Is at least one risk, boundary, or alternative route stated so that ambition looks manageable rather than unlimited?

## Conclusions not warranted by award abstracts

- These six cases cover the requested themes; they are not a random sample and do not represent the average rhetorical style of all 19,630 records.
- We see funded public abstracts without declined applications as a comparison group. Therefore, we cannot say a particular rhetorical move “caused” the funding decision.
- Peng, Qiu, Fosse, and Uzzi's [“Promotional language and the adoption of innovative ideas in science”](https://doi.org/10.1073/pnas.2320066121) analyzes funded and unfunded application texts and reports associations between promotional language, funding, innovativeness, and later impact. Its word-substitution experiment measures positive impressions of text, not randomized outcomes in real reviews. It makes rhetoric worth studying; it is not a reason to pile on hype words or overclaim.
- NSF outcome lists and paper acknowledgements help trace associations, but an item “listed as an outcome” is not necessarily funded exclusively by that award.
- Full proposals, detailed budget justifications, and review materials are not in public award abstracts. This note studies **how funded projects publicly describe their plans**, not every writing strategy in a complete proposal.
