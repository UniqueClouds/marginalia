# Re-run the review and half the program changes — Best Paper randomness and the floor of 'not-ugly'

<div class="lang-switch" markdown>
🌐 Language / 语言：[中文](021-best-paper-lottery.zh.md) · **English**
</div>

<div class='marg-meta'><span>📅 2026-09-06</span><span>🏷️ essay（随想）</span><span>🐙 issue #50</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-021</td></tr><tr><td>title</td><td>Re-run the review and half the program changes — Best Paper randomness and the floor of 'not-ugly</td></tr><tr><td>date</td><td>2026-09-06</td></tr><tr><td>published</td><td>2026-09-06</td></tr><tr><td>kind</td><td>essay（随想）</td></tr><tr><td>issue</td><td>50</td></tr></table></details>

> Twice, NeurIPS handed 10% of its submissions to two independent committees: in 2014 and 2021. Decisions disagreed on 23–26% of papers, and **accept precision — the probability that an accepted paper survives a second review — was about 50%**. Re-run the review and roughly half the accepted list changes. A seven-year follow-up added the colder cut: for accepted papers, review scores correlate **zero** with eventual citations. Reviewing is good at identifying bad papers and poor at identifying good ones. This essay connects those facts to a thesis: we may only ever certify that a paper is "**not ugly**" — meeting a defensible floor of criteria — while "good" is a product of taste, politics, and retroactive canonization; and it migrates the student project NOTUGLY-S's framework ("learn not-ugly, not beauty") onto paper evaluation.

## 1. Two experiments: the official numbers of randomness

In 2014, NeurIPS program chairs Cortes and Lawrence sent 166 submissions (~10%) through two independent reviews: 43 disagreed (25.9%), and the accept precision — the share of committee one's accepts that committee two rejected — was about 49.5%. The community compressed this into a harsher sentence: **rerun the process and half the accepted papers would not exist.** In 2021 the chairs replicated the experiment at 8,820-paper scale: 23.0% inconsistency, 50.6% accept precision — seven years and five times the scale, and the noise had not converged. The same experiment buried a less-discussed clue: **the more selective the tier, the closer to random** — the two committees agreed on only three orals/spotlights. Award-level randomness exceeds acceptance-level randomness, and almost no one has followed that thread. The revisit (arXiv:2109.09774) supplied the mechanism from calibration data: about half the variance in reviewer scores is subjective, and **scores of accepted papers correlate zero with seven-year citations** (for rejected papers, scores do predict future impact). The authors' sentence is this essay's thesis: that reviewing was "good for identifying poor papers, but poor for identifying good papers."

## 2. 'Not-ugly,' formalized: the RFC model

The conclusion has an elegant statistical form. A Bayesian reanalysis of the 2014 experiment introduced a hidden parameter: the probability that a submission meets **basic quality criteria** (novelty, no fatal methodological flaw, reproducibility, integrity) — estimated at ~56%. The model's meaning: below the floor, both committees reject stably; above it, they are nearly flipping coins — the authors call it reject-or-flip-a-coin. "Not-ugly" is therefore not a rhetorical figure but a defensible floor: correct, clear, honestly reported — below it, consistent rejection; above it, committees cannot distinguish "good" from "ordinary," only "like me" from "not like me."

## 3. The official embrace of taste

If "good" were an objective quantity, awarding bodies would hide the fact; they do the opposite. The ACL 2025 awards policy defines Best as work that is "particularly **fascinating, controversial, surprising**, impressive, and/or potentially field-changing" — **controversy is a stated criterion**. The same year, Eduard Hovy's keynote labeled the field's majority output "LLM popcorn," the hall's consensus was that acceptance is a bet on your meta-reviewer, and someone revived Hovy's proposal: admit everything, vote on site. The crack between awarding and reviewing is acknowledged by the institutions themselves.

## 4. Controversy as the norm: EN and CN communities

Best Paper announcement day is a festival of dispute. When BERT won NAACL 2019's best paper, the community grumbled that "it just scaled things up"; ACL 2020's award to a philosophical position paper raised the "should we award stances" fight. The Chinese-language record is louder: IJCAI 2019 results put "the worst reviewing in the universe" on Zhihu's hot list; in 2019 CVPR's community ran its own **worst-paper** awards — the mirror image of the official prize, a symmetry worth studying in itself; NeurIPS 2022 accepted a paper averaging 4.5, and the first author's long public rebuttal became an event; IJCAI 2025 was dubbed an "academic lottery"; during AAAI season a screenshot claimed "3,000 RMB buys a strong accept." Methodologically, the Texas A&M–Cornell team has shown how to study the bilingual communities: 1,261 score-sharing posts from Zhihu and Reddit, showing online scores systematically inflated by three selective voices (survivors, complainers, borderliners). **The discourse structure of controversy can be studied on exactly this template.**

## 5. Test of Time: goodness is retroactive

If "good" cannot be identified now, is it at least identifiable in a decade? The Test-of-Time archives give a subtle answer: ToT is not evidence that someone knew better at the time; it is an **institution of retroactive canonization**. SIGIR's fortieth-anniversary special issue revisited 21 ToT papers, including the 2-Poisson model — initially disappointing because it "lost" to simpler methods — which later became the theoretical ancestor of BM25. SIGCOMM's 2008 committee publicly narrated its inability to rank two candidates, ending with a three-way shared award. The award materials speak only in criteria available retrospectively ("opened a field," "lasting influence"). No one has systematically reconciled ToT lists against **the original public review records** — are classic papers' initial scores notably mediocre? The reconciliation is feasible, and worth doing.

## 6. NOTUGLY-P: from code to papers

Note 003 on this site recorded a proposal: rather than teaching a model what beauty is, teach it what not-ugly is — put the criteria on the defensible floor. Migrated to paper evaluation, this essay's landing point is that **evaluation has two modalities**. "Not-ugly" is the defensible floor: correct, reproducible, clear, honest about limitations — in principle codable, the 56% band of the RFC model. "Good" is the incomensurable ceiling: importance, elegance, resonance — dependent on taste (Kant's judgment without concepts), field position (Bourdieu's distinction), and the disciplinary culture of review panels (Lamont's *How Professors Think*), settled ex post at decade scale by citations, teaching, and ToT awards. The core anxiety of contemporary review is the conflation of the two modalities: **we make "not-ugly" decisions in the language of "good," then award "good" through "not-ugly" procedures.** Naming the misalignment is not cynicism; it moves review reform from the impossible goal of "identifying good more accurately" to the possible one of "guarding the floor more fairly."

## References

- The NeurIPS 2021 Consistency Experiment — [official blog](https://blog.neurips.cc/2021/12/08/the-neurips-2021-consistency-experiment/); paper — [arXiv:2306.03262](https://arxiv.org/pdf/2306.03262)
- Revisit of the 2014 experiment ("good for identifying poor papers, poor for identifying good papers") — [arXiv:2109.09774](https://arxiv.org/pdf/2109.09774)
- Bayesian reanalysis and the RFC model — [arXiv:1507.06411](https://ar5iv.labs.arxiv.org/html/1507.06411)
- ACL Conference Awards Policy — [aclweb.org](https://www.aclweb.org/adminwiki/index.php/ACL_Conference_Awards_Policy); ACL 2017 PC account — [link](https://acl2017.wordpress.com/2017/08/03/outstanding-and-best-papers-and-the-decision-process/)
- Score-sharing bias (Survivors/Complainers/Borderliners) — [report](https://www.yanfajia.com/news/6470.html)
- SIGCOMM 2008 ToT committee account — [doi:10.1145/1517480.1517488](https://doi.org/10.1145/1517480.1517488); Jeff Huang's best-paper dataset — [jeffhuang.com](https://jeffhuang.com/best_paper_awards/)
- Field materials: BERT award grumbling (HN) — [link](https://news.ycombinator.com/item?id=43398816); IJCAI 2019 on Zhihu ([QbitAI](https://www.qbitai.com/2019/05/2282.html)); CVPR 2019 community worst-paper awards ([Tencent Cloud](https://cloud.tencent.com/developer/article/1460113)); IJCAI 2025 "academic lottery" ([TrueSight](https://tsight.io/articles/16396475))
- Internal source: NOTUGLY-S proposal ([003 · NOTUGLY-S](003-notugly-s.en.md))
- Kant, *Critique of Judgment*; Bourdieu, *Distinction* (1984); Lamont, *How Professors Think* (2009)
- Related entry: [023 · Journal mediatization](023-journal-mediatization.en.md) (the demand side of taste redirection)


---

> 🌐 [阅读中文版](021-best-paper-lottery.zh.md)

