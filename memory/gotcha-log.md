# Gotcha Log

<!-- Structured problem/solution journal. Append-only.
     Part of the self-learning loop: Capture → Surface → Promote → Retire.

     PROMOTION LIFECYCLE:
     - New entries start here (Capture phase)
     - At end-of-session, review for patterns (Surface phase)
     - When an entry recurs 2-3 times, promote it to the relevant topic file
       as an "if X, then Y" pattern (Promote phase)
     - When a gotcha's root cause is fixed, mark it [RESOLVED] (Retire phase)
     - Track what you've promoted in the "Promoted" section below

     When the root cause is fixed, mark it resolved here (don't delete). -->

<!-- Template for new entries:

### [Short description] (YYYY-MM-DD)
**Problem**: What went wrong or was confusing.
**Root cause**: Why it happened.
**Fix**: What solved it.

-->

### Auto-memory creates invisible, uncurated knowledge (2026-03-19)
**Problem**: After months of using Claude Code's auto-memory (~/.claude/projects/), 75 memory files had accumulated across 28 projects. Most were unknown to the project owner. Stale entries survived. The "promote and retire" phases of the self-learning loop weren't happening because the memory was invisible.
**Root cause**: Auto-memory is stored in path-mangled directories outside the repo. Files don't appear in the editor, aren't version controlled, and aren't searchable. The design assumed a clean split between agent-facing (auto-memory) and human-facing (committed) content — but in practice, all memory benefits from human review.
**Fix**: Moved all memory files in-repo to visible `memory/` directories. Documented as ADR-001 in agent-ready-projects. Updated the framework to recommend in-repo memory by default. Also discovered and fixed a "global file cliff" — project-specific content in the global CLAUDE.md burning context tokens in every repo.

## Promoted

<!-- Track gotchas that have been promoted to topic files or the memory index.

| Entry | Promoted to | Date |
|-------|------------|------|

-->
