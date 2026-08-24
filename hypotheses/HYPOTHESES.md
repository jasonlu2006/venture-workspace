# Hypothesis Portfolio

Scored 2026-08-22. Scale 1-5 (see OPERATING.md). Higher avg = stronger.

## LEADER — MVP BUILT, TESTED, WIDGET ADDED (2026-08-22)
### H3 — AI customer-facing release-notes / changelog generator
(See full scoring above.) Status: MVP + web app + embeddable widget built.
- Code: products/release-notes-ai/ (releasenotes.py engine, webapp.py, widget.js)
- Tests: engine 6/6, webapp 4/4. Live demo on psf/requests works.
- Features: fetch PRs, categorize, rewrite, HIDE dependabot/CI noise,
  hosted page, JSON API, embeddable widget (NEW), Stripe Checkout path.
- Deploy-ready: Dockerfile, render.yaml, fly.toml, Procfile, LICENSE, DEPLOY.md.
- git: committed locally (branch master). Push gated on owner GitHub auth.

COMPETITIVE INTEL (2026-08-22):
- Changerawr (Supernova3339/changerawr, r/selfhosted) is a DIRECT
  open-source self-hosted competitor — BUT it is a *manual* changelog CMS
  (you write the notes; it stores/shares them), Next.js + DB + secrets.
  Heavier to run, not automated.
- Our wedge vs Changerawr: AUTOMATIC generation from merged PRs (zero writing)
  + single-file stdlib app (no Node/DB/compose) + drop-in widget.
- Incumbents (LaunchNotes/Beamer/Headway) charge $19-249/mo; the embeddable
  widget is something they monetize — we give it free/self-host.
- semantic-release/release-notes-generator (367★) confirms dev-facing-only gap.

MOAT STRATEGY (recurring value + defensibility):
1. Automation (generate from PRs) — Changerawr doesn't do this.
2. Embeddable widget (free) — incumbents charge for it.
3. Zero-dependency single file — lowest self-host friction vs Changerawr's stack.
4. Pro (hosted): scheduled auto-publish, multi-repo, email digests, version diff.

NEXT: validate demand (A — public posts), then push + deploy + optional Stripe.
All gated on owner credentials per DEPLOY.md / HUMAN_RELEASE_REVIEW_H3.md.

## WATCH
### H6 — AI content repurposing (1 asset -> many formats)
Demand real, reachable, but saturated. Secondary. avg ~3.1.

## DEFER
### H7 — License/cert renewal tracking for niche trades
Sticky, real pain, tedious rules = moat, but hard to reach offline trades
and needs a rules DB. Defer until a reachable channel is found. avg ~3.4.

## KILLED (this round)
- H1 Vertical FSM for septic/grease/waste haulers — heavy build + hard to
  reach offline customers. avg ~2.9.
- H2 Single-location local review aggregator — crowded + API ToS friction. avg ~2.7.
- H4 Sales-tax for Etsy/Shopify resellers — regulated, crowded, infra-heavy. avg ~2.9.
- H5 AI meeting-notes/action extractor — saturated. avg ~2.6.

## Evidence anchors (2026-08-22)
- FSM market: USD 6.26B (2026), ~10% CAGR (Mordor Intelligence).
- Micro-SaaS "boring verticals" consensus: redwerk.com, bigideasdb.com,
  ideaproof.io all cite vertical workflow + integration + reporting gaps.
- Changelog tools gap: personabox.app "7 Best Changelog Automation Tools (2026)"
  — free tools produce raw PR markdown; no cheap customer-facing AI rewrite.
  Also corroborated by github-changelog-generator, git-cliff, release-please
  being dev-facing only.
