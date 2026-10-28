#!/usr/bin/env python3
"""Create an unapproved property from the canonical template.

Example: python scripts/new_property.py --name "A Working Title" --slug a-working-title
No accounts or media are created. This only writes local repository files.
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
    parser.add_argument("--name", required=True)
    parser.add_argument("--slug", required=True, help="lowercase letters/numbers with hyphens")
    parser.add_argument("--owner", default="operator")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        parser.error("slug must be lower-case a-z, digits and internal hyphens")
    root = args.root.resolve()
    props = root / "properties"
    template = props / "_template"
    registry_path = props / "registry.csv"
    if not template.is_dir() or not registry_path.is_file():
        parser.error("property templates or registry not found")

    with registry_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = reader.fieldnames or []
        rows = list(reader)
    if not fields or "property_id" not in fields or "property_path" not in fields:
        parser.error("registry has incompatible fields")
    if any(x["slug"] == args.slug for x in rows):
        parser.error("slug already registered")

    existing = [int(m.group(1)) for p in props.iterdir() if p.is_dir()
                if (m := re.match(r"PROP-(\d+)-", p.name))]
    existing += [int(x["property_id"].split("-")[1]) for x in rows
                 if re.fullmatch(r"PROP-\d+", x.get("property_id", ""))]
    n = max(existing, default=0) + 1
    pid = f"PROP-{n:03d}"
    dest = props / f"{pid}-{args.slug}"
    if dest.exists():
        parser.error("target folder already exists")
    shutil.copytree(template, dest)

    for path in dest.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".csv", ".yaml", ".json"}:
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("PROP-XXX", pid), encoding="utf-8")

    prop_path = dest / "property.yaml"
    record = yaml.safe_load(prop_path.read_text(encoding="utf-8"))
    record.update({
        "property_id": pid,
        "name": args.name,
        "slug": args.slug,
        "owner": args.owner,
        "status": "proposed",
        "created_at": dt.datetime.now(dt.timezone.utc).date().isoformat(),
        "approval": {
            "human_launch_approved": False,
            "human_publish_approval_required": True,
            "autonomous_publish_allowed": False,
            "autonomous_spend_allowed": False,
        },
    })
    prop_path.write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True), encoding="utf-8")

    row = dict.fromkeys(fields, "")
    row.update({
        "property_id": pid,
        "slug": args.slug,
        "name": args.name,
        "property_type": "undecided",
        "status": "proposed",
        "owner": args.owner,
        "created_at": record["created_at"],
        "property_path": str(dest.relative_to(root)),
    })
    rows.append(row)
    with registry_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Created {pid} at {dest.relative_to(root)} (UNAPPROVED)")
    print("Next: complete the identity, psychology and engagement strategy, then seek human launch approval.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
