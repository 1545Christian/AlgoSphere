# Roadmap and open blockers

<!-- HUMAN_TEXT_START -->

The roadmap lists concrete verification work, not performance promises. A task is only accepted when its stated evidence and acceptance criterion are met.

<!-- HUMAN_TEXT_END -->

<!-- AUTO_VALUES_START -->
| Priority | Task | Current status | Dependency | Acceptance criterion | Required evidence | Next concrete step |
|---|---|---|---|---|---|---|
| P0 | Resolve `7` runtime-context cases | blocked | complete runtime context | gate has no remaining scoped failures | fresh gate artifact and independently rerun applicable check | isolate and resolve missing context |
| P1 | Re-run applicable gate after remediation | not verified | P0 complete | current evidence is independently rerun | dated test/gate output | run only safe, scoped verification |
| P1 | Keep activation disabled while evidence is incomplete | observed boundary | P0 unresolved | activation remains disallowed until evidence supports change | current scalar artifact | preserve fail-closed state |
| P2 | Maintain sanitised public evidence documentation | ongoing documentation work | human review | public texts and generated values remain separated | validated export and manifest | review before publication |
<!-- AUTO_VALUES_END -->
