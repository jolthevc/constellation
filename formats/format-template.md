# Format Research Record Template

```yaml
format_id: FMT-XXX
name:
layers: [presentation, story_engine]
family:
status: proposed # proposed | researched | tested | validated | retired
last_reviewed:
source_links: []
reference_posts: []
psychology_tags: []
supported_platforms: []
candidate_audiences: []
candidate_properties: []
production_methods: []
automation_feasibility: unknown # low | medium | high | unknown
rights_and_disclosure_review_required: true
owner:
```

## Format definition
What makes this recognizably distinct from adjacent formats? Include canonical opening, scene structure, narrative shape, pacing, sound, length and end state. Define what is *not* this format.

## Audience job and psychology
- Context: when does the viewer encounter this?
- Desired emotional / functional job:
- Attention mechanism and first seconds:
- Retention mechanism and how it changes over the piece:
- Satisfying payoff:
- Why someone would share or save:
- Why someone would follow the account:
- Relationship and credibility mechanism:
- Commerce fit, with trust boundaries:
- Alternative hypotheses that could explain success:
- Known risks / potentially harmful use:

## Verified and exploratory examples
| URL | Platform | Account | Date | Audience/niche | Observable hook | Outcome metric if public | Reliability |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

Do not make up metrics or imply that views prove a specific causal mechanism.

## Production grammar
Define shot sizes, framing, required real footage, synthetic assets, text overlays, music and VO style, editing rhythm, accessibility, sources, citations, and constraints.

## Economics and reproducibility
- Human production steps:
- Agent-assisted production steps:
- Blockers to full automation:
- Per-post cost/time estimates and assumptions:
- Quality floor and failure modes:
- Authenticity, intellectual property, brand safety and platform compliance:

## Experiments
- Hypothesis and predicted viewer behavior:
- Variables and controls:
- Audience, niche, platform, sample size and measurement window:
- Primary metric, secondary metrics, guardrails:
- Results and uncertainty:
- Decision: test further, adopt, modify, or retire:

## Required engagement-specific design
Link approved hook family IDs from `../psychology/hook-library.csv` and document:
- The exact first frame/opening (or first slide/line), 3 alternate openings where worthwhile.
- The opening's honest viewer promise, first meaningful reward, and why it fits this audience/property.
- The beat-by-beat escalation, useful progression, re-hooks and optional rewatch bonus.
- The payoff family, location and test showing the opening promise is fulfilled.
- One primary desired viewer behavior (or none), natural/optional CTA, and what would feel manipulative.
- Primary hook/retention/payoff metric, comparator and uncertainty.

See `engagement-design.md` and `../strategy/attention-retention-payoff-standard.md`.
