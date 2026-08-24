# LAUNCH COPY — Release Notes AI
Prepared 2026-08-22. Ready to paste the moment the repo is public.
Rule of thumb: launch HN first (Show HN, weekday 7-9 AM ET), then Reddit,
then Product Hunt ~1-2 weeks later with the traction numbers in the gallery.

====================================================================
1. SHOW HN POST
====================================================================
Title (pick one — A is the strongest hook):
  A) Show HN: Release Notes AI – customer-facing release notes from merged PRs
  B) Show HN: I built a free alternative to $49/mo release-notes tools
  C) Show HN: Turn your merged PRs into release notes your users understand

URL: https://github.com/jasonlu2006/release-notes-ai
LIVE DEMO (mention in first comment!): https://release-notes-ai.onrender.com/demo?repo=psf/requests

First comment (post immediately after submitting, from your account):
---
Hi HN! I kept noticing that every "automated changelog" tool just dumps raw
PR titles ("fix: crash when uploading empty CSV file") and someone still has
to hand-write the customer version. The FSE'25 paper on SmartNote found the
same thing: devs hate writing release notes, and conventional-commit-based
tools fail on more than half the projects they're pointed at.

Release Notes AI does three things differently:

1. Rewrites technical titles into plain-language sentences customers can read.
   "fix: crash when uploading empty CSV file" becomes "Fixed a crash when
   uploading an empty CSV file."

2. Hides internal noise by default. Dependabot bumps, pre-commit hooks, CI
   churn — none of it belongs in front of users, so it's filtered out. On
   psf/requests it turned 25 merged PRs into 8 clean notes.

3. It's one Python file with zero dependencies. No Node, no database, no
   docker-compose. `python3 webapp.py` gives you a hosted What's New page,
   a JSON API, an embeddable widget for your app, and a live demo.

There's also a GitHub Action so notes generate automatically on every tag.

Everything is MIT licensed and self-hostable for $0. If there's enough demand
I'll add a hosted tier (~$9/mo) with scheduled auto-publishing and email
digests, but the self-hosted version stays free forever.

Try it live (no signup): https://release-notes-ai.onrender.com/demo?repo=psf/requests
Repo: https://github.com/jasonlu2006/release-notes-ai

What would make this a no-brainer for your team? Roast my rewriter — it's
heuristic-based right now (works offline, costs nothing), with an optional
LLM mode if you set OPENAI_API_KEY.

Reply strategy:
- Thank every commenter; answer the "how is this different from git-cliff /
  release-please / semantic-release" question fast (they emit raw dev-facing
  markdown; we produce customer-facing prose + noise filtering + widget).
- If someone says the heuristics are weak: agree, note LLM upgrade path,
  ask what their worst-case PR title looks like (feature research).
- Never argue about pricing; point at the free self-host option.

====================================================================
2. REDDIT POSTS
====================================================================
r/selfhosted (title): Self-hosted release-notes generator that hides
Dependabot/CI noise — single Python file, zero deps

Body: I got tired of changelog tools that dump PR titles, so I built one that
rewrites them into actual sentences users understand and filters out bot
commits. Single .py file, stdlib only, runs anywhere Python runs. Web UI has
a demo where you paste any GitHub repo and see generated notes instantly.
MIT licensed. Feedback welcome — especially on the rewriting rules.

r/opensource (title): I made an OSS release-notes generator (MIT) — looking
for contributors and feedback
Body: similar, plus: "good first issues" = improving rewrite_title() verb
mappings and categorization regexes. Tests are stdlib-only unittest style,
6 engine tests + 4 webapp tests, all runnable offline.

r/SideProject / r/imadeathing: shorter, casual tone, lead with the demo GIF
or screenshot of before/after output.

Reddit rules: no cross-posting the same text within days; engage comments for
the first hour; disclose you're the author (Reddit requires it).

====================================================================
3. PRODUCT HUNT KIT
====================================================================
Name: Release Notes AI
Tagline (<60 chars):
  A) Customer-friendly release notes, straight from your PRs
  B) Stop hand-writing release notes
  C) Your merged PRs, rewritten for humans
Description (~260 chars):
Release Notes AI turns merged GitHub pull requests into plain-language,
customer-facing release notes — filtering out Dependabot, CI, and internal
noise automatically. Self-hostable single-file app with a hosted What's New
page, JSON API, embeddable widget, and a GitHub Action. Free & MIT.

Maker comment:
Hi PH! I'm a solo dev who hated writing release notes twice (once for devs,
once for humans). This tool reads your merged PRs and writes the human
version. It's one Python file, zero dependencies, MIT licensed, and the
embeddable widget is something paid tools charge $49+/mo for. The free
self-hosted version is the whole product today; a hosted tier may come later.
Ask me anything!

Gallery (make these 5 images later):
 1. Before/after: raw PR title vs rewritten sentence (biggest text possible)
 2. The /demo screenshot showing psf/requests generating 8 clean notes
 3. The widget floating on a fake SaaS dashboard
 4. One-line architecture: "1 Python file · 0 dependencies · $0/mo"
 5. GitHub Action YAML snippet → "notes on every tag"

Topics: Developer Tools, Open Source, Productivity
Launch window: Tuesday-Thursday, 12:01 AM PT. First hour matters most;
have 2-3 friends ready but never buy upvotes (bannable).

Pricing field: Free (self-hosted). Paid tier listed only when it exists.

====================================================================
4. ONE-LINE DESCRIPTIONS (for directories/listings)
====================================================================
- Short (Twitter/X bio): Turns merged PRs into customer-friendly release
  notes. Single Python file, zero deps, MIT.
- Medium: Open-source release-notes generator that rewrites technical PR
  titles into plain language and hides bot/CI noise. Self-hostable web app +
  embeddable widget + GitHub Action.
- Long (npm/PyPI-style): See README intro paragraph.

====================================================================
5. PRE-LAUNCH CHECKLIST
====================================================================
[ ] Repo public on GitHub (blocked: needs gh auth)
[ ] Live demo deployed (Render free tier via render.yaml — needs account)
[ ] Demo GIF/screen recording (30s: paste repo -> notes appear -> widget click)
[ ] README badge/shields added once repo URL known
[ ] Set YOUR_GH_USER in .github/workflows/release-notes.yml to jasonlu2006
[ ] Domain or stable onrender.com URL chosen for all copy links above
[ ] Post Show HN between Tue-Thu, 7-9 AM ET
[ ] Reply to every HN comment within the first 3 hours
[ ] Wait 7+ days, then Product Hunt with traction numbers in gallery

Success metric from outreach-drafts.md still applies: 25+ qualified waitlist
signups in 2 weeks -> greenlight building the hosted Pro tier ($9/mo).
