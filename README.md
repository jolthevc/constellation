# Constellation

**An AI-native media portfolio and the operating foundation for a broad, credible audience distribution graph.**

The aim is to build differentiated properties, including AI characters, faceless editorial brands, animated publishers, fictional formats and other media forms, that collectively earn relevant attention across many communities. Start with one manually operated property; retain the architecture to scale research, creative learning, measurement and eventually bounded automation.

**Current state, 2026-10-28:** Documentation, 149-component format taxonomy, hook/payoff frameworks, 68 candidate audience contexts, 147 candidate interest communities, 30 interest-to-commerce hypotheses, property/content templates, graph/metric schemas, local bootstrap scripts, research, operations and agent instructions are built. **No real property has been selected or launched in this repository. No publishing automation is active.** Audience profiles and opportunities are candidates, not validated market claims.

## October 2026 audience and creative evidence enrichment

Start with the [research synthesis](research/2026-evidence-synthesis.md), [source-bound evidence points](research/datasets/evidence-points-2026.csv), [Pew US demographic adoption table](research/datasets/platform-adoption-us-2026.csv), [researched cohort interpretation](audiences/researched-cohorts-2026.md), [format study](formats/researched-performance-2026.md), and [property research priorities](research/2026-property-opportunity-priorities.md).

The intelligence layer now includes 8 research-stage segment profiles, 10 research-stage interest profiles and 15 macro-evidence format deep dives. These are NOT 68 fully researched audiences, 147 verified interest markets or 149 performance-validated formats. The [creator forensic audit](research/format-and-creator-audit-plan.md) and [open questions](research/2026-open-questions.csv) remain before creator-specific claims.

## Start in five minutes

1. Read the [mission](strategy/north-star.md), [creative constitution](strategy/operating-principles.md) and [technical architecture](architecture.md).
2. Explore [audience hypotheses](audiences/README.md) and [segmentation design](audiences/segmentation-design.md), [formats](formats/README.md), [psychology](psychology/framework.md), [36 hook families](psychology/hook-library.csv), and the [attention-to-payoff standard](strategy/attention-retention-payoff-standard.md).
3. Choose a **real first pilot** using [portfolio allocation questions](strategy/portfolio-allocation.md) and [research protocol](research/README.md). Do not assume the seed candidates have validated demand.
4. Create its folder: `python scripts/new_property.py --name "Working Name" --slug working-name`. Complete the identity, audience psychology, property-specific [engagement strategy](properties/_template/engagement-strategy.md), format, production and commercial templates.
5. Create content drafts: `python scripts/new_content.py --property PROP-001`. Use the per-content [brief](properties/_template/content-brief.md), [creative approval gate](operations/creative-approval-gate.md), manual publishing process, and [engagement tests](performance/engagement-testing.md).
6. Record actual snapshots and learnings, rather than inventing future metrics or claims.
7. Run `python scripts/validate_repo.py` to check basic CSV/YAML/JSON contracts. Install `pip install -r requirements-dev.txt` first.

## Repository map

| Directory | Responsibility | Key link |
| --- | --- | --- |
| `strategy/` | North star, business model, operating principles, roadmap and allocation | [North star](strategy/north-star.md) |
| `audiences/` | Reusable SEG and INT research, psychology and commercial adjacency | [Audience guide](audiences/README.md) |
| `formats/` | 149 modular formats: presentation, storytelling, visuals, engagement and surfaces | [Format guide](formats/README.md) |
| `psychology/` | Viewer motivations, hooks, retention, satisfaction, following, sharing and commerce | [Framework](psychology/framework.md) |
| `research/` | Dated sourced observations, competitors, trends and opportunity backlog | [Research guide](research/README.md) |
| `properties/` | Distinct property bibles, accounts and content production packages | [Property guide](properties/README.md) |
| `graph/` | Portfolio relationships, coverage, overlap evidence and white space | [Graph model](graph/model.md) |
| `performance/` | Platform-native measurement, experiments and portfolio reviews | [Metrics dictionary](performance/metric-definitions.md) |
| `operations/` | Manual editorial cadence, permissions, quality, compliance and release | [Playbook](operations/operating-playbook.md) |
| `agents/` | Future role contracts, bounded workflows, evaluations and schemas | [Agent guide](agents/README.md) |
| `.claude/skills/` | Reusable Claude Code research, property, content and analysis workflows | [Skills](.claude/skills/research-audience/SKILL.md) |
| `scripts/` | Create a property/content package and validate local data | [Commands](scripts/README.md) |

## Non-negotiables

**Quality:** Every post has an appropriate scroll-stop, meaningful progression, actual payoff, and a natural reason for the viewer to respond or return. No uniform clickbait, gimmick or mandatory CTA.

**Trust:** Synthetic media must be represented honestly; no fake encounters, testimonials, experiences, sponsored endorsements or engagement. Source claims and rights, and obey current platform disclosures.

**Portfolio:** Properties don't have to be million-follower accounts. Measure incremental audience coverage with evidence, not the sum of account follower totals.

**Operations:** No background autonomous posting, spend or external account creation. Human approval is required at pilot stage. Media assets, secrets and detailed analytics belong in controlled storage, not the Git repository.

## Contributors and agents

Read [AGENTS.md](AGENTS.md) or [CLAUDE.md](CLAUDE.md). All strategic, audience and creative claims should distinguish hypothesis from sourced observation and internal tests. Record date/source and precise limitations. New account launch and identity changes require an approved decision.

**Next real milestone:** choose and launch the first pilot property, then replace assumptions with evidence from actual output, watch behavior, authentic interactions and production costs.
