# Public repository scope

This repository is the public documentation and evidence layer for AlgoSphere.

It is not a downloadable release of the private trading application.

## What is public here

The repository may contain:

- project status and dated updates
- research methodology and lifecycle documentation
- validation and verification summaries
- selected public evidence exports
- roadmap and completed-work records
- FAQ, contribution and support information
- small verification scripts/tests used to check the public export itself

## What is not public here

The repository intentionally excludes:

- the private trading/runtime application source
- credentials, API keys and account configuration
- exchange account data
- private market databases and raw operational logs
- trained model bundles/checkpoints
- proprietary strategy names, parameters, thresholds and signal formulas
- exact feature sets, labels, weights, scoring/ranking logic and model hyperparameters
- exact entry/exit rules, prices, position sizing, leverage, stop/target logic and risk configuration
- private venue-selection, retry, failover and execution-routing logic
- internal schema/table/column names where they reveal implementation structure
- private prompts/contracts, field mappings, queue names and runtime topology
- deployment, infrastructure and operational-security details
- combinations of otherwise harmless details that materially reduce the work needed to reconstruct the private system


The presence of small public verification tools under tools/ or tests/ does not mean the AlgoSphere trading application is open source.

## Why publish the documentation at all?

The purpose is to keep a public, reviewable but reconstruction-resistant record of what has actually been built, tested, rejected, improved and left unresolved.

That includes negative results, but only at a level that does not expose reproducible private trading logic.

A public status should make it possible to distinguish:

- implemented
- tested
- observed in runtime
- proven prospectively
- still awaiting evidence
- deliberately not public

## Releases and downloads

No public application download is currently offered from this repository.

If a future Demo or client package is released, it will be documented as a separate release track with its own integrity, configuration, permission and safety boundaries.

Until then, repository visibility should not be interpreted as product availability or live-trading readiness.

## Licensing

Public documentation and public evidence authored for this repository are licensed under **CC BY-SA 4.0**, unless a file says otherwise.

The small public verification tools under `tools/` and `tests/` use the **MIT License**.

These licenses apply only to material actually published in this repository. Public documentation is intentionally descriptive rather than implementation-complete. They do not license the private AlgoSphere application, unpublished models, private strategy material, credentials, account data or infrastructure.

See [Licensing](../legal/LICENSING.md).
