#!/usr/bin/env python3
"""Verify the integrity of a public AlgoSphere documentation export.

This program uses only Python's standard library. It has no network, trading,
exchange, wallet, Telegram or private-project dependency.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path


EXPECTED_COLUMNS = ("public_report_id", "category", "record_date_utc", "status", "sha256")
ALLOWED_CATEGORIES = {"BUILD", "DELIVERY", "QA", "TEST", "OTHER"}
ALLOWED_STATUSES = {"REGISTERED", "HASH_NOT_PUBLISHED"}
HASH_RE = re.compile(r"^[0-9a-f]{64}$", re.I)
MANIFEST_RE = re.compile(r"^\| `([^`]+)` \| [^|]+ \| `([0-9a-f]{64})` \|$", re.I)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def manifest_entries(root: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    manifest = root / "evidence" / "EXPORT_CONTENTS.md"
    if not manifest.is_file():
        return {}, ["FAIL: EXPORT_CONTENTS.md is missing"]
    entries: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        match = MANIFEST_RE.match(line)
        if not match:
            continue
        relative, digest = match.groups()
        if relative == "EXPORT_CONTENTS.md":
            errors.append("FAIL: self-referential manifest entry must be omitted")
        elif relative in entries:
            errors.append(f"FAIL: duplicate manifest entry: {relative}")
        else:
            entries[relative] = digest.lower()
    if not entries:
        errors.append("FAIL: no SHA-256 manifest entries found")
    return entries, errors


def verify_register(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "evidence" / "REPORTS_PUBLIC_REGISTER.csv"
    if not path.is_file():
        return ["FAIL: REPORTS_PUBLIC_REGISTER.csv is missing"]
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != EXPECTED_COLUMNS:
            return ["FAIL: REPORTS_PUBLIC_REGISTER.csv schema does not match the public schema"]
        rows = list(reader)
    ids: set[str] = set()
    for index, row in enumerate(rows, 1):
        report_id = row["public_report_id"]
        if not re.fullmatch(r"R\d{5}", report_id or ""):
            errors.append(f"FAIL: row {index} has an invalid neutral ID")
        if report_id in ids:
            errors.append(f"FAIL: duplicate neutral ID: {report_id}")
        ids.add(report_id)
        if row["category"] not in ALLOWED_CATEGORIES:
            errors.append(f"FAIL: row {index} has an unsupported category")
        status = row["status"]
        if status not in ALLOWED_STATUSES:
            errors.append(f"FAIL: row {index} has an unsupported status")
        digest = row["sha256"]
        if status == "REGISTERED" and not HASH_RE.fullmatch(digest or ""):
            errors.append(f"FAIL: row {index} must have a SHA-256 value")
        if status == "HASH_NOT_PUBLISHED" and digest:
            errors.append(f"FAIL: row {index} publishes a hash despite HASH_NOT_PUBLISHED")
    evidence = root / "evidence" / "EVIDENCE_SUMMARY.md"
    if evidence.is_file():
        match = re.search(r"Current sanitised register count: `(\d+)`", evidence.read_text(encoding="utf-8"))
        if match and int(match.group(1)) != len(rows):
            errors.append("FAIL: published evidence count does not match the register row count")
    return errors


def verify(root: Path) -> list[str]:
    errors: list[str] = []
    entries, manifest_errors = manifest_entries(root)
    errors.extend(manifest_errors)
    for relative, expected in entries.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"FAIL: manifest file is missing: {relative}")
        elif sha256(path) != expected:
            errors.append(f"FAIL: SHA-256 mismatch: {relative}")
    errors.extend(verify_register(root))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a public AlgoSphere documentation export.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="public repository or export directory")
    args = parser.parse_args()
    errors = verify(args.root.resolve())
    if errors:
        print("FAIL: public export verification failed")
        print("\n".join(errors))
        return 1
    print("PASS: SHA-256 manifest, report-register schema, neutral IDs, categories, statuses and published row count verified.")
    print("PASS: EXPORT_CONTENTS.md is treated as self-referential and is not hashed by this verifier.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
