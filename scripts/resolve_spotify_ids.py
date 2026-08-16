# -*- coding: utf-8 -*-
"""Use Spotify official API (client credentials) to resolve episode IDs and remaining show IDs."""
import json, os, re, time, subprocess, urllib.parse
from spotify_creds import get as _creds, sys

CLIENT_ID, CLIENT_SECRET = _creds()
DATA = r"C:\Users\yunqi\ZCodeProject\data"

def token():
    r = subprocess.run(["curl", "-sS", "-m", "15", "-X", "POST", "https://accounts.spotify.com/api/token",
                        "-H", "Content-Type: application/x-www-form-urlencoded",
                        "-d", f"grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"],
                       capture_output=True, text=True, encoding="utf-8").stdout
    return json.loads(r)["access_token"]

def api(url):
    for attempt in range(3):
        r = subprocess.run(["curl", "-sS", "-m", "20", "-H", f"Authorization: Bearer {TOK}", url],
                           capture_output=True, text=True, encoding="utf-8").stdout
        try:
            j = json.loads(r)
        except Exception:
            time.sleep(2); continue
        if "error" in j and j.get("error", {}).get("status") == 429:
            time.sleep(3); continue
        return j
    return {}

def search_show(name, expect):
    q = urllib.parse.quote(name)
    j = api(f"https://api.spotify.com/v1/search?q={q}&type=show&limit=10")
    items = j.get("shows", {}).get("items", []) or []
    for s in items:
        if expect in (s.get("name") or "").lower():
            return s
    return None

def search_episode(kw, show_expect, extra=()):
    q = urllib.parse.quote(kw[:60])
    j = api(f"https://api.spotify.com/v1/search?q={q}&type=episode&limit=20")
    items = j.get("episodes", {}).get("items", []) or []
    best = None
    for e in items:
        sn = (e.get("show") or {}).get("name") or ""
        en = e.get("name") or ""
        if show_expect not in sn.lower():
            continue
        score = sum(1 for w in kw.split()[:4] if w.lower() in en.lower())
        if extra:
            score += sum(2 for w in extra if w.lower() in en.lower())
        if score >= 1 and (best is None or score > best[0]):
            best = (score, e)
    return best[1] if best else None

TOK = token()
print("token ok", flush=True)

# --- 1) resolve remaining shows ---
SHOWS_TO_RESOLVE = [
    ("ripus", "The Rest Is Politics US", "rest is politics"),
    ("riplead", "The Rest Is Politics Leading", "rest is politics"),
    ("lrb", "LRB Podcast", "lrb"),
]
resolved_shows = {}
for key, q, expect in SHOWS_TO_RESOLVE:
    s = search_show(q, expect)
    resolved_shows[key] = {"id": s.get("id") if s else None, "name": s.get("name") if s else None}
    print("SHOW", key, "->", resolved_shows[key], flush=True)
    time.sleep(0.4)

# --- 2) resolve 26 episodes ---
eps = json.load(open(os.path.join(DATA, "episodes.json"), encoding="utf-8"))["episodes"]
QUERY = {
    "rih": ("The Rest Is History", ["Rest Is History"]),
    "riclass": ("The Rest Is Classified", ["Rest Is Classified"]),
    "rip": ("The Rest Is Politics", ["Rest Is Politics"]),
    "rient": ("The Rest Is Entertainment", ["Rest Is Entertainment"]),
    "rimoney": ("The Rest Is Money", ["Rest Is Money"]),
}
resolved_eps = []
for e in eps:
    show_expect, extras = QUERY[e["show"]]
    kw = e["title_en"].replace("Ep 2", "").replace("Ep 3", "").replace("Ep 6", "").replace("Ep 1", "")
    kw = re.sub(r"\(Part 1\)|\(Part 2\)", "", kw)
    hit = search_episode(kw, show_expect, extras)
    eid = hit.get("id") if hit else None
    resolved_eps.append({"key": e["show"] + "_" + e["number"], "title": e["title_en"],
                         "spotify_episode_id": eid,
                         "spotify_url": f"https://open.spotify.com/episode/{eid}" if eid else None,
                         "matched_title": hit.get("name") if hit else None})
    print("EP", e["title_en"][:42], "->", eid, "|", (hit.get("name") or "")[:40] if hit else "MISS", flush=True)
    time.sleep(0.35)

json.dump({"shows": resolved_shows, "episodes": resolved_eps},
          open(os.path.join(DATA, "spotify_lookup.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("DONE", flush=True)