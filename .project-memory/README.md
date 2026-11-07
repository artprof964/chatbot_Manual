# Small external project memory

Purpose: a compact, file-based handoff for later LLM sessions. This is not a vector database or a running service. Load this file and `facts.md` at startup, then retrieve detail from source or `docs/PROJECT_MAP.md` only when needed.

Update protocol:
1. Check the junction target and source availability before relying on source facts.
2. Read evidence before adding or changing a fact. Record the date and exact source pointer in `facts.md`; distinguish observed facts, decisions and open questions.
3. Replace stale entries rather than append repetitive session logs. Keep facts small (aim below 100 lines); keep long explanations in `docs/` and confidential material in the source.
4. For source changes, refresh affected inventory/dependency claims, the LLM context and review status. A past review does not validate later edits.
5. Have a separate reviewer validate substantial new structural claims, then update `docs/REVIEW.md`. Do not mark unanswered questions as resolved without evidence.

No credentials, user data excerpts, financial conclusions or large manual copies belong in memory.
