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
            en_link = f"\n\n---\n\n> 🌐 [Read this note in English]({num}-{slug.split('-',1)[1]}.en/)\n"
        body = rewrite_links(body, num, slug)
        out = f"# {title}\n\n{meta_table(front)}{body}{extra_html}{en_link}\n"
        open(os.path.join(DOCS, "entries", f"{num}-{slug.split('-',1)[1]}.zh.md"), "w", encoding="utf-8").write(out)
        # EN page
        if os.path.exists(en_p):
            front2, body2 = strip_front(open(en_p, encoding="utf-8").read())
            body2 = rewrite_links(body2, num, slug)
            out2 = f"# {title}\n\n{meta_table(front2)}{body2}\n\n---\n\n> 🌐 [阅读中文版]({num}-{slug.split('-',1)[1]}.zh/)\n"
            open(os.path.join(DOCS, "entries", f"{num}-{slug.split('-',1)[1]}.en.md"), "w", encoding="utf-8").write(out2)
        idx.append((num, title, slug))
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
    for num, title, slug in idx:
        label = slug.split("-", 1)[1].replace("-", " ")
        cards.append(
            f'<div style="border:1px solid #e0e0e0;border-radius:12px;padding:14px 16px;margin-bottom:10px;background:#fff;">'
            f'<div style="color:#1DB954;font-weight:700;font-size:12px;">ENTRY {num}</div>'
            f'<div style="font-weight:600;margin:4px 0;">{title}</div>'
            f'<div style="font-size:12.5px;color:#666;">'
            f'<a href="entries/{num}-{slug.split("-",1)[1]}.zh/">中文版</a> · '
            f'<a href="entries/{num}-{slug.split("-",1)[1]}.en/">English</a></div></div>')
    pod_card = ('<div style="border:1px solid #e0e0e0;border-radius:12px;padding:14px 16px;margin-bottom:10px;background:#fff;">'
                '<div style="color:#1DB954;font-weight:700;font-size:12px;">ENTRY 006 · ARTIFACT</div>'
                '<div style="font-weight:600;margin:4px 0;">🎧 Spotify Podcast Guide · 英文播客推荐（26 节目 / 46 集精选）</div>'
                '<div style="font-size:12.5px;color:#666;"><a href="podcast-guide/">进入播客清单</a> · '
                '<a href="podcast-guide/data/shows.csv">数据 CSV</a></div></div>')
    cards.append(pod_card)
    page = f"""# Marginalia

> *mar·gin·a·li·a* (n.) — notes scribbled in the margins of a book; the traces a reader leaves behind.

选择性研究与阅读笔记（双语发布，English / 中文）——每条笔记以 **issue → PR → squash commit** 的方式沉淀。

## 条目索引

{''.join(cards)}

## 数据与方法

- 仓库：github.com/UniqueClouds/marginalia · 站点由 MkDocs Material 构建，push 自动部署。
"""
    open(os.path.join(DOCS, "index.md"), "w", encoding="utf-8").write(page)
    print("index built")

if __name__ == "__main__":
    idx = build_entries()
    build_podcast()
    build_index(idx)
    print("DONE")