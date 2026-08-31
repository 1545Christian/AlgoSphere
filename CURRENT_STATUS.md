# Current public status

<!-- HUMAN_TEXT_START -->

## Plain-language summary

AlgoSphere remains within a fail-closed research boundary. The current observed records show some controls in passing states, but the runtime context gate remains blocked. That means the project does not claim activation, promotion or live-trading readiness.

## How to read this page

`export verified` describes checks carried out on this documentation package. `observed in current artifact` describes a scalar value read from a current private artifact. `independently rerun` is used only when this export actually ran the relevant application test. `blocked`, `not verified` and `not applicable` retain their ordinary meanings.

<!-- HUMAN_TEXT_END -->

<!-- AUTO_VALUES_START -->
## Technical status table

| Control | Observed value | Source artifact (UTC) | Status meaning | Practical effect |
|---|---|---|---|---|
| Canonical-history integrity | `PASS` | `2026-08-31T18:14:41Z` | observed in current artifact | integrity gate reports its state |
| Paper-watch guard | `PASS` | `2026-08-31T16:15:22Z` | observed in current artifact | guard observation does not activate trading |
| Runtime context gate | `FAIL_INCOMPLETE_V3_CONTEXT` | `2026-08-31T16:15:22Z` | blocked | context is not treated as complete |
| Remaining runtime context cases | `7` | `2026-08-31T16:15:22Z` | blocked | highest-priority remediation remains open |
| Research profile | `QUICK` | `2026-08-31T20:00:38Z` | observed in current artifact | profile label only |
| Activation allowed | `False` | `2026-08-31T20:00:38Z` | observed in current artifact | activation is not permitted by the observed artifact |
| Eligible experiments | `0` | `2026-08-31T20:00:38Z` | observed in current artifact | no eligible experiment is reported |

## What this export checked

- **export verified:** fixed allowlist, ZIP readability, manifest hashes, internal Markdown links and privacy/secret-pattern scan passed.
- **not applicable:** this export did not start trading, exchange, order, Telegram or other external API actions.
- **observed in current artifact:** values in the table were read as scalars at `2026-08-31T23:33:13Z UTC / 2026-09-01 00:33 Westeuropäische Sommerzeit Atlantic/Canary`.

## What was not rerun

Application test suites: not rerun during this export. Observed report values must not be read as independently rerun tests.

## Current main blocker and next step

**blocked:** `7` runtime-context cases remain under `FAIL_INCOMPLETE_V3_CONTEXT`. **Next required step:** resolve the missing context and then independently rerun the applicable gate before claiming completion.
<!-- AUTO_VALUES_END -->
