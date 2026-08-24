# H3 — Release Notes AI : Evidence Log

## Demand / pain (primary sources)
- Ask HN "How do you automate your release notes?" (news.ycombinator.com/item?id=46590623)
  - Multiple devs: release notes are tedious; raw PR-title changelogs are useless
    ("I hate when projects just lazily list every pull request").
  - One dev built his own script specifically to avoid "PR-title soup".
- Academic: SmartNote, FSE 2025 (arxiv 2505.17977v1)
  - "Many developers ... perceive writing release notes as time-consuming and
   tedious; ... often neglected."
  - Existing tools (Conventional Changelog, semantic-release) enforce conventional
   commits and "fail for more than half the projects analysed."
  => validates the "no rigid convention, filter the noise" approach.

## Competition / pricing (2026-08)
- Free / dev-facing: release-please, git-cliff, github-changelog-generator,
  semantic-release — emit raw/PR-title markdown only, not customer-facing.
- Customer-changelog SaaS pricing (per month):
  - Headway: free tier, paid from $19/mo
  - Beamer: $49 (Starter, 5k MAU) / $99 / $249
  - LaunchNotes: from $249/mo (enterprise, demo-led)
  - ReleasePad ~$35/mo; Frill $25; Canny $79; AnnounceKit $79; ProductLift $19-29
  - Changelogfy $19; Worknotes $29
  => No cheap, self-hostable, $0-OPEX option in the middle. Wedge confirmed.

## Buildability
- MVP built (products/release-notes-ai/releasenotes.py), stdlib-only, 0 deps.
- Tests 6/6. Live pipeline run on psf/requests: 25 PRs -> 8 clean notes;
  server HTTP 200 with real content + JSON API.
- Validation landing page built (validation/release-notes-ai/landing.py),
  local fake-door waitlist, tested (200/400, writes waitlist.txt).

## Open risks (to address before/at release)
- Wedge defensibility is thin (heuristic rewriter is easy to copy). Need a real
  moat: scheduled auto-publish, multi-repo, white-label widget, email digests,
  version diffing, or an LLM-quality rewrite that beats heuristics.
- Monetization requires infra (hosting, email) not yet provisioned — gated.
- Distribution: devs reachable via HN/Reddit/GitHub but CAC unknown.
