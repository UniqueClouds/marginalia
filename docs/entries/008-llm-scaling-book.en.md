# How to Scale Your Model — reading note: LLM training taken from alchemy to a roofline accounting (JAX-ML scaling book)

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> Language / 语言：[中文](008-llm-scaling-book.zh.md) · **English**
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-17</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> note (reading note)</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #15</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-008-en</td></tr><tr><td>title</td><td>How to Scale Your Model — reading note: LLM training taken from alchemy to a roofline accounting (JAX-ML scaling book)</td></tr><tr><td>date</td><td>2026-08-17</td></tr><tr><td>published</td><td>2026-08-17</td></tr><tr><td>kind</td><td>note (reading note)</td></tr><tr><td>issue</td><td>15</td></tr></table></details>

> Training LLMs often feels like alchemy, but understanding and optimizing the performance of your models doesn't have to.
> —— *How to Scale Your Model*, Introduction

## Musing

I keep switching sides on the SE × AI picture: I treat AI as an "upstream variable" reshaping software development, then step back to remind myself that however pretty an algorithm is, anything that fails the roofline never reaches production. This book lands squarely in that seam (2025-02-04). It is not about "another Transformer variant"; it is about the layer that lets the former kind of research *exist* — FLOPs per byte, ICI topology, sharded matmul, the roofline model — and which most papers hide. The one sentence I take away: algorithms aren't *discovered*, they're *squeezed out* against a hardware budget.

## The book

- **Source**: https://jax-ml.github.io/scaling-book/ · first release 2025-02-04 · 13-chapter open online book
- **Authors**: Jacob Austin, Sholto Douglas, Roy Frostig, Anselm Levskaya, Charlie Chen, Sharad Vikram, Federico Lebron, Peter Choy, Vinay Ramasesh, Albert Webson, Reiner Pope
- **Affiliation**: Google DeepMind / MatX
- **Acknowledgements**: James Bradbury, Reiner Pope, Noam Shazeer, Blake Hechtman "originally derived many of the ideas"; Sholto Douglas wrote the first draft, Jacob Austin polished it into a single artifact

Four parts, thirteen chapters:

| Part | Chapters | Theme |
|---|---|---|
| 1 Preliminaries | 1 Intro · 2 Roofline · 3 All About TPUs · 4 Sharded Matmuls | Roofline model and matmul's high FLOP/byte ratio |
| 2 Transformers | 5 Transformers · 6 Training · 7 Training LLaMA · 8 Inference · 9 Serving LLaMA | End-to-end "cost accounting" of LLaMA 3 on TPU v5e |
| 3 Practical | 10 Profiling · 11 All About JAX | Profiler usage + JAX's mental model for parallelism |
| 4 Conclusions | 12 Conclusions · 13 GPUs | Porting the same lens to GPUs |

## Claims, in my own words

1. **Three bottlenecks**: compute, communication, memory. Efficient scaling = making sure the communication cost new chips add does not exceed the throughput they add; otherwise you go communication-bound and stop scaling strongly.
2. **Matmul is a unique operator**: each byte read yields N floating-point operations — the shared premise behind both TPU design and LLM numerical alignment. Whether an op is matmul-shaped basically determines whether it is compute- or memory-bound.
3. **Co-design is fate**: hardware designers must predict what algorithms will need 2–3 years out; the TPU is flagged as a "resounding success" precisely because high-FLOP/byte matmul was hammered into a physical alignment point.
4. **Research ≈ systems engineering**: even "small" models now run at the hardware frontier; an architecture researcher who doesn't first close the roofline fails to ship — the bench win alone doesn't keep the method alive.
5. **A re-runnable exercise**: chapters 7 and 9 decompose LLaMA 3 into parameters, FLOPs, memory, ICI time, chip count and cost — modelling a "small ledger every architecture proposal should carry."

## Quotes I'll remember

- "Training LLMs often feels like alchemy, but understanding and optimizing the performance of your models doesn't have to."
- "A 20% win on benchmarks is irrelevant if it comes at a 20% cost to roofline efficiency."
- "When communication takes longer than computation we become 'communication bound' and cannot scale strongly."
- "The story of the TPU is a resounding success in this game."
- The conclusion is unusually restrained: it can be done "even without having many hardware accelerators on hand," and "There remains a lot of room for comprehensive writing in this area." — leaving a door open, and pointing back at the Acknowledgements (Bradbury / Shazeer / Hechtman / R. Pope).

## Who should read it / limits

- **For**: researchers who want their architecture proposals to actually run; MLEs doing serving-budget maths; anyone who flinches at words like Roofline / NVLink / ICI in papers.
- **Limits**: itches TPUs first, with GPUs only covered in the final chapter (13); reads as a textbook's "white-box teardown" rather than a runnable workbook for your own small cluster; silent on Megatron / DeepSpeed / vLLM, the de-facto cluster stacks — this is the JAX team's narrative lens, not an industry landscape.

## Ties to other marginalia

- Sits interestingly next to [002 · Writing like Dourish](002-writing-like-dourish.en.md) and [005 · Four disciplinary voices](005-discipline-style-voices.en.md): those notes measure *rhetorical* signals, this one measures *compute* signals. Reading them together has an ironic snap: the "scaling cost" that an SE paper compresses into a single future-work bullet gets a whole chapter here.
- Complementary to the AIDev dataset thread in my SE × AI CCF-B survey: effects of AI on software development measured from Stack Overflow / arXiv text still have to park on a roofline ledger before they actually land.


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [阅读中文版](008-llm-scaling-book.zh.md)

