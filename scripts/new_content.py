#!/usr/bin/env python3
"""Create a new content package for an existing registered property.

Example: python scripts/new_content.py --property PROP-001
Never publishes externally; only writes local draft files.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import shutil
from pathlib import Path

import yaml


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--property", required=True, help="e.g., PROP-001")
    parser.add_argument("--year", type=int, default=dt.datetime.now(dt.timezone.utc).year)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    if not re.fullmatch(r"PROP-\d{3,}", args.property):
        parser.error("property ID must be PROP-###")
    root = args.root.resolve()
    registry_path = root / "properties/registry.csv"
    if not registry_path.is_file():
        parser.error("property registry missing")

    with registry_path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    matches = [x for x in rows if x["property_id"] == args.property]
    if len(matches) != 1:
        parser.error("property must be registered exactly once")
    prop_dir = root / matches[0]["property_path"]
    if not (prop_dir / "property.yaml").is_file():
        parser.error("property metadata missing")

    existing = []
    for p in (root / "properties").glob("PROP-*/content/CNT-*"):
        m = re.fullmatch(r"CNT-(\d{4})-(\d+)", p.name)
        if m and int(m.group(1)) == args.year:
            existing.append(int(m.group(2)))
    content_id = f"CNT-{args.year}-{max(existing, default=0)+1:03d}"
    template = root / "properties/_template/content/_episode-template"
    dest = prop_dir / "content" / content_id
    if dest.exists():
        parser.error("content target already exists")
    shutil.copytree(template, dest)
    pub_path = dest / "publish.yaml"
    meta = yaml.safe_load(pub_path.read_text(encoding="utf-8"))
    meta.update({"content_id": content_id, "property_id": args.property, "status": "draft"})
    pub_path.write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True), encoding="utf-8")

    brief_template = root / "properties/_template/content-brief.md"
    brief = brief_template.read_text(encoding="utf-8")
    brief = brief.replace("Content ID:", f"Content ID: {content_id}", 1)
    brief = brief.replace("Property ID:", f"Property ID: {args.property}", 1)
    (dest / "brief.md").write_text(brief, encoding="utf-8")
    (dest / "script.md").write_text(f"# Script / Narrative — {content_id}\n\n## Opening\n\n## Main progression\n\n## Payoff\n\n## Factual sources\n", encoding="utf-8")
    (dest / "production.md").write_text(f"# Production — {content_id}\n\n## Shots and assets\n\n## Voice and edit instructions\n\n## Rights and disclosures\n", encoding="utf-8")
    (dest / "review.md").write_text(f"# Review — {content_id}\n\n## Quality gate\n\n## Actual performance (only after publishing)\n\n## Learning and next test\n", encoding="utf-8")
    print(f"Created {content_id} for {args.property} at {dest.relative_to(root)} (DRAFT)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
