# 四学科经典论文语言风格：跨学科对比总报告
**——Big Data & Society / HCI / Sociology / Software Engineering，314 篇、330 万词语料库分析（2026-08-15）**

> 分报告：[1_BigDataSociety](01-big-data-and-society.zh.md) · [2_HCI](02-hci.zh.md) · [3_Sociology](03-sociology.zh.md) · [4_SoftwareEngineering](04-software-engineering.zh.md)

---

## 0. 语料总览

| | Big Data & Society | HCI | Sociology | Software Engineering |
|---|---|---|---|---|
| 论文数 / 词数 | 27 篇 / 21.2 万 | 94 篇 / 81.8 万 | 79 篇 / 110.6 万 | 114 篇 / 116.7 万 |
| 主要来源 | BDS、NM&S（Sage） | CHI、CSCW（ACM） | AJS、ASR、BJS | ICSE、FSE、TSE、MSR |
| 年份跨度 | 2004–2021 | 2003–2025 | 1975–2026 | 1987–2023 |
| 篇均词数 | 7,847（最短） | 8,701 | **13,995（最长）** | 10,235 |

四库均取自同一 Zotero「各学科 Classic Papers」总库；同一提取管线（版面块段落 → 清洗 → 指标/keyness/n-gram → 人工精读），指标口径一致，所有引文经脚本核验。

## 1. 节奏层：四种呼吸方式

| 指标（每万词或%） | BDS | HCI | SOC | SE |
|---|---|---|---|---|
| 平均句长（词） | **26.8** | 23.7 | 23.6 | **18.8** |
| 句长 P50 / P90 | 20 / **44** | 20 / 39 | 18 / 41 | **16** / 34 |
| 长句占比（>30 词） | **33.1%** | 23.0% | 26.4% | **15.3%** |
| 短句占比（<10 词） | 17.4% | 16.0% | 20.9% | **28.7%** |
| 分号 | **46.3** | 22.6 | 44.2 | 23.3 |
| 破折号 | 16.8 | 13.5 | **34.6** | **7.1** |
| 弯引号（scare quotes） | 26.1 | 50.9 | **55.9** | **30.3** |
| 缩写词（don't 等） | **0.0** | 2.7 | **7.4** | 1.2 |
| 问句 | 6.9 | 7.3 | 6.1 | 8.5 |

一眼区分法：
- **BDS 用分号思考**——长句靠分号缝合多个论点，绝不口语化（零缩写）；
- **SOC 用破折号呼吸**——插入语随时打断句子，且允许缩写词（四学科唯一普遍使用），散文肌理最松弛；
- **SE 用句号交付**——P50 只有 16 词，破折号近乎禁用；
- **HCI 居中偏工程**，但问句、引号比 SE 多（社群允许更多表演性）。

## 2. 人称层：谁在说话

| 指标 | BDS | HCI | SOC | SE |
|---|---|---|---|---|
| we /万词 | **37.8（最低）** | 91.5 | 52.2 | **103.0（最高）** |
| our /万词 | 13.4 | 34.4 | 18.1 | **40.5** |
| I /万词 | 11.6 | 16.8 | 15.8 | **8.8（最低）** |
| 被动式（be+V-ed） | **83.5** | 72.1 | **64.7（最低）** | 82.2 |
| "this article" / "this paper"（篇数） | 21 vs **8** | 5 vs **82** | 53 vs 21 | 16 vs **103** |

**四种主语人格**：
- BDS：**文章在说话**（"This article argues..."），批判学者以单数 "I" 亲自现身；被动句悬置施动者——机制无名运行正是被批判的对象；
- HCI：**工坊在说话**（"We present... we conducted..."），"we" 的动词库最丰富（found/conducted/present/describe/argue）；
- SOC：**研究者在操作**——"we use/observe/argue"，被动最少（数据永远被主动处理）；但 AJS 摘要强制第三人称 "The authors"（正文与摘要人称分裂是社会学独有奇观）；
- SE：**团队在交付**——we/our 双冠军，但 "I" 最少；动词全是工具动词（use/found/present/describe/conducted）。

## 3. 句式签名层：每个学科一台概念机器

| 模式（次/万词） | BDS | HCI | SOC | SE | 解读 |
|---|---|---|---|---|---|
| not simply/just/only...but | **2.9** | 1.5 | 1.6 | 0.8 | 概念翻转机：BDS 的批判引擎，SE 几乎不用 |
| rather than | **5.1** | 3.5 | 3.3 | 2.0 | 同上，同一光谱 |
| hedge: may / might / suggest | 15.6/6.9/7.4 | **16.6/7.6/8.8** | 13.7/5.5/6.5 | 14.6/4.5/5.7 | HCI 三项全部最高：小样本永远留余地 |
| in other words | 0.2 | 0.1 | **0.4** | 0.0 | SOC 的解释循环（理论→白话复述） |
| a set of | 0.9 | 1.4 | 0.9 | **2.6** | SE 的集合思维 |
| increasingly | **3.6** | 1.2 | 1.0 | 0.5 | BDS 的现代性进行时 |
| there is/are 存在句 | 8.4 | 10.0 | 10.3 | 10.3 | 各科相当（BDS 略低） |

**同一个意思，四种句法**（以"X 依赖 Y"为例）：
- BDS："X is not simply a technical artifact but an assemblage of..."（否定重述）
- HCI："Our findings suggest that X may depend on..."（hedge+发现句）
- SOC："The effect of X persists net of Y"（净效应句）
- SE："We use X to address Y. Table 2 shows the results."（工具+证据句）

## 4. 引用与证据层：知识靠什么站立

| 指标 | BDS | HCI | SOC | SE |
|---|---|---|---|---|
| 数字引用 [n] /万词 | 0.8 | **90.1** | 3.2 | **88.1** |
| author-date /万词 | **36.0** | 0.5 | 16.0 | 2.3 |
| et al. /万词 | **23.1** | 6.1 | 6.4 | 12.7 |
| p< 检验（篇数） | 3/27 | **39/94** | 12/79 | 35/114 |
| "consistent with"（篇数） | 4/27 | 30/94 | **45/79** | 41/114 |
| "net of"（篇数） | 0 | 0 | **13/79** | 0 |
| RQ 编号（篇数） | 1 | 14 | 0 | **45** |
| Threats to validity（篇数） | 0 | 2 | 2 | **48** |
| future work（篇数） | 10/27 | 46/94 | 28/79 | **80/114** |

**证据文化的三层分裂**：
- **人文名（BDS/SOC）vs 编号（HCI/SE）**：批判学科把对手名字挂在句子里（author-date + 高 et al.），工程学科把文献压进方括号；
- **SOC 的"与假设对话"**（consistent with/net of/Model 1 递进）vs **HCI 的"与人对话"**（引语+参与者编号）vs **SE 的"与工具对话"**（accuracy/F-measure/数据集规模）；
- **自首制度**是 SE 独有：Threats to Validity 章节在 48/114 篇里按 construct/internal/external 三段清算自己——批判学科把同样内容写成 "limitations"（BDS/SOC 的 limitations 动块），语气是反思而非审计。

## 5. 体裁仪式层：论文的固定动作

| 动作 | BDS | HCI | SOC | SE |
|---|---|---|---|---|
| 开篇公式 | 宣言断言（"Data are a form of power."）/时事钩子 | "We present a study of..." | epigraph 对置/三连问 | "To understand X, we conducted..."/规模开场 |
| 摘要人称 | This article + I | We present... | **The authors（AJS 强制）** | We present/an approach that... |
| 贡献声明 | 无显式清单（贡献即论点） | contributions 小节+design implications | 理论贡献段（we argue） | **bulleted contributions + "first study" 声明** |
| 方法登记 | 民族志 tactics | 参与者/报酬/伦理逐项 | 数据集+模型表 | 工序+数据集规模 |
| 收尾 | 对学科的规训呼吁 | design implications+future work | limitations+未来研究方向 | **Threats→Related Work→Future Work** |

## 6. 标题层：四种命名法

| 特征 | BDS (n=30) | HCI (n=96) | SOC (n=85) | SE (n=136) |
|---|---|---|---|---|
| 含冒号 | **63%** | 55% | 60% | **30%** |
| >10 词 | **60%** | 52% | 51% | **33%** |
| 完整问句 | 0% | 4% | 6% | **8%** |
| 带引号 | 17% | **19%** | 9% | 10% |
| 含数字 | 10% | 0% | **18%** | 2% |
| The/A/An 开头 | 20% | 12% | **22%** | 20% |

- **BDS**：概念杠杆 "The X of Y"（*The politics of 'platforms'*）+ 最长冒号副标题；
- **HCI**：引号+俗语戏仿+第一人称（*"everyone wants to do the model work, not the data work"*、*Why Johnny Can't Prompt*、*Goodbye text, hello emoji*）；
- **SOC**：隐喻主标题+年代范围副标题（*...Lynching in the Deep South, 1882–1930*）——时间范围即设计；
- **SE**：最短名词短语+工程痛点问句（*Who should fix this bug?*），近年向 HCI 戏谑风合流（*Don't touch my code!*）。

## 7. 四种声音：一页画像

| | 一句话画像 | 句法签名 | 人称 | 证据 | 收尾 |
|---|---|---|---|---|---|
| **BDS** | 写长句的公共知识分子 | not X but Y / rather than / increasingly | This article + I | author-date 拉扯 + 宣言 | 规训性呼吁 |
| **HCI** | 兴奋的工坊主持人 | We present / may-suggest / 引语并陈 | we（工坊） | N+报酬+p 值+参与者引语 | design implications |
| **SOC** | 与韦伯和 GSS 同时对话的理论统计学家 | consistent with / net of / in other words | we+摘要 the authors | 模型递进表+假设对话 | limitations+方向 |
| **SE** | 写清单的工程师 | To understand X / a set of / 16 词短句 | we+our（团队） | 数据规模+阈值+表格 | Threats→Future Work |

**边界地带的启示**：批判 HCI（Bardzell/Irani/Keyes/Dourish 线）在 HCI 库内形成 BDS 风格飞地（critique 密度 6.5 vs BDS 7.0，几乎持平）；Zeller 与 Hindle 在 SE 库内是修辞破格者（epigraph、设问、口语判词）；计算社会学（Macy/Centola/Watts 线）则正在向 SE 的实证仪式靠拢（RQ、robustness）。**文体是光谱而非国界，但每个学科的重心清晰可辨。**

## 8. 与 Dourish 的对照（衔接前一份报告）

把 Dourish 21 文本基线（32.4 万词）与本四学科语料并置：

| 模式（次/万词） | Dourish | BDS | HCI | SOC | SE |
|---|---|---|---|---|---|
| not simply...but | **9.2** | 2.9 | 1.5 | 1.6 | 0.8 |
| rather than | **8.2** | 5.1 | 3.5 | 3.3 | 2.0 |
| ways in which | **10.5** | — | — | — | — |
| 缩写词 | 少 | 0 | 2.7 | 7.4 | 1.2 |

Dourish 的签名句式密度**高于四学科中的任何一个**——连最接近他的 BDS 也只有其三分之一。这印证了前一份报告的定位：Dourish 不是"典型 HCI/BDS 写作者"，而是把批判句法推到个人极端的异数；反之，若想"写得像个学科"而不是"像个 Dourish"，BDS 库的平均密度才是校准参考。

## 9. 局限与可复用产物

**局限**：(1) 子库由 yunqi 手工圈定，代表"我的经典清单"而非随机样本；(2) BDS 库 27 篇偏小，docfreq 指标解读需谨慎；(3) SE 缺 19 篇 IEEE 快照论文；OCR/连字/水印噪声已按管线清洗但无法归零；(4) 各库年份分布不同（SOC 含 1975–1990 经典，BDS 全部 2004 后），部分差异是年代而非学科；(5) 段落级统计受单栏/双栏版式影响，句子级指标不受影响。

**可复用产物**（`ZCodeProject/discipline_style_analysis/`）：
- `corpus_items.json` / `corpus_meta.json` —— 347 条目与 314 篇入语料的键值、词数、年份、venue
- `paras.json` —— 段落级全文（键 = `学科_ ZoteroKey`）
- `00_resolve.py`…`05_cjk_clean.py` —— 解析→提取→指标→keyness→清洗全管线
- `metrics.json` / `moves.json` / `keyness.json` / `ngrams.json` —— 全部量化结果
- `verify_quotes.py` —— 引文核验（连字/换行/脚注容错）

**下一步可选**：把四学科风格画像蒸馏成 4 个润色 skill（对标本人的 dourish-style），或用 keyness 词表做"学科伪装检测器"（给一段文字判断它最像哪个学科写的）。
