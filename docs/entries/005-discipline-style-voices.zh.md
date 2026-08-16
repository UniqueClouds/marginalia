# 四种学科的声音：Big Data & Society / HCI / Sociology / Software Engineering 经典论文的语言风格测量（314 篇 / 330 万词）

<details><summary style='cursor:pointer;color:#888;'>Provenance（来源与元数据）</summary><table style='border:1px solid #eee;border-radius:8px;'><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>id</td><td style='padding:3px 10px;'>marginalia-005</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>title</td><td style='padding:3px 10px;'>四种学科的声音：Big Data & Society / HCI / Sociology / Software Engineering 经典论文的语言风格测量（314 篇 / 330 万词）</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>date</td><td style='padding:3px 10px;'>2026-08-15</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>published</td><td style='padding:3px 10px;'>2026-08-15</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>kind</td><td style='padding:3px 10px;'>analysis（分析笔记）</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>issue</td><td style='padding:3px 10px;'>11</td></tr></table></details>


# 四种学科的声音

> 量完一个作者（[002：Dourish](002-writing-like-dourish.zh.md)），接下来量学科：同一家 Zotero、同一条管线、四个领域的经典论文——文体差异能否被数出来？答案是：能，而且每个学科都有一台自己的"概念机器"。

## 随想

写作建议通常以人为单位（"写得像某某"），但学术写作其实是被**学科仪式**塑造的：你投哪个会、哪个刊，就继承了哪套句法与动块。我想验证这件事的可测量性——不是印象式的"SE 论文很干、社会学论文很绕"，而是给出密度、排位、和可核验的例句。这也是 002 的续篇：Dourish 的签名句式密度是 9.2/万词，那他所在（或相邻）学科的普通论文呢？

## 语料

Zotero「各学科 Classic Papers」四个子库，共 347 条目、327 篇带 PDF；清洗（去水印、去中文翻译段、剔 OCR 过差件、剔专著）后入语料 **314 篇 / 330 万词**：

| 学科 | 篇数 | 词数 | 主场 | 年份 |
|---|---|---|---|---|
| Big Data & Society | 27 | 21.2 万 | *Big Data & Society*、*New Media & Society* | 2004–2021 |
| Human-Computer Interaction | 94 | 81.8 万 | CHI、CSCW（ACM） | 2003–2025 |
| Sociology | 79 | 110.6 万 | AJS、ASR、BJS | 1975–2026 |
| Software Engineering | 114 | 116.7 万 | ICSE、FSE、TSE、MSR | 1987–2023 |

## 方法

与 002 同一条管线：PyMuPDF 版面块段落提取 → 去参考文献/水印/CJK 段 → 词频与 2–5 元 n-gram（文档频率）→ **对数比值 keyness（本学科 vs 其余三学科联合）** → 60+ 修辞动块正则（RQ 编号、threats to validity、we+动词搭配、epistemology/power 词场……）→ 标题风格统计 → 人工精读。报告里 **39 条引文全部经 `verify_quotes.py` 机器核验**（连字丢失、换行拆词、脚注数字均容错）。

## 四种声音

**Big Data & Society：写长句的公共知识分子。** 平均句长 26.8 词、分号最密（46/万词）、全库零缩写词；否定—重述句式（not X but Y / rather than）四学科第一——先复述主流理解再翻转之；被动语态最高（施动者被悬置，恰是批判对象的存在方式）；以 "This article" 自称、宣言句开场（"Data are a form of power."）、以对学科的规训呼吁收尾；标题爱 "The X of Y" 概念杠杆。

**HCI：兴奋的工坊主持人。** "We present…" 开门见山；we 的动词库最丰富（found/conducted/present/describe/argue）；hedges 三项全部第一（may/might/suggest）——小样本永远诚实；参与者登记细到报酬金额与利手；引语与 p 值并陈；发现必须折算成 design implications；标题四学科最敢玩（第一人称、俗语戏仿、参与者原话直接上标题）。

**Sociology：与韦伯和 GSS 同时对话的理论统计学家。** 论文最长（1.4 万词/篇）；破折号、缩写词、scare quotes 三项第一——散文肌理最松弛；被动最少（研究者永远在主动操作数据）；证据句式是 "consistent with / net of / Model 1 递进"；epigraph 对置开场（Weber 段落 vs 竞选广告）；AJS 摘要强制第三人称 "The authors"，正文却满篇 "we"——人称分裂是它独有的刊物奇观。

**Software Engineering：写清单的工程师。** 句长中位数仅 16 词、破折号近禁用；we/our 双冠军但 "I" 最少；动词全是工具动词（use/found/present/describe）；名词场全是可数实体（bugs/commits/repositories）；固定仪式最重：To understand X 开头 → 贡献清单 → RQ 编号 → Threats to Validity 按 construct/internal/external 三段自首 → future work 收尾（70% 篇必有）。

## 最有趣的三个发现

1. **一个代词分辨文体出身**：期刊论文自称 "this article"（BDS 21/27 篇、SOC 53/79 篇），会议论文自称 "this paper"（HCI 82/94 篇、SE 103/114 篇）。投稿前看一眼自称就知道你在哪个文体里。
2. **Dourish 仍是异数**：最接近他的 BDS 学科均值（not-simply 2.9/万词）也只有他个人密度（9.2）的三分之一。"写得像学科"和"写得像 Dourish"是两个不同的校准目标。
3. **风格是光谱不是国界**：批判 HCI（Bardzell/Irani/Keyes/Dourish 线）在 HCI 库内构成 BDS 风格飞地（critique 密度 6.5 vs BDS 7.0）；Zeller 与 Hindle 是 SE 库内的修辞破格者；计算社会学正在向 SE 的实证仪式靠拢。

## 速查表

| | 句法签名 | 人称 | 证据 | 收尾 |
|---|---|---|---|---|
| BDS | not X but Y / rather than / increasingly | This article + I | author-date 拉扯 | 规训性呼吁 |
| HCI | We present / may-suggest / 引语并陈 | we（工坊） | N+报酬+p 值+引语 | design implications |
| SOC | consistent with / net of / in other words | we（摘要 the authors） | 模型递进+假设对话 | limitations |
| SE | To understand X / a set of / 16 词短句 | we+our（团队） | 数据规模+表格 | Threats→Future Work |

## 产物与局限

- **五份完整报告**（中文，原样发布）：[BDS](reports/01-big-data-and-society.zh.md) · [HCI](reports/02-hci.zh.md) · [Sociology](reports/03-sociology.zh.md) · [SE](reports/04-software-engineering.zh.md) · [跨学科对比](reports/05-cross-discipline.zh.md)
- 可复用管线留在本地 `ZCodeProject/discipline_style_analysis/`（解析→提取→指标→keyness→清洗→引文核验六段）；`paras.json` 键 = 学科_ZoteroKey。
- 局限：子库为手工圈定的"我的经典清单"而非随机样本；SE 缺 19 篇仅有 IEEE 网页快照的论文；SOC 含 1970s–80s 经典，部分差异含年代因素；段落级统计受单/双栏版式影响（句子级不受影响）。

**下一步可选**：把四份画像蒸馏成四个润色 skill（对标 002 的 dourish-style），或用 keyness 词表做一个"学科伪装检测器"——给一段文字，判断它最像哪个学科写的。


<div style='font-size:12.5px;color:#555;'>📎 附属材料：[01-big-data-and-society.zh.md](../005-discipline-style-voices/reports/01-big-data-and-society.zh.md) · [02-hci.zh.md](../005-discipline-style-voices/reports/02-hci.zh.md) · [03-sociology.zh.md](../005-discipline-style-voices/reports/03-sociology.zh.md) · [04-software-engineering.zh.md](../005-discipline-style-voices/reports/04-software-engineering.zh.md) · [05-cross-discipline.zh.md](../005-discipline-style-voices/reports/05-cross-discipline.zh.md)</div>


---

> 🌐 [Read this note in English](005-discipline-style-voices.en.md)

