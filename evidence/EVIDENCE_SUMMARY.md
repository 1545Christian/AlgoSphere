# Public evidence summary and register guide

<!-- HUMAN_TEXT_START -->

## Purpose of the register

[REPORTS_PUBLIC_REGISTER.csv](REPORTS_PUBLIC_REGISTER.csv) is a sanitised inventory of discovered report artifacts. It lets visitors check register count, neutral IDs, category, UTC date, registration state and published hashes without disclosing report filenames, paths or raw contents.

## Categories and states

- **BUILD**: build-oriented artifact metadata.
- **DELIVERY**: delivery or release-oriented artifact metadata.
- **QA**: quality-assurance or audit-oriented artifact metadata.
- **TEST**: test-oriented artifact metadata.
- **OTHER**: registered artifact metadata not placed in the preceding public categories.
- **REGISTERED**: the artifact was included in the sanitised inventory. It does not mean that its result passed.
- **HASH_NOT_PUBLISHED**: one record intentionally has no published raw-file hash because a stable raw hash can itself be a private-material fingerprint.

## SHA-256 limits

A SHA-256 value can help compare a file against the same file later. It does not prove that the report is correct, that a test passed, that a result was independently reproduced, or that the file is safe to rely on for trading.

## How to use the register

Use a neutral ID to locate a row, inspect its category and date, and compare a published hash only where one is available. Do not treat a register row as a test certificate or completed development task.

<!-- HUMAN_TEXT_END -->

<!-- AUTO_VALUES_START -->
**Export integrity: verified.** Current sanitised register count: `2854`; published hashes: `2853`; `HASH_NOT_PUBLISHED` rows: `1`.

| Category | Count |
|---|---:|
| BUILD | 1 |
| DELIVERY | 161 |
| QA | 275 |
| TEST | 92 |
| OTHER | 2325 |
| **Total** | **2854** |

The register count is not a count of passed tests, completed features or performance improvements.
<!-- AUTO_VALUES_END -->
