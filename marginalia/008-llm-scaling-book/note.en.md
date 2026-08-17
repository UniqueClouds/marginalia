---
id:              marginalia-008-en
title:           "How to Scale Your Model — reading note: LLM training taken from alchemy to a roofline accounting (JAX-ML scaling book)"
date:            2026-08-17
published:       2026-08-17
kind:            note (reading note)
sources:
  - "How to Scale Your Model — https://jax-ml.github.io/scaling-book/ (open online book, first release 2025-02-04)"
  - "Authors: Jacob Austin · Sholto Douglas · Roy Frostig · Anselm Levskaya · Charlie Chen · Sharad Vikram · Federico Lebron · Peter Choy · Vinay Ramasesh · Albert Webson · Reiner Pope (Google DeepMind / MatX)"
initial-prompt: "New marginalia note: a brief summary of this Google book — mainly a note on the book (https://jax-ml.github.io/scaling-book/)"
agent:           ZCode CLI
model:           GLM (Zhipu)
issue:           15
---

# How to Scale Your Model — reading note

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

- Sits interestingly next to [002 · Writing like Dourish](../002-writing-like-dourish/note.en.md) and [005 · Four disciplinary voices](../005-discipline-style-voices/note.en.md): those notes measure *rhetorical* signals, this one measures *compute* signals. Reading them together has an ironic snap: the "scaling cost" that an SE paper compresses into a single future-work bullet gets a whole chapter here.
- Complementary to the AIDev dataset thread in my SE × AI CCF-B survey: effects of AI on software development measured from Stack Overflow / arXiv text still have to park on a roofline ledger before they actually land.
