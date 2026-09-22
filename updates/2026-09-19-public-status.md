# Public status update — 2026-09-19

Deutsch: [Öffentliches Status-Update](./2026-09-19-public-status_DE.md)

## Summary

September 19 focused on three recurring project problems: Canonical Memory / V2 lineage, Research-storage growth, and WebUI truth/clarity.

Important progress:

- The current and shadow research projections were repaired and browser-checked with stable state.
- The shadow research path now consumes governed learning evidence in addition to market context.
- New shadow-path writes enforce required state evidence more strictly; a narrowly scoped historical repair remains blocked by an active writer.
- A Research→Canonical handoff loss was identified and fixed for future writes; compact research evidence is now preserved across the boundary.
- A large research-storage growth issue was traced to duplicate representations inside future snapshots. The future writer was reduced materially without deleting historical evidence. Exact schema and field names are intentionally not published.
- The WebUI table/filter contract was made more stable and compact while preserving larger readable text and tooltips.
- No training, replay, promotion or live activation was triggered by these repairs.

The main scientific problem is still unchanged: more infrastructure now works, but ML uplift and a fully closed learning loop are not yet proven.

## Canonical Decision / Learning contract

The project continues to converge on one comparable chain:

`Decision → Research candidate → simulated/counterfactual outcome → evidence memory → learning → lifecycle`

The audit showed that the chain is still uneven by lane/variant.

Known gaps remain around some historical identity, lineage and population-consistency evidence. Exact field names and lane mappings are intentionally not published.


New CONTEXT_V2 decisions/outcomes now fail closed when required state evidence is missing.

### Historical exact-only repair

A narrowly scoped historical repair exists, but the apply remains incomplete because an active writer prevented a safe maintenance state. The system intentionally did not force writes around that condition. Exact schema, table names and join keys are intentionally not published.

## CONTEXT_V2 now consumes Canonical Learning Delta

A concrete missing connection was fixed:

`governed learning evidence → shadow research selection`

The existing learning engine and Strategy × State Matrix were reused.

For new shadow research decisions, the system can trace how governed evidence changed a selection outcome. Exact score components and decision fields are intentionally not published.


CURRENT remains the control path and is unchanged.

Counterfactual / NO_TRADE evidence is not counted as an executed trade.

Focused runtime/canonical/learning checks passed; exact internal test counts are intentionally not published.

## Trade Like Che WebUI and V1/V2 separation

The Trade Like Che view was repaired in several layers.

Confirmed fixes cover population separation, refresh-stable UI state, preservation of existing evidence, and clearer pending/outcome presentation. Exact identifiers, internal host aliases and field names are intentionally not published.


The table contract was standardized for readability and compact display. Exact CSS/layout constants are intentionally not published.


A browser-verified checkpoint confirmed consistent current/shadow projections. Exact population counts are intentionally not published.


These are UI/runtime evidence counts, not proof that the historical Canonical population is fully comparable.

## Research storage root cause

Research storage had grown substantially. The root cause was duplicate internal representations inside future snapshots rather than duplicate whole snapshots. The future writer was corrected while historical evidence remained untouched. Exact database sizes, row counts, schema names and duplicated field pairs are intentionally not published.

## Research evidence handoff

A second Research-side handoff gap was found before the evidence-memory boundary. A compact future-only evidence subset is now projected forward, while full private research payloads remain private. Natural forward proof is still pending; no historical reprojection is currently required.

## What remains open

1. Execute the scoped historical repair only when the active writer can be safely paused; do not force around the lock.
2. Resolve the remaining simulated-population mismatch before claiming fully comparable learning populations.
3. Prove the new Research handoff on the next natural research run.
4. Finish the remaining evidence-population contract for new writes and classify historical gaps without inventing values.
5. Continue prospective control-vs-shadow outcome collection; current UI counts are not enough to claim V2 is better.
6. Keep ML uplift as an open scientific question; infrastructure progress does not prove predictive improvement.
7. Continue WebUI simplification, especially reducing oversized header/filter regions while preserving stable state and readable tables.
8. Preserve the new future research-snapshot writer; any historical storage cleanup must remain a separate, evidence-based migration decision.

## Safety boundary

`LIVE=false` · `REAL_CAPITAL=0` · automatic promotion disabled.

No documentation update authorizes live trading, forced historical repair, automatic model promotion or real-capital execution.

[Current status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Documented work](../docs/progress/COMPLETED_WORK.md) · [Test results](../docs/verification/TEST_RESULTS.md)
