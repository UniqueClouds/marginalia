# 项目说明

**Marginalia**（书页边注）——选择性研究与阅读笔记，中英双语发布。每条笔记以 **issue → PR → squash commit** 的方式沉淀，保证仓库历史像目录一样可读。

> 🌐 **网站（本站）：<https://uniqueclouds.github.io/marginalia/>**
> 本页即该网站的一部分：所有内容物（研究笔记、报告、技能、播客清单）都在这里在线阅读，由 MkDocs Material 构建，**push 到 main 即自动重新部署**。

## 内容结构

| 板块 | 说明 |
|---|---|
| 条目 001–005 | 研究随想/分析（每条含中英双语正文 + provenance 元数据 + 附属报告/提案） |
| 006 · Podcast Guide | Spotify 英文播客推荐清单（26 节目 / 46 集精选，全部官方链接） |

## 发布机制

1. **Issue** — 随想本身：触发点、数据来源、原始想法；
2. **Pull request** — 蒸馏后的双语笔记（`note.en.md` + `note.zh.md`）+ 索引行；
3. **Commit** — 每条一个 squash commit，历史即目录。

## 数据与复现

- 原始语料与工作区**不随仓库公开**（default-deny `.gitignore`，仅白名单文件可提交）；
- 各条目内的 `sources` 字段列出数据与工具来源；
- 站点由 `scripts/build_site_pages.py` 从条目目录自动生成，`mkdocs build` 本地可复现。

## 链接

- 仓库：<https://github.com/UniqueClouds/marginalia>
- 网站：<https://uniqueclouds.github.io/marginalia/>
- 作者：[Yunqi Chen](https://github.com/UniqueClouds)
