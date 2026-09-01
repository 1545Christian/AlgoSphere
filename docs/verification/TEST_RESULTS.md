# Test and gate results

<!-- HUMAN_TEXT_START -->

## Reading the table

Each row identifies a control or gate, its purpose, its latest observed artifact timestamp, whether it was independently rerun in this export, the observed result, an evidence reference and a limitation. A passing observed artifact is not rewritten as a newly executed test.

## Export checks

Export checks validate the documentation package itself: allowlist, manifest hashes, archive readability, links and privacy scanning. They do not validate the private application.

## Application tests

Application test suites are only described as independently rerun when this export actually performs them. Otherwise the page says “not rerun during this export.”

<!-- HUMAN_TEXT_END -->

<!-- AUTO_VALUES_START -->
| Gate or test | Purpose | Last observed artifact (UTC) | Independently rerun in this export | Observed result | Evidence reference | Limitation |
|---|---|---|---|---|---|---|
| Canonical-history integrity | historical-record integrity | `2026-09-01T00:00:56Z` | No | `PASS` | `canonical_history_integrity.json` | observed artifact only |
| Paper-watch guard | paper/watch boundary guard | `2026-08-31T16:15:22Z` | No | `PASS` | `paper_watch_guard_last.json` | observed artifact only |
| Runtime context gate | required runtime-context completeness | `2026-08-31T16:15:22Z` | No | `FAIL_INCOMPLETE_V3_CONTEXT`; `7` cases | `runtime_entry_snapshot_coverage.json` | blocked; not independently rerun |
| Research autopilot | research eligibility boundary | `2026-09-01T00:25:51Z` | No | `QUICK`, activation `False`, eligible `0` | `research_autopilot_last.json` | observed artifact only |

| Export check | Result |
|---|---|
| Fixed allowlist | PASS |
| SHA-256 manifest | PASS |
| ZIP readability | PASS |
| Internal Markdown links | PASS |
| Secret and privacy patterns | PASS |
| Application test suites | Not rerun during this export |
<!-- AUTO_VALUES_END -->
