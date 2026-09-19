# Documented engineering work

Items below are dated, reviewed engineering results. They are not claims of profitability or global end-to-end closure.

## September 19 — reviewed engineering progress

### Trade Like Che WebUI and storage truth

- Restored CURRENT and CONTEXT_V2 projection/linkage in the WebUI.
- Restored context, capture, MFE/MAE, Post-Exit and learning-state fields where canonical evidence exists.
- NO_TRADE stays separate from executed trades and is stored through existing runtime/canonical decision paths.
- Stabilized variant selection across refresh with URL state and aria-selected semantics.
- Latest browser proof used WebUI 90.8.10.196 on local IP and both configured aliases.
- Shared table contract: 14 px primary text, 12 px secondary, compact rows, ellipsis + tooltips, internal horizontal scrolling.

### CONTEXT_V2 Canonical Learning consumer

- Found the missing reader connection from memory_learning_deltas into the existing CONTEXT_V2 selector.
- Reused the existing learning handoff and Strategy×State evidence.
- Added variant-safe matching by coin, side, strategy family and market state.
- Preserved CURRENT as control path and excluded counterfactual/NO_TRADE from trade-count semantics.
- Added without-vs-with-memory trace fields for new decisions.
- Focused validation: 75 passed.

### Canonical historical repair work

- Added nested market-context state evidence extraction and stricter fail-closed new-write handling for CONTEXT_V2.
- Corrected the Exact-only backfill operator to the real memory_decisions.decision_id schema.
- Proved exact read-only chains for PAPER/CURRENT, TLC/CURRENT and TLC/CONTEXT_V2.
- Did not fabricate PAPER/CONTEXT_V2 outcomes or missing state fields.
- Historical apply remains blocked by repeated SQLite database locks; no repair commit claimed.

### Research storage future writer

- Proved that active_strategies snapshots are mostly unique, so classic deduplication would save ~0 GB.
- Found duplicate representations inside each snapshot: decoded fields plus *_json aliases.
- Future snapshot writer now keeps only canonical decoded representation.
- No historical rows changed, no migration/delete/vacuum.
- Representative size estimate: ~134.5 MB before versus ~65.3–71.7 MB after; nominal ~49.1% reduction.

### Research → standardized memory handoff

- Found the first upstream loss in normalize_report(): rows/results were projected, but compact Candidate/Rule/Nested-Fold/Contract evidence from active_strategies was dropped.
- Extended the existing Research handoff with compact artifact/strategy identity, nested-fold metrics, data/code/execution identity, baseline/stress evidence and hashes for setup/thresholds/exit-policy/features.
- Did not copy full strategy payloads into Canonical Memory.
- Existing projection tests pass.
- Natural future run proof is still pending: FUTURE_RESEARCH_HANDOFF_PROVEN = AWAITING_REAL_RUN.

### WebUI performance and correctness

- Fixed slow Trade Like Che projection paths by using index-friendly latest-decision reads, hot-read caching, compact TLC details and removal of unnecessary OpenAI snapshot loading.
- Exact TLC API request returned HTTP 200 and ~1.5 s cold on the tested historical as_of.
- Global overview cold load remained separately slower and is not claimed fully solved.

## September 18 — reviewed engineering progress

See the [September 18 public update](../../updates/2026-09-18-public-status.md) for ENA pilot, Robustness Gate, Research Forward Context V2 activation and OpenAI input-contract work.

## Safety / interpretation

A green focused test suite proves the tested contract, not profitability. A completed training run proves technical execution, not model quality. Negative and insufficient evidence is intentionally retained.

[Current status](../../CURRENT_STATUS.md) · [Outstanding work](ROADMAP.md) · [September 19 update](../../updates/2026-09-19-public-status.md)