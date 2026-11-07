# Independent implementation evaluation

Date: 2026-11-07 (Europe/Vienna). Evaluator separate from the outline author, source analyst and independent reviewer. This evaluates the proposed design and case coverage; it is not a database benchmark, deployment approval or proof that all future errors are eliminated. All six candidates remain in scope, and no database has been selected, deployed or benchmarked.

## Evaluation scope

Read project startup instructions, handoff, source map/review, research/comparison and their reviews, implementation options and project outline. Rechecked that `root_manual` is a junction to `C:\Users\Fred_U\Documents\COPS\PMS` and the manual entry point exists. No source writes, database installation or cloud upload were performed.

The criterion is the user's combination of open-source preference, maintainable updates, efficient local/cloud transfer and access from both locations. Six production adapters are unnecessary for an initial outline; six explicit evaluation records and equivalent evidence semantics are necessary before claiming a comparative result.

## Findings and correction loop

| ID | Priority | Finding | Required correction | Status |
| --- | --- | --- | --- | --- |
| E1 | High | A disconnected local reader cannot depend on cloud leases or immediate cloud authorization revocation. | Define local reader/retention coordination, offline grant expiry and honest revocation limits before enabling the mirror. | Closed after re-reading outline section 2: local leases/GC, scoped expiring grants and denial after expiry; immediate-revocation policy disables offline access. |
| E2 | Medium | Gate 1 made PostgreSQL/AGE passing a prerequisite even if another candidate would qualify. | Keep neutral work independent; failed AGE qualification triggers an explicit alternative qualification instead of silently changing the candidate or halting all progress. | Closed after re-reading section 9 Gate 1: failed AGE qualification permits another retained candidate and independent neutral pipeline work. |
| E3 | Medium | Delta transport alone does not establish cheap or fast destination revision imports. | Measure graph/vector materialization and index-rebuild time, peak storage and reuse separately from uploaded bytes. | Closed after re-reading section 9: separate destination-work measurements and explicit warning that small deltas can require full index rebuilds. |

Also checked the reviewer's corrections in outline sections 2 and 5: authority cutover revokes the old publisher and authenticates the handoff; upload/staging leases protect objects before publication. These close identified design gaps, while implementation of the specified races remains untested.

## Decision quality

The provisional PostgreSQL/AGE/pgvector preference is reasonable as the **first compatibility spike**, because consolidation may reduce operational boundaries. It remains conditional: a failed compatibility, upgrade/restore or graph-query test can outweigh that benefit. The AGE repository currently describes PostgreSQL 11–18 support while the FAQ says through 16, supporting the explicit released-version gate rather than an invented deployment pin. [AGE repository](https://github.com/apache/age), [AGE FAQ](https://age.apache.org/faq/).

Revision-filtered retrieval needs a correctness baseline. pgvector documents post-filtering of approximate index candidates and possible short result sets; exact filtered retrieval is therefore a useful reference test, not evidence that PostgreSQL wins. [pgvector filtering](https://github.com/pgvector/pgvector#filtering).

Keep the other five candidates distinct: Neo4j for graph-development convenience; Jena/Fuseki for open-source RDF; ArangoDB for document/graph integration subject to its actual distribution terms; GraphDB for semantic governance subject to edition and projection costs; Neptune for an AWS-managed scenario, with local client access distinguished from an autonomous local engine. These are scenario judgments grounded in `IMPLEMENTATION_OPTIONS.md` and the reviewed all-six comparison, not performance rankings.

## Source-case evaluation

Completed the case-coverage/design evaluation of `SOURCE_TEST_CASES.md` during the resumed planning task. The source analyst and independent reviewer separately confirmed S01–S15 against the manual, diagram and branch hashes; their only correction clarified that S15 diagnostic normalization replaces tags with spaces. The source-evidence verdict is in `IMPLEMENTATION_REVIEW.md`; this evaluator checked how the cases test the proposed process and distinguish candidates, and accepted the clarified diagnostic without changing the semantic oracle. Runtime acceptance gates remain unrun.

### Common correctness gates

| Cases | What every implementation must preserve | Where to attribute failure |
| --- | --- | --- |
| S01–S04, S06–S10 | Operation prerequisites, unknown reactions, field codes, units, exact case, conditional defaults and literal delimiter notation | Compare parsed neutral records with the source oracle first; then compare retrieval and generated answers separately. A parser or answer-model error is not evidence against a database. |
| S05 | Directed Markt → Stadt → Land → Währung dependency chain and the two distinct Indexverzeichnis dependencies | Verify edge type/direction and evidence at extraction; test the same qualified graph assertions in each native model. This demonstrates a three-edge case, not arbitrary deep-query performance. |
| S11–S13 | Word-style hierarchy, table ancestry, permission qualification and diagram-linked evidence | Verify hierarchy/image provenance before ingestion. A manual permission statement is descriptive evidence, never an API authorization grant. |
| S14–S15 | Exact branch identity, scoped revision evidence, separate occurrences and raw versus extracted-content identity | Check the canonical manifest and evidence membership, then revision-filtered retrieval. A missing entry in one branch is not proof that the other is globally authoritative. |
| P01–P05 | Idempotency, old/new evidence separation, complete-scan deletion, image dependency invalidation and complete cache keys | Exercise the neutral pipeline before native adapters, then repeat end-to-end for each candidate. |
| P06–P08 | Staged readiness, retry/fencing/retention and honest offline freshness | Inject failures at actual service boundaries and verify pinned evidence. A successful upload or final answer alone does not prove the protocol safe. |

All 15 source cases are seed acceptance specifications, not a representative accuracy benchmark. Preserve positive expected evidence and forbidden conclusions, freeze source hashes and parser/model identities, and expand to the outline's 50–100 reviewed questions before making a deployment comparison. Keep the synthetic mutation/race cases separate from documented PMS behavior. P01–P08 summarize scenarios; implement distinct fault-injection steps for each race rather than counting one combined scenario as exhaustive coverage. The outline's mandatory tests additionally cover source disappearance, identity collisions, restore and upgrades.

### Six-candidate qualification matrix

These are proposed experiments and interpretation rules, not pass/fail results or new vendor-capability claims. Product/license evidence and its dated limits remain in `IMPLEMENTATION_OPTIONS.md` and `DATABASE_COMPARISON.md`.

| Candidate | Case-driven experiment that can distinguish it | Maintenance and access decision |
| --- | --- | --- |
| PostgreSQL + AGE + pgvector | Use S02/S07/S08 as typed evidence and S05 as AGE edges; abort a combined catalog/relational/graph write and verify no partial revision. For S04/S06/S14 compare exact identifiers and revision-filtered vector results with an exact baseline; exercise P07 under concurrent workers/readers. | First compatibility spike under the open-source/consolidation priority. Record extension upgrade/restore work and full versus incremental destination rebuilds. Reject the combined release if it fails; do not quietly substitute SQL adjacency and call that an AGE result. |
| Neo4j + native retrieval | Import the same qualified S05/S13 assertions, run direction/evidence tests and measure bounded traversal; delay native search readiness during P06 and test exact-code plus revision filters. | Main property-graph alternative. Compare implementation effort and operational requirements for the exact licensed edition against PostgreSQL's extension burden, including restore and local rebuild. |
| ArangoDB + integrated retrieval | Represent S07/S08 conditions as documents with S05 edges; test revision visibility and partial-write recovery in the actual chosen deployment topology during P02/P06. | Retained document/graph alternative. Qualification requires acceptable exact distribution terms, verified transaction scope and measured index maintenance; flexible records alone do not demonstrate an advantage on these cases. |
| GraphDB + external retrieval | Encode S02/S05 as evidence-qualified RDF assertions; ensure S07/S08 conditions and S14 branch scopes prevent unsupported inference. Delay the search projection during P06 and verify no cross-revision answer. | Retained semantic-governance alternative. Require an explicit ontology/inference benefit, acceptable licensing and measured reconciliation work before accepting the additional service boundary under these priorities. |
| Jena/Fuseki + separate retrieval | Use the same qualified RDF inputs and expected answers as GraphDB. Measure import queue growth and reader latency during P01/P06, then restore/rebuild both graph and retrieval projections. | Open-source RDF alternative. Compare its import/maintenance workflow and semantic-model benefit with the first spike; periodic imports may fit, but the workload and extra retrieval service must be measured. |
| Neptune Database + S3 + OpenSearch | Import the equivalent evidence model and run S05/S14; inject S3/graph/search lag or failure under P06 and test P08's explicitly supported local-access mode. | Retained managed-AWS alternative. Include networking, transfer/egress and reconciliation work. Local client access does not satisfy an autonomous local-engine requirement; report that requirement as unsupported or qualify a separately named local implementation. |

For a fair comparison, first supply identical reviewed extracted records and candidate sets to isolate graph/evidence behavior. Then evaluate each full native retrieval stack with the same frozen questions, embeddings, revision/permission filters and output budgets. Record native schemas and query choices rather than forcing identical physical layouts. Correctness failures block speed rankings. Unavailable licenses/services or untested configurations remain **untested**, not failed performance scores.

### Evaluation verdict and next evidence

The source cases reinforce the neutral evidence pipeline and the provisional PostgreSQL/AGE/pgvector first spike: the hard requirements include structured conditional evidence, exact identifiers, provenance and safe publication as well as graph traversal. They do not establish that PostgreSQL is faster, easier to operate in practice, or the final database choice. Neo4j remains the graph-focused alternative and Jena the open-source RDF alternative; ArangoDB, GraphDB and Neptune remain explicit qualification records.

Fast local/cloud movement must be judged by no-change, one-topic, image-only, rename/delete and parser/model-upgrade runs. Report bytes sent/retried, reused artifacts, destination graph/index rebuild time, peak staging plus retained storage, end-to-end publication time and operator interventions. A small delta does not guarantee a small import. For local/cloud parity compare the same pinned revision and permission scope; for an older offline mirror assess freshness and expiry behavior separately, not as an unexplained accuracy regression.

The design evaluation identifies no additional blocking contradiction in the current outline. The independent reviewer confirmed all source cases and rechecked the S15 diagnostic clarification. The planning evaluation is complete with no open blocking finding in this bounded review; this does not certify the absence of all future errors. The next implementation evidence is a frozen reviewed fixture, neutral pipeline checks and an isolated released-version compatibility spike. Hosting, upload policy, offline requirements, workload/budget and recovery targets remain the explicit gates in outline section 10. No database, cloud transfer, publication race, security boundary, restore or benchmark has been executed by this evaluation.
