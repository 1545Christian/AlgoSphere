# Contributing to AlgoSphere

Thanks for taking an interest in the project.

AlgoSphere is currently an independent research project, not an open-source trading product. The private trading/runtime code, credentials, trained models and proprietary strategy parameters are not part of this repository.

That said, useful public contributions are welcome.

Before contributing, please read the [Public Repository Scope](docs/project/PUBLIC_REPOSITORY_SCOPE.md) so it is clear which parts of AlgoSphere are public and which remain private.

## Good ways to contribute

You can help by reporting:

- documentation errors or outdated links
- inconsistencies between public status and public evidence
- reproducible UI/documentation issues
- research questions worth testing
- references to relevant papers, methods or validation approaches
- unclear wording that could give a misleading impression

## What makes a useful issue?

Please include:

- what you expected
- what you observed
- where you saw it
- a screenshot or public file reference when useful
- why you think it matters
- whether the issue is about documentation, evidence, research methodology or public UI

For research ideas, explain the hypothesis rather than only suggesting a model or indicator.

For example, “test model X” is less useful than:

> I think this method may improve regime-specific calibration because …  
> Here is the paper / evidence …  
> I would compare it against the existing Rule baseline on the same OOS folds.

## What is out of scope?

Please do not post:

- API keys, account IDs or credentials
- private trading configuration
- proprietary strategy parameters
- personal financial information
- requests for guaranteed returns or trading signals
- claims of profitability without reproducible evidence

## Pull requests

Small documentation corrections are welcome.

By submitting a contribution, you agree that it may be distributed under the license that applies to the part of the repository you are changing: public documentation/evidence under CC BY-SA 4.0, and the small public verification tools under MIT. See [Licensing](docs/legal/LICENSING.md).

Larger code or architecture changes should first be discussed in an issue. This public repository is mainly a documentation/evidence layer, so not every internal implementation change belongs here.

## Research principles

Contributions should respect the same principles used by the project:

- causal data only
- no hidden future information
- preserve negative evidence
- compare Rule and ML fairly
- separate Paper, Watch, Research, OpenAI and Counterfactual evidence
- do not turn technical completion into a performance claim
- reproducibility before promotion

## Questions

For common questions, see [docs/FAQ.md](docs/FAQ.md).

For short public project updates, see the Telegram channel linked in the README.

## Before you submit

A good public contribution should be understandable without access to the private AlgoSphere application.

Before opening an issue or pull request, check that:

- the claim can be supported by public evidence or is clearly presented as a question/hypothesis
- no private paths, credentials, account data or proprietary parameters are included
- current and historical states are not mixed
- a technical PASS is not described as a profitability result
- any external paper, article or method is linked to its original source where possible

If you are unsure which route to use, start with the [FAQ](docs/FAQ.md) or [Support](SUPPORT.md).
