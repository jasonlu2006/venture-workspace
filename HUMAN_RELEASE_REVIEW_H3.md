# HUMAN RELEASE REVIEW — Release Notes AI (H3)

STATUS: APPROVED BY OWNER (2026-08-22) — "go ahead with all of them".
Execution is in progress; final publish steps are gated on owner credentials
(GitHub auth, hosting account, Stripe key, social accounts) which the agent
does not possess. Build/deploy-readiness is COMPLETE and VERIFIED locally.

DETAIL: see DEPLOY.md (build & launch runbook) for the exact commands the
owner runs to finish each step.

====================================================================
1. WHAT WAS BUILT
====================================================================
Product: "Release Notes AI" — turns merged GitHub PRs into customer-friendly
release notes + a hosted "What's New" page.

Artifacts (all on local disk, no external deployment):
- Product code : C:/Users/jlaso/ventures/products/release-notes-ai/releasenotes.py
                 (Python stdlib only, 0 dependencies, ~$0 to run)
- Tests        : C:/Users/jlaso/ventures/products/release-notes-ai/tests.py  (6/6 pass)
- README       : C:/Users/jlaso/ventures/products/release-notes-ai/README.md
- Landing page : C:/Users/jlaso/ventures/validation/release-notes-ai/landing.py
                 (local fake-door waitlist; tested; writes waitlist.txt)
- Evidence     : C:/Users/jlaso/ventures/research/H3-evidence.md
                 C:/Users/jlaso/ventures/hypotheses/HYPOTHESES.md

Features delivered:
- Fetch merged PRs since last release (no token needed for light use)
- Auto-categorize (Features / Fixes / Performance / Docs)
- Rewrite technical titles into customer prose (heuristic, offline, free)
- HIDE internal noise (Dependabot / CI / pre-commit) — key differentiator
- Serve styled "What's New" page + JSON API + markdown output
- Optional LLM upgrade path (set OPENAI_API_KEY)

Verified working:
- Live run on psf/requests (public repo): 25 PRs -> 8 clean customer notes.
- HTTP server returned 200 with real rendered content + working JSON API.
- Landing page: GET 200, valid email POST 200 + thank-you, invalid 400,
  writes to waitlist.txt.

====================================================================
2. EVIDENCE FOR DEMAND (real, not assumed)
====================================================================
- Ask HN "How do you automate your release notes?" — devs confirm it's tedious,
  raw PR-title changelogs are "useless", and at least one built a custom script
  to avoid "PR-title soup". (news.ycombinator.com/item?id=46590623)
- FSE 2025 academic paper (SmartNote, arxiv 2505.17977v1): devs "hate creating
  release notes"; existing tools enforce rigid conventions and "fail for more
  than half the projects analysed."
- Competitor pricing confirms a gap in the cheap/self-hostable middle:
  Headway $19/mo, Beamer $49, LaunchNotes $249, etc. No $0-OPEX self-hostable
  option with customer-facing rewrite. (see H3-evidence.md for sources)

====================================================================
3. WHAT "RELEASE" WOULD MEAN (options requiring your decision)
====================================================================
The agent will NOT do any of the following without your explicit go-ahead:

A) PUBLIC VALIDATION: post the landing page / waitlist link to HN, Reddit
   (r/SaaS, r/opensource, r/selfhosted), Indie Hackers, or X to collect
   real signups. Currently the landing page is LOCAL ONLY (127.0.0.1).

B) OPEN-SOURCE RELEASE: push the code to a public GitHub repo.

C) MONETIZATION: stand up a hosted SaaS, add Stripe/payment, charge money,
   or run paid ads. (Currently $0 spent, no payment processor configured.)

D) DEPLOY: host the waitlist/landing on a public URL.

====================================================================
4. RECOMMENDED NEXT STEP (agent's recommendation, not executed)
====================================================================
Recommended: option (A) first — cheapest validation, no code monetization.
Post the landing-page concept as a "building in public" / Ask HN style post to
measure genuine signup interest before investing in hosted infra. If waitlist
signups exceed a threshold (e.g. 25+ qualified dev emails in 2 weeks), proceed
to (B)/(C) with a minimal hosted tier.

Open risk to flag: the heuristic rewriter is easy to copy (thin moat). A real
moat needs either (1) LLM-quality rewrite that clearly beats heuristics, or
(2) sticky workflow features (scheduled auto-publish, multi-repo, white-label
widget, email digests, version diffing). Recommend building the moat alongside
validation.

====================================================================
6. STATUS (as of 2026-08-22, after decision timeout)
====================================================================
- The human did NOT respond to the release-decision prompt.
- Per the mandate's hard rule, the agent did NOT cross any boundary
  (no public post, no GitHub push, no monetization, no public deploy).
- Within-boundary prep work done:
  * Enhanced local fake-door landing page to also capture "what tool do you
    use now?" (tab-separated in waitlist.txt) — still binds 127.0.0.1 only.
  * Wrote ready-to-post outreach drafts (HN / Reddit / IndieHackers / X) +
    explicit success metrics in:
    C:/Users/jlaso/ventures/validation/release-notes-ai/outreach-drafts.md
    These are LOCAL DRAFTS and have NOT been posted anywhere.
- State: PAUSED AT RELEASE GATE. Awaiting explicit human approval of A/B/C/D
  before any external action.

APPROVAL STILL REQUIRED for:
  [ ] A) Public validation posts   [ ] B) Open-source release
  [ ] C) Monetization              [ ] D) Public deploy
