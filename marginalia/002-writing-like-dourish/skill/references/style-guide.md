# Dourish Style Guide（蒸馏版）

来源：21 种文本（2004–2026，约 40.8 万词）的语料库分析（报告：`ZCodeProject/Dourish_语言特征分析报告.md`）。所有引文均已脚本核验。**引用原文仅作例证；绝不把原句写进用户稿件。**

## 1. 两种语域（先选一种，别混）

| | **Register A：实践语域**（1995–2013 主导） | **Register B：物质语域**（2016–2017 起） |
|---|---|---|
| 理论资源 | Garfinkel 常民方法论、现象学（Suchman/Sacks/Heidegger） | 物质文化研究、软件研究（Miller/Star/Edwards） |
| 核心词 | practice(s), everyday, encounter, occasion, accountability, mundane, witnessable, in the course of, achievement | materiality/materialities, format, representation, infrastructure, constraint, affordance(他拒绝), substrate |
| 适合 | 民族志、CSCW、qualitative HCI、语境/情感/隐私论文 | 数据研究、算法研究、软件/基础设施、数据基础设施论文 |
| 密度参考 | practice 3.2/kw, everyday 1.0/kw, encounter 0.7/kw | materiality 0.2/kw（全书 2.6/kw——单书现象，稿件别照抄） |

判断标准：稿件谈"人们实际做什么"→A；谈"形式/格式/系统如何 constrain 行动"→B。2018 后他常混用（data 叙事 + materiality 词）。

## 2. 句法指纹（跨语域不变，是安全强化项）

1. **否定—重述**（最核心，0.93/kw，18/20 篇）：`not simply/just/only/merely X, but Y`；`X ... , but rather Y`；`rather than`（0.82/kw，19/20 篇）。用途：定义、纠偏、thesis 句。
   原文例证："my topic here is not the materiality of information but the materialities of information"（2017, ch.1）
2. **the ways in which**（1.05/kw）：引入研究对象的标准框架。
   原文例证："properties of representations and formats that constrain, enable, limit, and shape the ways in which those representations can be created, transmitted, stored, manipulated, and put to use"（2017, ch.1）
3. **教学式改写对**：`..., that is, ...`（0.34/kw）与 `in other words`（0.19/kw）——术语句后紧跟一个更具体的重述。2017 年 that is, 密度达基线 2.45 倍。
4. **复数量词**：a set/range/variety/series of（0.98/kw）+ sorts/kinds/forms/types of（2.15/kw）——拒绝单因。
5. **限定语校准**：might/may（0.84/kw）、perhaps/arguably（0.63/kw）、indeed（0.33）、of course（0.26）。判断的锋利全部交给 not-X-but-Y，从不说满。
6. **in the course of**（0.13/kw，Register A 专用）：把静态属性改写成进行中的成就。

## 3. 段落与篇章习惯

- **开场**：轶事（具体日期/物品/事故）或成对设问。原文例证："On November 16, 2015, the United States Air Force announced..."（2017, ch.1 第一句）
- **设问密度**：理论文 ~1/200 词；实证文骤降。设问悬置常识，不设 strawman。
- **抽象→具象落差**：每个抽象论点配一个可感画面（35 吨穿孔卡；天花板里的电缆；伸手够咖啡杯的 homunculus）。
- **教师口吻**（仅限 position/essay 类）："I tell my students that..."。
- **dry humor / 轻反讽**：低频、插入语式。原文例证："Neither was it my intent that it be exhausting, although I may have missed the mark on that one. Apologies."（2017, ch.2）
- **标题**：交错配列（X of Y and Y of X）、头韵、文学戏仿；避免 "A Study of..."。

## 4. 第一人称政策

专著独著大量 I（WtAI 305 处）；合著转 we；评论/essay 高密度 I。CHI/CSCW 主论文：方法+立场段可用 we/our，避免 I；intro 的动机句可用第一人称复数。

## 5. 反模式（改稿时删除）

- "It is important to note that..."（他全文 21 种文本只用了 4 次）——直接说事
- "plays a crucial/vital role"、"shed light on"（4 次，均在转述他人）
- 连续两句以上纯抽象无实例
- 过度名词化串（the utilization of...）→ 改动词
- 把 hedging 当模糊：他 hedge 的是判断强度，从不 hedge 事实陈述
