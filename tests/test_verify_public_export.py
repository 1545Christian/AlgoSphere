from __future__ import annotations

import csv
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "verify_public_export.py"
SPEC = importlib.util.spec_from_file_location("verify_public_export", MODULE_PATH)
verify_public_export = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(verify_public_export)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class VerifyPublicExportTests(unittest.TestCase):
    def make_fixture(self) -> Path:
        root = Path(tempfile.mkdtemp())
        (root / "evidence").mkdir()
        register = root / "evidence" / "REPORTS_PUBLIC_REGISTER.csv"
        with register.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(verify_public_export.EXPECTED_COLUMNS)
            writer.writerow(("R00001", "QA", "2026-08-31", "REGISTERED", "a" * 64))
            writer.writerow(("R00002", "OTHER", "2026-08-31", "HASH_NOT_PUBLISHED", ""))
        (root / "evidence" / "EVIDENCE_SUMMARY.md").write_text("Current sanitised register count: `2`\n", encoding="utf-8")
        entries = {
            "evidence/REPORTS_PUBLIC_REGISTER.csv": digest(register),
            "evidence/EVIDENCE_SUMMARY.md": digest(root / "evidence" / "EVIDENCE_SUMMARY.md"),
        }
        lines = ["# Export contents", "", "| Relative filename | Bytes | SHA-256 |", "|---|---:|---|"]
        for relative, value in entries.items():
            lines.append(f"| `{relative}` | 0 | `{value}` |")
        lines.append("| `EXPORT_CONTENTS.md` | self | intentionally omitted (self-referential) |")
        (root / "evidence" / "EXPORT_CONTENTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        return root

    def test_valid_fixture_passes(self) -> None:
        self.assertEqual(verify_public_export.verify(self.make_fixture()), [])

    def test_duplicate_id_fails(self) -> None:
        root = self.make_fixture()
        register = root / "evidence" / "REPORTS_PUBLIC_REGISTER.csv"
        with register.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        rows[2][0] = "R00001"
        with register.open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle).writerows(rows)
        self.assertTrue(any("duplicate neutral ID" in error for error in verify_public_export.verify(root)))


if __name__ == "__main__":
    unittest.main()
