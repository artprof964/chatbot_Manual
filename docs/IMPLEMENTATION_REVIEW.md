# Independent implementation and source-case review

Date: 2026-11-07 (Europe/Vienna). Reviewer is separate from the outline/options authors and the source-case analyst. Status: planning review complete; design corrections and all 15 source-case oracles independently checked. No database has been selected, deployed or benchmarked. This review does not certify runtime behavior or eliminate all possible future errors.

## Scope and method

Read the startup instructions, project skills, handoff, context/memory, project map, prior research/comparison and review artifacts, corpus profile and profiler. Reviewed `IMPLEMENTATION_OPTIONS.md`, `PROJECT_OUTLINE.md`, `README.md` and continuity updates. Rechecked the source junction: it targets `C:\Users\Fred_U\Documents\COPS\PMS`. Source inspection is read-only; report writes are outside the junction. Earlier full inventory figures are inherited evidence, not newly recomputed results.

The design preserves six candidates: Neo4j, PostgreSQL/AGE/pgvector, ArangoDB, GraphDB, Jena/Fuseki and Neptune Database. PostgreSQL/AGE is a provisional first compatibility spike under the newer open-source/maintenance priorities. Earlier Neo4j recommendations remain historical scenario assessments. None is an empirical winner.

## Review loop and issue ledger

| Finding | Severity | Correction and recheck | Status |
| --- | --- | --- | --- |
| R1: disconnected mirror authorization lacked expiry/revocation rules | High | Outline section 2 now requires encrypted cache, scoped time-bounded authorization, revalidation after expiry/reconnection and an explicit inability to guarantee immediate revocation offline. Immediate-revocation policies disable offline access. Local leases/retention are independent of cloud leases. | Closed for design |
| R2: independent publication catalogs could not fence one another merely by local epoch | Medium | Outline section 2 now disables/revokes old publication authority, transfers authenticated authority identity/epoch through trusted receiver configuration, rejects old authority and stops cutover if revocation cannot be established. | Closed for design |
| R3: GC could delete newly uploaded objects before a published revision referenced them | Medium | Outline section 5 now makes active upload/staging/import sessions protected roots; registers protection before acknowledgment; serializes final GC checks with session and publication changes; expired sessions must reacquire protection and revalidate. | Closed for design |

Rechecked the actual corrected paragraphs after the orchestrator applied them. The evaluator separately challenged candidate-fallback gating and destination rebuild cost; the outline now permits another candidate when AGE fails and separates transfer from destination materialization/storage work. These remain implementation obligations, not passed tests.

## Design checks

The outline distinguishes complete dataset revisions, PMS version scope and monotonic publication generations; rollback is a new publication of retained data. It rejects partial/missing-source scans as deletions, requires a quiescent export or coherent snapshot, preserves exact branch/path identity, and hashes canonical manifests independently of publication metadata. Its publication contract binds readiness to exact projection identities and uses immutable request pins across every retrieval stage.

Reader admission and retention marking are serialized; stale worker commits require fencing; incomplete imports cannot move the active pointer. Local/cloud serving may use different complete revisions only with explicit freshness. All six native models retain equivalent qualified assertions/evidence, with external search readiness treated as a separate consistency boundary. Source-documented PMS behavior must remain distinct from assistant/pipeline behavior.

## Product evidence rechecked

Reopened official primary documentation for material new claims:

- [GraphDB 11.5 licensing](https://graphdb.ontotext.com/documentation/11.5/licensing.html): Free request/install process and two-concurrent-query limit; edition/deployment and connector limits require package-specific qualification.
- [PostgreSQL logical replication restrictions](https://www.postgresql.org/docs/current/logical-replication-restrictions.html): schema/DDL and sequence state are not automatically replicated. This supports rejecting logical replication as a complete portable AGE deployment mechanism.
- [Apache AGE repository](https://github.com/apache/age): Apache-2.0 project and PostgreSQL extension; a repository capability statement does not prove a released/tested combined deployment.
- [ArangoDB 3.12 editions](https://docs.arango.ai/arangodb/stable/features/): Community binary production-commercial restriction and 100 GiB cap differ from source BUSL terms and later Apache conversion.

Other inherited product claims retain their earlier review evidence. Not every outbound link was reopened. Exact release compatibility, applicable license terms, operating-system/runtime parity, performance and recovery remain future qualification gates.

## Source-case review

Resumed independent review on 2026-11-07 checked every S01–S15 oracle against the read-only source. Source IDs below resolve to the exact topic paths and headings in `SOURCE_TEST_CASES.md`'s evidence register. UTF-8 HTML was read with tags removed for interpretation; raw paragraph classes, anchors and table boundaries were inspected where structure mattered. The K.2 image was viewed directly. The junction target was rechecked; the full corpus inventory was not repeated.

| Cases | Independently checked evidence | Result |
| --- | --- | --- |
| S01, S10 | T 1.3.4–1.3.5, lines 1141–1295: operation prerequisites, unknown reaction cells, `.err`/`.bad`, pipe responses and possible reactions | Supported; no invented reaction or runtime guarantee. |
| S02–S04 | F 1.2–1.2.1, lines 138–154: six field classifications, 5% example with exceptions and field 99999 | Supported with distinctions preserved. |
| S05 | T 1.3.3, lines 659–760: table headers and Währung/Land/Stadt/Markt/Indexverzeichnis rows | Supported three-edge dependency chain; DBEnum is a separate column. |
| S06–S09 | C parameter rows 985–997, 1197–1203 and sections 1.4.7/1.4.10, lines 1370–1405 | Supported; case, blank/invalid distinction, defaults, override, numeric zero and literal delimiter notation retained. Source says three stages but lists four. |
| S11–S12 | B.2.1, B.3 and B.4.1.1, lines 992–1044; raw `WD_HBÜ3`, `WD_HBÜ4`, table-header classes | Supported ABACUS/Settings/CalculationLogging ancestry and explicit user-rights qualification. |
| S13 | K.2 lines 145–147 and `01-pms_online_handbuch/appx_k-er-diagramme_de/image004.jpg` | Visually confirmed B_BSET_EXT.BATCH_NAME marked PK,FK1, B_BSET.BATCH_NAME marked PK and connecting arrow; no extra cardinality/cascade/live-constraint claim. |
| S14 | U10 lines 2965–2974 and A10 anchor search | Confirmed 20 February 2019 heading and Ticket 10049/116268 correction in U10; named anchor absent in A10. No global authority inferred. |
| S15 | A7/U7 whole-file SHA-256 and independent normalized-body comparison | Both recorded raw hashes reproduced; corrected tag-to-space normalization reproduces shared `3f8089782e0a391114ac119a2c74259b93fa3464c978f63f22976302bd9154a5`. |

Review finding R4 (low, reproducibility): the original phrase “strip remaining tags” was ambiguous. Deleting tags with no replacement produces different unequal body hashes, whereas replacing tags with spaces reproduces the recorded equality. The analyst clarified the exact procedure in `SOURCE_TEST_CASES.md`; independently rerun and closed. This remains only a text-normalization diagnostic, not proof of equivalent rendering or linked assets.

P01–P08 were reviewed as synthetic acceptance specifications covering retries, mutation, rename/delete, images, cache provenance, transfer/readiness, fencing/retention and offline freshness. They were not executed. They supplement the outline's mandatory failure tests rather than exhaust every security/recovery case. All six case-to-candidate assessments remain qualitative hypotheses; no source case demonstrates an engine performance winner. The revised outline explicitly separates source-backed S05 from synthetic expanded graph workloads. README now permits compatibility qualification alongside neutral pipeline work, matching the outline's fallback rule.

Verdict: accepted as a bounded source-backed planning specification. All identified blocking/high-priority design findings are closed for planning, with R4 also corrected and rechecked. This closes the interrupted source-case review; frozen fixtures, broader question coverage and executable acceptance tests are next-stage implementation work.

## Limits and stopping condition

The planning stopping condition is met: source-case evidence has been independently checked and identified blocking/high-priority design findings are closed for design. This does not establish that all possible errors have been found. Cloud account/region, source-transfer policy, budget, offline requirements, workload, recovery targets and exact versions remain explicit implementation inputs. There is no deployed API, database, synchronization service, measured benchmark or tested restore in this workspace. Agent review loops are invoked work, not an always-running service.
