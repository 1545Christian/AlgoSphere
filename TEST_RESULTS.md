# Current test and QA results

Evidence timestamp: `2026-08-30T16:04:31Z`

| Area | Latest reported result |
|---|---|
| WebUI chronology / score data | Scoped QA pass; targeted regressions `7/7` |
| WebUI research-forward / role isolation | Scoped QA pass; targeted regressions `14/14` |
| No-capital shadow E2E retry | Pass; pytest `36/36`, canonical-validator regressions `47/47` |
| Retrospective-row authorisation quarantine | Scoped QA pass; owner-bound pytest `23/23`, validator regressions `47/47` |
| Research-infrastructure selector v2 | Scoped QA pass; bound suite `47/47` |
| Candidate terminal decisions | Scoped classifications passed; promotion remains blocked |
| Runtime entry-snapshot coverage | **Fail:** incomplete v3 context; seven scoped contract failures remain |
| Canonical-history integrity | **Pass** |

## Interpretation

Passing a scoped QA suite means the named contract passed within that scope. It does not establish profitable trading performance, complete system readiness or safe live activation.

No new test run was started for the public export, and no application code was changed while creating it.
