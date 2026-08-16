#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_pipeline.py — Spotify 播客清单 · 自动化增量更新管线

用法:
    python scripts/update_pipeline.py [--force-episodes]

流程（幂等，可反复执行）:
  A. 刷新 The Rest Is… 系列官方 RSS（curl → data/_feeds/），更新集数与首集日期
  B. 刷新 iTunes 元数据（节目名/出品方/类型/集数/Apple 节目页）→ data/itunes_meta.json
  C. （可选 --force-episodes）重新解析 26 集精选的 Spotify 官方单集链接
  D. 增量扫描：用主题关键词扫新上架单集 → data/new_episode_candidates.json（只建议，不自动并入）
  E. 重建 data/shows.json+csv / episodes.json+csv → 重建博客 Markdown
  F. 写 data/state.json（上次更新时间戳）
"""
import json, os, subprocess, sys, time, re, glob, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SCRIPTS = os.path.join(ROOT, "scripts")
FEED_DIR = os.path.join(DATA, "_feeds")
os.makedirs(FEED_DIR, exist_ok=True)

RESTIS_FEEDS = {
    "rih": "https://feeds.megaphone.fm/GLT4787413333",
    "rip": "https://feeds.megaphone.fm/GLT9190936013",
    "ripus": "https://feeds.megaphone.fm/GLT5336643697",
    "riplead": "https://feeds.megaphone.fm/GLT9029505120",
    "rient": "https://feeds.megaphone.fm/GLT2052042801",
    "rimoney": "https://feeds.megaphone.fm/therestismoney",
    "riclass": "https://feeds.megaphone.fm/therestisclassified",
}
# 主题关键词 → 命中即进"新单集候选"
KEYWORDS = [r"mao", r"china", r"soviet", r"cold war", r"cia", r"spy",
            r"philby", r"nuclear", r"japan", r"samurai", r"genghis", r"bond",
            r"chilean", r"litvinenko", r"ai race", r"data cent", r"dune", r"star wars",
            r"beatles", r"oscars", r"spielberg", r"nolan", r"brics", r"murasaki",
            r"berlin wall", r"tolkien", r"dostoevsky", r"shakespeare", r"marcus aurelius"]

def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return r.stdout

def step_a():
    print("A. 刷新 Rest Is RSS ...", flush=True)
    for k, url in RESTIS_FEEDS.items():
        out = os.path.join(FEED_DIR, f"{k}.xml")
        r = subprocess.run(["curl", "-s", "-m", "40", "-A", "Mozilla/5.0", url, "-o", out],
                           capture_output=True, text=True)
        print("   ", k, os.path.getsize(out) if os.path.exists(out) else 0, flush=True)
        time.sleep(0.6)
    meta = {}
    for k in RESTIS_FEEDS:
        p = os.path.join(FEED_DIR, f"{k}.xml")
        raw = open(p, encoding="utf-8", errors="replace").read()
        dates = re.findall(r"<pubDate>([^<]*)</pubDate>", raw)
        items = len(re.findall(r"<item>", raw))
        meta[k] = {"items_in_feed": items, "first_date": dates[-1][:16] if dates else "",
                   "last_date": dates[0][:16] if dates else ""}
    json.dump(meta, open(os.path.join(DATA, "feed_meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("   feed_meta.json 已更新", flush=True)

def step_b():
    print("B. 刷新 iTunes 元数据 ...", flush=True)
    names = json.load(open(os.path.join(DATA, "shows.json"), encoding="utf-8"))["shows"]
    out = {}
    for s in names:
        key = s["key"]
        if key in ("rih", "rip", "ripus", "riplead", "rient", "rimoney", "riclass"):
            ids = {"rih": 1537788786, "rip": 1611374685, "ripus": 1743030473,
                   "riplead": 1665265193, "rient": 1718287198, "rimoney": 1703785141,
                   "riclass": 1780384916}
            url = f"https://itunes.apple.com/lookup?id={ids[key]}"
        else:
            url = "https://itunes.apple.com/search?term=" + urllib.parse.quote(s["name"]) + "&media=podcast&limit=3"
        try:
            r = sh(["curl", "-s", "-m", "15", url])
            j = json.loads(r)
            res = None
            for cand in j.get("results", []):
                if key == "cinephiliacs":
                    if "cinephiliac" in (cand.get("collectionName") or "").lower() and "elbow" not in (cand.get("collectionName") or "").lower():
                        res = cand; break
                elif s["name"].split()[0].lower() in (cand.get("collectionName") or "").lower():
                    res = cand; break
            if res is None and j.get("results"):
                res = j["results"][0]
            if res:
                out[key] = {"trackCount": res.get("trackCount"), "genre": res.get("primaryGenreName"),
                            "publisher": res.get("artistName"), "apple_url": res.get("trackViewUrl"),
                            "first_release": (res.get("releaseDate") or "")[:10]}
        except Exception as e:
            print("   ", key, "ERR", str(e)[:60], flush=True)
        time.sleep(0.5)
    json.dump(out, open(os.path.join(DATA, "itunes_meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("   itunes_meta.json 已更新", flush=True)

def step_c(force):
    if force or not os.path.exists(os.path.join(DATA, "spotify_episode_lookup.json")):
        print("C. 重新解析 Spotify 单集直链 ...", flush=True)
        sh(["python", os.path.join(SCRIPTS, "resolve_episode_ids.py")])
    else:
        print("C. 跳过单集解析（已有缓存；用 --force-episodes 强制重跑）", flush=True)

def step_d():
    print("D. 增量扫描新单集候选 ...", flush=True)
    cands = []
    for k in RESTIS_FEEDS:
        p = os.path.join(FEED_DIR, f"{k}.xml")
        if not os.path.exists(p):
            continue
        raw = open(p, encoding="utf-8", errors="replace").read()
        for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
            t = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", it, re.S)
            d = re.search(r"<pubDate>([^<]*)</pubDate>", it)
            if not t:
                continue
            title = t.group(1).strip()
            hits = [kw for kw in KEYWORDS if re.search(kw, title, re.I)]
            if hits and title not in [c["title"] for c in cands]:
                cands.append({"feed": k, "title": title, "date": d.group(1)[:16] if d else "", "hits": hits})
    picked = set(e["title_en"].lower() for e in json.load(open(os.path.join(DATA, "episodes.json"), encoding="utf-8"))["episodes"])
    cands = [c for c in cands if c["title"].lower() not in picked]
    def dkey(c):
        try:
            return time.mktime(time.strptime(c["date"], "%a, %d %b %Y"))
        except Exception:
            return 0
    cands.sort(key=dkey, reverse=True)
    json.dump({"generated": time.strftime("%Y-%m-%d %H:%M"), "candidates": cands[:40]},
              open(os.path.join(DATA, "new_episode_candidates.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"   候选 {len(cands[:40])} 条 → new_episode_candidates.json", flush=True)

def step_e():
    print("E. 重建数据 + 博客 ...", flush=True)
    json.dump({"last_update": time.strftime("%Y-%m-%d %H:%M:%S")},
              open(os.path.join(DATA, "state.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    sh(["python", os.path.join(SCRIPTS, "build_podcast_data.py")])
    sh(["python", os.path.join(SCRIPTS, "build_blog.py")])

def step_f():
    print("F. state.json 已写入（见 E 步）", flush=True)

if __name__ == "__main__":
    force = "--force-episodes" in sys.argv
    t0 = time.time()
    step_a(); step_b(); step_c(force); step_d(); step_e(); step_f()
    print(f"✅ 管线完成，耗时 {time.time()-t0:.0f}s")