#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch the user's followed Spotify shows via device flow; save to JSON."""
import json, os, sys, time, urllib.parse

try:
    import requests
except ImportError:
    sys.exit("pip install requests")

S = requests.Session()
S.trust_env = False  # 直连 accounts/api.spotify.com，不走系统代理（代理会拦 Spotify 鉴权）

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", "")
# scopes: read followed shows
SCOPES = "user-follow-read playlist-read-private"

def device_flow():
    r = S.post("https://accounts.spotify.com/api/token", data={
        "client_id": CLIENT_ID,
        "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        "scope": SCOPES})
    j = r.json()
    if "verification_uri" not in j:
        sys.exit("DEVICE_FLOW_FAIL: " + json.dumps(j, ensure_ascii=False))
    print("AUTH_URL=" + j["verification_uri"] + " AUTH_CODE=" + j["user_code"] + " EXPIRES=" + str(j["expires_in"]), flush=True)
    interval = j.get("interval", 5)
    for _ in range(int(j["expires_in"] / interval) + 10):
        time.sleep(interval)
        jr = S.post("https://accounts.spotify.com/api/token", data={
            "grant_type": "urn:ietf:params:oauth:grant-type:device_token",
            "client_id": CLIENT_ID, "device_code": j["device_code"]}).json()
        if jr.get("access_token"):
            return jr
        if jr.get("error") in ("authorization_pending", "slow_down"):
            continue
        if jr.get("error") == "expired_token":
            sys.exit("AUTH_EXPIRED")
        if jr.get("error") == "access_denied":
            sys.exit("AUTH_DENIED")
        time.sleep(2)
    sys.exit("AUTH_TIMEOUT")

def main():
    if not CLIENT_ID:
        sys.exit("NO_CLIENT_ID")
    tok = device_flow()
    h = {"Authorization": "Bearer " + tok["access_token"]}
    shows, offset = [], 0
    while True:
        r = S.get("https://api.spotify.com/v1/me/shows", headers=h,
                         params={"limit": 50, "offset": offset})
        j = r.json()
        items = j.get("items", [])
        if not items:
            break
        for it in items:
            s = it.get("show") or {}
            shows.append({"name": s.get("name"), "id": s.get("id"),
                          "publisher": s.get("publisher"),
                          "description": (s.get("description") or "")[:200],
                          "total_episodes": s.get("total_episodes"),
                          "added_at": it.get("added_at")})
        offset += len(items)
        if offset >= j.get("total", offset):
            break
        time.sleep(0.4)
    out = {"token_ok": True, "count": len(shows), "shows": shows}
    path = r"C:\Users\yunqi\ZCodeProject\data\spotify_my_shows.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("FOLLOWED_DONE count=" + str(len(shows)), flush=True)

if __name__ == "__main__":
    main()