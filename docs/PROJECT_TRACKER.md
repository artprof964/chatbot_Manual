# Project tracker

Updated: 2026-11-07 (Europe/Vienna). Current workspace: `C:\Users\Fred_U\Dropbox\AI\chatbot_manual`. Reviewed code baseline: `38ce618` on `master`, matching the public [GitHub repository](https://github.com/artprof964/chatbot_Manual). This file is the current task ledger; [implementation status](IMPLEMENTATION_STATUS.md) describes executable scope and commands, and dated reviews retain their original scope.

## Review outcome

The project has a reviewed design and an initial local capture/extraction/validation implementation. It is not yet a working chatbot or synchronization service. The most useful next delivery is a stronger neutral evidence contract with executable correctness fixtures, while database qualification proceeds separately. PostgreSQL/AGE/pgvector remains the first candidate to qualify; no engine has been selected or benchmarked.

Fresh checks before and after workspace relocation: 15 tests ran, **14 passed and one symlink test was skipped**; all **10 frozen source fingerprints matched**. Git history and origin were preserved. `root_manual` remains a junction to `C:\Users\Fred_U\Documents\COPS\PMS`; no source changes were made. The prior independent review tested an actual Windows junction separately; that check was not repeated here. Full corpus inventory, database/runtime inventory and cloud operation were not repeated. Evidence: [code review](PIPELINE_REVIEW.md), [preflight](COMPATIBILITY_STATUS.md), [source registry](../evaluation/source_evidence.json), [tests](../tests/).

The registry is hashes and locators, not executable semantic answer tests. Existing tests validate a bounded local pipeline; they do not establish whole-corpus accuracy, revision publication safety, retrieval quality or performance. No completion percentage or delivery date is assigned because effort, staffing and deployment targets are not established.

## Milestone dashboard

| Gate | Status | Completion evidence / remaining exit requirement |
| --- | --- | --- |
| G0: design | Done within planning scope | [Design review](IMPLEMENTATION_REVIEW.md) and [evaluation](IMPLEMENTATION_EVALUATION.md); no claim of runtime certification |
| G1: engine qualification | Blocked on prerequisite; runtime untested | Prior preflight found no AGE or usable WSL/container runtime in inspected locations; isolated released-version combination, rollback/graph/retrieval and restore evidence still required |
| G2: neutral pipeline | Partial | Capture/extraction/validation baseline passes local tests; contracts, evidence mapping and revision-change coverage remain |
| G3: reliable updates | Not started | Delta transfer, receiver, idempotent retries and correct publication must pass fault injection |
| G4: serving | Not started | Authenticated graph/text/vector API, pinned citations and permission tests |
| G5: fair selection | Not started | Equivalent correctness-first results for all six; unavailable options explicitly untested |
| G6: operations | Not started | Measured restore/upgrade/rollback drills and agreed workload/recovery/cost targets |

Gate meanings and detailed invariants remain in [PROJECT_OUTLINE.md, sections 9–10](PROJECT_OUTLINE.md#9-milestones-and-acceptance-gates). Gates are acceptance criteria, not a requirement to serialize independent work.

## Work queue

Statuses: **Done** = bounded deliverable verified; **Ready** = can start; **Planned** = prerequisites outstanding; **Blocked** = named prerequisite missing; **Conditional** = only if the requirement is selected. Priority P1 is next, P2 follows, P3 is later qualification. Owner columns name roles needed; no individual is assigned and no agent runs persistently.

| ID | Gate / priority | Status | Deliverable | Dependencies | Owner role | Acceptance evidence |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | G0 | Done | Corpus map, six-option research, source-case planning review | — | Analyst / reviewer | Existing dated reviews, S01–S15 and P01–P08 specifications; runtime limits explicit |
| T02 | G2 | Done, initial slice only | Local capture, extraction and validation | T01 | Engineering / reviewer | 14 tests pass; one skip documented; deterministic rerun, corruption and partial-scan checks; ten fingerprint matches |
| T03 | G2 / P1 | Ready | Reproducible CI and package checks | T02 | Engineering | Synthetic-only Windows/Linux jobs; declared minimum Python tested; build/install/CLI checks; no private manual dependency |
| T04 | G2 / P1 | Ready | Versioned neutral evidence contract | T02 | Engineering / analyst | Golden schemas for source branch/version, sections/chunks/assertions, source span mapping and extractor provenance; stable identities and unknown values preserved |
| T05 | G2 / P1 | Planned | Executable S01–S15 oracles | T04 | Analyst / reviewer | Required evidence and forbidden assertions checked separately; synthetic public fixtures; real source checks local and hash-pinned; extraction errors separated from answer errors |
| T06 | G2 / P1 | Planned | Revision-change and cache invalidation fixtures | T04 | Engineering / reviewer | Rename reuses bytes with new occurrence identity; deletion changes new membership only; old evidence remains resolvable; image-only/config changes invalidate affected artifacts; incomplete scans never imply deletion |
| T07 | G1 / P1 | Ready; setup required | Discover/reuse/install isolated engine qualification environment | Resolve D01 within task | Engineering / operator when interaction required | Existing apps checked first; missing required runtime installed and verified; released compatibility/license matrix and pinned versions/digests; existing PostgreSQL service untouched |
| T08 | G1 / P1 | Planned | PostgreSQL/AGE/pgvector qualification spike | T07 | Engineering / reviewer | Extensions load; mixed relational/AGE rollback, directed evidence traversal, exact filtered vector retrieval and fresh restore reproduce expected results; failures recorded and alternative qualified if needed |
| T09 | G3 / P2 | Planned | Parent revisions, deterministic segments and delta report | T04, T06 | Engineering | No-change, one-topic, rename/delete and image-only changes report changed/reused bytes; unchanged segment IDs stable; complete revision membership retained |
| T10 | G3 / P2 | Planned | Local staging receiver and resumable transfer | T09 | Engineering / reviewer | Corruption, missing objects, interrupted/replayed transfers and expired sessions handled; final references revalidated; transfer is not publication |
| T11 | G3 / P2 | Planned | Jobs, publication catalog, fencing and retention | T10, qualified storage from T08 or retained alternative | Engineering / reviewer | Wrong-parent, stale-worker, simultaneous-publisher, lost-response and reader-pin/GC races pass; old complete revision remains available on failures |
| T12 | G4 / P2 | Planned | Baseline native graph/text/vector adapter | T04, T08 or retained alternative, T11 | Engineering | Same evidence model and revision scopes; exact identifiers, bounded graph expansion and exact filtered-vector baseline pass |
| T13 | G4 / P2 | Planned | Authenticated API and cited answer path | T05, T12, D02, D03 | Engineering / reviewer | One revision throughout retrieval/reranking/answer/citations; unauthorized queries and evidence fetches rejected; local model-only default until external processing authorized |
| T14 | G5 / P3 | Planned | Broader oracle and all-six comparison | T05, T13, D04 | Analyst / evaluator | 50–100 reviewed questions; synthetic stress graphs labeled; six qualification/result sheets; correctness precedes latency; inaccessible tests unrun, never fabricated |
| T15 | G3–4 / P3 | Planned | Authorized cloud trial | T10–T13, D02, D04 | Operator / engineering | Same protocol and pinned evidence locally/remotely; measure transfer versus destination rebuild/storage cost and operator effort |
| T16 | G6 / P3 | Planned | Restore, upgrade, rollback and operating runbooks | T11–T13, D04, D05 | Operator / reviewer | Cold restore with no original DB files, failed upgrade/rollback and retention drills pass; agreed recovery/capacity/cost targets met; cloud-specific drills after T15 |
| T17 | G4 / conditional | Conditional | Read-only offline mirror | T11, T13, D03 | Engineering / reviewer | Complete import before activation; explicit freshness; local reader leases/GC; expiring grants and reconnect checks; immediate-revocation requirement disables offline access |
| T18 | Workspace | Done with residual directory | Move project and preserve repository/source boundary | — | Operator | New workspace tests/hashes pass and Git HEAD/origin unchanged; old location retains empty `.git`; Dropbox sync and app sidebar registration not verified |

## Decisions and blockers

| ID | Decision / missing input | Working default | Needed before |
| --- | --- | --- | --- |
| D01 | Isolated supported AGE runtime and setup | Discover/reuse first; choose and install a supported isolated environment as necessary; do not repurpose existing database service | Resolve within T07; ask only for actual interactive/system constraints; neutral T03–T06 continue independently |
| D02 | Hosting/account/region, source transfer rights and access scope | Real corpus/model processing stays local; one private dataset; operator/reader separation | Real upload/remote model call and API access design |
| D03 | Connected local access versus offline requirement; model choice/license | Shared API for connected clients; offline optional; provider-neutral, locally evaluated models | T13/T17; offline model capability and revocation policy must be explicit |
| D04 | Workload, budget, SLA, RPO/RTO and test capacity | Single-instance prototype; no promised latency or availability | Comparative load tiers, paid provisioning and production qualification |
| D05 | Retention/citation lifetime and source authority | Active plus prior two revisions, seven-day grace and leases are proposals; retain both change-log branches | Production deletion policy or claims of current PMS applicability |

Publishing project code/analysis to the public repository does not authorize uploading the raw manual, derived corpus bundles or credentials. Tracked exclusions remain in [.gitignore](../.gitignore). Future CI must use synthetic data.

## Next work package and handoff

Execution brief: [IMPLEMENTATION_HANDOFF.md](IMPLEMENTATION_HANDOFF.md), reviewed in [HANDOFF_REVIEW.md](HANDOFF_REVIEW.md). It replaces the earlier planning-only stopping condition for implementation: continue through necessary installation, functional use and recovery acceptance. Fresh existing-app/path evidence is in [READINESS_AUDIT.md](READINESS_AUDIT.md); reuse compatible apps before installing anything.

Start **T04** and **T03**, while a worker resolves **D01/T07** through existing-app discovery and necessary isolated installation. Request operator participation only for actual required interaction or missing external inputs. Then implement **T05/T06** before building delta transport. Keep the first engine spike small and synthetic; do not build six production adapters before the common evidence contract is stable. No database deployment or source upload is needed to advance the next neutral work package.

The question-set expansion within T14 can begin after T05; only comparative execution needs the serving and workload prerequisites. Preparing evaluation inputs need not wait for the full API.

At each completion, update the task row with commit/test evidence, record any failed/skipped checks, and obtain independent review before closing the relevant gate. Keep this file as the single current queue rather than appending session logs to memory. Change dates/owners only when actually agreed. The original [project map](PROJECT_MAP.md) and [review](REVIEW.md) describe their earlier inspection; they are not current Git-status records.

## Relocation and review notes

The move preserved all project entries, including `.git`, ignored local runtime files and the external-source junction. An initial combined move/cleanup command was rejected by automatic command review with “blocked by policy”; the move-only approach succeeded after handling the hidden Git directory. No deletion retry was performed. Only an empty hidden `.git` directory remains at the old workspace location. The pre-existing ignored synthetic junction fixture was moved unchanged; its prior absolute test target may be stale and is not part of the executable tests or deliverables.

Verification is of local filesystem state, not completion of Dropbox upload/synchronization. The readiness audit confirmed Codex project registration and current chat cwd still point at the old location, and the ignored test junction target is stale. Open/add the new folder for future implementation chats; meanwhile use explicit new working directories. Keep future live databases, credentials and private derived corpus data outside Dropbox. Independent verification of this tracker is recorded in [PROJECT_TRACKER_REVIEW.md](PROJECT_TRACKER_REVIEW.md).
