# PMS manual assistant: project definition

This workspace contains corpus analysis, an implementation outline and a first local capture/extraction/validation package for a source-grounded PMS manual assistant. No database has been selected, deployed or benchmarked. The external `root_manual` junction is read-only.

## Start here

Current workspace: `C:\Users\Fred_U\Dropbox\AI\chatbot_manual`. See the [project tracker](docs/PROJECT_TRACKER.md) for reviewed milestone status, priorities, dependencies, decision gates and next work.

To start implementation, use the [execution handoff](docs/IMPLEMENTATION_HANDOFF.md). It requires checking existing apps before installing missing dependencies and continuing through independent review to usable operation. The [readiness audit](docs/READINESS_AUDIT.md) records verified software and the remaining old-path app/test references.

Read `AGENTS.md`, the project skills, `docs/LLM_CONTEXT.md` and `.project-memory/README.md` before working. `docs/HANDOFF_PROMPT.md` identifies the earlier research and its review limits.

The current planning work responds to priorities of open-source components, simple data updates, efficient local-to-cloud transfer, and local plus cloud access:

- [Implementation options](docs/IMPLEMENTATION_OPTIONS.md): reassesses all six database candidates under these priorities.
- [Project outline](docs/PROJECT_OUTLINE.md): proposed modules, update/publication protocol, deployment stages and acceptance gates.
- [Implementation review](docs/IMPLEMENTATION_REVIEW.md): independent findings, corrections and remaining verification limits.
- [Source-derived test cases](docs/SOURCE_TEST_CASES.md): detailed manual evidence, expected answers and case-driven all-six evaluation.
- [Independent evaluation](docs/IMPLEMENTATION_EVALUATION.md): operational tradeoffs and test-coverage assessment.

The outline defines a proposed service; the local package implements only its initial neutral bundle slice. Current scope and commands are in [Implementation status](docs/IMPLEMENTATION_STATUS.md), with [runtime preflight](docs/COMPATIBILITY_STATUS.md) and [independent code review](docs/PIPELINE_REVIEW.md). Prior research remains available in [the all-six comparison](docs/DATABASE_COMPARISON.md) and [the architecture research](docs/DATABASE_RESEARCH.md), with their corresponding review files.

## Working boundary

Keep generated bundles, databases, credentials and runtime output outside `root_manual`. Preserve both change-log branches and exact Unicode source paths. A database-neutral evidence manifest should make derived data rebuildable in any of the six candidate stacks.

After planning review, begin Gate 1 engine/version qualification alongside the independent Gate 2 neutral contracts and synthetic fixtures. Validate extraction before incremental transfer and serving; compare retrieval and recovery only with equivalent reviewed inputs. A failed first engine spike does not block neutral pipeline work. Cloud deployment details and source-transfer rights remain implementation inputs; this planning work uploads no manual content.
