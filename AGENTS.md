# Project startup and agent workflow

Read `docs/LLM_CONTEXT.md`, then `.project-memory/README.md`. Consult `docs/PROJECT_MAP.md` for locations and dependencies and `docs/REVIEW.md` for validation limits.

Always read and apply `SKILL.md` (general working skills) and `SKILL_Mem.md` (PMS project skills) at project startup. Each starts with a skills contents list; keep that list current when adding skills. The general file is reusable in other workspaces; this startup rule applies to this workspace.

This is a documentation analysis workspace. `root_manual` is a Windows junction to `C:\Users\Fred_U\Documents\COPS\PMS`, an external manual source. It is locally excluded by `.git/info/exclude`; it is not a source copy. Treat this target as read-only unless the user explicitly requests source changes. Write analysis, notes and generated artifacts in this workspace outside `root_manual`.

For project analysis, an orchestrating agent should scope the task, delegate source inspection to an analyst and have a separate reviewer check claims against source before finalizing. Agents run only when invoked; these files provide continuity, not an always-running service. For simple unrelated work, use normal judgment rather than spawning unnecessary agents.

Preserve exact Unicode paths and PMS version context. Do not merge the two change-log folders by name. Cite source topic paths/headings for substantive answers; distinguish manual claims from verified running-system behavior. Read German HTML as UTF-8, strip export chrome for interpretation, and inspect linked images where text depends on screenshots or diagrams.

Keep memory compact: update verified facts and evidence pointers after meaningful discoveries, record unresolved items honestly, and never store secrets or reproduce large manual sections. Revalidate source/junction and dated inventory after source changes. See `.project-memory/README.md` for the update protocol.
