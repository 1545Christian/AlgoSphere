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
HASH_RE = re.compile(r"^[0-9a-f]{64}$")
MANIFEST_RE = re.compile(r"^\| `([^`]+)` \| (\d+) \| `([0-9a-f]{64})` \|$", re.I)
SELF_MANIFEST_RE = re.compile(r"^\| `(?:evidence/)?EXPORT_CONTENTS\.md` \| self \| intentionally omitted ", re.I)
MARKER_RE = re.compile(r"<!--\s*((?:HUMAN_TEXT|AUTO_VALUES)_(?:START|END)(?::[A-Z0-9_]+)?)\s*-->")
LOCAL_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
UPDATE_EN_RE = re.compile(r"^updates/(\d{4}-\d{2}-\d{2})-public-status\.md$")
UPDATE_DE_RE = re.compile(r"^updates/(\d{4}-\d{2}-\d{2})-public-status_DE\.md$")
SECRET_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN(?: [A-Z]+)? PRIVATE KEY-----", re.I),
    "credential_assignment": re.compile(
        r"(?:api[_-]?key|access[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-/+=]{8,}",
        re.I,
    ),
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "windows_path": re.compile(r"\b[A-Z]:[\\/]", re.I),
    "unc_path": re.compile(r"\\\\[^\\\s]+\\"),
    "object_dump": re.compile(r"\$\(@\{|System\.Object", re.I),
    "proprietary_metrics": re.compile(r"\bPnL\b|profit factor|open_positions|research_code_fingerprint", re.I),
}

BASE_EXPORT_MANIFEST_FILES = {
    "README.md",
    "README_DE.md",
    "CURRENT_STATUS.md",
    "SECURITY.md",
    "docs/progress/COMPLETED_WORK.md",
    "docs/progress/ROADMAP.md",
    "docs/project/PROJECT_HISTORY.md",
    "docs/project/VERSIONS.md",
    "docs/project/VERSION_AND_BUILD_IDENTIFIERS.md",
    "docs/verification/TEST_RESULTS.md",
    "docs/legal/DISCLAIMER.md",
    "evidence/EVIDENCE_SUMMARY.md",
    "evidence/REPORTS_PUBLIC_REGISTER.csv",
    "evidence/GIT_STATUS_AND_LOG.md",
}
EXPORT_MANIFEST_FILES = BASE_EXPORT_MANIFEST_FILES | {
    "updates/2026-08-31-public-status.md",
    "updates/2026-08-31-public-status_DE.md",
}
SUPPORT_FILES = {
    ".gitattributes",
    ".github/FUNDING.yml",
    ".gitignore",
    "evidence/EXPORT_CONTENTS.md",
    "tests/test_verify_public_export.py",
    "tools/verify_public_export.py",
    "updates/2026-08-30-initial-public-status.md",
    "updates/2026-08-30-public-history-and-status.md",
}
REPOSITORY_ALLOWLIST = BASE_EXPORT_MANIFEST_FILES | SUPPORT_FILES
LANGUAGE_COUNTERLINKS = {
    "README.md": "README_DE.md",
    "README_DE.md": "README.md",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            files.append(path)
    return sorted(files, key=lambda p: _relative(p, root))


def manifest_entries(root: Path) -> tuple[dict[str, tuple[int, str]], list[str]]:
    errors: list[str] = []
    manifest = root / "evidence" / "EXPORT_CONTENTS.md"
    if not manifest.is_file():
        return {}, ["FAIL: EXPORT_CONTENTS.md is missing"]
    entries: dict[str, tuple[int, str]] = {}
    saw_self_reference = False
    for line in manifest.read_text(encoding="utf-8").splitlines():
        match = MANIFEST_RE.match(line)
        if match:
            relative, byte_count, digest = match.groups()
            if relative in {"EXPORT_CONTENTS.md", "evidence/EXPORT_CONTENTS.md"}:
                errors.append("FAIL: self-referential manifest entry must be omitted")
            elif relative in entries:
                errors.append(f"FAIL: duplicate manifest entry: {relative}")
            else:
                entries[relative] = (int(byte_count), digest.lower())
            continue
        if SELF_MANIFEST_RE.match(line):
            saw_self_reference = True
    if not entries:
        errors.append("FAIL: no SHA-256 manifest entries found")
    if not saw_self_reference:
        errors.append("FAIL: self-referential manifest omission note is missing")
    return entries, errors


def manifest_update_files(entries: dict[str, tuple[int, str]]) -> tuple[set[str], list[str]]:
    errors: list[str] = []
    en_dates = {match.group(1) for relative in entries if (match := UPDATE_EN_RE.fullmatch(relative))}
    de_dates = {match.group(1) for relative in entries if (match := UPDATE_DE_RE.fullmatch(relative))}
    update_files = {
        relative
        for relative in entries
        if UPDATE_EN_RE.fullmatch(relative) or UPDATE_DE_RE.fullmatch(relative)
    }
    unexpected_updates = sorted(
        relative
        for relative in entries
        if relative.startswith("updates/")
        and not (UPDATE_EN_RE.fullmatch(relative) or UPDATE_DE_RE.fullmatch(relative))
    )
    if unexpected_updates:
        errors.append(f"FAIL: manifest has unexpected update entries: {', '.join(unexpected_updates)}")
    if len(en_dates) != 1 or len(de_dates) != 1 or en_dates != de_dates:
        errors.append("FAIL: manifest must contain exactly one matched EN/DE dated status update pair")
    return update_files, errors


def expected_manifest_files(entries: dict[str, tuple[int, str]]) -> tuple[set[str], list[str]]:
    update_files, update_errors = manifest_update_files(entries)
    return BASE_EXPORT_MANIFEST_FILES | update_files, update_errors


def is_historical_update_file(relative: str) -> bool:
    return bool(UPDATE_EN_RE.fullmatch(relative) or UPDATE_DE_RE.fullmatch(relative))


def verify_manifest(root: Path) -> list[str]:
    errors: list[str] = []
    entries, manifest_errors = manifest_entries(root)
    errors.extend(manifest_errors)
    expected_files, expected_errors = expected_manifest_files(entries)
    errors.extend(expected_errors)
    actual_manifest_files = set(entries)
    if actual_manifest_files != expected_files:
        missing = sorted(expected_files - actual_manifest_files)
        extra = sorted(actual_manifest_files - expected_files)
        if missing:
            errors.append(f"FAIL: manifest allowlist is missing entries: {', '.join(missing)}")
        if extra:
            errors.append(f"FAIL: manifest allowlist has unexpected entries: {', '.join(extra)}")
    for relative, (expected_size, expected_hash) in entries.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"FAIL: manifest file is missing: {relative}")
            continue
        if path.stat().st_size != expected_size:
            errors.append(f"FAIL: manifest byte mismatch: {relative}")
        if sha256(path) != expected_hash:
            errors.append(f"FAIL: SHA-256 mismatch: {relative}")
    return errors


def verify_register(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "evidence" / "REPORTS_PUBLIC_REGISTER.csv"
    if not path.is_file():
        return ["FAIL: REPORTS_PUBLIC_REGISTER.csv is missing"]
    raw = path.read_bytes()
    if b"\r" in raw:
        errors.append("FAIL: REPORTS_PUBLIC_REGISTER.csv must use LF line endings")
    if raw and not raw.endswith(b"\n"):
        errors.append("FAIL: REPORTS_PUBLIC_REGISTER.csv must end with LF")
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != EXPECTED_COLUMNS:
            return errors + ["FAIL: REPORTS_PUBLIC_REGISTER.csv schema does not match the public schema"]
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
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}|not available", row["record_date_utc"] or ""):
            errors.append(f"FAIL: row {index} has an invalid UTC record date")
        status = row["status"]
        if status not in ALLOWED_STATUSES:
            errors.append(f"FAIL: row {index} has an unsupported status")
        row_hash = row["sha256"]
        if status == "REGISTERED" and not HASH_RE.fullmatch(row_hash or ""):
            errors.append(f"FAIL: row {index} must have a SHA-256 value")
        if status == "HASH_NOT_PUBLISHED" and row_hash:
            errors.append(f"FAIL: row {index} publishes a hash despite HASH_NOT_PUBLISHED")
    evidence = root / "evidence" / "EVIDENCE_SUMMARY.md"
    if evidence.is_file():
        match = re.search(r"Current sanitised register count: `(\d+)`", evidence.read_text(encoding="utf-8"))
        if match and int(match.group(1)) != len(rows):
            errors.append("FAIL: published evidence count does not match the register row count")
    return errors


def verify_repository_allowlist(root: Path, *, export_only: bool = False) -> list[str]:
    errors: list[str] = []
    entries, manifest_errors = manifest_entries(root)
    expected_files, expected_errors = expected_manifest_files(entries)
    errors.extend(manifest_errors)
    errors.extend(expected_errors)
    allowed = expected_files | {"evidence/EXPORT_CONTENTS.md"} if export_only else expected_files | SUPPORT_FILES
    for path in _iter_files(root):
        relative = _relative(path, root)
        if "__pycache__" in path.parts or ".pytest_cache" in path.parts or path.suffix.lower() in {".pyc", ".pyo", ".pyd"}:
            errors.append(f"FAIL: cache artifact is forbidden: {relative}")
        if relative not in allowed and not (not export_only and is_historical_update_file(relative)):
            errors.append(f"FAIL: unexpected public repository file: {relative}")
    present = {_relative(path, root) for path in _iter_files(root)}
    missing = allowed - present
    if missing:
        label = "export" if export_only else "repository"
        errors.append(f"FAIL: required {label} files are missing: {', '.join(sorted(missing))}")
    return errors


def verify_privacy_scan(root: Path) -> list[str]:
    errors: list[str] = []
    text_suffixes = {".csv", ".md", ".py", ".txt", ".yml", ".yaml", ".gitignore", ".gitattributes"}
    for path in _iter_files(root):
        relative = _relative(path, root)
        if relative in {"tools/verify_public_export.py", "tests/test_verify_public_export.py"}:
            continue
        if path.suffix.lower() not in text_suffixes and path.name not in {".gitignore", ".gitattributes"}:
            continue
        text = path.read_text(encoding="utf-8", errors="strict")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"FAIL: forbidden private {label} pattern in {relative}")
    return errors


def verify_markdown_links(root: Path) -> list[str]:
    errors: list[str] = []
    resolved_root = root.resolve()
    for path in _iter_files(root):
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for link in LOCAL_LINK_RE.findall(text):
            target_text = link.strip()
            if not target_text or "://" in target_text or target_text.startswith("#") or target_text.startswith("mailto:"):
                continue
            target_part = target_text.split("#", 1)[0]
            if not target_part:
                continue
            target = (path.parent / target_part).resolve()
            if target != resolved_root and resolved_root not in target.parents:
                errors.append(f"FAIL: markdown link escapes repository: {_relative(path, root)} -> {target_text}")
            elif not target.exists():
                errors.append(f"FAIL: broken local markdown link in {_relative(path, root)}: {target_text}")
    return errors


def verify_language_counterlinks(root: Path) -> list[str]:
    errors: list[str] = []
    for relative, counterpart in LANGUAGE_COUNTERLINKS.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"FAIL: language navigation source is missing: {relative}")
            continue
        if counterpart not in path.read_text(encoding="utf-8"):
            errors.append(f"FAIL: missing language navigation: {relative} -> {counterpart}")
    dated_updates = {
        _relative(path, root)
        for path in _iter_files(root)
        if path.suffix.lower() == ".md" and is_historical_update_file(_relative(path, root))
    }
    dates = {
        match.group(1)
        for relative in dated_updates
        for match in (UPDATE_EN_RE.fullmatch(relative) or UPDATE_DE_RE.fullmatch(relative),)
        if match
    }
    for date in sorted(dates):
        en_relative = f"updates/{date}-public-status.md"
        de_relative = f"updates/{date}-public-status_DE.md"
        en_path = root / en_relative
        de_path = root / de_relative
        if not en_path.is_file():
            errors.append(f"FAIL: language navigation source is missing: {en_relative}")
            continue
        if not de_path.is_file():
            errors.append(f"FAIL: language navigation source is missing: {de_relative}")
            continue
        if f"{date}-public-status_DE.md" not in en_path.read_text(encoding="utf-8"):
            errors.append(f"FAIL: missing language navigation: {en_relative} -> {date}-public-status_DE.md")
        if f"{date}-public-status.md" not in de_path.read_text(encoding="utf-8"):
            errors.append(f"FAIL: missing language navigation: {de_relative} -> {date}-public-status.md")
    return errors


def verify_marker_blocks(root: Path) -> list[str]:
    errors: list[str] = []
    for path in _iter_files(root):
        if path.suffix.lower() != ".md":
            continue
        stack: list[tuple[str, int]] = []
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in MARKER_RE.finditer(line):
                marker = match.group(1)
                base = marker.split(":", 1)[0]
                kind = "HUMAN_TEXT" if base.startswith("HUMAN_TEXT_") else "AUTO_VALUES"
                edge = "START" if base.endswith("_START") else "END"
                if edge == "START":
                    if stack:
                        errors.append(f"FAIL: HUMAN_TEXT and AUTO_VALUES blocks must not be nested in {_relative(path, root)}:{line_number}")
                    stack.append((kind, line_number))
                elif not stack:
                    errors.append(f"FAIL: unmatched {kind} block end in {_relative(path, root)}:{line_number}")
                else:
                    current_kind, start_line = stack.pop()
                    if current_kind != kind:
                        errors.append(
                            f"FAIL: mismatched marker block in {_relative(path, root)}:{line_number}; "
                            f"{current_kind} started at line {start_line}"
                        )
        for kind, start_line in stack:
            errors.append(f"FAIL: unclosed {kind} block in {_relative(path, root)}:{start_line}")
    return errors


def verify_lf_text_files(root: Path) -> list[str]:
    errors: list[str] = []
    text_suffixes = {".csv", ".md", ".py", ".txt", ".yml", ".yaml", ".gitignore", ".gitattributes"}
    for path in _iter_files(root):
        if path.suffix.lower() not in text_suffixes and path.name not in {".gitignore", ".gitattributes"}:
            continue
        raw = path.read_bytes()
        if b"\r" in raw:
            errors.append(f"FAIL: file must use LF line endings: {_relative(path, root)}")
    return errors


def verify(root: Path, *, export_only: bool = False) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    errors.extend(verify_manifest(root))
    errors.extend(verify_register(root))
    errors.extend(verify_repository_allowlist(root, export_only=export_only))
    errors.extend(verify_privacy_scan(root))
    errors.extend(verify_markdown_links(root))
    errors.extend(verify_language_counterlinks(root))
    errors.extend(verify_marker_blocks(root))
    errors.extend(verify_lf_text_files(root))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a public AlgoSphere documentation export.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="public repository or export directory",
    )
    parser.add_argument(
        "--export-only",
        action="store_true",
        help="validate a sanitised export directory that intentionally omits repository support files",
    )
    args = parser.parse_args()
    errors = verify(args.root.resolve(), export_only=args.export_only)
    if errors:
        print("FAIL: public export verification failed")
        print("\n".join(errors))
        return 1
    print("PASS: SHA-256 manifest, manifest byte sizes and report-register CSV bytes verified.")
    print("PASS: allowlist, cache, private path, secret scan, Markdown links and EN/DE counterlinks verified.")
    print("PASS: HUMAN_TEXT and AUTO_VALUES blocks are present only as non-nested blocks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
