# 「How to Scale Your Model」摘记：把 LLM 训练从玄学拆成 roofline 公算法（JAX-ML scaling book）

<div class="lang-switch" markdown>
<svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> 语言 / Language：**中文** · [English](008-llm-scaling-book.en.md)
</div>

<div class='marg-meta'><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5.5" width="16" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 10h16" stroke="currentColor" stroke-width="2"/><path d="M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="14.7" r="1.7" class="acc-dot"/></svg> 2026-08-17</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h6.1c.4 0 .78.16 1.06.44l7 7a1.5 1.5 0 0 1 0 2.12l-6.1 6.1a1.5 1.5 0 0 1-2.12 0l-7-7A1.5 1.5 0 0 1 4 11.48V5.5Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.7" cy="8.7" r="1.4" class="acc-dot"/></svg> note（读书笔记）</span><span><svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5.85 8.5l12.3 7M18.15 8.5l-12.3 7" class="acc" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg> issue #15</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-008</td></tr><tr><td>title</td><td>「How to Scale Your Model」摘记：把 LLM 训练从玄学拆成 roofline 公算法（JAX-ML scaling book）</td></tr><tr><td>date</td><td>2026-08-17</td></tr><tr><td>published</td><td>2026-08-17</td></tr><tr><td>kind</td><td>note（读书笔记）</td></tr><tr><td>issue</td><td>15</td></tr></table></details>

> 训练 LLM 像炼金 —— 但读懂你模型的性能，不必。
> —— *How to Scale Your Model*, Introduction

## 随想

近期我在 SE × AI 的图景里反复换边：先把 AI 视作"上游变量"看它如何重构软件开发，再退一步提醒自己——无论算法多漂亮，凡跑不进 roofline 的架构都进不了生产。这本书恰卡在这条缝里出版（2025-02-04）：讲的不是"又一个 Transformer 变体"，而是让前一类研究得以成立的那层被多数论文隐去的底料——FLOPs per byte、ICI 拓扑、sharded matmul、roofline 模型。读完只想说一句：算法不是被"发现"的，而是在硬件预算上被"挤出来"的。

## 这本书

- **出处**：https://jax-ml.github.io/scaling-book/ · 首版 2025-02-04 · 13 章开源在线书
- **作者**：Jacob Austin、Sholto Douglas、Roy Frostig、Anselm Levskaya、Charlie Chen、Sharad Vikram、Federico Lebron、Peter Choy、Vinay Ramasesh、Albert Webson、Reiner Pope
- **单位**：Google DeepMind / MatX
- **致谢**：James Bradbury、Reiner Pope、Noam Shazeer、Blake Hechtman "originally derived many of the ideas"；Sholto Douglas 撰写初稿，Jacob Austin 整理格式与编辑成书

四部分、十三章：

| Part | 章节 | 主题 |
|---|---|---|
| 1 基础 | 1 Intro · 2 Roofline · 3 All About TPUs · 4 Sharded Matmuls | 屋顶线模型与 matmul 的高算/带宽比 |
| 2 Transformers | 5 Transformers · 6 Training · 7 Training LLaMA · 8 Inference · 9 Serving LLaMA | 端到端把 LLaMA 3 在 TPU v5e 上"算价" |
| 3 实战 | 10 Profiling · 11 All About JAX | Profiler 用法 + JAX 的并行化心智模型 |
| 4 收束 | 12 Conclusions · 13 GPUs | 把同样的视角平移到 GPU |

## 论点译白

1. **被三个瓶颈锁住**：计算、通信、内存。高效扩展 = 让"新增芯片带来的通信开销"不超过"它带来的算力收益"，否则进入 communication-bound，扩不动。
2. **Matmul 是独特的算子**：每读一个字节就能产出 N 个浮点运算——这是 TPU 设计与 LLM 数值对齐的共同前提。一个算子是不是 matmul，基本决定了它是 compute-bound 还是 memory-bound。
3. **Co-design 是命运**：硬件设计师要预测 2–3 年后算法需要什么；TPU 之所以是 success story，成功在把"高 FLOPs/byte 的矩阵乘法"锤成物理对齐点。
4. **研究 ≈ 系统工程**：如今连"小"模型都贴着硬件上限跑；做新架构的人若不先把 roofline 算清，"算法正确"不足让方法活下去。
5. **可复算的练习题**：第 7、9 章直把 LLaMA 3 拆成参数、FLOPs、显存、ICI 时间、芯片数与成本——示范一种"任何架构提案都该附带的小账本"。

## 记下的几句

- "Training LLMs often feels like alchemy, but understanding and optimizing the performance of your models doesn't have to."
- "A 20% win on benchmarks is irrelevant if it comes at a 20% cost to roofline efficiency."
- "When communication takes longer than computation we become 'communication bound' and cannot scale strongly."
- "The story of the TPU is a resounding success in this game."
- 结语收得很克制：这一域 "can be done even without having many hardware accelerators on hand"，"There remains a lot of room for comprehensive writing in this area."——等于留一扇门，等后来人补——并说把致谢里的 Bradbury / Shazeer / Hechtman / R. Pope 读完。

## 适合谁读 / 局限

- **适合**：想让自己的架构提案"能跑"的研究者、做 serving 预算估算的 MLE、以及在论文里看到 Roofline / NVLink / ICI 这类词会发怵的人。
- **局限**：以 TPU 为主语，GPU 仅在收束章（第 13 章）带过；叙述偏教科书式的"白盒拆解"，没有给"如何在自己的小集群上复算"做完整工作手册；对 Megatron / DeepSpeed / vLLM 这类已在主流集群栈里成事实标准的方法只字未提——是 JAX 团队的视角叙事，而非产业全景。

## 与其他 marginalia 的勾连

- 与 [002 · 写作如 Dourish](002-writing-like-dourish.zh.md) 和 [005 · 四学科声音](005-discipline-style-voices.zh.md) 同席别有趣味——那些笔记量的是"修辞信号"，这本量的是"算力信号"。但合读会撞出一句反讽：SE 论文里被压成一句 fut. work 的"扩展成本"，在这本书里占满整整一章。
- 与我 SE × AI CCF-B 调研里的 AIDev 数据集那条线互补：用 Stack Overflow / arXiv 文本测出的"AI 对软件开发的影响"，最后都要 park 在一份 roofline 小账本上才算真落地。


---

> <svg class="marg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.8 2.6 4.2 5.6 4.2 9s-1.4 6.4-4.2 9c-2.8-2.6-4.2-5.6-4.2-9S9.2 5.6 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/></svg> [Read this note in English](008-llm-scaling-book.en.md)

