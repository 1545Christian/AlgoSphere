# Public status update — 2026-09-01

Deutsch: [Öffentliches Status-Update](2026-09-01-public-status_DE.md)

<!-- AUTO_VALUES_START -->

This update is generated from current scalar artifacts; the repository guidance is maintained separately in human-reviewed templates.

## Research feature-contract addendum

- **observed in reviewed internal evidence:** a regression in research feature-contract composition was corrected and an immutable research core was checked.
- **observed in reviewed internal evidence:** a time-clean feature-contract run confirmed consistency between training, holdout and runtime. This is a contract and data-availability result, not a performance or profitability result.
- **observed in reviewed internal evidence:** the relevant regression tests and runtime-delivery tests passed. They were not rerun by this public export.
- **not applicable:** no live trades, orders, exchange actions, capital actions, paper activation or candidate promotions were performed.
- **observed in reviewed internal evidence:** the research core is prepared for the next natural research start. That start has not been claimed as completed.

**blocked:** the runtime-entry snapshot still lacks provenance-bound trade-window candles. Capture them immutably, then repeat exact-hash QA and a fresh trade review.


## Change since the previous published snapshot

The previous public register snapshot contained 1,742 records. The current sanitised register contains 2854 records, a difference of 1112. The register does not disclose raw filenames or causal provenance, so the cause of this increase is not verified. It must not be read as 1112 new tests, completed development tasks or performance progress. The requested intermediate count of 1,841 is not current in this re-inventory and is not stated as a current value.

## Verified engineering and operational artifacts reviewed today

- **Stale Slot-B guard:** a `CLEARED_STALE_RESOURCE_GUARD` artifact records that a persisted resource guard was released only after the recorded PID and lease were absent. Its validation records `13 passed` and compile checks. It records no Paper, Live, capital or data-deletion action.
- **QUICK attempt:** a real QUICK attempt was observed as interrupted by a resource guard (`ExitCode 15`) after a private-memory observation of approximately `3.63 GiB` against a `2.50 GiB` limit. The selector observed 69 candidates in 12 families; zero were eligible and zero selected. This is an operational resource result, not a QUICK PASS and not a hypothesis rejection. Activation and promotion remained disabled.
- **Runtime-health projection:** the reviewed artifact records Active Paper and Research Forward as proven, while Watch Scanner and Watch Exit Evaluator remain not proven. Its attached verification records `108 passed` and compile PASS; those are historical artifact claims, not tests rerun by this export.
- **Storage and retention:** the latest reviewed capacity profile recorded approximately `136.60 GiB` free against a `9.25 GiB` required threshold, with zero cleanup bytes. No destructive cleanup occurred. Referenced lineage backups remain protected and an explicit retention policy remains open.
- **F_META:** the reviewed readiness artifact remains `PREPARED_WAITING_CURRENT_INDEPENDENT_RUNTIME_QA_TERMINAL`; an independent QA confirmation and a new terminal Active-Paper decision are still not established.

## Controls with current artifacts

- Canonical-history integrity: `PASS` observed at `2026-09-01T00:00:56Z`.
- Paper-watch guard: `PASS` observed at `2026-08-31T16:15:22Z`.
- Runtime context gate: `FAIL_INCOMPLETE_V3_CONTEXT` observed at `2026-08-31T16:15:22Z`; `7` scoped cases remain.
- Research profile: `QUICK`; activation allowed: `False`; eligible experiments: `0` observed at `2026-09-01T00:42:46Z`.

## Test boundary and next step

Application test suites were not rerun during this export. The unchanged main blocker is the runtime context gate. The next concrete step is to resolve the remaining context cases and then independently rerun the applicable gate.

Export integrity: verified. See [Current status](../CURRENT_STATUS.md), [Test results](../docs/verification/TEST_RESULTS.md) and the binding [Evidence summary](../evidence/EVIDENCE_SUMMARY.md).
<!-- AUTO_VALUES_END -->
