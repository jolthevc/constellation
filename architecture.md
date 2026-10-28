# Constellation Technical Architecture (Manual-First)
Version 1.0 | 2026-10-28

## Current stage: a knowledge-and-workflow repository
GitHub is the source of truth for strategy, taxonomies, creative guidelines, research summaries, property bibles, editorial templates, approvals, schemas and scripts. The system is **not** operating a network autonomously and does not contain platform credentials or scheduled publishing agents.

### Source and output flow
```text
Public research / official platform guidance / real examples
    -> research/ (sources, evidence and opportunities)
    -> audiences/ + formats/ + psychology/ (shared reusable intelligence)
    -> strategy/ + graph/ (portfolio opportunities)
    -> properties/PROP-... (approved distinct identity, audience, content and monetization)
    -> individual CNT package (hook -> progression -> payoff -> publish review)
    -> manual platform publication (human-approved)
    -> performance/ (platform definitions, snapshots, tests)
    -> property learnings / validated shared knowledge / graph evidence
```

## Key structural invariants
- Properties and their platform channels are different entities. IDs are stable; display names and handles can change.
- All audience and interest associations are many-to-many and carry evidence grade. Do not store individual-level covert social identities.
- Engagement tactics are property-specific applications of a shared evidence-aware library, not mandatory scripts.
- Research and behavior claims carry URL, date, evidence level and caveat. Experiments remain separate from assumed causal facts.
- A content package includes rights, disclosures, deliberate payoff, human approval record and measurable post outcomes.
- GitHub changes to strategy are versioned and reviewable. Agents cannot silently rewrite canonical identity docs.

## Components already implemented
Markdown operating documents, YAML/CSV taxonomies and registries, reusable creative briefs, basic bootstrap scripts and contract validation with CI.
No API keys, platform analytics ingestion, automated content generator, job queue, scheduling or publishing integration exists yet.

## Future system, once supported by evidence
- Source fetchers with rate limits and provenance; structured research extraction.
- Durable orchestrator/queue with agent roles, dependency and retry management.
- Separate object storage for media and audio with versioned asset manifests and licenses.
- Relational database for property/channel/content/metric/event records. Normalized graph edges can live there initially.
- Authorized platform analytics connectors and compliant publishing tools. Explicit review and approval states.
- Creative evaluators comparing a property's actual quality with human-graded examples, not imagined viral probabilities.
- Experiment manager and portfolio reporting, including uncertain audience overlap and incremental reach.
- Human audit dashboard for content, budgets, disclosures, identity edits and external actions.

## Suggested build order
1. Complete one real property, publish a repeatable series and learn actual editing/asset bottlenecks.
2. Add scripts/templates for the specific format that succeeds (Remotion for programmatic graphics, editing orchestration, image/voice systems as appropriate).
3. Add read-only analytic ingestion, if permissions and volume justify it.
4. Add an internal job queue and approval state machine.
5. Add bounded content production assistance.
6. Add authorized publication only when real workflows, platform terms, support and reliable evaluation justify it.
7. Optimize allocation with coverage evidence rather than speculative graph values.

## Avoid premature complexity
No microservices, proprietary graph database, hundreds of separate agents, custom CMS or brittle multi-platform publishing bots without proof they're needed. Documents plus portable IDs create a clean bridge to later architecture.

## Governance
Use `AGENTS.md`, `strategy/operating-principles.md`, `operations/compliance.md`, `operations/assets-and-credentials.md` and `agents/README.md`. External actions always require appropriate approval and permission. This repo is not a secret store.
