# Constellation Graph Data Model
Version: 1 | Last updated: 2026-10-28
Status: conceptual schema; coverage and overlap metrics are unpopulated until observed.

## Node classes
PROP = portfolio property (`properties/registry.csv`)
CHAN = actual channel on TikTok / Instagram / YouTube / other, stored in property `channels.yaml`
SEG = audience segment (`audiences/segments/index.csv`)
INT = interest group (`audiences/interests/index.csv`)
FMT = content component (`formats/catalog.csv`)
HK = hook family (`psychology/hook-library.csv`)
COM = commercial category (`audiences/commercial-categories.yaml`)
CNT = actual content ID (`post-performance.csv` and property content package)

## Edge semantics
| From -> To | relationship | Meaning | Evidence |
| --- | --- | --- | --- |
| PROP -> CHAN | published_on | Official account relationship | Verified owner and account URL |
| PROP -> SEG | targets | Intended segment | Property strategy, hypothesis |
| PROP -> INT | covers_interest | Editorial relevance | Property strategy and content samples |
| PROP -> FMT/HK | uses | Selected creative structures | Property/content metadata |
| CHAN -> SEG | reaches | Aggregated actual audience reach, when platform reports it | Platform analytics with methodology |
| SEG -> INT | interested_in | Hypothesized or measured affinity | Research, survey or permitted analytics |
| PROP -> COM | commercially_relevant_to | Editorially suitable category, NOT purchasing propensity | Property monetization strategy |
| CHAN -> CHAN | overlaps_with | Deduplicated shared aggregate audience | Supported measured methodology only |

## Edge contract
`edge_id,from_id,to_id,relationship,claim_type,evidence_grade,evidence_source_id,confidence,observed_at,last_reviewed_at,notes`.
`claim_type` is hypothesis/observed/measured. A hypothesis should never silently become measured. `confidence` describes evidentiary confidence, not percent unique reach.

## Coverage table
At minimum: channel/property ID, target SEG or INT, metric, value, numerator/denominator semantics, reporting window, source, evidence quality, confidence and overlap assumptions. Empty numeric values until measured. Different platforms' reported views/reach definitions cannot be automatically combined.

## Overlap
- **Measured overlap** only when privacy-safe, platform-approved aggregate or experimental data supports it; record method and window.
- **Estimated overlap** may be scenario-modeled with documented assumptions and uncertainty ranges, never disguised as measurement.
- **Unknown overlap** is the default. Sum of followers is only a gross account-count total, not unique persons.
- Maintain identity privacy; no scraping personal follower lists or sensitive traits to build a shadow identity graph.

## White space
Opportunity derived from reach gap, verified audience demand, potential distinct creative strategy, content cost and commercial fit. Rank only after actual data and explicit assumptions.

## Future migration
Relational database (Postgres) plus normalized edge tables is likely sufficient initially. Introduce graph database only if traversal scale/complexity justifies it. Keep IDs portable and files importable.
