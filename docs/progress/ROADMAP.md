# Current public roadmap

Publication: **2026-09-19**. Human-reviewed.

## Lifecycle contract

HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION

Rule evidence remains preserved independently from ML-selector success.

## P0 — Canonical Memory / learning closure

- **OPEN:** Run the scoped Exact-only historical backfill only after the active SQLite writer is safely paused.
- **OPEN:** Resolve PAPER/CURRENT Contribution/Delta population mismatch without synthetic relabeling.
- **OPEN:** Keep new CONTEXT_V2 writes fail-closed for required state evidence.
- **IMPLEMENTED / NEEDS PROSPECTIVE PROOF:** Canonical Learning Delta is connected to the CONTEXT_V2 selector.
- **OPEN:** Make future without-vs-with-memory traces visible and auditable on natural decisions.

## P0 — Research evidence handoff

- **IMPLEMENTED / NEEDS NATURAL RUN:** compact Candidate/Rule/Nested-Fold/Contract evidence is projected before the Canonical Memory handoff.
- **OPEN:** Prove this on the next natural QUICK/Research handoff; do not start training only for proof.
- **OPEN:** Keep full active_strategies payloads out of Canonical Memory.

## P0 — Research storage

- **CLOSED FUTURE-WRITE FIX:** remove duplicated decoded + *_json aliases from future active_strategies snapshots.
- **OPEN:** Observe future real runs to confirm expected storage reduction.
- **NO ACTION AUTHORIZED:** no historical DELETE, VACUUM or migration.

## P0 — model quality

- **OPEN:** Explain Rule-vs-ML degradation before broader training.
- **OPEN:** Evaluate eligible candidates through the Robustness Gate.
- **OPEN:** Keep broad multi-coin training and automatic promotion blocked until uplift is proven.

## P1 — WebUI

- **CLOSED:** CURRENT / CONTEXT_V2 filter and KPI separation repaired.
- **CLOSED:** filter/variant/scroll persistence through background refresh.
- **CLOSED:** shared table typography/compact-row contract at WebUI 90.8.10.196.
- **OPEN:** continue reducing dense headers/cards and add pagination/virtualization for large histories.

## P1 — legacy and historical evidence

- **OPEN:** keep legacy gaps explicit as LEGACY_SCHEMA_GAP / NOT_RECONSTRUCTABLE where exact values are unavailable.
- **OPEN:** evaluate legacy MTF entry confirmation, Pending/Recheck and manual-signal provenance only through controlled evidence/replay.

## Verification

- Focused green suites prove the changed contracts, not global profitability or total project closure.
- Complete suite classification remains separate from focused acceptance.

## Safety boundary

`LIVE=false` · `REAL_CAPITAL=0` · automatic promotion disabled.

[Current status](../../CURRENT_STATUS.md) · [September 19 update](../../updates/2026-09-19-public-status.md) · [Completed work](COMPLETED_WORK.md) · [Test results](../verification/TEST_RESULTS.md)