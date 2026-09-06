# Test results and verification limits

## Documented checks — not rerun by this export

- **2026-09-05 · Documented verification:** The Factory identity fix has 15 passing tests documented. They are not rerun by the public export and do not establish full operational proof.
- **2026-09-06 · Documented verification:** The installed publisher module passed its bundled offline regression suite locally. This is not ML/trading acceptance and the test did not publish to GitHub.
- **2026-09-06 · Documented verification:** The installed publisher module passed its bundled offline regression suite locally. This is not ML/trading acceptance and the test did not publish to GitHub.

## Observed gate reports — not independently rerun

- **2026-09-06 · Observation:** Paper/Watch guard: report status PASS at 2026-09-06T22:27:38.498349+00:00. Observed artifact only; the gate was not rerun by this publication.
- **2026-09-06 · Failure / blocker:** Runtime context gate: report status FAIL_INCOMPLETE_V3_CONTEXT at 2026-09-06T22:27:38.431034+00:00. Observed artifact only; the gate was not rerun by this publication.

## What publication validates

Allowlist, public-safe text, internal file links, exact per-path manifest byte counts and SHA-256, and equality of final staged bytes with ZIP members. A code-test PASS is not runtime acceptance.

[Source projection](../../evidence/DAILY_SUMMARY.json)
