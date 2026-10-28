# Measurement and Learning
This folder holds manually entered or exported aggregate content/account metrics and experiment learnings. The CSVs start header-only until a real channel is launched.

## Data flow
1. Record real channel in `properties/<id>/channels.yaml` and property in registry.
2. Assign `CNT-YYYY-NNN` to every content item, `EXP-YYYY-NNN` when deliberately testing.
3. Log at least one standardized snapshot after publishing, preserving the native platform definitions and export timestamp.
4. Use `metric-definitions.md`; report null/missing for unavailable metrics, not zero.
5. Weekly: review comparable posts and the `engagement-testing.md` diagnosis. Monthly: synthesize per property and portfolio using review template.
6. Upgrade to database/API ingestion only after repeatability, volume and permissions justify the cost.

## Evidence and accuracy
- Never merge cross-platform views into a deduplicated unique person count without a real method.
- Never equate follows or likes with purchase behavior.
- Preserve raw source/export pointer, units, reporting window and paid vs organic distinctions.
- Retention spikes may reflect replays, confusion, or a rewatched scene. Qualitative review is required.
- Don't store identifiable follower data; cohort-level analytics only.
