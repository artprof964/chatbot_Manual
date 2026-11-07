# Independent review

Later implementation-planning review (2026-11-07): see `IMPLEMENTATION_REVIEW.md` and `IMPLEMENTATION_EVALUATION.md` for the new local/cloud outline, source-derived tests and correction rounds. The structural review below remains scoped to its original artifacts; it does not validate the later design or establish runtime correctness.

Review date: 2026-11-07 (Europe/Vienna). Reviewer was a separate agent from the analyst and document author.

Verdict: accepted for use as a structural map and bounded LLM handoff, with the additions below. This is a full file inventory plus sampled source review; it is not a semantic review of the entire manual or a running-system validation.

## Artifacts reviewed

`AGENTS.md`, `docs/PROJECT_MAP.md`, `docs/LLM_CONTEXT.md`, `.project-memory/README.md` and `.project-memory/facts.md`. Checked their source boundary, startup sequence, object/topic locations, dependency distinctions, compact memory protocol and stated uncertainty. Agent orchestration is an invocation workflow; the files do not create a persistent agent service.

## Independently reproduced checks

- PowerShell `Get-Item root_manual` reports a Junction targeting `C:\Users\Fred_U\Documents\COPS\PMS`; `.git/info/exclude` contains `/root_manual/`. Git has an unborn HEAD. Review writes were confined to project-owned Markdown outside the junction.
- Python `Path.rglob`, file sizes and suffix counts reproduce 24,500 files, 741,945,184 bytes, and every extension count in the map. Per-tree totals are 17,653 + 216 + 736 + 1,180 + 608 + 2,217 + 1,762 + 1 + 127 root-level files = 24,500. HTM counts and main/interface topic-directory counts also match the map.
- Exact directory `19-00-positionkeeping_de` exists. The two change-log names are distinct on disk. SHA-256 comparison at matching relative paths independently reproduces 736 shared, 463 identical, 273 different, zero ASCII-only and 444 Unicode-only files. Presence and hashes establish overlap, not content authority or chronology.
- `root_manual/Handbuch/de/index.htm`, lines 7–10, identifies RoboHelp 11, WebHelp 5.50 and UTF-8. Its viewer scripts and skin-selection code support the documented generated-help classification. `whproj_xml.js` independently confirms homepage, language 1031 and `whxdata` references.
- Foreword `_handbuch_vorwort_de/_handbuch_vorwort_de.htm`, lines 8–11, records original Word filename and local/shared CSS links. Its shared `../../RHStyleMapping.css` resolves to absent `Handbuch/de/RHStyleMapping.css`. This is a sampled missing reference; no rendering consequence was tested.
- UTF-8 topic inspection in `02-pms_online_standardschnittstelle/01-03-itf_technische_erlaeuterungen_de/01-03-itf_technische_erlaeuterungen_de.htm`, section 1.3.5, verifies database-state prerequisites for insert/update/delete and explicit list/dependency checks. `01-02-itf_formale_erlaeuterungen_de/01-02-itf_formale_erlaeuterungen_de.htm`, line 147, verifies key-directory validation code `S`. These are source-backed domain/interface dependencies, not workspace runtime requirements.

## Review amendments

Added independently reproduced change-log hash comparison to the map and compact memory. Added explicit source-backed database/key validation dependencies to the map. Retained exact positionkeeping path and the distinction between generated viewer dependencies and documented PMS integrations. The context and guidance already state the appropriate read-only source boundary and limits; no further edits were required there.

## Limits and unresolved items

No browser launch, import execution, database connection, deployed PMS version/license verification, comprehensive hyperlink audit or network-system inspection was performed. No diagram-based relationship claim is made; ER images and screenshots must be inspected for future answers that depend on them. The map locates documented business objects and schema reference topics; it does not reconstruct the entire object model or establish executable classes or a live schema. Current export completeness, source authoring files and authority between overlapping version trees remain unresolved. Refresh inventory and this review after meaningful source or structural changes.
