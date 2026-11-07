# Runtime compatibility preflight

Inspected 2026-11-07 (Europe/Vienna). Gate 1 remains incomplete. This bounded, read-only host inventory is not a database connection, extension load test, benchmark or deployment selection. Neutral pipeline work can proceed independently.

## Observed host evidence

| Check | Observed result | Interpretation |
| --- | --- | --- |
| `Get-Command python` and `python --version` | `C:/Python314/python.exe`, Python 3.14.0 | Available for the neutral implementation; dependency support must still be tested. |
| `Get-Command docker,podman,psql` | No commands found on PATH | PATH absence alone does not establish absence of installed software. |
| `wsl.exe --list --verbose` | Reports that Windows Subsystem for Linux is not installed | The Windows launcher exists, but no usable WSL runtime was established. No installation was attempted. |
| Bounded inventory of Program Files Docker/PostgreSQL directories | PostgreSQL 18 binaries found; PostgreSQL 16 directory has no `bin`; expected Docker Desktop CLI path absent | No usable container runtime found in the inspected locations. This is not an exhaustive machine-wide inventory. |
| `C:/Program Files/PostgreSQL/18/bin/pg_config.exe --version` | PostgreSQL 18.1 | Native Windows installation exists despite PATH result. `psql.exe` and `initdb.exe` also exist. |
| `Get-Service postgresql-x64-18` | Running | Existing service was not connected to, stopped, modified or repurposed. |
| PostgreSQL 18 `share/extension/vector.control` | `default_version = '0.8.1'`; `lib/vector.dll` exists | pgvector files are present; this does not prove the extension is installed in any database or compatible at runtime. |
| PostgreSQL 18 `share/extension/age.control` and `lib/age.dll` | Both absent | The combined PostgreSQL/AGE/pgvector candidate cannot be qualified from these installed extension files. |

No source files, existing database data directories, OS features or services were changed. No manual data was uploaded and no paid resources were provisioned. The preflight did not inspect database credentials or connect to the existing PostgreSQL server.

## Gate 1 result and next requirements

**Blocked for the combined candidate on the inspected host setup:** AGE artifacts and a qualified isolated runtime are missing. This is an infrastructure prerequisite, not a failed graph correctness test. PostgreSQL 18.1 plus pgvector 0.8.1 observed on disk are not a selected deployment pin and do not resolve AGE compatibility.

Before running the spike:

1. Provide an isolated supported build/runtime capable of loading the exact chosen AGE and pgvector releases. The planning default is a Linux-compatible container/VM; enabling Windows features or installing/rebooting the host is outside this preflight. An already available isolated Linux host can serve the same purpose, using synthetic data only.
2. Recheck official released artifacts, compatibility and license terms; pin PostgreSQL, AGE, pgvector, OS/architecture and image/build digests together. Do not infer released compatibility from repository main-branch support statements or the local PostgreSQL version.
3. Start a disposable database cluster isolated from the existing running PostgreSQL service. Load both extensions and record actual server/extension versions, then test graph creation, evidence-qualified directed traversal, relational/AGE transaction rollback, exact vector retrieval and revision filtering.
4. Dump/restore the disposable synthetic fixture into a fresh instance, reproduce evidence and graph results, and record outputs plus teardown. Only then mark the corresponding checks passed. Upgrade qualification remains a separate test.

Existing official-source research and the required qualification gates are in [IMPLEMENTATION_OPTIONS.md](IMPLEMENTATION_OPTIONS.md) and [PROJECT_OUTLINE.md](PROJECT_OUTLINE.md). This preflight adds observed host facts, not new vendor support claims. No exact combined release was chosen and no new compatibility claim was researched or asserted.

## All-six qualification status

| Candidate | Runtime status | Evidence still required |
| --- | --- | --- |
| PostgreSQL + AGE + pgvector | **Untested; preflight prerequisite missing** | Isolated released combined build, extension loads, mixed rollback, graph/retrieval and restore checks |
| Neo4j + native retrieval | **Untested** | Exact edition/license/runtime qualification, evidence/graph/retrieval and restore checks |
| ArangoDB + integrated retrieval | **Untested** | Exact distribution/license and topology qualification, revision/transaction/retrieval and restore checks |
| GraphDB + external retrieval | **Untested** | Exact license/runtime qualification, qualified RDF/condition handling, cross-store readiness and restore |
| Jena/Fuseki + separate retrieval | **Untested** | Exact runtime qualification, RDF evidence preservation, writer/read behavior, cross-store readiness and restore |
| Neptune Database + S3 + OpenSearch | **Untested** | Authorized AWS test setup, exact service/model contract, graph/search readiness and access/restore checks |

No candidate has a measured performance score. Runtime unavailability must not be converted into an invented benchmark failure. Continue the engine-neutral capture/extraction/bundle milestone while Gate 1 prerequisites are resolved.
