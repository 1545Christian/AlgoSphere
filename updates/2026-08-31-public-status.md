# Public status update — 2026-08-31

<!-- AUTO_VALUES_START -->

This update is generated from current scalar artifacts; the repository guidance is maintained separately in human-reviewed templates.

## Change since the previous published snapshot

The previous public register snapshot contained 1,742 records. The current sanitised register contains 1946 records, a difference of 204. The register does not disclose raw filenames or causal provenance, so the cause of this increase is not verified. It must not be read as 204 new tests, completed development tasks or performance progress. The requested intermediate count of 1,841 is not current in this re-inventory and is not stated as a current value.

## Controls with current artifacts

- Canonical-history integrity: `PASS` observed at `2026-08-31T12:42:36Z`.
- Paper-watch guard: `PASS` observed at `2026-08-31T10:15:28Z`.
- Runtime context gate: `FAIL_INCOMPLETE_V3_CONTEXT` observed at `2026-08-31T10:15:28Z`; `7` scoped cases remain.
- Research profile: `QUICK`; activation allowed: `False`; eligible experiments: `0` observed at `2026-08-31T12:45:44Z`.

## Test boundary and next step

Application test suites were not rerun during this export. The unchanged main blocker is the runtime context gate. The next concrete step is to resolve the remaining context cases and then independently rerun the applicable gate.

Export integrity: verified. See [Current status](../CURRENT_STATUS.md), [Test results](../TEST_RESULTS.md) and the binding [Evidence summary](../evidence/EVIDENCE_SUMMARY.md).
<!-- AUTO_VALUES_END -->
