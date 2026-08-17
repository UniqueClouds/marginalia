#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate mkdocs docs/ pages from marginalia content (entries + podcast guide).
Run locally; commit the generated docs/ so CI only needs `mkdocs build`."""
import os, re, shutil, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTRIES_DIR = os.path.join(ROOT, "marginalia")
DOCS = os.path.join(ROOT, "docs")
os.makedirs(os.path.join(DOCS, "entries"), exist_ok=True)
os.makedirs(os.path.join(DOCS, "podcast-guide", "data"), exist_ok=True)

FRONT = re.compile(r"^---\n.*?\n---\n", re.S)

def strip_front(text):
    m = FRONT.match(text)
    return m.group(0) if m else "", (text[m.end():] if m else text)

def meta_table(front):
    rows = []
    for line in front.splitlines():
        if line.startswith(("id:", "title:", "date:", "published:", "kind:", "issue:")):
            k, _, v = line.partition(":")
            rows.append((k.strip(), v.strip().strip('"').strip("'")))
    if not rows:
        return ""
    cells = "".join(f"<tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>{k}</td><td style='padding:3px 10px;'>{v}</td></tr>" for k, v in rows)
    return f"<details><summary style='cursor:pointer;color:#888;'>Provenance（来源与元数据）</summary><table style='border:1px solid #eee;border-radius:8px;'>{cells}</table></details>\n\n"

BLOB = "https://github.com/UniqueClouds/marginalia/blob/main/marginalia"

def rewrite_links(text, num, slug):
    # 跨条目 note 链接 → 站内条目页
    text = re.sub(r"\.\./(\d{3}-[a-z0-9-]+)/note\.(zh|en)\.md", r"\1.\2.md", text)
    # 跨条目 artifact 链接 → GitHub 直链
    text = re.sub(r"\.\./(\d{3}-[a-z0-9-]+)/artifact\.(zh|en)\.md",
                  BLOB + r"/\1/artifact.\2.md", text)
    # 本条目内 artifact 链接（无 ../）→ GitHub 直链
    text = re.sub(r"\]\((?:\./)?artifact\.(zh|en)\.md\)",
                  lambda m: "](%s/%s/artifact.%s.md)" % (BLOB, slug, m.group(1)), text)
    return text

def build_entries():
    idx = []
    for d in sorted(glob.glob(os.path.join(ENTRIES_DIR, "*-*"))):
        if not os.path.isdir(d):
            continue
        slug = os.path.basename(d)
        num = slug.split("-")[0]
        zh_p, en_p = os.path.join(d, "note.zh.md"), os.path.join(d, "note.en.md")
        if not os.path.exists(zh_p):
            continue
        front, body = strip_front(open(zh_p, encoding="utf-8").read())
        title_m = re.search(r"title:\s*[\"']?(.+?)[\"']?\s*$", front, re.M)
        title = title_m.group(1) if title_m else slug
        date_m = re.search(r"^(?:date|published):\s*(.+?)\s*$", front, re.M)
        entry_date = (date_m.group(1) if date_m else "").strip()
        # 条目附属文件（skill/docs/reports/artifact）作为子页
        extras = []
        for sub in sorted(os.listdir(d)):
            sp = os.path.join(d, sub)
            if os.path.isfile(sp) and sub.endswith(".md") and sub not in ("note.zh.md", "note.en.md", "artifact.zh.md", "artifact.en.md"):
                extras.append(sub)
            elif os.path.isdir(sp):
                for f in sorted(glob.glob(os.path.join(sp, "*.md"))):
                    extras.append(os.path.relpath(f, d).replace("\\", "/"))
        extra_html = ""
        if extras:
            links = " · ".join(f"[{os.path.basename(x)}]({BLOB}/{slug}/{x})" for x in extras[:8])
            extra_html = f"\n\n<div style='font-size:12.5px;color:#555;'>📎 附属材料：{links}</div>\n"
        # 复制子目录文档（reports/ docs/）使条目内相对链接可用
        for sub in ("reports", "docs"):
            sp = os.path.join(d, sub)
            if os.path.isdir(sp):
                dst = os.path.join(DOCS, "entries", sub)
                os.makedirs(dst, exist_ok=True)
                for f in glob.glob(os.path.join(sp, "*.md")):
                    shutil.copy(f, os.path.join(dst, os.path.basename(f)))
        en_link = ""
        if os.path.exists(en_p):
            en_link = f"\n\n---\n\n> 🌐 [Read this note in English]({num}-{slug.split('-',1)[1]}.en.md)\n"
        body = rewrite_links(body, num, slug)
        out = f"# {title}\n\n{meta_table(front)}{body}{extra_html}{en_link}\n"
        open(os.path.join(DOCS, "entries", f"{num}-{slug.split('-',1)[1]}.zh.md"), "w", encoding="utf-8").write(out)
        # EN page
        if os.path.exists(en_p):
            front2, body2 = strip_front(open(en_p, encoding="utf-8").read())
            body2 = rewrite_links(body2, num, slug)
            out2 = f"# {title}\n\n{meta_table(front2)}{body2}\n\n---\n\n> 🌐 [阅读中文版]({num}-{slug.split('-',1)[1]}.zh.md)\n"
            open(os.path.join(DOCS, "entries", f"{num}-{slug.split('-',1)[1]}.en.md"), "w", encoding="utf-8").write(out2)
        idx.append((num, title, slug, entry_date))
        print("entry:", num, title[:40])
    return idx

def build_podcast():
    src = os.path.join(ROOT, "marginalia", "006-podcast-guide")
    if not os.path.exists(src):
        print("podcast-guide 不在仓库，跳过")
        return
    for name in ("artifact.zh.md",):
        p = os.path.join(src, name)
        if os.path.exists(p):
            front, body = strip_front(open(p, encoding="utf-8").read())
            title_m = re.search(r"title:\s*[\"']?(.+?)[\"']?\s*$", front, re.M)
            title = title_m.group(1) if title_m else "Spotify Podcast Guide"
            out = f"# {title}\n\n{meta_table(front)}{body}\n"
            open(os.path.join(DOCS, "podcast-guide", "index.md"), "w", encoding="utf-8").write(out)
            print("podcast index built")
    for f in glob.glob(os.path.join(src, "data", "*")):
        shutil.copy(f, os.path.join(DOCS, "podcast-guide", "data", os.path.basename(f)))
    print("podcast data copied")

def build_index(idx):
    cards = []
    for num, title, slug, entry_date in idx:
        s = slug.split("-", 1)[1]
        zh_url = f"entries/{num}-{s}.zh.md"
        en_url = f"entries/{num}-{s}.en.md"
        cards.append(
            f"- :material-book-open-outline: **ENTRY {num}** · {entry_date}\n\n"
            f"    ---\n\n"
            f"    {title}\n\n"
            f"    [中文版]({zh_url}) · [English]({en_url})")
    cards.append(
        f"- :material-podcast: **ENTRY 006 · ARTIFACT** · 2026-08-17\n\n"
        f"    ---\n\n"
        f"    🎧 Spotify Podcast Guide · 英文播客推荐（26 节目 / 46 集精选）\n\n"
            f"    [进入播客清单](podcast-guide/index.md) · [数据 CSV](podcast-guide/data/shows.csv)")
    cards_str = "\n\n".join(cards)
    page = f"""# Marginalia

<div class="marg-hero" markdown>

**Marginalia** \u2014 书页边注，选择性研究与阅读笔记。

*mar·gin·a·li·a* (n.) — notes scribbled in the margins of a book; the traces a reader leaves behind.

<sub>📖 [项目说明](about.md) · 🐙 [GitHub](https://github.com/UniqueClouds/marginalia) · 🌐 [English README](https://github.com/UniqueClouds/marginalia/blob/main/README.md)</sub>

</div>

## 📚 条目 Entries

每条以 **issue → PR → squash commit** 仪式沉淀；中英双语，开头带完整溯源元数据。

<div class="grid cards" markdown>

{cards_str}

</div>

## 关于这个站

- 站点由 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建，push 到 `main` 即自动重新部署（见 [.github/workflows/deploy.yml](https://github.com/UniqueClouds/marginalia/blob/main/.github/workflows/deploy.yml)）。
- **仓库刻意保持稀疏**：默认全部 `gitignore`，只有显式加入白名单的、精选过的笔记才会被提交——不会有随手的提交。
- 数据复现：每条条目内的 `sources` 字段列出依据的本地语料与工具来源；原始语料本身不随仓库公开。
- 📖 详见 [项目说明](about.md) · 🐙 在 [GitHub](https://github.com/UniqueClouds/marginalia) 上查看仓库与发布历史。

<sub>本页由 <code>scripts/build_site_pages.py</code> 自动生成；改首页请改脚本而非本文件。</sub>
"""
    open(os.path.join(DOCS, "index.md"), "w", encoding="utf-8").write(page)
    print("index built")

if __name__ == "__main__":
    idx = build_entries()
    build_podcast()
    build_index(idx)
    print("DONE")