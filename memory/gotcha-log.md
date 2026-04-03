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

### Auto-memory creates invisible, uncurated knowledge (2026-03-19) [RESOLVED] [PROMOTED]
**Problem**: After months of using Claude Code's auto-memory (~/.claude/projects/), 75 memory files had accumulated across 28 projects. Most were unknown to the project owner. Stale entries survived. The "promote and retire" phases of the self-learning loop weren't happening because the memory was invisible.
**Root cause**: Auto-memory is stored in path-mangled directories outside the repo. Files don't appear in the editor, aren't version controlled, and aren't searchable. The design assumed a clean split between agent-facing (auto-memory) and human-facing (committed) content — but in practice, all memory benefits from human review.
**Fix**: Moved all memory files in-repo to visible `memory/` directories. Documented as ADR-001 in agent-ready-projects. Updated the framework to recommend in-repo memory by default. Also discovered and fixed a "global file cliff" — project-specific content in the global CLAUDE.md burning context tokens in every repo.

### Astro base path missing from internal links (2026-03-29) [RESOLVED]
**Problem**: All internal links on the site gave 404s on GitHub Pages. Links like `/patterns/context-is-architecture` resolved to `ducroq.github.io/patterns/...` instead of `ducroq.github.io/augmented-engineering/patterns/...`.
**Root cause**: Hardcoded `href="/..."` paths in .astro files don't include the `base` configured in astro.config.mjs. Astro doesn't rewrite hrefs automatically — only asset paths through its build pipeline.
**Fix**: Use `import.meta.env.BASE_URL` in all components and pages. Normalize with trailing slash since Astro returns `/augmented-engineering` (no trailing slash) which concatenates wrong with `patterns/...`.

### Astro eats Mermaid curly braces (2026-03-29) [RESOLVED]
**Problem**: Mermaid diagrams with `{}` (diamond/rhombus nodes) rendered as syntax errors. The `{` and `}` were stripped from the built HTML.
**Root cause**: Astro interprets `{}` in templates as expression delimiters. Mermaid syntax like `Q1{"Multiple sessions?"}` gets the braces eaten.
**Fix**: Define diagrams as JS strings in the frontmatter or `<script>` and inject with `set:html` or `textContent`. Never put Mermaid code with `{}` directly in Astro template markup.

### Mermaid can't render in display:none tabs (2026-03-29) [RESOLVED]
**Problem**: Switching tabs showed "Syntax error" instead of diagrams. Only the first tab's diagram rendered.
**Root cause**: Mermaid needs elements to be visible in the DOM to measure and render SVGs. Hidden tabs (`display: none`) can't be rendered.
**Fix**: Show all tabs on page load, run `mermaid.run().then()`, then hide non-active tabs after rendering completes. Tab switching just toggles display — no re-rendering.

## Promoted

| Entry | Promoted to | Date |
|-------|------------|------|
| Auto-memory creates invisible, uncurated knowledge | MEMORY.md (Recently Promoted) + CLAUDE.md hard constraint (in-repo memory) | 2026-03-28 |
| Astro template gotchas (base path, curly braces, display:none) | MEMORY.md (Recently Promoted) — shared root cause: Astro silently transforms non-HTML content | 2026-04-03 |
