# Publication transport and history

The publisher reads and writes the approved repository using the GitHub Git Data API. It does not create a local clone, run a trading process or publish private Git history.

The commit is based on the current remote tree and uses a non-forced branch update. The authenticated account, before/after commit IDs and changed paths are recorded in the local run receipt. Dry runs do not contact GitHub. No future commit ID is guessed inside this pre-commit artifact.

The generated manifest covers the current staged publication, not every historical page already in the repository.
