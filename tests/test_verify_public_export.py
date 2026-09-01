from __future__ import annotations

import csv
import hashlib
import importlib.util
import shutil
import unittest
import uuid
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TMP_ROOT = Path("D:/Bot_research/AlgoSphere/.tmp_public_verify_tests")
MODULE_PATH = REPO_ROOT / "tools" / "verify_public_export.py"
SPEC = importlib.util.spec_from_file_location("verify_public_export", MODULE_PATH)
verify_public_export = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(verify_public_export)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_lf(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def link_from(relative: str, target: str, label: str | None = None) -> str:
    source_dir = Path(relative).parent
    prefix = "" if str(source_dir) == "." else "../" * len(source_dir.parts)
    return f"[{label or target}]({prefix}{target})"


class VerifyPublicExportTests(unittest.TestCase):
    def setUp(self) -> None:
        TMP_ROOT.mkdir(parents=True, exist_ok=True)
        self.root = TMP_ROOT / f"case_{uuid.uuid4().hex}"
        self.update_date = "2026-09-01"
        self.root.mkdir()
        self.make_fixture()

    def tearDown(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def manifest_files(self) -> set[str]:
        return set(verify_public_export.BASE_EXPORT_MANIFEST_FILES) | {
            f"updates/{self.update_date}-public-status.md",
            f"updates/{self.update_date}-public-status_DE.md",
        }

    def make_fixture(self) -> None:
        for relative in sorted(self.manifest_files()):
            if relative == "README.md":
                write_lf(
                    self.root / relative,
                    "# AlgoSphere\n\nDeutsch: [README_DE.md](README_DE.md)\n\n"
                    "<!-- HUMAN_TEXT_START -->\nHuman maintained overview.\n<!-- HUMAN_TEXT_END -->\n\n"
                    "<!-- AUTO_VALUES_START:CURRENT_STATUS -->\n| Area | State |\n|---|---|\n| Runtime | BLOCKED |\n"
                    "<!-- AUTO_VALUES_END:CURRENT_STATUS -->\n",
                )
            elif relative == "README_DE.md":
                write_lf(
                    self.root / relative,
                    "# AlgoSphere\n\nEnglish: [README.md](README.md)\n\n"
                    "<!-- HUMAN_TEXT_START -->\nMenschlich gepflegter Ueberblick.\n<!-- HUMAN_TEXT_END -->\n\n"
                    "<!-- AUTO_VALUES_START:CURRENT_STATUS -->\n| Bereich | Stand |\n|---|---|\n| Runtime | BLOCKIERT |\n"
                    "<!-- AUTO_VALUES_END:CURRENT_STATUS -->\n",
                )
            elif relative == f"updates/{self.update_date}-public-status.md":
                write_lf(
                    self.root / relative,
                    f"# Public status update\n\nDeutsch: [Status]({self.update_date}-public-status_DE.md)\n\n"
                    "<!-- AUTO_VALUES_START -->\nExport integrity: verified.\n<!-- AUTO_VALUES_END -->\n",
                )
            elif relative == f"updates/{self.update_date}-public-status_DE.md":
                write_lf(
                    self.root / relative,
                    f"# Oeffentliches Status-Update\n\nEnglish: [Status]({self.update_date}-public-status.md)\n\n"
                    "<!-- AUTO_VALUES_START -->\nExportintegritaet: verifiziert.\n<!-- AUTO_VALUES_END -->\n",
                )
            elif relative == "evidence/REPORTS_PUBLIC_REGISTER.csv":
                self.write_register(
                    [
                        ("R00001", "BUILD", "2026-08-31", "REGISTERED", "a" * 64),
                        ("R00002", "DELIVERY", "2026-08-31", "REGISTERED", "b" * 64),
                        ("R00003", "QA", "2026-08-31", "REGISTERED", "c" * 64),
                        ("R00004", "TEST", "2026-08-31", "REGISTERED", "d" * 64),
                        ("R00005", "OTHER", "2026-08-31", "HASH_NOT_PUBLISHED", ""),
                    ]
                )
            elif relative == "evidence/EVIDENCE_SUMMARY.md":
                write_lf(
                    self.root / relative,
                    "# Evidence summary\n\nCurrent sanitised register count: `5`\n\n"
                    "See [REPORTS_PUBLIC_REGISTER.csv](REPORTS_PUBLIC_REGISTER.csv).\n",
                )
            else:
                current_status = link_from(relative, "CURRENT_STATUS.md", "Current status")
                test_results = link_from(relative, "docs/verification/TEST_RESULTS.md", "Test results")
                roadmap = link_from(relative, "docs/progress/ROADMAP.md", "Roadmap")
                evidence = link_from(relative, "evidence/EVIDENCE_SUMMARY.md", "Evidence summary")
                write_lf(
                    self.root / relative,
                    f"# {Path(relative).stem.replace('_', ' ')}\n\n"
                    "<!-- HUMAN_TEXT_START -->\nPublic documentation fixture.\n<!-- HUMAN_TEXT_END -->\n\n"
                    "<!-- AUTO_VALUES_START -->\nNo live trading action.\n<!-- AUTO_VALUES_END -->\n"
                    f"\nSee also: {current_status}, {test_results}, {roadmap}, {evidence}.\n",
                )
        self.write_support_files()
        self.rewrite_manifest()

    def write_support_files(self) -> None:
        write_lf(self.root / ".gitattributes", "* text=auto\n")
        write_lf(self.root / ".gitignore", "__pycache__/\n*.pyc\n.pytest_cache/\n.env\n")
        write_lf(self.root / ".github/FUNDING.yml", "github: [1545Christian]\n")
        write_lf(self.root / "tools/verify_public_export.py", "# public verifier fixture\n")
        write_lf(self.root / "tests/test_verify_public_export.py", "# public verifier tests fixture\n")
        write_lf(self.root / "updates/2026-08-30-initial-public-status.md", "# Initial public status\n")
        write_lf(self.root / "updates/2026-08-30-public-history-and-status.md", "# Public history and status\n")

    def write_register(self, rows: list[tuple[str, str, str, str, str]], lineterminator: str = "\n") -> None:
        path = self.root / "evidence" / "REPORTS_PUBLIC_REGISTER.csv"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, lineterminator=lineterminator)
            writer.writerow(verify_public_export.EXPECTED_COLUMNS)
            writer.writerows(rows)

    def read_register(self) -> list[list[str]]:
        with (self.root / "evidence" / "REPORTS_PUBLIC_REGISTER.csv").open("r", encoding="utf-8", newline="") as handle:
            return list(csv.reader(handle))

    def rewrite_register(self, rows: list[list[str]], lineterminator: str = "\n") -> None:
        with (self.root / "evidence" / "REPORTS_PUBLIC_REGISTER.csv").open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle, lineterminator=lineterminator).writerows(rows)

    def rewrite_manifest(self) -> None:
        lines = [
            "# Export contents",
            "",
            "**verified:** SHA-256 values were calculated from the final staged files.",
            "",
            "| Relative filename | Bytes | SHA-256 |",
            "|---|---:|---|",
        ]
        for relative in sorted(self.manifest_files()):
            path = self.root / relative
            lines.append(f"| `{relative}` | {path.stat().st_size} | `{digest(path)}` |")
        lines.append("| `EXPORT_CONTENTS.md` | self | intentionally omitted (self-referential) |")
        write_lf(self.root / "evidence" / "EXPORT_CONTENTS.md", "\n".join(lines) + "\n")

    def errors_after(self, mutate) -> list[str]:
        mutate()
        return verify_public_export.verify(self.root)

    def assert_error(self, mutate, expected: str) -> None:
        errors = self.errors_after(mutate)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_realistic_fixture_passes(self) -> None:
        self.assertEqual(verify_public_export.verify(self.root), [])

    def test_manifest_matches_final_lf_bytes(self) -> None:
        manifest = (self.root / "evidence" / "EXPORT_CONTENTS.md").read_text(encoding="utf-8")
        self.assertNotIn("\r", manifest)
        entries, errors = verify_public_export.manifest_entries(self.root)
        self.assertEqual(errors, [])
        for relative, (size, expected_hash) in entries.items():
            path = self.root / relative
            raw = path.read_bytes()
            self.assertNotIn(b"\r", raw, relative)
            self.assertEqual(size, len(raw), relative)
            self.assertEqual(expected_hash, hashlib.sha256(raw).hexdigest(), relative)

    def test_missing_manifest_fails(self) -> None:
        self.assert_error(lambda: (self.root / "evidence" / "EXPORT_CONTENTS.md").unlink(), "EXPORT_CONTENTS.md is missing")

    def test_self_referential_manifest_hash_entry_fails(self) -> None:
        def mutate() -> None:
            manifest = self.root / "evidence" / "EXPORT_CONTENTS.md"
            text = manifest.read_text(encoding="utf-8")
            text += f"| `evidence/EXPORT_CONTENTS.md` | {manifest.stat().st_size} | `{'e' * 64}` |\n"
            write_lf(manifest, text)

        self.assert_error(mutate, "self-referential manifest entry must be omitted")

    def test_missing_self_referential_manifest_omission_note_fails(self) -> None:
        def mutate() -> None:
            manifest = self.root / "evidence" / "EXPORT_CONTENTS.md"
            lines = [
                line
                for line in manifest.read_text(encoding="utf-8").splitlines()
                if "intentionally omitted (self-referential)" not in line
            ]
            write_lf(manifest, "\n".join(lines) + "\n")

        self.assert_error(mutate, "self-referential manifest omission note is missing")

    def test_duplicate_manifest_entry_fails(self) -> None:
        def mutate() -> None:
            manifest = self.root / "evidence" / "EXPORT_CONTENTS.md"
            text = manifest.read_text(encoding="utf-8")
            first = next(line for line in text.splitlines() if line.startswith("| `README.md`"))
            write_lf(manifest, text + first + "\n")

        self.assert_error(mutate, "duplicate manifest entry")

    def test_extra_manifest_entry_fails(self) -> None:
        def mutate() -> None:
            manifest = self.root / "evidence" / "EXPORT_CONTENTS.md"
            text = manifest.read_text(encoding="utf-8")
            write_lf(manifest, text + "| `docs/unknown.md` | 1 | `" + "0" * 64 + "` |\n")

        self.assert_error(mutate, "manifest allowlist has unexpected entries")

    def test_unmatched_manifest_update_pair_fails(self) -> None:
        def mutate() -> None:
            manifest = self.root / "evidence" / "EXPORT_CONTENTS.md"
            lines = [
                line
                for line in manifest.read_text(encoding="utf-8").splitlines()
                if not line.startswith(f"| `updates/{self.update_date}-public-status_DE.md`")
            ]
            write_lf(manifest, "\n".join(lines) + "\n")

        self.assert_error(mutate, "exactly one matched EN/DE dated status update pair")

    def test_multiple_current_manifest_update_pairs_fail(self) -> None:
        def mutate() -> None:
            extra_en = "updates/2026-09-02-public-status.md"
            extra_de = "updates/2026-09-02-public-status_DE.md"
            write_lf(self.root / extra_en, "# Later public status\n\nDeutsch: [Status](2026-09-02-public-status_DE.md)\n")
            write_lf(self.root / extra_de, "# Spaeteres Status-Update\n\nEnglish: [Status](2026-09-02-public-status.md)\n")
            manifest = self.root / "evidence" / "EXPORT_CONTENTS.md"
            text = manifest.read_text(encoding="utf-8")
            text += f"| `{extra_en}` | {(self.root / extra_en).stat().st_size} | `{digest(self.root / extra_en)}` |\n"
            text += f"| `{extra_de}` | {(self.root / extra_de).stat().st_size} | `{digest(self.root / extra_de)}` |\n"
            write_lf(manifest, text)

        self.assert_error(mutate, "exactly one matched EN/DE dated status update pair")

    def test_export_only_rejects_historical_extra_update_file(self) -> None:
        def mutate() -> None:
            write_lf(
                self.root / "updates/2026-08-31-public-status.md",
                "# Historical update\n\nDeutsch: [Status](2026-08-31-public-status_DE.md)\n",
            )
            write_lf(
                self.root / "updates/2026-08-31-public-status_DE.md",
                "# Historisches Update\n\nEnglish: [Status](2026-08-31-public-status.md)\n",
            )

        mutate()
        errors = verify_public_export.verify(self.root, export_only=True)
        self.assertTrue(any("unexpected public repository file" in error for error in errors), errors)

    def test_repository_mode_allows_historical_extra_update_file(self) -> None:
        write_lf(
            self.root / "updates/2026-08-31-public-status.md",
            "# Historical update\n\nDeutsch: [Status](2026-08-31-public-status_DE.md)\n",
        )
        write_lf(
            self.root / "updates/2026-08-31-public-status_DE.md",
            "# Historisches Update\n\nEnglish: [Status](2026-08-31-public-status.md)\n",
        )

        self.assertEqual(verify_public_export.verify(self.root), [])

    def test_missing_manifest_entry_fails(self) -> None:
        def mutate() -> None:
            manifest = self.root / "evidence" / "EXPORT_CONTENTS.md"
            lines = [line for line in manifest.read_text(encoding="utf-8").splitlines() if not line.startswith("| `README.md`")]
            write_lf(manifest, "\n".join(lines) + "\n")

        self.assert_error(mutate, "manifest allowlist is missing entries")

    def test_manifest_byte_mismatch_fails(self) -> None:
        def mutate() -> None:
            manifest = self.root / "evidence" / "EXPORT_CONTENTS.md"
            text = manifest.read_text(encoding="utf-8")
            size = (self.root / "README.md").stat().st_size
            write_lf(manifest, text.replace(f"| `README.md` | {size} |", "| `README.md` | 999999 |"))

        self.assert_error(mutate, "manifest byte mismatch")

    def test_manifest_hash_mismatch_fails(self) -> None:
        def mutate() -> None:
            write_lf(self.root / "README.md", (self.root / "README.md").read_text(encoding="utf-8") + "\nchanged\n")

        self.assert_error(mutate, "SHA-256 mismatch")

    def test_missing_export_file_fails(self) -> None:
        self.assert_error(lambda: (self.root / "SECURITY.md").unlink(), "manifest file is missing")

    def test_unexpected_file_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "private_notes.md", "not allowed\n"), "unexpected public repository file")

    def test_pyc_file_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "tools" / "x.pyc", "cache\n"), "cache artifact is forbidden")

    def test_pycache_directory_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "tools" / "__pycache__" / "x.py", "cache\n"), "cache artifact is forbidden")

    def test_pytest_cache_directory_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / ".pytest_cache" / "state", "cache\n"), "cache artifact is forbidden")

    def test_private_windows_path_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "CURRENT_STATUS.md", "Private path D:\\Bot_research\\AlgoSphere\n"), "windows_path")

    def test_secret_assignment_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "SECURITY.md", "api_key = 'abcdefghi'\n"), "credential_assignment")

    def test_broken_markdown_link_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "README.md", "[missing](docs/nope.md)\n"), "broken local markdown link")

    def test_markdown_link_escaping_repository_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "README.md", "[escape](../private.md)\n"), "markdown link escapes repository")

    def test_missing_language_navigation_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "README.md", "# AlgoSphere\n\nNo language link.\n"), "missing language navigation")

    def test_missing_update_counterlink_fails(self) -> None:
        self.assert_error(
            lambda: write_lf(
                self.root / "updates" / f"{self.update_date}-public-status.md",
                "# Public status update\n\nNo German counterpart.\n",
            ),
            "missing language navigation",
        )

    def test_nested_human_and_auto_blocks_fail(self) -> None:
        def mutate() -> None:
            write_lf(
                self.root / "README.md",
                "<!-- HUMAN_TEXT_START -->\ntext\n<!-- AUTO_VALUES_START -->\nauto\n"
                "<!-- AUTO_VALUES_END -->\n<!-- HUMAN_TEXT_END -->\nREADME_DE.md\n",
            )

        self.assert_error(mutate, "must not be nested")

    def test_mismatched_human_and_auto_blocks_fail(self) -> None:
        def mutate() -> None:
            write_lf(
                self.root / "README.md",
                "<!-- HUMAN_TEXT_START -->\ntext\n<!-- AUTO_VALUES_END -->\nREADME_DE.md\n",
            )

        self.assert_error(mutate, "mismatched marker block")

    def test_unclosed_marker_block_fails(self) -> None:
        self.assert_error(
            lambda: write_lf(self.root / "README.md", "<!-- AUTO_VALUES_START -->\nvalue\nREADME_DE.md\n"),
            "unclosed AUTO_VALUES block",
        )

    def test_register_schema_fails(self) -> None:
        def mutate() -> None:
            rows = self.read_register()
            rows[0] = ["public_report_id", "category", "status", "sha256"]
            self.rewrite_register(rows)
            self.rewrite_manifest()

        self.assert_error(mutate, "schema does not match")

    def test_invalid_neutral_id_fails(self) -> None:
        def mutate() -> None:
            rows = self.read_register()
            rows[1][0] = "private_report_name"
            self.rewrite_register(rows)
            self.rewrite_manifest()

        self.assert_error(mutate, "invalid neutral ID")

    def test_duplicate_id_fails(self) -> None:
        def mutate() -> None:
            rows = self.read_register()
            rows[2][0] = "R00001"
            self.rewrite_register(rows)
            self.rewrite_manifest()

        self.assert_error(mutate, "duplicate neutral ID")

    def test_unsupported_category_fails(self) -> None:
        def mutate() -> None:
            rows = self.read_register()
            rows[1][1] = "SECRET"
            self.rewrite_register(rows)
            self.rewrite_manifest()

        self.assert_error(mutate, "unsupported category")

    def test_invalid_record_date_fails(self) -> None:
        def mutate() -> None:
            rows = self.read_register()
            rows[1][2] = "31-08-2026"
            self.rewrite_register(rows)
            self.rewrite_manifest()

        self.assert_error(mutate, "invalid UTC record date")

    def test_unsupported_status_fails(self) -> None:
        def mutate() -> None:
            rows = self.read_register()
            rows[1][3] = "PRIVATE"
            self.rewrite_register(rows)
            self.rewrite_manifest()

        self.assert_error(mutate, "unsupported status")

    def test_registered_row_without_hash_fails(self) -> None:
        def mutate() -> None:
            rows = self.read_register()
            rows[1][4] = ""
            self.rewrite_register(rows)
            self.rewrite_manifest()

        self.assert_error(mutate, "must have a SHA-256 value")

    def test_hash_not_published_row_with_hash_fails(self) -> None:
        def mutate() -> None:
            rows = self.read_register()
            rows[5][4] = "f" * 64
            self.rewrite_register(rows)
            self.rewrite_manifest()

        self.assert_error(mutate, "publishes a hash despite HASH_NOT_PUBLISHED")

    def test_evidence_count_mismatch_fails(self) -> None:
        def mutate() -> None:
            write_lf(self.root / "evidence" / "EVIDENCE_SUMMARY.md", "Current sanitised register count: `6`\n")
            self.rewrite_manifest()

        self.assert_error(mutate, "published evidence count does not match")

    def test_crlf_register_bytes_fail(self) -> None:
        def mutate() -> None:
            rows = self.read_register()
            self.rewrite_register(rows, lineterminator="\r\n")
            self.rewrite_manifest()

        self.assert_error(mutate, "must use LF line endings")

    def test_crlf_markdown_bytes_fail(self) -> None:
        def mutate() -> None:
            (self.root / "README.md").write_bytes(b"# AlgoSphere\r\n\r\nREADME_DE.md\r\n")
            self.rewrite_manifest()

        self.assert_error(mutate, "file must use LF line endings")

    def test_private_email_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "SECURITY.md", "contact test@example.com\n"), "email")

    def test_private_ipv4_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "SECURITY.md", "internal host 192.168.1.10\n"), "ipv4")

    def test_proprietary_metric_phrase_fails(self) -> None:
        self.assert_error(lambda: write_lf(self.root / "CURRENT_STATUS.md", "profit factor was high\n"), "proprietary_metrics")


if __name__ == "__main__":
    unittest.main()
