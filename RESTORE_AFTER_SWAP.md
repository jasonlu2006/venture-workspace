# RESTORE AFTER LINUX SWAP
Written 2026-08-22 before laptop OS swap. Everything below is already
pushed to GitHub. After the swap, run these to continue exactly where we
left off.

## CRITICAL: two repos, not one
`$HOME/ventures` is the PARENT workspace repo. Inside it,
`products/release-notes-ai` is a SEPARATE git repo (a gitlink). Cloning the
parent alone will show an EMPTY `products/release-notes-ai/` folder. You must
clone BOTH.

## Clone on the new Linux machine
```bash
# 1. Parent workspace (operating docs, hypotheses, research, launch drafts)
git clone https://github.com/jasonlu2006/venture-workspace.git ~/ventures
cd ~/ventures

# 2. Product repo (separate repo inside)
git clone https://github.com/jasonlu2006/release-notes-ai \
    ~/ventures/products/release-notes-ai
```

## What's already live (does NOT need the laptop)
- Public repo:     https://github.com/jasonlu2006/release-notes-ai
- Live demo:       https://release-notes-ai.onrender.com  (Render auto-deploys
                   from the repo on every push — no local machine needed)
- Discord gateway: goonBot#9140 in your server (runs on THIS Windows machine
                   via Startup folder — see "After swap" note below)
- Daily 6 AM report: cron job 94c4b69b851d → Discord channel 1540647201229766688

## Local state that WILL be lost on swap (and is fine)
- The running `hermes gateway run` process — it's a local background service.
- Anything only in /tmp or not committed — none expected; verify with
  `git status` in both repos after clone.
- The Render deploy is independent of this machine (it builds from GitHub).

## After swap: re-secure the gateway (so Discord alerts resume)
The gateway currently runs on Windows Startup. On Linux you'll reinstall it:
```bash
hermes gateway install    # Linux: installs a systemd user service
hermes gateway run        # or just rely on the service
```
The Discord token + WhatsApp-off config live in the Hermes config dir
(`%LOCALAPPDATA%/hermes/` on Windows; `~/.local/share/hermes/` or similar on
Linux — Hermes migrates via its own config on first run). If the bot goes
offline after swap, re-run `hermes gateway setup` and re-paste the Discord
token (it's the one you pasted earlier, the 72-char MTI0... value).

## Continue the launch
- Launch posts are at: ~/ventures/validation/release-notes-ai/POSTS_READY.md
- HN is the first move (Tue-Thu, 7-9 AM ET). Paste me the link after posting.
- Traction gate: if waitlist >= 25 qualified emails → build Pro tier
  (needs your Stripe account; see research/MONETIZATION.md).

## Verify after clone
```bash
cd ~/ventures && git status          # expect clean
cd products/release-notes-ai && git status && python3 tests.py && python3 test_webapp.py
```
