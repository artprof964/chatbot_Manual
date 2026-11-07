# All-six graph stack comparison

Compared 2026-11-07 (Europe/Vienna). This follows `DATABASE_RESEARCH.md` and compares all six candidates separately, including GraphDB and Jena. It is a capability/design comparison for this corpus, not a performance benchmark. Review: `DATABASE_COMPARISON_REVIEW.md`.

Assumptions: the known German manual corpus, shared LLM retrieval, private-first deployment, many more reads than reviewed writes, and future source refreshes. Hosting, budget, SLA, actual simultaneous requests and data-growth targets remain unspecified. Fit, effort and cost judgments below are architectural estimates; no numerical vendor ranking is invented.

## 1. Complete proposed stacks

Every stack includes an API, ingestion/review workers, an immutable asset store, and an explicit version/evidence model. These common components are not repeated in every cell. Files can remain local initially; object storage is an operational option. No source bytes need to be stored as graph properties.

| Candidate | Graph and query model | Text/vector retrieval in this comparison | Primary advantage | Primary disadvantage |
| --- | --- | --- | --- | --- |
| Neo4j | Property graph, Cypher | Native full-text and vector indexes | Dedicated graph querying plus retrieval in one engine | Enterprise operational features cost extra; provenance remains application design |
| PostgreSQL + AGE | Property graph/openCypher plus relational SQL | PostgreSQL text search + pgvector in the same database | Consolidates application transactions, jobs, evidence and graph | Extension compatibility and graph query behavior require verification |
| ArangoDB | JSON documents and graph edges, AQL | Integrated full-text and vector facilities | Flexible document/graph model with one query language | Commercial production terms and deployment-specific transaction guarantees |
| GraphDB | RDF/SPARQL | OpenSearch/Elasticsearch connector | Formal semantics, shared vocabulary and configurable inference | Additional search service and ontology skills |
| Jena Fuseki/TDB2 | RDF/SPARQL | Separate PostgreSQL/pgvector text/vector service | Open-source RDF and serializable storage transactions | One active TDB writer plus more integration/operations work |
| Neptune Database | Property graph via openCypher/Gremlin, or RDF/SPARQL | OpenSearch; S3 for assets/manifests | Managed AWS graph infrastructure and read replicas | Several services, cloud coupling and a primary writer |

Product evidence: [Neo4j search](https://neo4j.com/docs/cypher-manual/current/indexes/search-indexes/), [AGE](https://age.apache.org/faq/), [pgvector](https://github.com/pgvector/pgvector), [ArangoDB capabilities](https://docs.arango.ai/arangodb/stable/features/), [GraphDB connector](https://graphdb.ontotext.com/documentation/11.5/elasticsearch-graphdb-connector.html), [Jena storage](https://jena.apache.org/documentation/tdb/tdb_transactions.html), [Neptune query models](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview.html). Neptune's RDF and property-graph models should be evaluated as distinct model implementations, not presumed to expose identical data automatically.

## 2. Deep connections, provenance and redundant knowledge

The next table compares modeling fit and implementation work, not measured traversal speed. All six can represent the required graph. None automatically determines which conflicting manual revision is authoritative.

| Candidate | Deep/cyclic dependencies | Several sources for the same claim | Versions, duplicates and conflicts | Formal reasoning |
| --- | --- | --- | --- | --- |
| Neo4j | Direct path-oriented Cypher patterns; bound fan-out and paths | Assertion/evidence nodes and source links | Explicit revision nodes, hashes, aliases and claim scopes | Implement domain rules or add a separate reasoning layer |
| PostgreSQL/AGE | Graph patterns plus SQL; test target query plans/depths | Relational constraints and evidence rows linked to graph IDs | Strong fit for transactional revision catalogs and dedup keys | SQL/application rules; not equivalent to an RDF reasoner |
| ArangoDB | AQL traversal with explicit documents/edges | Assertion documents connected through typed edges | Flexible JSON for provenance and evolving extraction metadata | Application-defined rules for this stack |
| GraphDB | SPARQL paths and configured rules; scope inference by version | IRIs, named graphs, explicit assertion records and PROV-O | Good semantic exchange model; equality/inference must not collapse incompatible versions | Built-in configurable RDF reasoning |
| Jena/Fuseki | SPARQL paths; add/configure Jena reasoning deliberately | Same RDF/provenance design as GraphDB | Explicit revision graphs/assertions; search projection must match | Jena reasoners/rule engines require configuration; TDB2 alone is not an automatic reasoner |
| Neptune | Traversal/path queries depend on chosen graph/query model | Property-graph claims or RDF assertion resources | Explicit revisions plus coordinated search publication | Do not assume GraphDB-style reasoning from RDF storage support |

Reasoning evidence: [GraphDB 11.5](https://graphdb.ontotext.com/documentation/11.5/reasoning.html), [Jena inference](https://jena.apache.org/documentation/inference/); provenance vocabulary: [W3C PROV-O](https://www.w3.org/TR/prov-o/). Other modeling cells are proposed implementation patterns, not preinstalled vendor features.

For every option, content-hash deduplication should share bytes while preserving source occurrences. Similar passages and labels remain candidates for review; differing versions remain separate. Identical graph structure does not establish identical truth. The known 273 different files at overlapping change-log paths must retain branch/path identity; they are not a measured count of contradictory claims.

An unlimited path search can explode in any highly connected graph. Separate node reachability from all-path enumeration, apply indexed seeds and edge/version filters, and bound interactive work. A deep exhaustive job should report budgets/truncation. Neo4j's own documentation illustrates why a final LIMIT does not prevent expensive path enumeration. [Path guidance](https://neo4j.com/docs/cypher-manual/current/patterns/variable-length-paths/).

## 3. Parallel access and consistency

All six support shared server clients. The important differences are write coordination, isolation, replica lag and cross-engine publication. One write-coordinator server does not mean only one client write transaction can be in progress. One active writer transaction, as in TDB, is a different limitation.

| Candidate | Concurrent readers | Concurrent updates | Stable view for one multi-step answer | Main operational concern |
| --- | --- | --- | --- | --- |
| Neo4j | Concurrent sessions; Enterprise replicas can distribute reads | Concurrent transactions; conventional database topology has one elected write coordinator; conflicts/deadlocks remain | Default read committed is not a request-wide snapshot; use immutable pinned revisions and appropriate replica bookmarks/routing | Hot shared nodes, long traversals, replica freshness |
| PostgreSQL/AGE | MVCC; optional replica architecture | Concurrent transactions with row/other conflicts | Repeatable Read gives a transaction snapshot; pin revisions across multiple transactions or external assets | Hot rows, query plans, long snapshots, retries at stronger isolation |
| ArangoDB | Concurrent server clients | Concurrent operations; guarantees depend on single-server/OneShard versus distributed transactions | Use explicit revision scoping; validate isolation and search visibility for selected deployment | Cross-shard failure behavior and transaction size |
| GraphDB 11.5 | Parallel reads alongside updates | Update processing/commits sequential | Read committed does not guarantee one state throughout a multi-operation transaction | Serialized ingestion/inference work plus external index readiness |
| Jena TDB2/Fuseki | Multiple concurrent readers | One active write transaction; queue others | Serializable storage transactions; pin revisions across HTTP requests and the external search service | Writer queue; direct multi-process access to storage is unsupported |
| Neptune Database | Snapshot semantics for ordinary read-only queries; replicas can lag | One primary coordinates concurrent write workload; range locks/conflicts | Snapshot scope is a query; session mode matters and external OpenSearch is separate | Mutation conflicts, freshness and graph/search coordination |

Official concurrency evidence: [Neo4j locking/isolation](https://neo4j.com/docs/operations-manual/current/database-internals/concurrent-data-access/), [Neo4j cluster topology](https://neo4j.com/docs/operations-manual/current/clustering/introduction/), [PostgreSQL isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [ArangoDB transaction scope](https://docs.arango.ai/arangodb/stable/develop/transactions/limitations/), [GraphDB 11.5 transactions](https://graphdb.ontotext.com/documentation/11.5/storage.html), [Jena transactions](https://jena.apache.org/documentation/tdb/tdb_transactions.html), [Neptune isolation](https://docs.aws.amazon.com/neptune/latest/userguide/transactions-neptune.html).

Neptune reads in Gremlin standing sessions/openCypher Bolt read-write sessions use mutation isolation; do not generalize the ordinary read-only snapshot guarantee. Neptune Analytics is a different product, and its vector changes are explicitly non-atomic/non-isolated. [Analytics vector limits](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vector-index.html).

Across all six: workers should extract/compute outside database transactions, publish idempotent batches, and expose a revision only after its graph and search data are ready. Readers pin a revision and enforce it on every query. Retries, pools, timeouts and bounded queues remain necessary even with a cluster.

## 4. Retrieval, deployment, cost and portability

These are qualitative ownership judgments for the proposed stacks. A native feature does not establish better relevance or faster execution. Compare equal extraction, models and evidence before attributing outcomes to a database.

| Candidate | Retrieval/publication burden | Deployment and software-cost tradeoff | Portability / skills | Principal decision gate |
| --- | --- | --- | --- | --- |
| Neo4j | Lower service count with native graph/text/vector; still validate index visibility | Single-server Community evaluation; commercial Enterprise/Aura for selected production capabilities | Cypher and property-graph skills; vendor procedures/features reduce portability | Does it deliver the required graph/retrieval behavior at acceptable production cost? |
| PostgreSQL/AGE | One database can coordinate rows, graph and vectors; filtered ANN recall still needs testing | Open-source components; self-host or verify host allows AGE; extension upgrades add work | SQL skills transfer, but AGE value types and Cypher subset need adapters | Released compatible extension versions and acceptable graph plans |
| ArangoDB | One engine reduces integration, but verify search freshness/vector rebuild behavior | Commercial production license for current packaged Enterprise route | AQL-specific application queries; JSON model is easy to export | Accepted terms and single-server/OneShard or required cluster guarantees |
| GraphDB | External search needs readiness/reconciliation; inference increases ingest work | Verify edition/license and cluster terms; more than one service | RDF/SPARQL/ontology skills; portable IRIs/data with vendor-specific connector/query extensions | Is formal semantic governance worth the extra modeling and operations? |
| Jena/Fuseki | External vector/text store plus identity/revision coordination | Open-source RDF stack; lower database license expense can mean higher engineering effort | RDF/SPARQL plus Java/Jena/server operations; exchange formats help migration | Can a queued writer and self-operated service meet the load/recovery needs? |
| Neptune | Graph/S3/OpenSearch publication and networking | Managed AWS spending; fewer database host duties, multiple metered services | AWS operations and chosen query language; engine dialects/connectors still matter | Is managed AWS infrastructure an existing requirement? |

Commercial and compatibility facts: [Neo4j editions](https://neo4j.com/docs/operations-manual/current/introduction/), [Neo4j licensing](https://neo4j.com/open-core-and-neo4j/), [AGE FAQ](https://age.apache.org/faq/), [AGE repository/releases](https://github.com/apache/age/releases), [ArangoDB edition terms](https://docs.arango.ai/arangodb/stable/features/). AGE's FAQ and current repository differ on PostgreSQL version coverage; pin an explicitly released/tested combination. Arango Community binary and BUSL source terms differ. No monetary quote or legal suitability determination is supplied.

Specifically, current ArangoDB Community binaries (3.12.5 onward) prohibit commercial production and impose a 100 GiB dataset limit; Enterprise permits commercial use and removes that limit. Its BUSL source route has different conditions, so this is not a claim that every source-built commercial deployment requires Enterprise. Confirm the actual distribution and use case. [ArangoDB edition terms](https://docs.arango.ai/arangodb/stable/features/).

For vector evaluation: pgvector approximate-index filters can return too few candidates unless configured appropriately. Arango vector indexes are trained and can lose quality as the data distribution changes. Neither issue proves a competitor is faster or more accurate. [pgvector filtering](https://github.com/pgvector/pgvector#filtering), [Arango vector training](https://docs.arango.ai/arangodb/stable/indexes-and-search/indexing/working-with-indexes/vector-indexes/).

RDF portability is strongest at the data/vocabulary level; a SPARQL query using proprietary extensions is not automatically portable. Likewise openCypher naming does not guarantee unchanged Neo4j/AGE/Neptune applications. Preserve a database-neutral manifest of documents, chunks, entities, assertions and evidence IDs so any stack can be rebuilt.

## 5. Scenario decisions across all six

There is no defensible universal first-to-sixth performance ranking without tests. These are preferences under explicit scenarios, and every candidate remains in the evaluation set.

| Dominant requirement | Preferred candidate | Credible alternative | What changes the choice |
| --- | --- | --- | --- |
| Current manual assistant: graph exploration plus grounded answers | Neo4j | PostgreSQL/AGE | Existing SQL operating expertise and production edition cost |
| Many agents writing jobs, annotations and reviewed structured data | PostgreSQL/AGE | Neo4j or ArangoDB | Actual write conflicts, isolation requirements and tested query plans |
| Evolving JSON extraction records with graph traversal | ArangoDB | PostgreSQL/AGE or Neo4j | License and transaction/deployment requirements |
| Formal shared definitions, inference and multi-system semantic exchange | GraphDB | Jena/Fuseki | Packaged semantic tooling versus engineering budget |
| Open-source RDF with periodic controlled imports | Jena/Fuseki | PostgreSQL/AGE if RDF standards are not essential | Whether writer serialization and external retrieval are acceptable |
| Organization already standardized on managed AWS services | Neptune Database | Neo4j Aura or managed/self-hosted alternatives if approved | Full AWS service bill, availability needs and data handling constraints |

For this corpus, I still provisionally prefer Neo4j, with PostgreSQL/AGE close behind. GraphDB becomes the leading choice if an enterprise ontology is the actual product; Jena is the open-source RDF counterpart. Arango and Neptune can win their respective document-first and AWS-first scenarios. These preferences reflect implementation fit, not benchmark evidence.

## 6. Fair evaluation of every candidate

The follow-up expands the prior two-candidate benchmark suggestion to **all six stacks**. This is an evaluation specification; databases have not been installed or tested.

1. Freeze one database-neutral extracted manifest: same passages/tables, images, entity IDs, qualified assertions, evidence and revision boundaries. Map it faithfully to each native graph model; do not force RDF into an unnecessarily poor property-graph representation or vice versa.
2. Use the same embeddings, model/tokenizer, candidate counts, reranker and 50–100 reviewed questions. Test both each stack's native retrieval baseline and a controlled common retrieval input to separate retrieval quality from graph execution. Keep raw timing and end-to-end quality distinct.
3. Run the same exact-ID, version-conflict, duplicate-content, table/field, provenance and 2/4/8-hop dependency cases. Include cycles, high-degree nodes and exhaustive reachability with the same work budget.
4. Exercise 10/50/200 simultaneous API requests, first readers only, then mixed with 1/4/8 ingestion workers and review writes. Measure queue time, p50/p95/p99 latency, throughput, memory/I/O, lock waits, retry/error rate and version correctness. These are test tiers, not capacity promises.
5. Separate single-instance comparisons from production HA comparisons. Document CPU/RAM/storage, replicas, query plans, tuning, edition and total service cost. Managed deployments cannot be hardware-equalized perfectly; report that limitation and compare service-level/cost outcomes separately.
6. Interrupt imports and search projections, publish during queries, and restore from backup. Require no mixed revisions, preserved evidence, idempotent recovery and reproducible citations. Test degraded/failover behavior only for topologies that actually provide it.
7. Publish six result sheets and let a reviewer audit correctness before choosing. A capable cheap stack that fails provenance is unsuitable; a graph engine that wins a traversal microbenchmark can still lose overall on retrieval quality, operating effort or reliability.

The current result is a complete all-six design comparison. The empirical winner remains unmeasured. Keep the source junction read-only whichever stack is eventually chosen.
