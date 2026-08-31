# AlgoSphere

For the German introduction, see [README_DE.md](README_DE.md).

<!-- HUMAN_TEXT_START: reviewed, revised and approved before publication -->

## What AlgoSphere is

AlgoSphere is an independent research and engineering project for building an auditable trading-research workflow. Its purpose is not to promise market results. The practical aim is to make research, testing, paper observation, monitoring and any future activation decisions traceable, bounded and fail-closed.

## How the project began

I have been working on the underlying ideas and Python prototypes for approximately three years. I initially learned by rebuilding and adapting examples from YouTube videos and other educational material. From that learning phase, I developed several of my own Python prototypes and revised them repeatedly as I learned what needed stronger controls, clearer evidence and better separation between research and operation.

## AI-assisted work and personal review

I use Codex and ChatGPT to support implementation, debugging, technical review and documentation. AI-assisted drafts are reviewed, revised and approved by me before publication. Project decisions and responsibility remain mine.

## What this public repository is

This repository is the public technical documentation record for AlgoSphere. It is the place to review the current documented status, observed gates, known blockers, evidence register and dated public updates. GitHub is the binding public technical source. The [Telegram channel](https://t.me/AlgoSphereOfficial) may share short summaries that link back here.

The repository intentionally does not publish private source code, credentials, environment files, wallet or account details, raw reports, databases, market data, trained models, checkpoints, strategy parameters, proprietary trading logic, private logs, personal information or internal paths.

## How to use this repository

Start with the current status, then read the test boundary and open blockers. Use the evidence register to confirm that an artifact was registered, not to infer that a result is independently reproduced. Historical updates retain their original numbers and are clearly labelled as snapshots.

## Start here

| If you want to review | Read |
|---|---|
| Current technical state and blocker | [Current status](CURRENT_STATUS.md) |
| Gates, tests and what was not rerun | [Test results](TEST_RESULTS.md) |
| Binding evidence summary and register guide | [Evidence summary](evidence/EVIDENCE_SUMMARY.md) |
| Project development history | [Project history](PROJECT_HISTORY.md) |
| Priorities and acceptance criteria | [Roadmap](ROADMAP.md) |
| Dated public changes | [Updates](updates/) |
| Security boundary and reporting route | [Security](SECURITY.md) |
| Financial and technical boundary | [Disclaimer](DISCLAIMER.md) |

## Verify the public export

From a public clone, run:

```text
python tools/verify_public_export.py
```

This script verifies the integrity of the public export. It does not reproduce private application tests and does not prove strategy quality, profitability or live-trading readiness.

## Interface preview

No suitable current, sanitised WebUI screenshots were found during this review, so no product image is published in this revision. Required future images are a sanitised dashboard overview, research status and runtime-safety view. Before publication, each must remove local URLs, internal paths, account data, private tabs, taskbar material, credentials, balances, strategy settings and sensitive runtime information.

When approved screenshots are available, their boundary notice will state: “The screenshots below show the current private AlgoSphere WebUI. They document the project’s development and operating model. The WebUI and the underlying application are not included in this public repository.”

## What visitors can verify

Visitors can verify that the documented export has an integrity manifest, that the report register has a stated schema and count, that public links resolve, and that observed scalar control values are presented with an artifact timestamp. Visitors can also inspect the Git history of this documentation repository.

## Limits of public verification

Public documentation cannot independently reproduce private code, data, model, configuration or strategy results. A reported PASS is not automatically an independently rerun test, and an entry in the report register is not automatically a passed test or completed development task. No page here establishes profitability, live-trading readiness, model success or a guaranteed project outcome.

## Control terms

- **Canonical-history integrity** checks whether the maintained historical record satisfies its documented integrity contract. A PASS is an observed artifact state, not a performance result.
- **Paper-watch guard** is a fail-closed control for the paper/watch boundary. A PASS means the observed guard artifact reported its passing state; it does not activate trading.
- **Runtime context gate** checks whether required runtime context is complete. A blocked state prevents treating the context contract as complete.
- **Research profile QUICK** is the observed research-autopilot profile label. It describes a report context, not a claim about quality or readiness.
- **Activation allowed** records whether the observed research artifact permits activation. `False` means activation is not allowed by that artifact.
- **Eligible experiments** records the observed count of experiments that meet that artifact's eligibility condition. It is not a count of profitable or live-ready systems.

## Community and support

- Public technical record: [GitHub](https://github.com/1545Christian/AlgoSphere)
- Short public updates: [Telegram](https://t.me/AlgoSphereOfficial)
- Voluntary support: [GitHub Sponsors](https://github.com/sponsors/1545Christian)

Voluntary support helps fund research, development, testing infrastructure and public technical documentation. Sponsorship is not an investment and provides no ownership, repayment, profit participation, financial return, trading signals, investment advice, exclusive access or guaranteed project outcome. See the full [Disclaimer](DISCLAIMER.md).

## Copyright and reuse

No open-source license is currently granted. Unless expressly stated otherwise, all rights are reserved. Publication of this repository does not grant permission to use proprietary source code, data, models, strategy materials or AlgoSphere branding.

<!-- HUMAN_TEXT_END -->

<!-- AUTO_VALUES_START: this section is generated from current scalar artifacts -->
## Current observed controls

| Control | Observed value | Source artifact (UTC) | Status meaning | Practical effect |
|---|---|---|---|---|
| Canonical-history integrity | `PASS` | `2026-08-31T18:14:41Z` | observed in current artifact | integrity gate reports its state |
| Paper-watch guard | `PASS` | `2026-08-31T16:15:22Z` | observed in current artifact | guard observation does not activate trading |
| Runtime context gate | `FAIL_INCOMPLETE_V3_CONTEXT` | `2026-08-31T16:15:22Z` | blocked | context is not treated as complete |
| Remaining runtime context cases | `7` | `2026-08-31T16:15:22Z` | blocked | highest-priority remediation remains open |
| Research profile | `QUICK` | `2026-08-31T20:00:38Z` | observed in current artifact | profile label only |
| Activation allowed | `False` | `2026-08-31T20:00:38Z` | observed in current artifact | activation is not permitted by the observed artifact |
| Eligible experiments | `0` | `2026-08-31T20:00:38Z` | observed in current artifact | no eligible experiment is reported |

Observed artifact snapshot: `2026-08-31T22:45:02Z UTC / 2026-08-31 23:45 Westeuropäische Sommerzeit Atlantic/Canary`. The main blocker is `FAIL_INCOMPLETE_V3_CONTEXT` with `7` remaining scoped cases.

Export integrity: verified. Application test suites: not rerun during this export. See [Current status](CURRENT_STATUS.md) and [Test results](TEST_RESULTS.md).
<!-- AUTO_VALUES_END -->
