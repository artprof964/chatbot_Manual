# Workspace and installation readiness audit

Verified: 2026-11-07 (Europe/Vienna). Scope: local project paths, Git integrity, the existing test baseline and a bounded read-only inventory of relevant software. No installations, database connections, service changes, source writes, credential inspection or cleanup were performed. This is evidence for the implementation handoff, not a completed installation or deployment qualification.

## Path and repository audit

| Check | Observed result | Consequence |
| --- | --- | --- |
| `git rev-parse --show-toplevel` | `C:/Users/Fred_U/Dropbox/AI/chatbot_manual` | Git resolves the new workspace correctly. |
| Git directory / worktree configuration | `.git`; no `core.worktree` override returned | No old absolute worktree binding found in local Git configuration. |
| HEAD and remote branch | `38ce6189524f7a74abab485a9a532bea94dd1893`; `origin/master` reported the same SHA | Committed baseline survived relocation. Tracker/continuity edits remain separate uncommitted work; do not discard them. |
| Origin | `https://github.com/artprof964/chatbot_Manual.git` | Existing public repository remains the remote; no replacement repository is needed. |
| `git fsck --no-reflogs` | Exit 0; reported dangling trees/blob, no corrupt object error | Do not confuse unreachable prior objects with failed repository integrity; no pruning was attempted. |
| Active file search | No old workspace path matched in project-owned source/config/docs/evaluation files using slash and backslash forms | No active text reference requiring replacement was found. Source trees, Git objects, runtime fixtures and caches were excluded from this text search. |
| Local Markdown references | No missing local link targets in checked project Markdown | Referenced repository documents/assets exist at the new location; external URLs and anchor targets were not exhaustively tested. |
| `root_manual` | Junction to `C:\Users\Fred_U\Documents\COPS\PMS` | This external source path is intentional and must not be rewritten to the new workspace. |
| Source exclusion | `git check-ignore` accepts `root_manual/...` and `.runtime/...` | Source/runtime remain excluded; Git exclusion alone says nothing about Dropbox synchronization behavior. |
| Old directory | Contains only an empty hidden `.git` directory | No project file remains there; no cleanup was attempted in this audit. |
| Ignored synthetic junction | `.runtime/review-junction/source/nested` targets `C:\Users\Fred_U\Documents\ChatGPT\chatbot_Manual\.runtime\review-junction\target` | Stale test-only reference remains. It is not used by current tests or shipped as project content. Prior cleanup rejection remains respected; do not bypass it. |
| Codex app registration | Orchestrator's `list_projects` result still registered `chatbot_Manual` at the old folder; current chat's listed cwd also remained old | App metadata was not automatically retargeted by moving files. Open/add the new folder in the app and start implementation there; until then every command needs an explicit new working directory. Available project tools did not expose a folder-path update. |

The app metadata observation above comes from the orchestrator's tool check during this same audit, not a direct filesystem inference. Dropbox upload completion, remote synchronization, reparse-point synchronization behavior and all editor settings remain unverified. Therefore **not every path-related integration is complete**, even though current project files, Git and source verification work at the new location.

## Fresh executable checks

- On Python **3.14.0**, **3.12.0** and **3.11.7**, `PYTHONPATH=src` plus `python -m unittest discover -s tests -q` each ran 15 tests: **14 passed, one skipped** because symbolic-link creation was denied on this host. These are three interpreter runs of the same suite, not 42 different test cases.
- `python evaluation/verify_source_evidence.py` checked all **10** registered fingerprints with no failures.
- Selected original source semantics and the real Windows junction test retain the earlier evidence in [PIPELINE_REVIEW.md](PIPELINE_REVIEW.md); this audit did not rerun all manual semantic reviews or recreate junction fixtures.
- No package build/install test, CI job, database query, engine benchmark, cloud transfer, model generation, serving API or recovery drill was run here.

## Existing software inventory

Methods: `Get-Command`, version commands for observed executables, Python launcher inventory, three Windows uninstall registry roots, selected common installation paths, and named service state. `Win32_Product` was not used. A missing PATH entry is not proof that software is absent from the machine.

| Component | Verified local evidence | Reuse / next action |
| --- | --- | --- |
| Python default | `C:\Python314\python.exe`, **3.14.0**; pip **25.3** observed | Already runs the baseline. Use an isolated project environment for dependencies; do not reinstall merely because setup instructions mention Python. |
| Python alternative | `C:\Users\Fred_U\AppData\Local\Programs\Python\Python312\python.exe`, **3.12.0**, listed by `py -0p` | Available if pinned dependencies need another interpreter; baseline suite passed. |
| Anaconda Python | Registry entry Anaconda3 2024.02-1; `C:\ProgramData\anaconda3\python.exe` executes **3.11.7** | Already covers the package's declared minimum Python major/minor in the baseline tests. Avoid modifying the shared base environment; choose an isolated environment. |
| Git | **2.54.0.windows.1**, user-local Git executable | Reuse existing installation and repository. |
| GitHub CLI | **2.83.0**, `C:\Program Files\GitHub CLI\gh.exe` | Installed. This audit did not inspect authentication; prior successful Git push does not prove CLI authentication. Check the intended workflow only when needed. |
| Node.js / npm | Node **24.12.0**, npm command at `C:\Program Files\nodejs\npm.ps1` | Node already exists; npm version/use not tested here. Current Python package does not require Node. Add frontend tooling only when the implementation needs it. |
| Windows package manager | `winget` **1.29.380** executes | Can be considered for missing dependencies after checking exact official package/source; availability does not authorize broad upgrades. |
| Native PostgreSQL | Off PATH, `C:\Program Files\PostgreSQL\18\bin\pg_config.exe` reports **18.1**; `psql.exe` exists; service `postgresql-x64-18` is running | Existing unrelated installation must not be overwritten or silently repurposed. Do not install another native server before evaluating reuse/isolation requirements. No database connection was made. |
| pgvector | PostgreSQL 18 `vector.control` declares **0.8.1** and `lib/vector.dll` exists | Artifacts present, not proof of extension installation in a database or runtime compatibility. |
| Apache AGE | PostgreSQL 18 `age.control` and `lib/age.dll` absent | Combined candidate remains unqualified; do not assume native pgvector presence supplies graph capability. |
| WSL | `wsl.exe` exists, but `wsl --list --verbose` explicitly reports Windows Subsystem for Linux is not installed | Launcher presence is not a working Linux runtime. Decide the isolated supported environment before installing features/distributions. |
| Docker / Podman | Neither command found; no matching uninstall entry found; expected Docker Desktop and RedHat Podman executables absent | No usable runtime established in bounded checks. This is not a full disk search. Recheck before installation and avoid installing both by default. |
| Local model runners | Ollama / LM Studio CLI commands absent; no matching uninstall entry; selected common executables absent | No runner established. Hardware/model/license/size qualification is still needed; do not download models merely to satisfy a tool checklist. |
| Other optional tools | `uv`, `java`, `mvn` not found on PATH | Not prerequisites for current neutral Python slice. Install only if the chosen dependency/engine path requires them; no whole-machine absence claim. |

No package from this table is a new selected deployment pin. Exact compatible released versions, licenses, hardware support and official installation procedures must be checked at implementation time before changing the host. Repository main-branch support and installed-file presence are not qualification evidence.

## Required implementation behavior

1. Start at the new workspace explicitly; confirm the source junction and preserve all uncommitted tracker/handoff changes. Do not create another project copy or rebuild the initial skeleton.
2. Inventory executable path, version, service/port use and relevant environment before each install. Classify each dependency as available and usable, available but incompatible/unqualified, or not found within stated scope. Reuse qualified tools; install only the missing requirements of the chosen path.
3. Establish the isolated graph qualification runtime without altering the existing PostgreSQL service/data. Run extension loads, qualified graph queries, mixed rollback, exact retrieval and fresh restore before accepting a database combination. Keep neutral tasks moving while runtime prerequisites are resolved.
4. Keep runtime state such as database files and model caches in an explicitly configured location suitable for that runtime; do not infer that an active database directory can safely be synchronized by Dropbox just because the source repository moved there. Make this a deployment decision and test backup/restore separately.
5. Record actual installed versions, locations, commands, checks, errors and restart requirements. Do not claim installation completion from an installer exit alone: verify the executable/service and the project's actual end-to-end use.
6. Preserve the existing public-repository source boundary: no raw manual, derived private bundles, database dumps or credentials in Git/CI. A project upload authorization is not authorization to publish the source corpus.

Current stage remains the bounded local pipeline described in [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md); gates and dependencies remain in [PROJECT_TRACKER.md](PROJECT_TRACKER.md). The audit closes neither database qualification nor the full implementation.
