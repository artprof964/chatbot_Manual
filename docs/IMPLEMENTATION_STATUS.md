# Local implementation status

Date: 2026-11-07 (Europe/Vienna). This is a first executable neutral bundle slice, not the completed knowledge service. The previous planning review remains valid only for its stated planning scope. No database has been selected or benchmarked.

## Implemented

- Standard-library Python package in `src/manual_knowledge`, requiring Python 3.11 or newer; verified on this host's Python 3.14.0.
- Strict UTF-8 HTML extraction of Word-style heading paragraphs, anchors, source line locators, tables/cells/spans, exact codes and image references. Script/style/head/nav/footer content is excluded; unknown chrome is retained. No active source content executes and no asset URL is fetched.
- Complete local capture into a new immutable-by-convention bundle directory: content-addressed blobs, distinct path occurrences, deterministic records and manifest/revision digests. The same bytes at different Unicode paths retain separate identities.
- Source/output overlap and nested reparse-point rejection, unreadable inventory failure, second inventory/content checks, and staged finalization. An externally quiescent source/snapshot is required; two scans do not create an atomic filesystem snapshot.
- Validation checks structure, identities, hashes, lengths, record coverage and reproducible extraction. Image references bind to captured occurrence/hash or explicitly carry missing/external-or-unsafe status; all visual semantics remain unreviewed in generated records.
- `evaluation/source_evidence.json` freezes ten topic/image fingerprints and maps S01–S15 to source locators. It contains no manual file copies. The verifier checks local hashes without changing the source.

## Run locally

From the repository root in PowerShell, no package installation or network access is necessary:

```powershell
$env:PYTHONPATH = 'src'
python -m unittest discover -s tests -v
python evaluation/verify_source_evidence.py
python -m manual_knowledge --help
```

Capture a **quiescent** directory of synthetic fixtures or an authorized local source export to a new output directory outside that source:

```powershell
$env:PYTHONPATH = 'src'
python -m manual_knowledge capture PATH_TO_SOURCE .runtime/example-bundle --dataset example --quiescent-source
python -m manual_knowledge validate .runtime/example-bundle
```

Use a new output path for each capture. Capture does not modify the source and refuses an existing output. Missing local images are recorded for review, not silently presented as available evidence. Successful validation checks bundle consistency; it does not authorize publication or certify semantic answer quality. Bundle hashes are not signatures or access controls.

## Validation and limits

The local synthetic suite exercises deterministic reruns, byte deduplication with separate occurrences, exact extraction, invalid UTF-8, source mutation/additions, unreadable subtrees, corruption, unsafe paths, tampered extraction, output overlap and image-reference status. Test results and independent findings are recorded in `PIPELINE_REVIEW.md`. Ten frozen evidence fingerprints matched the external source on this date.

This does not complete all of Gate 2. Still outstanding: full source-to-original-offset mapping, semantic assertion extraction, schema migrations, exhaustive malformed HTML/layout handling, complete link auditing, OCR/visual review workflow, expanded 50–100 question oracle and performance qualification. Row/column span attributes are retained, not expanded into a semantic grid. Source files and records are currently held in memory per document, and validation reparses HTML; large-corpus scaling is unmeasured. Capture assumes a trusted, quiescent local filesystem; it is not a defense against a hostile process replacing filesystem objects during the operation.

No incremental cross-revision segment reuse, transport/receiver, database adapter, job leases, publication/GC protocol, authenticated API, model integration, offline mirror, cloud deployment or restore drill is implemented. The synthetic P01–P08 specifications are not all executable tests yet. Local capture/validation must not be described as passing those end-to-end gates.

Gate 1 preflight found PostgreSQL 18.1 and pgvector 0.8.1 files but no AGE extension or usable WSL/container runtime in the inspected locations. No existing database service/configuration was changed. See `COMPATIBILITY_STATUS.md`; the six candidate runtime qualification results remain untested.

## Next work

1. Qualify a released AGE/PostgreSQL/pgvector combination in an isolated supported environment; keep the five alternatives in evaluation.
2. Expand the neutral contracts and failure fixtures, then implement local incremental import/transport independently of database choice.
3. Gate publication, serving and any cloud trial on the outline's correctness, access and deployment inputs.

The tracked `.gitignore` excludes `root_manual`, local bundles/runtime data, environments and common credential files. The external manual and generated real-corpus data must not be pushed to GitHub. The repository contains project documentation, code, synthetic tests and evidence fingerprints/locators only.
