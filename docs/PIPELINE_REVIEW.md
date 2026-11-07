# Independent local pipeline review

Date: 2026-11-07 (Europe/Vienna). Reviewer separate from bundle and extraction authors. Scope: `src/manual_knowledge/bundles.py`, `extraction.py`, `__main__.py`, and their synthetic tests. Accepted as an initial local capture/validation slice after the corrections below; this is not completion of all Gate 2 requirements or a serving/publication readiness certificate.

## Findings and rechecks

| Finding | Impact | Correction and verification |
| --- | --- | --- |
| PR1: `os.walk` silently ignored unreadable subdirectories | High: a partial snapshot could be labeled complete | Reproduced with synthetic source and injected `PermissionError`. Author added fail-closed `onerror`; dedicated regression passes. |
| PR2: image paths had no explicit resolution/provenance state | Medium: missing images could be mistaken for complete visual evidence | Each record now binds available image paths to occurrence IDs and hashes; missing and external/unsafe references are explicit, all visual review starts unreviewed. Validator recomputes bindings; regression passes. |
| PR3: unanchored paragraph evidence lacked source lines | Medium: retrieval text could lose its raw locator | Extraction author added block line/class metadata. Rechecked actual appendix B: CalculationLogging maps to line 1033 with ABACUS/Settings heading ancestry. |
| PR4: Word-style table headings were not marked as headers | Medium: native `th` detection missed manual table semantics | Extraction author recognizes `WD_HBTabellenüberschrift` in cells. Actual ABACUS table header flags and synthetic regression rechecked. |

No unresolved blocker identified for this bounded local-only slice. The snapshot prerequisite remains external: the quiescent flag is the operator's assertion, not an OS snapshot mechanism.

## Executed verification

- `PYTHONPATH=src python -m unittest discover -s tests -v`: 15 tests, 14 passed and one skipped because this Windows host denied symbolic-link creation. Tests cover deterministic capture, duplicate occurrences, source/inventory mutation, strict UTF-8, overlap/overwrite refusal, malformed paths/identity, corrupted hashes, rehashed forged extraction, unreadable inventory, asset bindings and structural extraction.
- Independently created a real Windows junction in an ignored synthetic fixture; capture rejected it as a nested link. This supplements the skipped symlink test without claiming every reparse-point type tested.
- Independent temporary-source probes confirmed unchanged revision after mtime-only changes, distinct Unicode path occurrences sharing one blob, output-inside-source rejection before writing, and rejection of corrupted records/blobs.
- Actual source read-only smoke checks confirmed S05's Markt → Stadt → Land → Währung table rows, and S11's ABACUS hierarchy, Word-header flags and raw paragraph locator. These are parser checks of selected manual topics, not all 15 semantic answer tests.
- Reviewed CLI error handling and explicit quiescent-source option. Bundle validation recomputes extraction from immutable raw blobs rather than trusting an attacker-updated records checksum alone.

Review performed no writes in `root_manual`, source upload, remote embedding, database query or cloud operation. Code paths resolve source/output overlap before output creation, reject observed nested links, stage outside source and move the completed directory only after validation.

## Remaining limits

The implementation retains full source blobs and one monolithic records segment; it does not yet provide contextual extraction caches, segmented delta transport, parent revisions, explicit revision deltas, graph/assertion modeling, character-offset evidence spans, embeddings, jobs, publication fencing, reader leases, retention, authentication or recovery operations. No database compatibility or performance gate passes from these tests.

Extraction is structural HTML parsing, not browser rendering/OCR or semantic inference. It preserves spans rather than expanding a logical table grid; unknown chrome remains, and unresolved image references are recorded rather than fetched. Visual content remains unreviewed until a separate workflow records an inspection. The selected real-source checks do not establish whole-corpus extraction accuracy.

Filesystem checks assume an operator-controlled quiescent source and output parent. They do not defeat a hostile concurrent filesystem attacker replacing paths between checks and reads. Final inventory and rehashing detect tested mutations but cannot prove a coherent multi-file snapshot. Atomic directory rename is not a tested power-loss durability guarantee; no fsync/recovery claim is made. Validation proves internal consistency with the supplied manifest, not external authority, authenticity or historical source completeness.

The small synthetic junction fixture remains under ignored `.runtime/review-junction/`: automatic command policy rejected cleanup. It contains no manual data and is not part of deliverables. Future review should check the exact committed files and rerun appropriate tests after changes.
