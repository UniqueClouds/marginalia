# Laying the track ahead of the train: the political economy of release cycles, from CPU benchmarks to SOTA

<div class="lang-switch" markdown>
🌐 Language / 语言：[中文](024-release-cycle-politics.zh.md) · **English**
</div>

<div class='marg-meta'><span>📅 2026-09-06</span><span>🏷️ essay（随想）</span><span>🐙 issue #53</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-024</td></tr><tr><td>title</td><td>Laying the track ahead of the train: the political economy of release cycles, from CPU benchmarks to SOTA</td></tr><tr><td>date</td><td>2026-09-06</td></tr><tr><td>published</td><td>2026-09-06</td></tr><tr><td>kind</td><td>essay（随想）</td></tr><tr><td>issue</td><td>53</td></tr></table></details>

> Smartphones announce CPU gains of a few dozen percent year after year; AI models refresh SOTA weekly; game consoles wait five to seven years for a new "generation"; and VR/AR never took off under the same spec discourse. **The release cycle is not a property of technology — it is an institution**, a temporal rhythm jointly determined by logistics and logistical power, capital flows and return horizons, and the public's expectations of "progress." This essay offers a five-platform comparison matrix and asks three questions: why does the process sustain itself? What does it actually provide materially? And where do its cultural and economic motivations come from?

## 1. A tempo matrix for five platforms

| Platform | Cadence | Coordination device | Material throughput | Revenue structure |
|---|---|---|---|---|
| PC/CPU | 18–24 months (tick-tock) | Moore's Law + ITRS roadmap | wafers/lithography/rare earths | chip margins |
| Smartphone | annual (Apple sets it) | fall launch calendar + carrier contracts + trade-ins | global logistics/e-waste | hardware+services+finance (HaaS) |
| Game console | 5–7-year "generations" | generation narrative (Next Gen) + exclusives | bulk single-config manufacturing | sell hardware at a loss + software cut |
| VR/AR | no stable cadence (failed) | absent | high-friction hardware, low repurchase | unfound |
| AI models | big versions diverge / small versions accelerate | benchmark leaderboards (public, automatic) | GPUs/power/data centers (heaviest) | API/subscription/funding flywheel |

## 2. Cadence as self-fulfilling prophecy

Semiconductors supply the most complete anatomy of this institution. Moore's Law began in 1965 as an empirical observation, was revised by Moore himself in 1975, and then became the industry's timetable: the ITRS roadmap — over nine hundred participating companies at its peak — aimed every firm at the same future node, in Moore's own phrase a matter of "**putting the track ahead of the train** to stay on plan." Historian Ethan Mollick canonicalized it as a self-fulfilling prophecy; Lécuyer showed Moore's Law was always a multipurpose tool — driving process innovation, selling chips, crushing competitors. The best two summaries come from engineers themselves: "Moore's Law is not a law, it is an act of will"; and "we make Moore's Law happen because we want it to be true." **Cadence precedes technology**: it is not the rate of technical progress that sets the release cycle, but the promise of the release cycle that dictates the rate technology must reach.

## 3. Two ledgers: big versions and small ones

After hitting the wall, the law survived by two acts of accounting. **First, changing the period (the time ledger)**: Intel officially retired tick-tock in 2016 for the three-phase Process-Architecture-Optimization scheme — stretching each process generation from two years to three, because dropping a process after two years had become "uneconomic." **Second, changing the metric (the number ledger)**: process naming "stopped matching the actual gate-length metric in 1997" (Intel's own press release), yet the 0.7× sequence marched on — until 2021, when Intel joined the game outright, renaming 10nm "Intel 7" and declaring the "angstrom era." ASML's official roadmap deck pulled back the curtain: "3nm" (N3) has an actual metal half-pitch of 23 nanometers; "1nm" (A10) corresponds to 18nm; TSMC's research vice president Philip Wong said it plainly — process nodes "have become a marketing game." The AI side is structurally parallel: big-version (hero-run) intervals diverged — OpenAI's GPT-4 to GPT-5 spanned about 2.5 years while Anthropic/Google/xAI accelerated to four flagships in twenty-five days in late 2025 — and small versions accelerated universally: point updates, dated snapshots, mini/nano/flash tiers, silent rolling updates, plus a deprecation treadmill with eight forced changes on one platform in 180 days. Intel's "toothpaste" (14+/14++) and AI point updates are the same cadence-maintenance art: **when big versions slow, the high-frequency presence of small versions stands in for progress itself**. Moore's Law versus scaling laws repeats the pattern: both follow the recipe "name a curve a law → turn it into a timetable → turn it into justification for capital expenditure → pivot axes at saturation" — the Kaplan–Chinchilla exponent dispute misallocated billions of dollars of compute, just as node numbers drifted from physics for three decades.

## 4. Two materialities: why phones cannot update like AI

The difference in release cadence finally lands on a materiality question. The product materiality of phones and computers is **embodied**: user state is embedded in the device; replacement involves real money, data migration, and complex reconfiguration — high switching costs keep everything predictable, and cadence is locked by the slowest layer (manufacturing, logistics, retail). The materiality of AI models is **informational** — Dourish's the stuff of bits: flipping weights does not touch user state, and the **stateless** architecture makes model-layer substitution nearly free. Hence decoupled layer tempos: infrastructure (GPUs, power, data centers — decade-scale CapEx) slowest; model weights fastest; the harness sediment layer (stale prompts, stale skills) in between — **the release cadence is set by the fastest layer, while revenue is underwritten by the slowest**. This is temporal arbitrage across material strata, and phones cannot do it: their product is layer-fused, cadence locked to the slowest layer. The industry's counter-move is equally telling: because stateless models retain no one, ChatGPT's Memory (referencing full chat history since 2025), Files, and agent memories are re-atomizing bits — **grafting the phone's retention economics into the world of software**. The 2026 "memory wars" proved the point: switching models has never been easier; switching what the model knows about you has never been harder.

## 5. The failure case: why VR never found a tempo

Negative cases test the proposition. VR had every hardware condition and never produced a release cycle: Meta's Reality Labs accumulated roughly $88 billion in losses and officially pivoted to AI glasses in 2026 (VR headset shipments down ~40% that year, AI glasses up ~200%); Apple's Vision Pro has been read as a "developer-platform bet" — the high price a filter, not a mistake — but the return wave among its most devoted buyers within two weeks of launch announced the bet's outcome. The shared post-mortem is this essay's proposition in reverse: **spec discourse needs compounding material dependency — subscriptions, cloud, APIs, ecosystem lock-in — to sustain itself as a cadence**; VR was a one-time purchase with no recurring dependency, so no amount of roadshow could turn it into a rhythm. A post-mortem headline closes the section: "they made the product better at the thing people had already decided they didn't want."

## 6. Apple's persuasion, and the console counterpoint

Apple is the paradigm case of the release-cycle institution: 95% of new iPhones in the US are bought through monthly plans and over 80% with trade-ins, while the actual replacement cycle is ~34 months — Apple's institutional design aims to compress it toward 12–24; **the gap between release rhythm and consumption rhythm is precisely where power operates**. History's irony deserves recording: in 2001 Apple ran the "Megahertz Myth" campaign against spec-worship, and later A-series launches perfected the "X% faster" discourse — denouncing parameters and embracing parameters are two faces of the same persuasion. Consoles provide the comparison: the 5–7-year generation cycle is determined by the lose-on-hardware, take-a-cut-on-software revenue structure (Nieborg calls standardized hardware cycles unique to cultural industries), and the mid-generation refresh since the PS4 Pro is fusing console logic with the phone's annual logic. Logistical power (in Cowen's sense) and capital flow then explain AI's inversion: the release is the lightest of the five platforms (flipping a set of weights) while the logistics are the heaviest (gigawatt power plants and million-GPU clusters) — **the lightest release leverages the heaviest material commitment**, which is exactly why scaling laws are needed as capital narrative.

## 7. Coda

What release-cycle studies ultimately asks is an old STS question in an AI-era version: who sets technology's tempo, in whose interest, and at what material cost? Moore's own metaphor — laying the track ahead of the train — is the emblem of the whole answer: cadence always runs ahead of technology, and technology is required to catch up to its own timetable; and when technology cannot, what gets revised is never the timetable but the calendar and the ruler. The empirical program (a five-platform event library, an archive of naming discourse, paired analyses of cadence–capital–logistics) is registered separately.

## References

- Mollick, "Establishing Moore's Law," *IEEE Annals* (2006) — [doi:10.1109/mahc.2006.45](https://doi.org/10.1109/mahc.2006.45); Lécuyer, "Driving Semiconductor Innovation," *Enterprise & Society* (2020)
- Mack, "The End of the Semiconductor Industry as We Know It" (2003) — [PDF](https://lithoguru.com/scientist/litho_papers/2003_The_End_of_the_Semiconductor_Industry_as_We_Know_It.pdf); IEEE Spectrum on node-naming fiction (2020) — [PDF](https://www.ece.ucdavis.edu/~bbaas/116/docs/paper.spectrum.better.meas.progress.semi.pdf)
- Intel 2021 press release ("stopped matching the actual gate-length metric in 1997") — [intc.com](https://www.intc.com/news-events/press-releases/detail/1486/intel-accelerates-process-and-packaging-innovations); tick-tock retirement (Ars Technica 2016) — [link](https://arstechnica.com/information-technology/2016/03/intel-retires-tick-tock-development-model-extending-the-life-of-each-process/); ASML roadmap expose (OFweek 2024) — [link](https://ee.ofweek.com/2024-06/ART-8500-2800-30637775.html)
- Corrocher & Paganuzzi, "Planned obsolescence and smartphone replacement," *Telecommunications Policy* (2025) — [link](https://www.sciencedirect.com/science/article/pii/S0308596125001193); Apple Upgrade and 34 months — [SAG](https://smartanalyticsglobal.com/apple-upgrade-hardware-as-a-service-us-smartphone-replacement-cycle/); IMF WP/20/70
- Nieborg, "Prolonging the Magic" (2014) — [doi:10.7557/23.6155](https://doi.org/10.7557/23.6155); Kretschmer & Claussen on backward compatibility — [link](https://pubsonline.informs.org/doi/10.1287/stsc.2022.0177); "Consoles are now smartphones" — [link](https://www.spacebar.news/consoles-are-now-smartphones/)
- VR failure set: [vr.org ($88B)](https://vr.org/articles/meta-reality-labs-q2-2026-earnings-loss-widens-88-billion), [CNBC VR winter](https://www.cnbc.com/2026/01/24/metas-reality-labs-cuts-sparked-fears-of-a-vr-winter.html), [Vision Pro platform bet](https://www.stratrix.com/decision-forks/apple-vision-pro-a-3-500)
- Scaling laws: Kaplan et al. 2020 — [arXiv:2001.08361](https://arxiv.org/abs/2001.08361); Pearce & Song 2024 — [arXiv:2406.12907](https://arxiv.org/pdf/2406.12907); Lilian Weng (2026-06) — [link](https://lilianweng.github.io/posts/2026-06-24-scaling-laws/); the law-naming contest — [link](https://blog.boxcars.ai/p/the-three-laws-driving-the-ai-revolution)
- Slade, *Made to Break* (2006); Cowen, *The Deadly Life of Logistics* (2014); Lipovetsky, *The Empire of Fashion*; Porter, *Trust in Numbers* (1995); Dourish, *The Stuff of Bits* (2017)
- Related entries: [018](018-sota-spectacle.en.md) / [019](019-tokenmaxxing.en.md) / [020](020-ai-as-utility.en.md) / [022](022-gravity-of-models.en.md)


---

> 🌐 [阅读中文版](024-release-cycle-politics.zh.md)

