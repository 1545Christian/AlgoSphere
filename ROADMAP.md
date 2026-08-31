# Roadmap and open blockers

<!-- HUMAN_TEXT_START -->

The roadmap lists concrete verification work, not performance promises. A task is only accepted when its stated evidence and acceptance criterion are met.

<!-- HUMAN_TEXT_END -->

<!-- AUTO_VALUES_START -->
| Priority | Task | Current status | Dependency | Acceptance criterion | Required evidence | Next concrete step |
|---|---|---|---|---|---|---|
| P0 | Resolve `7` runtime-v3 context cases | blocked | complete runtime context | no remaining scoped failures | fresh gate artifact | isolate missing context |
| P0 | Independently rerun runtime context gate | not verified | P0 remediation complete | independent gate run has current passing result | dated rerun output | run the scoped gate after remediation |
| P1 | Prove Watch Scanner and Watch Exit Evaluator | not proven | fresh witnesses | both components have current evidence | dated runtime-health projection | collect fresh witnesses |
| P1 | Analyse QUICK resource stop | observed operational result | reproducible resource measurement | cause and threshold behaviour are measured | bounded resource report | reproduce without activation |
| P1 | Measure memory limit and actual use reproducibly | not verified | safe measurement plan | measurement is repeatable and bounded | dated measurement artifact | define scoped measurement |
| P1 | Prove F_META independent QA and new terminal Active-Paper decision | not proven | independent QA and new terminal witness | both conditions are met | QA artifact and terminal witness | keep claim blocked until both exist |
| P1 | Keep activation fail-closed | observed boundary | incomplete evidence | activation remains disallowed | current scalar artifact | preserve disabled state |
| P2 | Define retention policy for lineage, checkpoints and referenced backups | open | explicit retention decision | deletion rules are reference-complete | approved policy and audit | define policy before deletion |
| P2 | Maintain sanitised public WebUI demo images | open | approved real screenshots | images pass privacy review | sanitised image review | obtain real screenshots |
| P2 | Maintain public export verifier | ongoing documentation work | public fixtures | verifier and tests pass | public test output | rerun before publication |
| P2 | Keep English and German communication consistent | ongoing documentation work | human review | corresponding guidance agrees | language review | review before publication |
<!-- AUTO_VALUES_END -->
