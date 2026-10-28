# Claude Code Operating Context: Constellation

**Read [AGENTS.md](AGENTS.md) before working.** [README.md](README.md) is the navigation guide; [architecture.md](architecture.md) describes the current manual system and future integration boundaries. This repo is an AI-native audience/media network, not an auto-publishing service yet.

## Mandatory contextual reading
- New audience research: `audiences/README.md`, `research/README.md`, `psychology/framework.md`
- Property concept: `strategy/north-star.md`, `strategy/portfolio-allocation.md`, `properties/README.md`, `properties/_template/`
- Any creative/script work: target property identity + psychology + engagement strategy, `strategy/attention-retention-payoff-standard.md`, `psychology/hook-library.csv`, `psychology/retention-and-payoff-playbook.md`, `formats/engagement-design.md`, `operations/creative-approval-gate.md`
- Any analytics: `performance/metric-definitions.md`, `performance/engagement-testing.md`

## Creative rule
Build genuinely engaging original media. Every piece must intentionally earn attention, hold the viewer by progressing toward a real payoff, deliver that payoff, and create an authentic optional reason to share/save/comment/follow/return. Design hooks for **this property**, not generic sales language. Never fabricate creator experiences, fake street interviews, testimonials or supposedly genuine social behavior.

## Workflow
1. Review evidence and audience/identity context; propose a precise hypothesis.
2. Select presentation, story, visual treatment and surface (FMT IDs), plus hook family (HK ID).
3. Create a brief with first-frame treatment and multiple original hook options where useful.
4. Develop and check narrative progression, payoff, voice, factual claims, rights, disclosure, production method and costs.
5. Prepare reviewable materials, then human approves any actual publication. No automatic external action.
6. Record real metrics/learning and update reusable intelligence with source and date.
7. Run `python scripts/validate_repo.py` for repository changes.

## Claude skills
`/.claude/skills/research-audience/`, `design-property/`, `produce-content/`, `analyze-performance/` provide task-specific instructions. They complement, not override, AGENTS.md and compliance rules.

## Code conventions
Python 3.11+, standard library by default, PyYAML and jsonschema for validation. Keep generated artifacts deterministic, auditable and easy to inspect. Stable IDs; avoid needless infrastructure. No credentials or media blobs in version control. Distinguish all research hypotheses from internally measured performance.

## October 2026 research enrichment
Use `research/2026-evidence-synthesis.md`, `research/datasets/README.md`, `audiences/researched-cohorts-2026.md`, `formats/researched-performance-2026.md` and `research/2026-property-opportunity-priorities.md` to ground new opportunity ranking. Read existing profile/deep-dive files; do not claim unresearched catalog rows are validated. The next evidence requirement is `research/format-and-creator-audit-plan.md`, with real creator/post samples and our own measured content experiments. Inherit all original synthetic-media, privacy and human-approval safeguards.
