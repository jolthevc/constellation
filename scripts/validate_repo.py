#!/usr/bin/env python3
"""Validate Constellation's portable registries, YAML, links, and identifier references.

Run: python scripts/validate_repo.py
No network access and no write side effects.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import validate as schema_validate

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

CSV_CONTRACTS = {
    "audiences/segments/index.csv": {"segment_id", "slug", "status", "evidence_grade"},
    "audiences/interests/index.csv": {"interest_id", "slug", "status", "evidence_grade"},
    "formats/catalog.csv": {"format_id", "layer", "family", "name"},
    "psychology/hook-library.csv": {"hook_id", "family", "opening_pattern"},
    "properties/registry.csv": {"property_id", "slug", "name", "status", "property_path"},
    "graph/relationships.csv": {"edge_id", "from_id", "to_id", "claim_type"},
    "graph/coverage.csv": {"coverage_id", "channel_id", "metric_name", "metric_value"},
    "graph/overlap-evidence.csv": {"overlap_id", "channel_id_a", "channel_id_b", "methodology"},
    "graph/white-space.csv": {"opportunity_id", "audience_or_interest_id"},
    "performance/account-snapshots.csv": {"snapshot_id", "channel_id", "snapshot_date"},
    "performance/post-performance.csv": {"observation_id", "content_id", "channel_id", "snapshot_at"},
    "performance/experiments.csv": {"experiment_id", "hypothesis", "primary_metric"},
    "operations/editorial-calendar.csv": {"calendar_id", "property_id", "content_id"},
    "research/sources.csv": {"source_id", "url", "accessed_date", "claim_supported"},
    "research/opportunity-backlog.csv": {"opportunity_id", "concept", "status"},
    "properties/_template/ideas.csv": {"idea_id", "property_id", "status"},
}
ID_PATTERNS = {"SEG": r"SEG-\d{3,}", "INT": r"INT-\d{3,}", "FMT": r"FMT-\d{3,}", "HK": r"HK-\d{3,}", "PROP": r"PROP-\d{3,}"}


def error(where: str, message: str) -> None:
    ERRORS.append(f"{where}: {message}")


def read_csv(relative: str) -> list[dict[str, str]]:
    path = ROOT / relative
    if not path.is_file():
        error(relative, "missing CSV")
        return []
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            error(relative, "missing CSV headers")
            return []
        missing = CSV_CONTRACTS.get(relative, set()) - set(reader.fieldnames)
        if missing:
            error(relative, "missing headers " + ", ".join(sorted(missing)))
        rows = list(reader)
        for line, row in enumerate(rows, 2):
            if None in row:
                error(f"{relative}:{line}", "row has more fields than header")
        return rows


def validate_ids(rows: list[dict], field: str, prefix: str, path: str) -> set[str]:
    seen: set[str] = set()
    for idx, row in enumerate(rows, 2):
        value = (row.get(field) or "").strip()
        if not re.fullmatch(ID_PATTERNS[prefix], value):
            error(f"{path}:{idx}", f"invalid {field}: {value!r}")
        if value in seen:
            error(f"{path}:{idx}", f"duplicate {field}: {value!r}")
        seen.add(value)
    return seen


def main() -> int:
    rows = {name: read_csv(name) for name in CSV_CONTRACTS}
    segments = validate_ids(rows["audiences/segments/index.csv"], "segment_id", "SEG", "audiences/segments/index.csv")
    interests = validate_ids(rows["audiences/interests/index.csv"], "interest_id", "INT", "audiences/interests/index.csv")
    formats = validate_ids(rows["formats/catalog.csv"], "format_id", "FMT", "formats/catalog.csv")
    hooks = validate_ids(rows["psychology/hook-library.csv"], "hook_id", "HK", "psychology/hook-library.csv")
    properties = validate_ids(rows["properties/registry.csv"], "property_id", "PROP", "properties/registry.csv")

    for i, row in enumerate(rows["audiences/segments/index.csv"], 2):
        for ref in filter(None, (row.get("related_interest_ids") or "").split(";")):
            if ref not in interests:
                error(f"audiences/segments/index.csv:{i}", f"unknown interest: {ref}")
        profile = (row.get("profile_path") or "").strip()
        if profile and not (ROOT / profile).is_file():
            error(f"audiences/segments/index.csv:{i}", f"missing profile: {profile}")

    for i, row in enumerate(rows["audiences/interests/index.csv"], 2):
        profile = (row.get("profile_path") or "").strip()
        if profile and not (ROOT / profile).is_file():
            error(f"audiences/interests/index.csv:{i}", f"missing profile: {profile}")

    for i, row in enumerate(rows["properties/registry.csv"], 2):
        pid = row.get("property_id", "")
        folder = ROOT / (row.get("property_path") or "")
        if not folder.is_dir() or not (folder / "property.yaml").is_file():
            error(f"properties/registry.csv:{i}", f"missing property.yaml for {pid}")
        for field, allowed in [("primary_segment_ids", segments), ("interest_ids", interests), ("primary_format_ids", formats)]:
            for ref in filter(None, (row.get(field) or "").split(";")):
                if ref not in allowed:
                    error(f"properties/registry.csv:{i}", f"unresolved {field}: {ref}")

    for file in ROOT.rglob("*.yaml"):
        if any(part.startswith(".") for part in file.relative_to(ROOT).parts):
            continue
        try:
            with file.open(encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
            if file.name == "property.yaml":
                schema = json.loads((ROOT / "agents/schemas/property.schema.json").read_text())
                schema_validate(data, schema)
                if "_template" not in file.parts and data["property_id"] not in properties:
                    error(str(file.relative_to(ROOT)), "property not listed in registry")
            if file.name == "publish.yaml":
                schema = json.loads((ROOT / "agents/schemas/publish.schema.json").read_text())
                schema_validate(data, schema)
        except Exception as exc:
            error(str(file.relative_to(ROOT)), f"YAML/schema invalid: {exc}")

    for item in (ROOT / "agents/schemas").glob("*.json"):
        try:
            json.loads(item.read_text(encoding="utf-8"))
        except Exception as exc:
            error(str(item.relative_to(ROOT)), f"JSON invalid: {exc}")

    for i, row in enumerate(rows["research/opportunity-backlog.csv"], 2):
        for ref in filter(None, (row.get("audience_segment_ids") or "").split(";")):
            if ref not in segments:
                error(f"research/opportunity-backlog.csv:{i}", f"unknown segment {ref}")
        for ref in filter(None, (row.get("interest_ids") or "").split(";")):
            if ref not in interests:
                error(f"research/opportunity-backlog.csv:{i}", f"unknown interest {ref}")
        for ref in filter(None, (row.get("format_candidates") or "").split(";")):
            if ref not in formats:
                error(f"research/opportunity-backlog.csv:{i}", f"unknown format {ref}")

    if ERRORS:
        print(f"FAILED: {len(ERRORS)} validation errors")
        for item in ERRORS:
            print(" - " + item)
        return 1
    print(f"PASS: {len(segments)} segments, {len(interests)} interests, "
          f"{len(formats)} formats, {len(hooks)} hooks, {len(properties)} real properties. "
          "YAML, JSON and CSV contracts checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
