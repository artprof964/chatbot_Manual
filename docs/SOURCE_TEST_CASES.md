# Source-derived process and retrieval test cases

Inspected 2026-11-07 (Europe/Vienna). Status: evidence-backed test specification and comparative design evaluation. No database has been selected, deployed or benchmarked. No PMS import was executed. The external `root_manual` junction remained read-only; its expected target was rechecked. Independent review is recorded in `IMPLEMENTATION_REVIEW.md`.

## Scope and evidence method

Re-read the specific UTF-8 HTML passages below, stripping tags/export chrome for interpretation while preserving line/anchor references. Inspected the actual batch-definition diagram. Compared two matching change-log topic pairs. This is a detailed sample, not a semantic review of all 351 topic files. Paths in the evidence register are relative to `root_manual/Handbuch/de/`; line numbers refer to the current source bytes, not a permanent identifier. Freeze source hashes with the eventual evaluation fixture.

The test oracle is what the manual states, including qualifications and gaps. It is not a claim about a current running PMS installation. Tests of the assistant must retrieve and cite those statements; they must not execute financial operations. Pipeline failure cases are separately labeled synthetic. No source content was uploaded.

## Evidence register

| ID | Exact topic path | Inspected heading / locator |
| --- | --- | --- |
| F | `02-pms_online_standardschnittstelle/01-02-itf_formale_erlaeuterungen_de/01-02-itf_formale_erlaeuterungen_de.htm` | 1.2 Formale Erläuterungen, lines 138–151; 1.2.1 Feldnummer 99999 als Informationsfeld, lines 153–154 |
| T | `02-pms_online_standardschnittstelle/01-03-itf_technische_erlaeuterungen_de/01-03-itf_technische_erlaeuterungen_de.htm` | 1.3.3, anchor `1_3_3_In_welcher`, lines 659–834; 1.3.4, `1_3_4_Reaktionen_der_PMS`, 1141–1157; 1.3.5, `1_3_5_Ebenen_der`, 1159–1295 |
| C | `02-pms_online_standardschnittstelle/01-04-itf_konfigurationsdatei_de/01-04-itf_konfigurationsdatei_de.htm` | Parameter rows, 985–997 and 1197–1203; 1.4.7 Trennzeichen, anchor `1_4_7_Trennzeichen`, 1370–1387; 1.4.10 Überprüfungslogik bei Enum-Feldern, `1_4_10_berpr_fungslogik`, 1400–1405 |
| B | `01-pms_online_handbuch/appx_b-konfigurationseinstellungen_de/appx_b-konfigurationseinstellungen_de.htm` | B.2.1 `B_2_1_Anlage_neuer_Items`, line 992; B.3 `B_3_Konfiguration_durch`, 1004–1008; B.4.1 Modul ABACUS / B.4.1.1 Sektion Settings and table, 1011–1044 |
| K | `01-pms_online_handbuch/appx_k-er-diagramme_de/appx_k-er-diagramme_de.htm` | K.2 Batchdefinition, `K_2_Batchdefinition`, 145–147; inspected asset `01-pms_online_handbuch/appx_k-er-diagramme_de/image004.jpg` |
| A10 / U10 | `03-pms_aenderungsprotokolle/protokoll_pms_10/protokoll_pms_10.htm` / `03-pms_änderungsprotokolle/protokoll_pms_10/protokoll_pms_10.htm` | U10 body anchor `PMS_Revision_10_2_8_vom`, lines 2965–2974; anchor absent from A10 |
| A7 / U7 | `03-pms_aenderungsprotokolle/protokoll_pms_7_0_100_release/protokoll_pms_7_0_100_release.htm` / `03-pms_änderungsprotokolle/protokoll_pms_7_0_100_release/protokoll_pms_7_0_100_release.htm` | Whole-file byte comparison and normalized body-text comparison; method below |

## Source-derived cases and expected answers

Each case should become a reviewed question plus expected evidence/negative assertions in the frozen test set. Expected answers below are paraphrases of source claims. All six candidates must pass the same semantic checks.

| Case | Question / input distinction | Required result and failure condition | Evidence |
| --- | --- | --- | --- |
| S01: operation prerequisites | What prior record state does Insert, Update or Delete require? | Preserve the distinction: insert requires absence; update/delete require presence. Explain these are documented prerequisites and configuration/record context may matter. Do not invent a precise error reaction: the source reaction cells for insert/delete show `?`. | T 1.3.5, 1253–1280 |
| S02: field classifications | Are `P`, `(P)`, `T`, `S`, `F` and `MX` interchangeable validation flags? | Keep all six codes distinct. In particular `(P)` is described as professionally useful but technically unnecessary; `T` compares with a DB table, `S` with the key directory; `MX` expresses mutual exclusivity. Reject a summary that turns all into mandatory fields. | F 143–149 |
| S03: numeric units | How is an ordinary 5% interest rate supplied? | Retrieve 0.05 / German `0,05`, retain the explicit exception qualification, and note configurable decimal/date separators. Never apply the conversion universally to every field. | F 140–142 |
| S04: informational field | Does field `99999` change the import record semantics? | Cite that it is an informational field ignored by the standard interface when importing; the ordinary record description still governs. Preserve the code for exact retrieval, including when queried without prose. | F 153–154 |
| S05: actual dependency chain | What documented prerequisites lead from Markt to Währung? | Preserve table columns and edge direction: Markt depends on Stadt, Stadt on Land, Land on Währung. A three-edge chain is supported by these rows; do not turn `DBEnum=Ja` into a dependency node or infer that hyperlinks are dependencies. Also preserve Indexverzeichnis's two listed dependencies, Markt and Währung. | T 659–760 |
| S06: case-sensitive enums | Is `PUT` equivalent to `Put`? | State the documented enum comparison is case-sensitive. Keep original code spelling while permitting case-insensitive discovery of the documentation. Semantic normalization must not collapse the input values. | C 1.4.10, 1401–1404 |
| S07: empty versus invalid enum | Compare an empty enum field with a supplied but unrecognized value. | Return the distinct controlling flags `STI_Skip_Blank_Enum_Fields` and `STI_skip_enum_field`; connect to their parameter rows. Rows describe blank handling (`yes` retains default) and rejected-value handling (`yes` defaults, `no` rejects record). Preserve the default labels and spelling variants; do not conflate absent value, invalid value and SQL NULL. Section 1.4.10 describes three stages but enumerates four items: retain rather than silently rewrite this source inconsistency. | C 985–997 and 1400–1405 |
| S08: omitted volume and override | What if `20X87` is not delivered, with `remaining_volume=yes` versus `no`? | Preserve the condition: yes uses `20X21`, no yields numeric zero. The word “null” in prose is explicitly followed by `= 0`, so do not translate it into SQL NULL. Mention per-record override field `20X99`; do not invent undocumented override values. | C 1197–1203 |
| S09: delimiter notation | What do `<Null>` and `<Tab>` describe here? | Identify them as documented defaults for text-field delimiter and field separator respectively. Keep literal notation and configuration context, not a database-null interpretation. | C 1.4.7, 1370–1387 |
| S10: error evidence and uncertainty | Where are rejected records/errors recorded and what can happen next? | Cite `.err` for errors and `.bad` for the causing line; pipe stdout reports Failed/OK. Keep the listed reactions as possible reactions, not a promise every error aborts the import. Pair with S01's unknown cells rather than filling them from general behavior. | T 1.3.4, 1141–1157; 1.3.5 |
| S11: Word-style hierarchy and table context | Locate ABACUS / Settings / CalculationLogging and distinguish B.2.1 from table headings. | Reconstruct module/section/table ancestry from paragraph classes and anchors; retain column titles Konfigurationsvariable, Bedeutung, Wertebereich. No native HTML heading dependency, and no table-header paragraph promoted into an unrelated section. This case asserts only location/hierarchy, not the variable's operational meaning. | B 992, 1011–1044 |
| S12: permission qualification | Can any user configure settings for other users? | Return the documented “provided the user has appropriate rights” qualification. Do not infer actual installed authorization behavior, or treat this manual rule as authorization for the assistant. | B 1004–1005 |
| S13: diagram evidence | Where is the batch configuration relation between B_BSET_EXT and B_BSET shown? | Preserve K.2 and the full image path. The inspected diagram shows B_BSET_EXT.BATCH_NAME marked PK,FK1 and B_BSET.BATCH_NAME marked PK with a connecting arrow. Cite visual evidence and review status. Do not infer cardinality, cascade rules or a live database constraint that the image does not establish. | K 145–147 and image004.jpg |
| S14: added revision versus global authority | Which branch contains the PMS 10.2.8 entry and what does Ticket 10049 / 116268 report? | U10 contains the dated 20 February 2019 heading and a correction concerning ambiguous in-memory entries/incorrect dates under large loads; the same anchor is absent from A10. Return U10-specific evidence. Absence from A10 does not prove a contradictory claim, global branch authority or a currently deployed fix. | U10 2965–2974; A10 anchor search |
| S15: bytes versus extracted-content difference | Must every changed file create a semantic conflict? | A7/U7 differ in bytes but the sampled normalized body text is equal. Keep two source occurrences and raw hashes, while permitting reuse only under complete extraction/embedding cache keys. Do not emit a business contradiction merely because raw hashes differ. | A7/U7 comparison below |

### Reproduced branch comparison detail

A7 raw SHA-256: `f6f0bf80c47f22ac419f7496327e45c6a74e7ac336fca0af636476fb39234333`.
U7 raw SHA-256: `1141d026861f9e8d2ad00856ce6a2de105c58a7a705ab2bc78926b25b27a75cc`.
Both normalized body-text SHA-256 values: `3f8089782e0a391114ac119a2c74259b93fa3464c978f63f22976302bd9154a5`.

Diagnostic normalization: take text from the first `<body`, remove script elements with case-insensitive DOTALL regex, replace each remaining tag with one space, HTML-unescape, collapse whitespace, UTF-8 encode and SHA-256. Tag replacement must preserve word boundaries: deleting tags without a replacement space does not reproduce these hashes. This is a bounded diagnostic, not a production parser or proof that rendered pages/assets are identical. A visible differing script uses `document.location.replace(...)` versus `document.location.href = ...`; scripts are excluded from this body-text comparison. A10/U10 inspection separately establishes an actual additional body revision entry, not merely a TOC/export-chrome difference.

## Synthetic pipeline tests derived from these structures

Create fixtures outside `root_manual`; never mutate the original topics. These are proposed tests, not executed results.

| Case | Controlled operation | Required invariant / measurement |
| --- | --- | --- |
| P01 | Import the same S01–S15 fixture twice | Same logical IDs and occurrence count; no duplicate assertions; record bytes sent and reused work. |
| P02 | Change only the S08 zero/condition in a synthetic revision | New evidence/claim version and dependent chunks; old pinned answer still resolves its old evidence. Never publish a mixed old/new rule. |
| P03 | Rename the S14 occurrence, then remove it in a complete fixture snapshot | New path occurrence with reusable bytes; deletion only affects new revision membership. Partial/unreadable capture must not imply deletion. |
| P04 | Replace S13's image while HTML stays unchanged | Invalidate visual extraction and dependent artifacts; retain old image for leased readers. Full path/hash prevents collision with other image004.jpg files. |
| P05 | Change parser/embedding context with unchanged A7/U7 bytes | Recompute affected artifacts by complete cache key; do not reuse vectors solely by blob hash. |
| P06 | Corrupt/intercept upload, delay search projection, lose publication response | Old complete revision remains served until all required projections are ready; retry is idempotent; record transfer versus index/publication time separately. |
| P07 | Expire worker lease; race two publishers; race reader pin with GC | Reject stale fencing token/conflicting generation; a leased revision retains every required evidence blob. |
| P08 | Serve S14 offline at an older complete revision | Display local revision/freshness and limited policy; no fabricated synchronization. Compare equivalent evidence only after pinning a common revision. |

## How the cases further evaluate all six options

These are design implications of actual source cases, not measured pass/fail results. Product capabilities and licensing evidence remain in `IMPLEMENTATION_OPTIONS.md` and `DATABASE_COMPARISON.md`.

| Candidate | Most discriminating checks | Case-driven assessment |
| --- | --- | --- |
| Neo4j + native retrieval | S05 typed/directed path and S13 visual-evidence assertion nodes; S06–S09 exact codes beside semantic search; P02/P06 index readiness | Strong property-graph fit, but code/default fidelity and source extraction are application work. Integrated retrieval reduces service boundaries; test chosen edition's restore and revision filtering. No evidence here proves it faster than AGE. |
| PostgreSQL + AGE + pgvector | S02/S07/S08 typed conditions, unknowns, exact codes plus S05 graph chain; P01/P02/P07 coordinated catalog/jobs/graph | These cases support the provisional consolidation preference: structured evidence and conditional rules matter at least as much as graph traversal. Require mixed relational/AGE rollback and exact-code/filtered-vector tests; source rules do not justify copying live PMS schema into this assistant. |
| ArangoDB + integrated retrieval | S07/S08 structured conditional documents plus S05 edges; P02/P06 per-revision search visibility | Flexible records suit heterogeneous evidence, but no sampled case creates a special need for AQL/document flexibility. Licensing and tested transaction topology remain material obstacles to the OSS-first default. |
| GraphDB + external search | S02/S05 qualified RDF assertions; S07/S08 prevent inference crossing conditions; P02/P06 cross-store readiness | Ontology/inference could encode controlled terms, but these samples require evidence fidelity rather than elaborate inference. Missing source knowledge must remain unknown, not be inferred as false. Additional semantic tooling is not yet shown necessary. |
| Jena/Fuseki + separate retrieval | Same RDF cases as GraphDB; S14 named/version scopes; P06 queued publication plus retrieval readiness | Remains the strongest OSS RDF alternative. A periodic reviewed import can fit a queued writer; whether the extra retrieval service is worthwhile depends on actual ontology demand and operational tests. |
| Neptune Database + S3 + OpenSearch | S05 native-model paths, S14 graph/search version consistency; P06/P08 cloud lag and offline parity | Managed AWS does not solve extraction or conditional-code fidelity. These samples add no demonstrated AWS-specific requirement; autonomous local engine parity remains weaker, while managed operations may matter under future hosting constraints. |

The source review strengthens the recommendation to implement the neutral evidence/extraction contract first, then give PostgreSQL/AGE the first compatibility spike. It does not select a database. S01–S15 are correctness gates common to every candidate; only after those pass should P01–P08 and the existing all-six concurrency/depth workload compare maintenance effort and speed. A failed extractor must not be scored as a database failure. Use common candidate inputs to isolate graph-engine behavior, then native hybrid retrieval to assess the complete stack. Three-hop S05 is source-backed; larger cyclic 4/8-hop stress graphs are synthetic unless additional manual evidence is separately established.

## Execution status and remaining work

Executed: source reads, one image inspection, A7/U7 hash/body comparison and A10/U10 anchor/body inspection. Not executed: ingestion pipeline, answer-generation evaluation, database queries, graph traversal timing, cloud transfer, restore, security or concurrent publication tests. No six-stack result sheet has a measured winner. Build frozen fixtures with source hashes and reviewer-approved expected answers before those tests; expand beyond this sample to 50–100 questions as already planned. Some source terminology/default wording and global version authority remain ambiguous and should be returned as such.
