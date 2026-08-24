# READY-TO-PASTE POSTS — Release Notes AI
Prepared 2026-08-22. Copy everything from the code blocks below exactly.
Order: HN first → Reddit (next day) → X (same day as Reddit is fine).

Links used everywhere:
- Repo:  https://github.com/jasonlu2006/release-notes-ai
- Demo:  https://release-notes-ai.onrender.com
- Killer demo link: https://release-notes-ai.onrender.com/demo?repo=psf/requests

====================================================================
1. HACKER NEWS (post Tue-Thu, 7-9 AM ET)
====================================================================
Go to https://news.ycombinator.com/submit

TITLE (paste exactly):
Show HN: Release Notes AI – customer-facing release notes from merged PRs

URL:
https://github.com/jasonlu2006/release-notes-ai

(text field: leave EMPTY)

--- FIRST COMMENT (paste immediately after submitting) ---
Hi HN! I kept noticing that every "automated changelog" tool just dumps raw
PR titles ("fix: crash when uploading empty CSV file") and someone still has
to hand-write the customer version. Research backs this up — the FSE'25
SmartNote paper found devs view writing release notes as tedious and
conventional-commit tools fail on over half the projects they analyze.

So I built Release Notes AI. Three things it does differently:

1. Rewrites technical titles into plain-language sentences customers can
   read. "fix: crash when uploading empty CSV file" becomes "Fixed a crash
   when uploading an empty CSV file."

2. Hides internal noise by default. Dependabot bumps, pre-commit hooks, CI
   churn — none of it belongs in front of users. On psf/requests it turned
   25 merged PRs into 8 clean notes.

3. It's one Python file with zero dependencies. No Node, no database, no
   docker-compose. `python3 webapp.py` gives you a hosted What's New page,
   a JSON API, and an embeddable widget. There's also a GitHub Action so
   notes generate automatically on every tag.

Try it live (no signup) — paste any repo:
https://release-notes-ai.onrender.com/demo?repo=psf/requests

Repo (MIT): https://github.com/jasonlu2006/release-notes-ai

The rewriting is heuristic-based right now (works offline, costs nothing),
with an optional LLM mode if you set OPENAI_API_KEY. Roast my rewriter —
what's the ugliest PR title in your repo? I'll add it to the test cases.
--- END FIRST COMMENT ---

--- REPLY TEMPLATES (keep these handy) ---
Q: "How is this different from git-cliff / release-please / semantic-release?"
A: "Those emit raw dev-facing markdown from commit messages — great for
contributors, not for users. This produces customer-facing prose, filters
bot/CI noise, and serves an embeddable widget. They solve changelog-for-devs;
this solves changelog-for-users."

Q: "The rewrites are too basic / regex won't scale"
A: "Fair — heuristics are the zero-cost offline baseline, and there's an LLM
upgrade path via OPENAI_API_KEY. What does the worst PR title in your repo
look like? Genuinely want to add gnarly cases to the test suite."

Q: "Why not just use GitHub's auto-generated release notes?"
A: "GitHub's are PR-title soup — same raw titles, no rewriting, no noise
filtering. This is the layer that makes them readable for customers."

Q: "Where does the hosted version / pricing come in?"
A: "Self-hosted stays free forever (MIT). If people want it, I'll add a
hosted tier around $9/mo — scheduled auto-publish, email digests, custom
domains. Building it only if there's real demand."
--- END REPLY TEMPLATES ---

====================================================================
2. REDDIT r/selfhosted (post NEXT DAY, morning US)
====================================================================
TITLE:
Self-hosted release-notes generator that hides Dependabot/CI noise — single Python file, zero deps

BODY (text post):
I got tired of changelog tools that just dump raw PR titles, so I built one
that rewrites them into actual sentences users understand and filters out
bot commits by default.

What it does:
- Point it at any GitHub repo, it pulls merged PRs since the last release
- Rewrites "fix: crash on empty CSV upload" → "Fixed a crash when uploading
  an empty CSV file"
- Auto-sorts into Features / Fixes / Performance / Docs
- Dependabot, renovate, pre-commit and CI churn are hidden automatically
  (on psf/requests: 25 PRs in, 8 useful notes out)
- Serves a "What's New" page + JSON API + embeddable widget
- GitHub Action included so notes generate on every tag

Why another changelog tool: everything existing is either dev-facing
(git-cliff, release-please — raw titles) or a $49/mo SaaS (Beamer, Headway,
LaunchNotes). This is the free self-hosted middle ground.

Tech: single Python file, standard library only, zero dependencies. Runs
with `python3 webapp.py` — no pip install, no Docker required (though a
Dockerfile is included).

Try the live demo (no signup): https://release-notes-ai.onrender.com/demo?repo=psf/requests
GitHub (MIT): https://github.com/jasonlu2006/release-notes-ai

Feedback welcome — especially on the rewriting rules. What's the worst PR
title in your repos?

====================================================================
3. REDDIT r/opensource (post 2-3 days after r/selfhosted)
====================================================================
TITLE:
I made an MIT-licensed release-notes generator (single Python file, zero deps) — looking for feedback and contributors

BODY:
Hi all — I built Release Notes AI: it turns merged GitHub PRs into
customer-facing release notes, hiding Dependabot/CI noise automatically.

The problem: devs hate writing release notes (there's actual research on
this — FSE'25 SmartNote paper), and existing automation just dumps raw PR
titles that users can't understand.

What makes it interesting technically: the whole thing is ONE Python file
using only the standard library. No pip install. The rewriting engine is a
transparent heuristic system (~40 verb mappings, conventional-commit prefix
stripping, label-based categorization) with an optional LLM upgrade path.

Looking for:
1. Feedback on the rewrite quality — try your ugliest repo here:
   https://release-notes-ai.onrender.com/demo?repo=YOUR_REPO
2. Contributors: good-first-issues are improving rewrite_title() verb
   mappings and the categorization regexes. Tests are stdlib-only and run
   offline in seconds.
3. Star if useful: https://github.com/jasonlu2006/release-notes-ai

MIT licensed. Live demo: https://release-notes-ai.onrender.com

====================================================================
4. X / TWITTER (post same day as Reddit, afternoon)
====================================================================
POST 1 (the hook):
Most "automated changelogs" are just PR-title soup:

"fix: crash when uploading empty CSV file"

That's not a release note. That's a commit message.

So I built a free tool that turns this:

  fix(api): add webhook retries w/ exponential backoff
  chore(deps): bump astral-sh/ruff-pre-commit
  fix: crash when uploading empty CSV file

Into this:

  ✨ Added webhook retries with exponential backoff.
  🐛 Fixed a crash when uploading an empty CSV file.
  (Dependabot noise: hidden automatically)

🧵

POST 2:
It's ONE Python file. Zero dependencies. No Node, no database, no Docker
required.

  git clone → python3 webapp.py → done

MIT licensed, self-hostable, $0 forever.

POST 3:
Try it on any public repo right now, no signup:

https://release-notes-ai.onrender.com/demo?repo=psf/requests

That demo ran on psf/requests: 25 merged PRs → 8 clean customer notes.
Everything your users don't need to see (Dependabot, CI, pre-commit)?
Filtered automatically.

POST 4:
There's also a GitHub Action — drop one YAML file in your repo and
customer-facing release notes generate on every tag:

[attach screenshot of the workflow YAML or the generated notes]

POST 5:
GitHub (leave a ⭐ if useful):
https://github.com/jasonlu2006/release-notes-ai

Roast the rewriter — worst PR title in your repo gets added to the test
suite.

--- IMAGE TO ATTACH TO POST 1 ---
Screenshot the demo page showing BEFORE/AFTER, or use the /demo output for
psf/requests. One image doubles engagement.

====================================================================
5. r/SideProject (post ~1 week later, casual tone)
====================================================================
TITLE:
I built a tool that writes your release notes for you (free, open source)

BODY:
Every time I ship a feature I dread writing the "What's New" section.
Existing tools just list commit messages — useless for actual users.

So I spent a weekend building Release Notes AI:
- Reads your merged GitHub PRs
- Rewrites them into sentences humans understand
- Hides all the Dependabot/CI junk automatically
- Generates a hosted changelog page + embeddable widget for your app
- Free, open source (MIT), one Python file

Live demo (paste any repo, no signup):
https://release-notes-ai.onrender.com/demo?repo=psf/requests

GitHub: https://github.com/jasonlu2006/release-notes-ai

Would love feedback — especially brutal stuff about the note quality. What's
the scariest PR title you'd trust it with?

====================================================================
POSTING CHECKLIST (each platform)
====================================================================
[ ] HN: Tue-Thu 7-9 AM ET, first comment within 2 min, reply to all for 3 hrs
[ ] r/selfhosted: next morning, stay in comments 1 hr
[ ] X: afternoon, attach image to post 1, reply to every reply
[ ] r/opensource: 2-3 days later
[ ] r/SideProject: ~1 week later
[ ] Never post two platforms the same morning
[ ] Disclose you're the author everywhere (Reddit requires it, HN expects it)
[ ] Log every question you get — that's your FAQ and feature roadmap
