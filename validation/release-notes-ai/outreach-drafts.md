# Release Notes AI — OUTREACH DRAFTS (NOT POSTED)

These are prepared, ready-to-publish drafts for the PUBLIC VALIDATION step
(option A in HUMAN_RELEASE_REVIEW_H3.md). They are LOCAL DRAFTS ONLY.
Nothing here has been posted. Posting requires explicit human approval.

====================================================================
SUCCESS METRICS (define BEFORE posting)
====================================================================
Primary: number of qualified waitlist signups (dev / maintainer email).
Thresholds for proceeding to open-source + hosted build:
  - 25+ signups in 2 weeks  -> BUILD hosted tier (option C)
  - 10-24                   -> iterate copy, extend validation
  - <10                     -> weak signal; revisit positioning or hypothesis
Secondary: which "current tool" answers appear (validates competitor gap).
Guardrail: no paid ads, no bots, no astroturfing. Organic only.

====================================================================
DRAFT 1 — Hacker News (Ask HN)
====================================================================
Title: Ask HN: How do you write customer-facing release notes without the
PR-title soup?

Body:
We just built a small tool that pulls merged GitHub PRs since your last
release and turns them into plain-language, customer-facing release notes —
and, importantly, hides the Dependabot/CI/pre-commit noise by default.

The trigger was that thread a while back where people said raw PR-title
changelogs are useless, and the FSE'25 paper (SmartNote) finding devs "hate
creating release notes" while tools like Conventional Changelog fail on >50%
of projects.

It's a single self-hostable Python file, $0 to run. Curious:
- How are you doing release notes today (hand-written? release-please?
  Headway/Beamer/LaunchNotes? nothing?)?
- What would make a tool like this actually worth adopting for you?

(Not a launch — just validating. Happy to share the repo with anyone
interested in kicking the tires.)

====================================================================
DRAFT 2 — Reddit r/selfhosted (text post)
====================================================================
Title: Self-hosted release-notes generator that hides Dependabot noise

I got annoyed that every "automated changelog" just dumps PR titles, so I
built a tiny self-hosted tool: point it at a GitHub repo, it pulls merged PRs
since the last release, rewrites them into customer-friendly notes, and drops
the internal CI/dependabot churn. Outputs a "What's New" page + JSON.

Single Python file, no dependencies, runs locally. Looking for testers /
feedback on what would make it useful enough to actually adopt. What do you
use for release notes today?

====================================================================
DRAFT 3 — Indie Hackers (building-in-public)
====================================================================
Title: I built a free, self-hostable alternative to $49/mo release-note tools

Release-note SaaS starts at ~$19-249/mo. A lot of indie devs just want the
"80% draft" of customer-friendly notes without a subscription. So I built a
single-file, $0-OPEX tool that turns merged PRs into clean release notes and
hides internal noise.

Validating demand before I build the hosted tier. If you ship software, what's
your current release-notes workflow, and would a free self-hostable version
replace it?

====================================================================
DRAFT 4 — X / Twitter (thread hook)
====================================================================
Most "automated changelogs" are just PR-title soup.

So I built a tiny self-hostable tool that turns merged GitHub PRs into
customer-friendly release notes — and hides Dependabot/CI noise by default.

$0 to run, single Python file. Validating demand. What's your release-notes
workflow today?

====================================================================
WHERE THE WAITLIST LIVES (local only, until approved)
====================================================================
Landing page: validation/release-notes-ai/landing.py (binds 127.0.0.1)
Run: python3 landing.py --port 8000
Waitlist output: validation/release-notes-ai/waitlist.txt

To go public (requires approval): deploy landing.py to a public host and
post the drafts above. Do NOT do this without human sign-off.
