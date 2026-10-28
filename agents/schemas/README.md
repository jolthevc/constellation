# Structured Data Contracts
JSON Schema here is for portable machine-readable data validation. Authoritative records remain YAML in property folders and CSV in shared indices. `scripts/validate_repo.py` checks basic required fields, CSV contracts, YAML parsing and cross-references; use JSON Schema-compatible tooling for stricter full-record validation when adding new workflows.

## Key contracts
- `property.schema.json`: stable property identity, classification, linked audiences/formats and agent permissions.
- `publish.schema.json`: individual content, approval and publication metadata.

Data contracts are designed for later database ingestion without imposing a database during pilot. Approval flags in repository text are not authorization tokens; real external actions require authenticated, user-approved permissions.
