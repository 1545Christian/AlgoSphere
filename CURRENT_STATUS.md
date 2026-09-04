# Current public status

<!-- HUMAN_TEXT_START -->

## Plain-language summary

AlgoSphere remains within a fail-closed research boundary. The newest runtime and autonomous-training snapshot is published below. Older gate artifacts remain registered as historical evidence and do not override a newer runtime-acceptance state. Live-trading readiness is not claimed.

## How to read this page

`export verified` describes checks carried out on this documentation package. `observed in current artifact` describes a scalar value read from a current private artifact. `independently rerun` is used only when this export actually ran the relevant application test. `blocked`, `not verified` and `not applicable` retain their ordinary meanings.

## Research feature-contract addendum — 1 September

- **observed in reviewed internal evidence:** a regression in research feature-contract composition was corrected and an immutable research core was checked.
- **observed in reviewed internal evidence:** a time-clean feature-contract run confirmed consistency between training, holdout and runtime. This is a contract and data-availability result, not a performance or profitability result.
- **observed in reviewed internal evidence:** the relevant regression tests and runtime-delivery tests passed. They were not rerun by this public export.
- **not applicable:** the reviewed work did not perform live trades, orders, exchange actions, capital actions, paper activation or candidate promotion.
- **observed in reviewed internal evidence:** the research core is prepared for the next natural research start. That start has not yet been claimed as completed.

The fail-closed blocker remains unchanged: the runtime-entry snapshot still requires provenance-bound trade-window candles. They must be captured immutably and then checked again with exact-hash QA and a fresh trade review.

<!-- HUMAN_TEXT_END -->

<!-- AUTO_VALUES_START -->
## Technical status table

| Control | Observed value | Source artifact (UTC) | Status meaning | Practical effect |
|---|---|---|---|---|
| Canonical-history integrity | `PASS` | `2026-09-04T00:40:55Z` | observed in current artifact | integrity gate reports its state |
| Paper-watch guard | `PASS` | `2026-09-04T00:07:44Z` | observed in current artifact | guard observation does not activate trading |
| Runtime context gate | `FAIL_INCOMPLETE_V3_CONTEXT` | `2026-09-04T00:07:44Z` | blocked | context is not treated as complete |
| Remaining runtime context cases | `7` | `2026-09-04T00:07:44Z` | blocked | highest-priority remediation remains open |
| Research profile | `QUICK` | `2026-09-04T00:40:42Z` | observed in current artifact | profile label only |
| Activation allowed | `False` | `2026-09-04T00:40:42Z` | observed in current artifact | activation is not permitted by the observed artifact |
| Eligible experiments | `0` | `2026-09-04T00:40:42Z` | observed in current artifact | no eligible experiment is reported |

## What this export checked

- **export verified:** fixed allowlist, ZIP readability, manifest hashes, internal Markdown links and privacy/secret-pattern scan passed.
- **not applicable:** this export did not start trading, exchange, order, Telegram or other external API actions.
- **observed in current artifact:** values in the table were read as scalars at `2026-09-04T00:43:30Z UTC / 2026-09-04 01:43 Westeuropäische Sommerzeit Atlantic/Canary`.

## What was not rerun

Application test suites: not rerun during this export. Observed report values must not be read as independently rerun tests.

## Historical gate note

The older runtime-context gate remains visible in the public evidence history. Current operational status is taken from the latest runtime-acceptance and autonomous-training snapshot below.

<!-- GITHUB_NIGHTLY_V3_START -->
## Current runtime and autonomous-training snapshot

- Current runtime release observed: `v90_8_10_116`.
- ML autopilot: `QUICK_RUNNING` · profile `quick` · phase `CONTEXT_LOAD` · symbol `BTCUSDT` · coins `0/5`.
- Current-stage truth source: `LIVE_STAGE_HEARTBEAT`.
- Live trading: `No` · real-capital flag: `0` · automatic promotion: `disabled`.
- Snapshot observed: `2026-09-04T00:43:25.149915Z`.

This runtime/training snapshot is the current top-level operational view. Older gate artifacts remain part of the historical public register but are not treated as a newer runtime release state.
<!-- GITHUB_NIGHTLY_V3_END -->
<!-- AUTO_VALUES_END -->
