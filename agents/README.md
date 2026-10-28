# Agent Operating System (Design Stage)
This directory defines tasks that may later become bounded agents. It does **not** mean any automation is running. The initial pilot is operated by a human and publishing/spend/account creation requires explicit approval.

## Core roles
- `roles/researcher.md`: audience / creator / platform evidence.
- `roles/portfolio-strategist.md`: whitespace and new property proposals.
- `roles/creative-director.md`: property identity, format selection and psychological grammar.
- `roles/content-producer.md`: scripts, visuals and production packages.
- `roles/quality-reviewer.md`: editorial, payoff, provenance and compliance.
- `roles/performance-analyst.md`: standardized metrics and lessons.

## Agent contract
For any task, specify input files and stable IDs, allowed read/write paths, tools, output artifacts, human approval checkpoints, evidence level, cost limits and failure conditions. Keep raw evidence distinct from interpretation. Never overwrite a core bible after one short-term performance result.

## Task modes
- Research-only: may inspect permitted public sources and propose new docs.
- Draft-only: may create staged content packages and analysis.
- Human-review: may propose changes, but not approve itself.
- External action: **disabled by default**, requires approved integration and action-level authorization.

## Shared workflow
Read `../AGENTS.md`, `../strategy/attention-retention-payoff-standard.md`, applicable property docs and `../operations/compliance.md`. Produce structured artifact with source links and confidence. Validate files. Request human decision before publishing, account changes, spending or major repositioning.

## Planned future technical architecture
A scheduler/orchestrator, durable queue, source/research retrieval, asset warehouse, performance APIs, tool-specific execution agents, central relational database, audit log, quality evaluator and approval queue. Do not build them before the pilot identifies actual bottlenecks.
