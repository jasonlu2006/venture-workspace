#!/usr/bin/env python3
"""
Local validation landing page for the H3 venture (Release Notes AI).

This is a CHEAP VALIDATION artifact, NOT a public release. It runs locally
and collects interested emails into a local file (waitlist.txt). No external
service, no third-party tracker, no spam. It is a "fake door": submitting
records interest and shows a thank-you; no product is charged or deployed.

Run:  python3 landing.py --port 8000
Then open http://localhost:8000/

NOTE: Do NOT expose this publicly or collect real payment without first
creating a HUMAN RELEASE REVIEW task.
"""
from __future__ import annotations
import argparse
import os
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
WAITLIST = os.path.join(HERE, "waitlist.txt")
PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Release Notes AI — customer-friendly release notes from your git history</title>
<style>
  :root{--bg:#0b0e14;--card:#151a23;--fg:#e8eaed;--muted:#9aa3b2;
        --accent:#5b8cff;--accent2:#7c5bff;--border:#222a36;}
  *{box-sizing:border-box}
  body{margin:0;font:16px/1.6 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
       background:var(--bg);color:var(--fg);}
  .wrap{max-width:760px;margin:0 auto;padding:64px 22px 90px;}
  .badge{display:inline-block;font-size:12px;letter-spacing:.5px;text-transform:uppercase;
         color:var(--accent);border:1px solid var(--border);border-radius:999px;
         padding:4px 12px;margin-bottom:22px;}
  h1{font-size:40px;line-height:1.15;margin:0 0 14px;}
  h1 .grad{background:linear-gradient(90deg,var(--accent),var(--accent2));
           -webkit-background-clip:text;background-clip:text;color:transparent;}
  .sub{font-size:19px;color:var(--muted);margin:0 0 30px;}
  .card{background:var(--card);border:1px solid var(--border);border-radius:14px;
        padding:22px;margin:0 0 22px;}
  h2{font-size:20px;margin:0 0 12px;}
  ul{margin:0;padding-left:20px;color:var(--muted);}
  li{margin-bottom:6px;}
  .demo{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;
        background:#0d1117;border:1px solid var(--border);border-radius:10px;
        padding:14px;color:#c9d1d9;white-space:pre-wrap;overflow:auto;}
  form{display:flex;gap:10px;flex-wrap:wrap;margin-top:6px;}
  input[type=email]{flex:1;min-width:220px;padding:13px 14px;border-radius:10px;
        border:1px solid var(--border);background:#0d1117;color:var(--fg);font-size:15px;}
  button{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;
        border:0;border-radius:10px;padding:13px 22px;font-size:15px;font-weight:600;
        cursor:pointer;}
  button:hover{opacity:.92;}
  .note{font-size:13px;color:var(--muted);margin-top:10px;}
  footer{color:var(--muted);font-size:12px;margin-top:40px;text-align:center;}
</style></head>
<body><div class="wrap">
  <div class="badge">Early access · validation</div>
  <h1>Stop hand-writing <span class="grad">release notes</span>.</h1>
  <p class="sub">Release Notes AI turns your merged GitHub PRs into clean,
  customer-friendly "What's New" pages — automatically, and free to self-host.</p>

  <div class="card">
    <h2>What it does</h2>
    <ul>
      <li>Pulls merged PRs since your last release — no token needed for light use.</li>
      <li>Rewrites technical titles into plain-language customer sentences.</li>
      <li>Auto-categorizes into Features / Fixes / Performance / Docs.</li>
      <li><b>Hides internal noise</b> (Dependabot, CI, pre-commit churn) by default.</li>
      <li>Serves a hosted "What's New" page + JSON API you can embed anywhere.</li>
      <li>Zero dependencies, self-hostable, ~$0 to run.</li>
    </ul>
  </div>

  <div class="card">
    <h2>Example output</h2>
    <div class="demo">BEFORE (raw PR title):  fix: crash when uploading empty CSV file
AFTER  (customer note):  Fixed a crash when uploading an empty CSV file.

BEFORE:  chore(deps): bump astral-sh/ruff-pre-commit in pre-commit group
AFTER:   (hidden — internal noise, not shown to customers)

This release includes 3 changes. 1 new feature. 2 bug fixes.</div>
  </div>

  <div class="card">
    <h2>Get early access</h2>
    <p class="note" style="margin-top:0">Leave your email and we'll reach out when
    the hosted version is ready. One message, no spam.</p>
    <form method="post" action="/waitlist">
      <input type="email" name="email" placeholder="you@company.com" required>
      <button type="submit">Request access</button>
      <input type="text" name="current" placeholder="What do you use for release notes now? (optional)"
             style="flex-basis:100%;min-width:220px;padding:11px 14px;border-radius:10px;
                    border:1px solid var(--border);background:#0d1117;color:var(--fg);font-size:14px;">
    </form>
    <p class="note">Prefer to run it yourself now? It's a single Python file —
    reply and we'll send the link.</p>
  </div>

  <footer>Validation experiment. Not a commercial offering yet.</footer>
</div></body></html>"""

THANKS = """<!doctype html><html><head><meta charset="utf-8">
<title>Thanks — Release Notes AI</title><style>
body{margin:0;font:16px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;
background:#0b0e14;color:#e8eaed;display:flex;min-height:100vh;align-items:center;
justify-content:center;text-align:center;padding:24px;}
.box{max-width:460px;}h1{font-size:30px;margin:0 0 10px;}
p{color:#9aa3b2;}a{color:#5b8cff;}</style></head><body><div class="box">
<h1>You're on the list ✅</h1>
<p>Thanks — we'll email you when the hosted version is ready.
<br><a href="/">← back</a></p></div></body></html>"""


class H(BaseHTTPRequestHandler):
    def _send(self, code, body: bytes, ctype="text/html; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/waitlist"):
            self._send(200, THANKS.encode())
            return
        self._send(200, PAGE.encode())

    def do_POST(self):
        if self.path != "/waitlist":
            self._send(404, b"not found")
            return
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8", "replace")
        fields = urllib.parse.parse_qs(raw)
        email = (fields.get("email") or [""])[0].strip()
        current = (fields.get("current") or [""])[0].strip()
        if email and "@" in email:
            with open(WAITLIST, "a", encoding="utf-8") as f:
                f.write(email + ("" if not current else "\t" + current) + "\n")
            self._send(200, THANKS.encode())
        else:
            self._send(400, b"invalid email")

    def log_message(self, *a):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), H)
    print(f"Validation landing page at http://localhost:{args.port}/  (Ctrl+C to stop)")
    print(f"Waitlist saved to: {WAITLIST}")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
