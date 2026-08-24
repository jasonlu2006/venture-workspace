# USER ACQUISITION PLAN — Release Notes AI
Written 2026-08-22. Product: free self-hosted tool, live demo, MIT.
Audience: developers who ship software and write (or skip) release notes.
Principle: go where devs already are; every channel should compound (SEO,
marketplaces, embeds all keep working after the initial push).

## PHASE 1 — LAUNCH SPIKE (this week)
1. Show HN (copy ready in LAUNCH_COPY.md) — Tue-Thu 7-9 AM ET
2. Same day: r/selfhosted + r/opensource posts (copy ready)
3. X/Twitter thread with before/after screenshot
4. Post launch: reply to everything for 3 hours, then daily for a week

## PHASE 2 — COMPOUNDING CHANNELS (weeks 2-6)

### A. GitHub ecosystem (highest intent audience)
- **Awesome-lists PRs**: add to awesome-selfhosted, awesome-changelogs,
  awesome-github-actions, awesome-devtools. One-time PRs, permanent backlinks.
- **GitHub Topics**: already tagged. Also create a "made-with-rna" topic badge
  users can put in their README (viral loop: every user's README advertises us).
- **Answer Stack Overflow / GitHub Discussions questions** about changelog
  automation with genuinely helpful answers that mention RNA where relevant.

### B. SEO pages (the demo engine becomes content)
The demo endpoint is an SEO machine. Build static-ish pages:
- `/demo/psf/requests`, `/demo/pallets/flask` ... auto-generated per popular
  repo (cache results). Each page targets "X release notes" searches.
- Blog-style guides (static HTML, no CMS needed):
  - "How to write release notes (with examples)" 
  - "Conventional Commits vs customer-facing changelogs"
  - "Best free changelog tools compared (2026)" — honest comparison incl. us
  These target commercial-intent keywords competitors rank for at $49/mo CAC.

### C. Integration marketplaces (borrowed distribution)
- GitHub Marketplace listing (free app first, paid later)
- VS Code extension idea: generate notes from staged commits (later)

### D. Widget network effect (built-in growth loop)
Every widget embedded in a product shows "Powered by Release Notes AI"
linking back. Users' customers = our prospects (SaaS teams see it inside
products they use). This is why the widget stays free forever.

### E. Dev communities (help-first, never spam)
- r/golang, r/rust, r/javascript etc.: only when genuinely on-topic
- Discord/Slack dev communities: answer changelog questions
- Indie Hackers: build-in-public MRR updates (these perform well)

## PHASE 3 — PARTNERSHIPS & OUTBOUND (month 2+, once Pro exists)
- CI/CD integrations: CircleCI orb, GitLab CI template — each is a channel
- Agency/devshop angle: agencies ship many client apps; offer agency plan
- Cold outreach to OSS projects with bad changelogs: "I generated better
  notes for your repo in 10 seconds, here's the link" (genuinely useful,
  personalized, not spammy — include their actual generated output)

## METRICS & TARGETS
| Metric | Month 1 | Month 3 |
|---|---|---|
| GitHub stars | 100 | 500 |
| Demo generations | 1,000 | 10,000 |
| Waitlist emails | 100 | 400 |
| Pro subscribers | 0 (not built) | 15 ($135 MRR) |
| SEO pages indexed | 5 | 30 |

## WHAT NOT TO DO
- No paid ads yet (CAC >> LTV at $0 revenue; revisit at 50+ customers)
- No spammy mass outreach (reputation risk kills OSS trust permanently)
- No fake accounts/engagement anywhere
- Don't launch on multiple platforms same-day (stagger: HN -> Reddit -> PH)
