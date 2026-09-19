# Public status update — 2026-09-19

Deutsch: [Öffentliches Status-Update](./2026-09-19-public-status_DE.md)

## Summary

September 19 focused on three recurring project problems: Canonical Memory / V2 lineage, Research-storage growth, and WebUI truth/clarity.

Important progress:

- Trade Like Che CURRENT and CONTEXT_V2 projections were repaired again and browser-checked with stable variant/filter state.
- CONTEXT_V2 now consumes the existing Canonical Learning Delta instead of using only market-state/context-fit information.
- New CONTEXT_V2 writes now enforce state evidence more strictly, but the historical exact-only backfill remains blocked by an SQLite writer lock.
- The first Research→Canonical handoff loss was identified and fixed future-only: compact candidate/rule/fold/contract evidence is now projected before the Chat-2 memory owner.
- The large `research_runs.summary_json.active_strategies` growth was traced to duplicate decoded + `*_json` representations inside each future snapshot. The future writer was reduced by about half in representative-size estimates without deleting historical evidence.
- The WebUI table/filter contract was made more stable and compact while preserving larger readable text and tooltips.
- No training, replay, promotion or live activation was triggered by these repairs.

The main scientific problem is still unchanged: more infrastructure now works, but ML uplift and a fully closed learning loop are not yet proven.

## Canonical Decision / Learning contract

The project continues to converge on one comparable chain:

`Decision → Candidate → Entry Intent / NO_TRADE → Trade / Watch / Counterfactual → Outcome → Canonical Memory → Learning Contribution → Learning Delta → Lifecycle`

The audit showed that the chain is still uneven by lane/variant.

Known gaps include:

- historical `market_state_id` / `market_state_version` incompleteness
- incomplete historical Decision→Trade identity
- Paper CONTEXT_V2 currently has decisions but no comparable executed-outcome population
- some Paper CURRENT learning rows are still attributed to the Trade-Like-Che population
- historical variant/population consistency is not fully proven

New CONTEXT_V2 decisions/outcomes now fail closed when required state evidence is missing.

### Historical exact-only repair

A scoped exact-only historical repair operator exists for PAPER / TLC populations.

The real schema mismatch was corrected:

`canonical_trade_outcomes.decision_id → memory_decisions.decision_id`

and Contributions / Deltas link by `canonical_outcome_id`.

However, the historical apply is **not complete**. Repeated apply attempts were blocked by:

`sqlite3.OperationalError: database is locked`

Therefore the public status remains:

- historical repair committed: **NO**
- runtime/trading touched: **NO**
- training/promotion: **NO**

The system intentionally did not force writes around an active SQLite writer.

## CONTEXT_V2 now consumes Canonical Learning Delta

A concrete missing connection was fixed:

`memory_learning_deltas → CONTEXT_V2 selector`

The existing learning engine and Strategy × State Matrix were reused.

For new Trade Like Che CONTEXT_V2 decisions, the selector can now trace:

- base strategy score
- market-state evidence delta
- memory learning delta
- final strategy score
- WITHOUT_MEMORY decision
- WITH_MEMORY decision
- what changed
- why it changed

CURRENT remains the control path and is unchanged.

Counterfactual / NO_TRADE evidence is not counted as an executed trade.

Focused runtime/canonical/learning tests: **75 PASS**.

## Trade Like Che WebUI and V1/V2 separation

The Trade Like Che view was repaired in several layers.

Confirmed fixes include:

- CURRENT and CONTEXT_V2 use the correct Canonical Decision identity
- existing settlement/capture evidence is no longer overwritten by empty compact projections
- `PENDING_HORIZON_SETTLEMENT` is shown as an open learning horizon instead of a fake exit-quality result
- NO_TRADE reasons and state/context fields are visible
- variant selection survives refresh
- filter state survives refresh
- scroll position survives refresh
- CURRENT / CONTEXT_V2 compare metrics are projected separately
- `127.0.0.1`, `algosphere.intern` and `algoshere.intern` were verified on the same served WebUI build during the browser acceptance

The table contract was also standardized:

- main table text: 14 px
- secondary text: 12 px
- compact rows with ellipsis
- full long values available by tooltip
- internal table scrolling instead of forcing the whole page wide

One browser-verified checkpoint reported:

- CONTEXT_V2: Decisions 40, Settled 32, Memory 40
- CURRENT: Decisions 72, Settled 77

These are UI/runtime evidence counts, not proof that the historical Canonical population is fully comparable.

## Research storage root cause

The local SQLite database was measured at roughly 62 GB, with `research_runs` responsible for a very large share.

The important finding is that classic content deduplication is **not** the solution:

- 418 runs
- 329 runs with `active_strategies`
- 328 unique active-strategy snapshots
- ~33.93 GB inline
- potential identical-content dedup saving: ~0 GB

The real future-writer problem was duplicate representations inside every strategy snapshot.

`ResearchDB._decode_strategy()` exposes both decoded values and their physical `*_json` aliases; `snapshot_run_strategies()` previously copied both.

Confirmed duplicated pairs included:

- `metrics` + `metrics_json`
- `thresholds` + `thresholds_json`
- `setup_params` + `setup_params_json`
- `exit_policy` + `exit_policy_json`
- `feature_columns` + `feature_columns_json`

The future writer now stores only the canonical decoded representation while old summaries remain readable.

Representative estimated size reduction:

- before: ~134.50 MB
- after: ~65.33–71.71 MB
- nominal reduction: ~49%

No old database rows were migrated or deleted. No VACUUM was run.

## Research evidence handoff

A second Research-side gap was found before Canonical Memory:

`research_runs.summary_json → normalize_report() → standardized experiments`

The normal QUICK handoff called `normalize_report()` without the direct run-summary path, and the projection previously kept mainly `rows/results` while dropping valuable active-strategy evidence such as nested-fold and strategy-contract provenance.

The existing Research handoff now projects a compact evidence subset:

- artifact / strategy identity
- nested-fold metrics
- data / code / execution identity
- baseline / stress evidence
- setup / threshold / exit-policy / feature-column hashes

The full `active_strategies` payload is **not** copied into Canonical Memory.

This is a future-only patch. A natural Research/QUICK handoff has not yet occurred since the change, so forward proof remains:

`AWAITING_REAL_RUN`

No historical reprojection is currently required.

## What remains open

1. Execute the scoped historical PAPER/TLC exact-only repair only when the SQLite writer can be safely paused; do not force around the lock.
2. Resolve the PAPER CURRENT population mismatch before claiming fully comparable learning populations.
3. Prove the new Research handoff on the next natural QUICK/Research run.
4. Finish the Canonical population/variant/state contract for new writes and classify historical gaps without inventing values.
5. Continue prospective V1 vs V2 outcome collection; current UI counts are not enough to claim V2 is better.
6. Keep ML uplift as an open scientific question; infrastructure progress does not prove predictive improvement.
7. Continue WebUI simplification, especially reducing oversized header/filter regions while preserving stable state and readable tables.
8. Preserve the new future research-snapshot writer; any historical storage cleanup must remain a separate, evidence-based migration decision.

## Safety boundary

`LIVE=false` · `REAL_CAPITAL=0` · automatic promotion disabled.

No documentation update authorizes live trading, forced historical repair, automatic model promotion or real-capital execution.

[Current status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Documented work](../docs/progress/COMPLETED_WORK.md) · [Test results](../docs/verification/TEST_RESULTS.md)
