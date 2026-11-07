---
name: pms-manual-analysis
description: Analyze the German COPS PMS manual and maintain evidence-based project knowledge in chatbot_Manual. Read at every startup in this project; use extraction and database guidance only for those tasks.
---

# PMS project skills

## Skills contents

1. [Startup and source boundary](#startup-and-source-boundary)
2. [Manual retrieval and citations](#manual-retrieval-and-citations)
3. [Analysis and independent review](#analysis-and-independent-review)
4. [Extraction and database research](#extraction-and-database-research)
5. [Compact project memory](#compact-project-memory)

Apply startup, evidence and memory rules throughout project work; use the other workflows when applicable. Paths below are relative to this workspace.

## Startup and source boundary

Read `docs/LLM_CONTEXT.md`, then `.project-memory/README.md` and `.project-memory/facts.md`; consult `docs/PROJECT_MAP.md` and `docs/REVIEW.md`. Check that `root_manual` still targets `C:\Users\Fred_U\Documents\COPS\PMS` and the source is available before relying on it. Keep that external junction read-only unless source changes are explicitly requested; write outputs outside it.

## Manual retrieval and citations

Search substantive topics under `root_manual/Handbuch/de/`, using the project map to locate them. Read German HTML as UTF-8 and remove generated viewer chrome for interpretation. Preserve exact Unicode paths, headings/anchors and PMS version context; keep `03-pms_aenderungsprotokolle` and `03-pms_änderungsprotokolle` distinct. Inspect linked screenshots/diagrams when they carry relevant meaning; image filenames require their full topic path. Cite exact topic paths and headings. Manual statements do not establish deployed PMS behavior or a live database schema.

## Analysis and independent review

For project analysis, the orchestrator scopes the question, an analyst inspects relevant sources, and a separate reviewer checks substantive claims against evidence before finalization. Use normal judgment for simple unrelated work. These are invoked agents, not persistent services; report review limits honestly.

## Extraction and database research

For ingestion, consult `docs/DATABASE_RESEARCH.md`, `docs/DATABASE_RESEARCH_REVIEW.md` and `docs/research/CORPUS_PROFILE.json`. Recover Word-style paragraph headings and anchors rather than relying on native h1-h6 tags; preserve table headers, field codes, units, image links and evidence/version identity. Deduplicated bytes must retain every source occurrence. Neo4j and PostgreSQL/AGE/pgvector are evaluation candidates, not a selected or benchmarked deployment; recheck current capabilities and licenses before implementation.

## Compact project memory

Follow `.project-memory/README.md`: update verified facts with dates and exact evidence pointers after meaningful discoveries, replace stale entries and retain unresolved questions. Keep long analysis in `docs/`; exclude secrets and large manual copies. After source changes, refresh affected inventory/context and independent review status; prior review does not validate later changes.
