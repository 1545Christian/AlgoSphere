# Test results and verification limits

## September 16 focused verification

The following focused suites were reported during the latest repair work:

- OpenAI AI Market Analyst V2 relevant regression suite: **263/263 PASS**
- Unified trade-memory relevant suite: **264 PASS**
- Final focused suite after the last memory changes: **121 PASS**
- ADX / indicator-display focused suite: **154 PASS**
- Trade-Like-CHE entry projection focused suite: **22 PASS**
- Compact WebUI/table rendering focused suite: **14 PASS**

Additional checks reported during the same work included:

- Python compilation: PASS
- JavaScript syntax: PASS
- real Bitget data fetch: PASS
- real OpenAI V2 call: PASS
- WebUI API checks after visible restart: PASS at the relevant checkpoint
- visible runtime restart / safety rebind: PASS at the relevant checkpoint

These are meaningful scoped checks. They are **not equivalent to a complete project-suite acceptance**.

## Full-suite boundary still open

An earlier full-suite checkpoint from the broader project review recorded:

- total tests: **1,307**
- failures: **64**

The focused green suites above do not prove that every one of those earlier failures has been resolved. A complete suite rerun after the current runtime/data-source repair is still required, with every remaining failure either fixed or explicitly classified as intentional/non-blocking.

Until then, do not present the project as globally test-clean.

## Runtime acceptance still separate from tests

A unit/regression PASS does not by itself prove:

- Research Forward survives a fresh direct Bitget refresh without the current `WinError 10013` problem,
- `START_ALGOSPHERE.cmd` behaves correctly for already-running and truly stopped/orphaned states,
- Forecast propagation and Research open-position visibility are correct after restart,
- Capture and NO_TRADE render correctly in the final running browser state,
- OpenAI V2 is profitable or scientifically superior.

Those require runtime / browser / outcome evidence in addition to tests.

## Earlier documented verification

- **2026-09-05:** Factory identity fix had 15 passing focused tests documented.
- **2026-09-06:** Installed publisher module passed its bundled offline regression suite locally.
- **2026-09-13:** Paper/Watch guard report observed PASS; runtime context gate still reported `FAIL_INCOMPLETE_V3_CONTEXT` at that time.

## Publication verification boundary

The public documentation records reviewed engineering/test evidence. It does not independently rerun the private application test suite or certify live readiness.

[Current status](../../CURRENT_STATUS.md) · [Reviewed September 17 update](../../updates/2026-09-17-public-status.md) · [Roadmap](../progress/ROADMAP.md)
