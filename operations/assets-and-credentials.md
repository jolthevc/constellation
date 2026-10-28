# Asset, Credential and Data Handling
GitHub stores **control documents**, not the production warehouse.

## Do commit
Lightweight YAML/CSV/JSON/Markdown, published public URLs, permission-safe research summaries, identifiers, small test data and stable references to externally stored assets.

## Do not commit
Secrets, API keys, OAuth tokens, login credentials, private demographic analytics, customer emails, personal data, unlicensed third-party footage, raw published media libraries, 500MB+ binary generated files, or proprietary commercial contracts unless encrypted in a controlled repository and authorized.

## Proposed future storage
- Object storage for editable source files, final videos, voice assets and reference images with access control, retention and rights metadata.
- Secret manager for posting/API credentials, audited access, rotation and least privilege.
- Relational database for high-frequency performance logs, job queues, graph relationships and workflow state when scale justifies it.
- GitHub Actions / CI for validation only; no self-publishing without explicit approvals and supported integrations.

## Naming & provenance
`PROP-###/CHAN-###/CNT-YYYY-NNN/ASSET-###`. Keep link to source and license, date, provenance, synthetic disclosure status, version, approved voice/likeness consent and rights.

## First pilot
Use manual asset folder with well-defined manifest; keep paths in property production guide. Do not build a large media pipeline prematurely.
