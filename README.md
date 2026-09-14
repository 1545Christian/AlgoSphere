# AlgoSphere

Independent crypto-ML research and engineering project.

Building, testing and documenting the path from research and backtesting to paper and shadow execution.

Deutsch: [README_DE.md](README_DE.md)<br>
Latest status: [CURRENT_STATUS.md](CURRENT_STATUS.md)<br>
Latest update: [English status update](updates/2026-09-14-public-status.md)<br>
Telegram: https://t.me/AlgoSphereOfficial

## What AlgoSphere is

AlgoSphere is an independent research and engineering project. I have worked on the underlying ideas and Python prototypes for approximately three years, beginning by rebuilding and adapting examples from educational material, including YouTube videos.

That learning work grew into several of my own Python prototypes, revised repeatedly. The current aim is a consistent, auditable path from research and backtesting to paper and shadow execution.

## Current status

| Scope | Current reviewed state |
|---|---|
| Training | **Paused** |
| Factory / hypothesis producer | **Paused** |
| Active Paper | Running / fail-closed |
| Research Watch / Forward | Running with no-capital counterfactual observation enabled |
| OpenAI AI-only | Process alive; fresh natural E2E trade chain still unproven |
| WebUI | Reviewed repair status PASS, source version `v90_8_10_162` |
| Live trading | **No** |
| Real capital | **0** |
| Automatic promotion | **No** |

The project remains fail-closed. No research result is promoted when required runtime evidence is incomplete.

The current focus is not broad retraining. It is proving that Paper, Watch, Research Forward, OpenAI, exits, outcomes and canonical memory remain causally linked and learn from the right evidence.

## Key recent corrections

- The 0.30% expected-net guard remains hard for Paper, but blocked Research setup matches are now preserved as no-capital counterfactuals instead of being discarded.
- 49 counterfactual observations were created in the initial backfill; 13 were settled through 8h at the recorded checkpoint.
- 58 local 100-USDT trades were repaired through `Decision → Trade → Outcome → Canonical Memory`, including exit state and post-exit horizons.
- WebUI liveness/current-truth defects were corrected.
- OpenAI remains Futures-only and independent from local ML, but a fresh natural AI-only trade-to-learning chain is still pending proof.
- Training and Factory remain paused because Rule evidence must be preserved independently from ML selector success.
- The intended lifecycle is now `HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`; `candidate_eligible` is metadata, not a separate operating stage.

See [CURRENT_STATUS.md](CURRENT_STATUS.md) for the reviewed current state and the [September 14 update](updates/2026-09-14-public-status.md) for details.

## What visitors can do here

Visitors can:

- review the current documented project status,
- see passed and blocked controls,
- follow known technical problems and open work,
- compare dated public updates,
- inspect the sanitised evidence register,
- verify the integrity of a public export.

This repository is a public documentation and evidence record. It is not a downloadable release of the private AlgoSphere application.

## What is public / what remains private

| Public | Private |
|---|---|
| Status, test boundaries, blockers and history | Application source code and proprietary trading logic |
| Roadmap, dated EN/DE updates and public verifier | Credentials, accounts, exchange and Telegram configuration |
| Sanitised evidence register | Databases, market data, models, checkpoints and strategy parameters |
| Export integrity information | Private logs and runtime paths |

## Start here

| Purpose | Document |
|---|---|
| Current state and main blockers | [CURRENT_STATUS.md](CURRENT_STATUS.md) |
| Latest dated update | [English update](updates/2026-09-14-public-status.md) |
| Tests and verification limits | [Test results](docs/verification/TEST_RESULTS.md) |
| Open work and priorities | [Roadmap](docs/progress/ROADMAP.md) |
| Project history | [Project history](docs/project/PROJECT_HISTORY.md) |
| Evidence guide | [Evidence summary](evidence/EVIDENCE_SUMMARY.md) |

Browse all dated [updates](updates/).

## Development history and AI support

I have worked on the underlying ideas and Python prototypes for approximately three years. The project began by rebuilding and adapting examples from educational material, including YouTube videos. Over time, I developed and repeatedly revised several of my own prototypes.

Codex and ChatGPT now support implementation, debugging, technical review and documentation. Their output is reviewed and revised before publication. The architecture, project decisions and responsibility remain human.

Because repeated Codex handoffs caused uncertainty about the actual project state, I am rechecking important requirements against code, dated artifacts and tests before resuming broader training. That review has already exposed several cases where a technically running component was not yet equivalent to a proven end-to-end learning path.

## Publication note

The automatic nightly uploader worked on recent days, but its narrative source selection repeatedly carried older September 5/6 text forward while newer engineering work existed. The nightly publisher is currently paused by the operator; the September 14 status is human-reviewed to avoid another stale overwrite.

## Future use

In the long term, AlgoSphere is intended to become a controlled research-to-execution system for my own use. Own trading can only be considered after complete checks of data, runtime, risk and operations. Any later live use requires explicit human approval and independent safeguards. Live trading is not enabled now. No trading performance, profitability or successful project completion is promised.

## Support and disclaimer

Short updates: [Telegram](https://t.me/AlgoSphereOfficial). Voluntary support: [GitHub Sponsors](https://github.com/sponsors/1545Christian). Sponsorship is not an investment and provides no trading signals, investment advice, ownership, return or guaranteed outcome. See the full [Disclaimer](docs/legal/DISCLAIMER.md).
