# Durable facts and decisions

Verified 2026-11-07 (Europe/Vienna); evidence paths relative to workspace.

| Kind | Fact / decision | Evidence |
| --- | --- | --- |
| Observed | `root_manual` is a junction to `C:\Users\Fred_U\Documents\COPS\PMS`. | PowerShell `Get-Item root_manual` (LinkType/Target); recheck per session. |
| Observed | Local Git excludes the source junction; exclusion is not a tracked portable rule. | `.git/info/exclude`, `/root_manual/`. |
| Observed | Generated German RoboHelp 11/WebHelp 5.50 manual, 24,500 files at inspection. | `root_manual/Handbuch/de/index.htm`; recursive inventory in `docs/PROJECT_MAP.md`. |
| Observed | Two change-log folder spellings exist; Unicode tree also has a PMS 12 topic directory. | `root_manual/Handbuch/de/03-pms_aenderungsprotokolle/` and `03-pms_änderungsprotokolle/`. |
| Observed | Tables, ER diagrams and ITF documentation have dedicated topics. | `Handbuch/de/01-pms_online_handbuch/appx_g-datenbanktabellen_de/`, `appx_k-er-diagramme_de/`, `Handbuch/de/02-pms_online_standardschnittstelle/`, all below `root_manual`. |
| Observed | Sample foreword refers to absent shared CSS. | Foreword topic line 11; `root_manual/Handbuch/de/RHStyleMapping.css` does not exist. |
| Observed | Overlapping change-log paths are not equivalent: 736 shared paths, 463 identical and 273 different by SHA-256; 444 Unicode-only files. | Reviewer full relative-path/hash comparison, 2026-11-07; `docs/REVIEW.md`. |
| Decision | Keep linked source unchanged; persist compact evidence-based Markdown outside it. | User requested analysis, reusable LLM definition and small external memory; `AGENTS.md`. |
| Decision | Future substantial analysis uses orchestrator -> analyst -> independent reviewer. | User requested agent orchestration/review; `AGENTS.md`. |
| Observed | Database research compares all six stacks separately: Neo4j, PostgreSQL/AGE/pgvector, ArangoDB, GraphDB, Jena/Fuseki and Neptune. Neo4j is the provisional private-first preference; all six are in the follow-up evaluation plan. No database has been selected, deployed or benchmarked. | `docs/DATABASE_RESEARCH.md` and `docs/DATABASE_COMPARISON.md`, dated 2026-11-07; corresponding research/comparison review files. |
| Observed | Diagnostic profile of the four topic trees finds 351 HTM files, approximately 17,033,754 text characters and 4,044 table elements, with no native h1-h6 tags. These include duplicate content; Word-style paragraphs require structural parsing. | `docs/research/CORPUS_PROFILE.json`; reproducible diagnostic `docs/research/profile_corpus.py`; methodology/limits in database research. |

Open: deployed PMS version/architecture, source authoring files, complete link integrity, modern browser compatibility and authoritative choice between overlapping change-log trees are unverified. No assumption of always-running agents or automatic memory updates.

Detailed source test specification (2026-11-07): `docs/SOURCE_TEST_CASES.md` defines 15 source-derived cases and 8 separately labeled synthetic update/failure cases, with exact topic/heading pointers and all-six design implications. It includes conditional ITF rules, a three-edge dependency chain, diagram evidence and two branch-comparison cases. These are expected-answer specifications, not passed retrieval/database tests. Independent source/design review and operational evaluation are in `docs/IMPLEMENTATION_REVIEW.md` and `docs/IMPLEMENTATION_EVALUATION.md`.

Resumed planning review (2026-11-07): analyst and separate reviewer independently checked S01–S15, including the diagram and raw/normalized branch hashes. The normalization specification now explicitly replaces tags with spaces. README milestone order and outline synthetic stress-graph labels were clarified. See the implementation review/evaluation for closure and limits.

Local implementation (2026-11-07): first capture/extraction/validation slice and synthetic tests in `src/` and `tests/`; ten frozen evidence hashes verified via `evaluation/verify_source_evidence.py`. Independent code findings and results: `docs/PIPELINE_REVIEW.md`; scope/commands: `docs/IMPLEMENTATION_STATUS.md`. Gates 1/2 are incomplete, later service/runtime gates unrun. Preflight found PostgreSQL 18.1 and pgvector 0.8.1 files but no AGE or usable WSL/container runtime in inspected locations (`docs/COMPATIBILITY_STATUS.md`). Tracked `.gitignore` excludes source/runtime data; never publish the external manual.

Continuation, 2026-11-07: user prioritizes open-source, easy incremental updates, fast local/cloud transfer and access from both locations. `docs/IMPLEMENTATION_OPTIONS.md` and `docs/PROJECT_OUTLINE.md` propose PostgreSQL/AGE/pgvector as the conditional planning preference, portable immutable revisions and one publishing authority. This supersedes the earlier preference only for the new scenario; all six candidates remain, and none is selected/deployed/benchmarked. Review status and limits: `docs/IMPLEMENTATION_REVIEW.md`. Junction target and four topic-tree HTM counts (351 total) were rechecked; full inventory/profile was not recomputed. Exact dependency versions, host/budget, offline access policy, recovery/latency targets and performance remain open.
