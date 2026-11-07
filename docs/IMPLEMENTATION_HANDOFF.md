# Implementation handoff: continue to usable completion

Prepared 2026-11-07 (Europe/Vienna). This is an execution brief for the next implementation session, not a claim that implementation or installation is complete. Read [READINESS_AUDIT.md](READINESS_AUDIT.md) and [HANDOFF_REVIEW.md](HANDOFF_REVIEW.md) for the checked starting state and review limits.

## Copy this prompt to start

```text
Work in C:\Users\Fred_U\Dropbox\AI\chatbot_manual.
Read and follow docs/IMPLEMENTATION_HANDOFF.md and the startup instructions it references.
Start implementation now and continue through installation, integration, testing,
independent review and operator verification until the project is usable and all
applicable completion criteria are satisfied. Do not stop after a plan, one milestone,
the first passing test suite, or a scaffold.
Use an orchestrator -> worker -> independent reviewer -> evaluator -> correction
loop. Check which apps, runtimes, packages and services already exist before installing
anything. Reuse compatible installations safely; install missing required components
from official sources, then verify the actual running setup. Preserve existing services.
Keep the external PMS manual read-only. Keep raw/derived private corpus data and secrets
out of the public GitHub repository and outside Dropbox-synchronized runtime storage.
Update docs/PROJECT_TRACKER.md and durable handoff evidence after each accepted increment.
Continue independent local work while external inputs are pending. If a genuine
external dependency prevents remaining work, record the exact blocked item and required
user action; never call unrun or blocked acceptance criteria complete.
```

## 1. Startup and working directory

The authoritative code workspace is `C:\Users\Fred_U\Dropbox\AI\chatbot_manual`. Set every shell call's working directory explicitly and verify `git rev-parse --show-toplevel` before writing. Do not rely on the inherited chat working directory: the inspected Codex project registration and current chat still point at the former location. For a new implementation chat, open/add the new folder in the app. If that app step is still pending, explicit working-directory calls allow useful work in the correct repository.

Read in order:

1. `AGENTS.md`, `SKILL.md`, `SKILL_Mem.md`.
2. `docs/LLM_CONTEXT.md`, `.project-memory/README.md`, `.project-memory/facts.md`.
3. `docs/READINESS_AUDIT.md`, `docs/PROJECT_TRACKER.md`, `docs/IMPLEMENTATION_STATUS.md`, `docs/COMPATIBILITY_STATUS.md`.
4. `docs/PROJECT_OUTLINE.md`, `docs/IMPLEMENTATION_OPTIONS.md`, `docs/SOURCE_TEST_CASES.md` and their implementation review/evaluation records.
5. Current `src/`, `tests/`, `evaluation/`, `pyproject.toml`, `.gitignore`, Git diff/status and the existing reviews. Read the original research/map only for details needed by the current change.

Preserve uncommitted tracker/relocation/handoff updates; these are intended project work. The published baseline was `38ce618` on `master` at preparation time; inspect current HEAD rather than assuming it remains unchanged. The public remote is `https://github.com/artprof964/chatbot_Manual.git`. Do not reset, overwrite or force-push unrelated work. Use `codex/` for new implementation branches.

Verify `root_manual` is still a junction to `C:\Users\Fred_U\Documents\COPS\PMS`, and that the expected German source is readable. Preserve both change-log spellings. The ignored synthetic test junction with an old target is a known residual fixture, not a source dependency; do not repair it by recreating the old workspace. Earlier cleanup was policy-blocked: do not bypass that rejection or treat cleanup as a prerequisite for implementation.

## 2. Starting state and completion scope

The project currently implements local capture, structural HTML extraction and bundle validation only. The verified baseline is 14 passing tests, one skipped symlink test and ten matching source fingerprints. This is not an operational chatbot, database adapter, incremental receiver, publication service or API. The 15 source cases are reviewed specifications; the fingerprint registry does not implement semantic answer tests.

This brief supersedes the **planning-task stopping condition** in PROJECT_OUTLINE section 11 for the new implementation session. Retain that document's design invariants and acceptance gates. An accepted plan or partial Gate 2 is not the new stopping condition.

Deliver one maintainable graph-grounded manual assistant that an operator can install, launch, update, query with citations and recover. Support local use and a validated cloud deployment path using the same data/API contract. Complete actual cloud verification when an authorized account, region, budget and source-processing policy are available. Until then, finish all independent local work and mark the remaining cloud criteria blocked, not satisfied by a local mock.

Preserve six evaluation candidates: PostgreSQL/AGE/pgvector, Neo4j, ArangoDB, GraphDB, Jena/Fuseki and Neptune. Qualify PostgreSQL/AGE/pgvector first under current priorities, but switch to a retained alternative if evidence warrants it. Do not install six production backends merely to complete a checklist. Keep six comparable qualification/result sheets; distinguish tested, failed and unavailable/untested. Explain the final chosen deployment using evidence, and retain the limits of any incomplete comparison. Optional offline mirroring is required only if selected; connected local access alone does not prove offline capability.

## 3. Discover existing apps before installation

Freshly inspect before each installation or upgrade; the audit is dated evidence, not a permanent machine inventory. Inspect PATH **and** common installation locations/uninstall registry entries, executable versions, relevant services, selected ports and runtime state. Do not use `Win32_Product`, which can trigger installer repair. Do not dump environment variables, credentials, connection strings or unrelated account data.

Record each required component in an installation ledger with role, discovered path/version, installed/running/usable state, license/source, compatibility evidence, action (reuse/configure/install/defer), pinned resulting version/digest, verification command and rollback/removal procedure. Check at least:

| Component | Required discovery / decision |
| --- | --- |
| Python and packaging | Existing interpreters, declared minimum version, project virtual environment, build/install support; do not change global packages when an isolated environment suffices |
| Git/GitHub tooling | Git version, repository status/remote and available authentication; reuse authorized access without revealing tokens or blindly reinstalling tools |
| Linux/container runtime | WSL installation/distributions and feature/reboot state; Docker/Podman executable plus actual daemon/server availability; prefer one suitable existing runtime |
| Graph database stack | Existing PostgreSQL services/binaries, AGE and pgvector files plus actual extension loads in a **separate** disposable cluster; alternatively inspect the selected retained engine |
| Models and serving | Existing local model runner, model inventory/licenses, CPU/RAM/GPU/disk fit and service health; install only the chosen model/runtime, not every possible runner |
| Interface/toolchain | Node/browser/build tools only if the selected user interface needs them; a simpler supported interface may avoid additional runtimes |
| Deployment/operations | Existing cloud CLI/runtime, object storage, backup and logging tools only for the chosen deployment; verify authorization without exposing credentials |

The prior preflight found PostgreSQL and pgvector files but no AGE and no usable WSL/container runtime in the inspected setup. A binary on disk does not establish a working service; an existing service does not grant permission to repurpose its data. Use distinct project-owned ports, volumes, database names and credentials. Inspect collisions before starting anything. Never stop or reconfigure an unrelated database to make a test pass.

Necessary routine installations/configuration for this implementation are within the user's requested scope. Do not stop merely to ask permission to install an ordinary missing dependency from an official vendor or reputable package registry. Verify current official release compatibility, licensing, checksums/signatures and supported OS/architecture before choosing versions; record exact artifacts rather than silently using `latest`. Existing product claims in research are not deployment pins. Follow higher-priority approval rules when a specific action requires them. Request user participation only for genuine administrator/UAC interaction, reboot coordination, account/credential input, legally required license acceptance, paid resources/budget, broader security access or source-transfer authorization that has not already been established. Do not reboot automatically or expose database ports publicly. Continue unaffected work while waiting.

After installation, run version, health, extension/model load and functional smoke tests. Verify launch after a fresh shell/service restart, and document any reboot still required. Installed-but-unverified is a separate state from usable. Do not overwrite existing installations simply because they are absent from PATH.

## 4. Runtime layout and source boundary

Keep code, synthetic fixtures and configuration templates in the Dropbox repository. Use a configured **non-synchronized** runtime root, initially `%LOCALAPPDATA%\manual-knowledge` subject to checking the resolved location, for live database volumes, model caches, generated private corpus bundles, logs and backups pending a separate backup policy. Keep credentials in an appropriate local secret store or restricted untracked configuration outside Dropbox. No live database should depend on Dropbox file synchronization. Git ignore rules do not govern Dropbox, and Dropbox synchronization is not an application-consistent database backup.

Keep the external manual read-only and never copy it to GitHub, public CI, remote model services or cloud storage without the relevant explicit authorization. The public-repository authorization covers code/analysis, not raw/derived manual data. Run CI against synthetic fixtures; run private evidence tests locally. An install/run workflow must make source and data paths explicit, reject unsafe overlaps and preserve Unicode/branch identity.

## 5. Agent execution and correction loop

The orchestrator owns the current plan, task dependencies, acceptance evidence and coherent integration. Use the current tracker IDs; split large tasks into bounded increments with ownership and file boundaries. Parallelize only independent work, such as neutral contracts/CI and runtime discovery. Do not have two workers edit the same files without coordination.

For each increment:

1. Worker inspects the relevant source/code and implements the smallest complete change with meaningful tests and installation/configuration evidence where applicable.
2. A separate reviewer inspects the actual diff and independently checks invariants, errors, source fidelity, path safety and tests. The author cannot self-certify independent review.
3. Evaluator checks operability, maintainability, user workflow, candidate fairness and whether acceptance evidence establishes the claimed outcome. Reuse a separate evaluator across increments; do not invent measured rankings.
4. Record findings with ID, severity, evidence, correction and status. Worker fixes findings, reviewer rechecks the changed result, and evaluator revisits any affected operational conclusion. Repeat until blocking/high findings are closed; record remaining nonblocking risks and rationale.
5. Update tracker/status/memory with concise verified facts, exact commands/results and open dependencies. Commit coherent reviewed changes while preserving unrelated edits. Before an authorized push, verify no raw corpus, generated runtime data or secrets enter the public repository. Do not assert a push succeeded without matching the remote commit.
6. Start the next ready task immediately. Do not end the project because one milestone or review loop completed. Agents are invoked workers, not an always-running service.

If an agent/tool becomes unavailable, preserve its unfinished review status and continue safe independent work. Resume independent validation when available; do not relabel self-review as independent acceptance. If every remaining task requires external action, report each precise blocker, the attempted checks, the work completed and the smallest next action. Budget/usage/policy limits remain real limits; never bypass them or claim completion to end the loop.

## 6. Implementation sequence

1. **T03/T04 plus T07:** establish reproducible synthetic CI/package checks and neutral evidence schemas/identities/source mappings while discovering/reusing/installing an isolated runtime. Maintain the existing working baseline.
2. **T05/T06/T08:** turn source cases into executable expected-evidence and forbidden-assertion checks; cover revision rename/delete/image/config changes. Qualify the released graph stack, mixed transactions, exact filtered retrieval and fresh restore using synthetic data.
3. **T09–T11:** implement deterministic reusable segments, parent/delta contracts, staging receiver, retry/reconciliation, fenced publication and reader-safe retention. Test corruption, crashes, stale workers, concurrent publishers and lost responses before making publication available.
4. **T12/T13:** implement native graph/text/vector retrieval and one authenticated user-facing query path, with revision-pinned evidence and clear unknown/conflict responses. Choose a model that fits measured hardware/license requirements; test German questions and exact codes. Add a documented launcher/stop/update/health workflow, not just developer modules.
5. **T14:** expand reviewed questions to 50–100 and compare the retained candidates with equivalent evidence/conditions. Question preparation can begin after T05; full comparative execution needs working adapters and agreed workload. Separate extraction, engine, model, transfer and rebuild costs.
6. **T15/T16:** complete authorized cloud operation and measured transfer/rebuild behavior, then cold restore, upgrade/rollback and operator acceptance. Produce reproducible install/deployment artifacts, locked versions, runbooks and a compatibility record. Install/verify the selected runtime on each actual target rather than assuming local success proves cloud readiness.
7. **T17 only if selected:** implement a read-only offline mirror with independent local leases/retention, revision freshness and bounded authorization. Test disconnected operation and reconnection; do not imply immediate remote revocation is possible offline.

## 7. Definition of finished

Use a release acceptance table with **Pass / Fail / Blocked / Not applicable**, evidence links, environment/version and reviewer. No “Done” without evidence. All mandatory rows must pass for full completion; optional rows need an explicit applicability decision. Unavailable all-six comparisons remain disclosed and cannot support a claim of exhaustive empirical superiority.

| Area | Required operator-visible or reproducible result |
| --- | --- |
| Installation | Existing-app inventory completed; only needed missing components installed; isolated pinned runtime healthy; project setup reproduces from a clean environment; existing services preserved |
| User access | Documented launch starts a usable query interface; operator can stop/restart it, see health/errors and reach the same authenticated contract locally and on the authorized cloud target |
| Ingestion/evidence | Actual authorized local manual capture succeeds with preserved branches/codes/tables/image provenance; all seed oracles pass or source ambiguities are explicitly handled; unresolved image semantics are not fabricated |
| Answer quality | Ask representative German questions, inspect cited source/version and follow evidence links; exact identifiers, conditions, unknowns and conflicting branch claims preserved; agreed reviewed question set passes documented thresholds |
| Updates | No-change and small-change updates measured; interrupted/corrupt retries recover; rename/delete/image/config changes handled; no mixed-revision answers or missing leased evidence |
| Graph/retrieval | Selected real graph engine tested; bounded directed traversal, revision/permission filtering and exact reference retrieval checks pass; no SQL-only substitute mislabeled as an AGE result |
| Authorization | Reader/operator/publisher separation and unauthorized-query/evidence negatives pass; source scripts never execute; public repository/CI contain only permitted artifacts |
| Recovery | Operator updates, rolls back, restarts and restores into a fresh instance without original DB files; citations and reviewed expected answers reproduce after recovery |
| Local/cloud | Authorized real targets tested; transfer, destination rebuild, storage, freshness and access behavior reported separately; cloud-unavailable is blocked, not a passed local simulation |
| Maintainability | Install/start/stop/update/backup/restore instructions, exact version/model/license provenance, useful diagnostics and measured limitations delivered; no essential undocumented manual setup remains |
| Independent acceptance | Reviewer/evaluator findings closed or explicitly accepted as nonblocking; tracker matches actual release evidence; operator walkthrough passes |

Finish with a concise operator guide containing the exact launch command/URL, configuration/data locations, installed/reused components and versions, update/recovery commands, test evidence, measured limitations and any residual blocked criteria. Do not put credentials in the guide. State whether the whole project is complete or only the local portion is operational. A cloud or installation dependency still blocked means the full project remains unfinished.

## 8. First commands and immediate action

Use explicit working directory `C:\Users\Fred_U\Dropbox\AI\chatbot_manual`:

```powershell
Get-Location
git rev-parse --show-toplevel
git status --short
Get-Item -LiteralPath '.\root_manual' | Select-Object LinkType,Target
$env:PYTHONPATH = 'src'
python -m unittest discover -s tests -v
python evaluation/verify_source_evidence.py
```

Then inspect existing-app evidence, choose the next ready bounded task (T04/T03), and start implementing. Do not spend the session repeating the completed broad database survey or merely rewriting this handoff.
