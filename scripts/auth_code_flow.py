#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
auth_code_flow.py — Authorization Code + Secret 授权流（替代 Device Flow）
用法：
  1) developer.spotify.com → Dashboard → 你的 App → Settings/编辑设置
     在 Redirect URIs 里添加： http://localhost:8888/callback （保存）
  2) 运行本脚本，会打印一个授权 URL；用浏览器打开（登录你的 Spotify 账号并同意）
  3) 授权成功后浏览器会跳转到 localhost:8888/callback，脚本自动捕获 code 并换取 token
  4) 随后自动拉取你的已关注节目 → data/spotify_my_shows.json
"""
import json, os, sys, time, threading, urllib.parse, webbrowser
from spotify_creds import get as _creds
from http.server import BaseHTTPRequestHandler, HTTPServer

try:
    import requests
except ImportError:
    sys.exit("pip install requests")

CLIENT_ID, CLIENT_SECRET = _creds()
REDIRECT = "http://localhost:8888/callback"
SCOPES = "user-follow-read playlist-modify-public playlist-modify-private"
DATA = r"C:\Users\yunqi\ZCodeProject\data"
TOKEN_FILE = os.path.join(DATA, "spotify_user_token.json")

S = requests.Session()
S.trust_env = False

code_holder = {}
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q = urllib.parse.urlparse(self.path)
        if q.path == "/callback":
            params = urllib.parse.parse_qs(q.query)
            code_holder["code"] = params.get("code", [None])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h3>✅ 授权成功，可以关闭此页面了。</h3>".encode("utf-8"))
        else:
            self.send_response(404); self.end_headers()
    def log_message(self, *a):
        pass

def main():
    # start local server
    srv = HTTPServer(("127.0.0.1", 8888), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    auth_url = ("https://accounts.spotify.com/authorize?" + urllib.parse.urlencode({
        "client_id": CLIENT_ID, "response_type": "code", "redirect_uri": REDIRECT,
        "scope": SCOPES, "show_dialog": "false"}))
    print("=" * 66)
    print("  请先在开发者后台为 App 添加 Redirect URI: " + REDIRECT)
    print("  然后浏览器打开下面这个链接并登录授权：")
    print("  " + auth_url)
    print("=" * 66, flush=True)
    try:
        webbrowser.open(auth_url)
    except Exception:
        pass
    for _ in range(180):
        time.sleep(1)
        if code_holder.get("code"):
            break
    else:
        sys.exit("等待授权超时（3 分钟）。")
    r = S.post("https://accounts.spotify.com/api/token", data={
        "grant_type": "authorization_code", "code": code_holder["code"],
        "redirect_uri": REDIRECT, "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET})
    tok = r.json()
    if "access_token" not in tok:
        sys.exit("换取 token 失败: " + json.dumps(tok, ensure_ascii=False))
    tok["expires_at"] = time.time() + int(tok.get("expires_in", 3600)) - 60
    json.dump(tok, open(TOKEN_FILE, "w", encoding="utf-8"), ensure_ascii=False)
    print("✅ token 已保存:", TOKEN_FILE, flush=True)
    # fetch followed shows
    h = {"Authorization": "Bearer " + tok["access_token"]}
    shows, offset = [], 0
    while True:
        j = S.get("https://api.spotify.com/v1/me/shows", headers=h,
                  params={"limit": 50, "offset": offset}).json()
        items = j.get("items", [])
        if not items:
            break
        for it in items:
            s = it.get("show") or {}
            shows.append({"name": s.get("name"), "id": s.get("id"),
                          "publisher": s.get("publisher"),
                          "total_episodes": s.get("total_episodes"),
                          "added_at": it.get("added_at")})
        offset += len(items)
        if offset >= j.get("total", offset):
            break
        time.sleep(0.4)
    os.makedirs(DATA, exist_ok=True)
    json.dump({"count": len(shows), "shows": shows},
              open(os.path.join(DATA, "spotify_my_shows.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("✅ 已关注节目:", len(shows), "→ data/spotify_my_shows.json", flush=True)
    print("DONE", flush=True)

if __name__ == "__main__":
    main()