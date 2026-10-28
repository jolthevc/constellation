# Local Bootstrap Commands
These scripts only create/edit local tracked files. They never call a social platform API, publish media, create accounts, spend money or run in the background.

Install Python 3.11+ and `pip install -r requirements-dev.txt`.

## Check the repository
```bash
python scripts/validate_repo.py
```

## Create an unapproved property
```bash
python scripts/new_property.py --name "Working Name" --slug working-name --owner operator
```
This allocates a stable PROP ID, copies the canonical template, and writes an entry to `properties/registry.csv`. Before creating a real social account, fill in the bibles, research, source evidence, content pillars and launch approval.

## Create a draft content package
```bash
python scripts/new_content.py --property PROP-001
```
It allocates a unique CNT ID, creates brief/script/production/publish/review files, and marks the work draft. Complete the brief's opening/payoff contract and quality checks before external posting. Do not commit or upload raw large media.

## Validation caveat
This lightweight validation checks contract structure and YAML/CSV integrity, not creative truth, full rights compliance or whether an audience hypothesis is correct. Human review remains required.
