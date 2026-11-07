# Independent all-six comparison review

Reviewed 2026-11-07 (Europe/Vienna), by an agent separate from the comparison author. Verdict: accepted as a comparative architecture assessment and all-six evaluation specification, after the license clarification below. This is not a measured performance ranking or deployment approval.

Read the project startup guidance, existing research and independent research review, the complete `DATABASE_COMPARISON.md`, the research follow-up paragraph and compact-memory research row. Rechecked the source junction target; no linked PMS source was modified. Existing corpus/profile evidence was reused, not remeasured.

Coverage is complete for the six previously proposed candidates: Neo4j, PostgreSQL/AGE/pgvector, ArangoDB, GraphDB, Jena/Fuseki and Neptune Database. The report compares graph/query models, deep/cyclic traversal, evidence and redundant versions, inference, reader/write concurrency, isolation, publication, retrieval, deployment, qualitative cost and portability. It distinguishes a primary write coordinator from one active writer transaction, and RDF storage from automatic reasoning. Its scenario preferences and ownership estimates are explicitly judgments; concurrency tiers are proposed tests, with no fabricated results. The final plan includes all six, despite the original report's preserved two-candidate shortlist.

Independently reopened official documentation during this review:

- [GraphDB 11.5 storage](https://graphdb.ontotext.com/documentation/11.5/storage.html): read committed, sequential update commits and parallel readers; no single-state guarantee throughout a transaction. The comparison is version scoped.
- [Jena TDB transactions](https://jena.apache.org/documentation/tdb/tdb_transactions.html): TDB2 MVCC, serializable transactions, one active writer and multiple readers; multiple JVMs must use a server rather than sharing storage files.
- [Neptune isolation](https://docs.aws.amazon.com/neptune/latest/userguide/transactions-neptune.html): ordinary read-only snapshot behavior, replica lag and distinct mutation isolation for Gremlin standing/openCypher Bolt read-write sessions. These qualifications are retained.
- [ArangoDB editions](https://docs.arango.ai/arangodb/stable/features/): integrated models/search and distinct Community binary, Enterprise and BUSL-source terms. Added a direct paragraph spelling out the Community commercial-production restriction and 100 GiB cap, while preserving the distinction from source licensing.

No correction to the follow-up paragraph or compact-memory row was needed: both accurately describe an all-six comparison/evaluation plan, not executed testing. The prior independent research review remains the evidence for other inherited product claims; not every link was independently reopened. Actual performance, extraction quality, applicable licensing, edition/extension compatibility and operational recovery remain to be demonstrated with pinned versions. No database, paid resource or external ingestion was created by this review.
