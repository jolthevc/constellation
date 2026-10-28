# Property Operating System
A **property** is a media identity that might span several platform accounts (channels). It can be a fictional personality, faceless editorial brand, community page, illustrated series, live-action creator concept, or other distinct publisher.

## How to launch the first real property
1. Review `../strategy/north-star.md`, `../audiences/`, `../research/` and `../formats/`. Write a launch memo using `../strategy/portfolio-allocation.md`.
2. Create `PROP-001-<slug>/` by copying `_template/`. Keep PROP-001 stable as the ID. Do NOT treat this template as a live property.
3. Complete: `property.yaml`, `identity-bible.md`, `psychology.md`, `engagement-strategy.md`, `audience-strategy.md`, `content-strategy.md`, `production-guide.md`, `monetization.md`, `channels.yaml`.
4. Link only real audience/interest/format IDs; add proper research and record assumptions as hypotheses.
5. Record it in `registry.csv` (registry initially intentionally has no live rows).
6. Put each post in `content/CNT-YYYY-NNN/`. Use `content-brief.md` and the episode package template; include reference links, real asset URLs outside Git, publish metadata, quality review and a postmortem.
7. Follow `../operations/launch-checklist.md`, `../operations/creative-approval-gate.md` and `../performance/`.
8. Major identity shifts require an explicit decision log entry and owner approval.

## Invariants
- One property ID may map to many channel IDs.
- No unsupported fabricated creator biography, credentials, organic social activity or real-world experiences.
- Preserve stable voice, visual and editorial identity, but do not force a single content medium.
- An audience hypothesis is not a measured follower demographic.
- Private credentials and large generated media must not be committed to Git.
