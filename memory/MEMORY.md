# Memory

## Topic Files

| File | When to load | Key insight |
|------|-------------|-------------|
| `memory/gotcha-log.md` | Stuck or debugging | Problem-fix archive |
| `claims/claim-registry.md` | Writing any content with factual claims | 17 claims tracked; 59% coverage; P0 at 40% |

## Current State

- **Proposition written** (`PROPOSITION.md`): "What's new when engineers work with AI agents" — four patterns from nine projects
- **Reviewed by 6 agents** (`REVIEW-SYNTHESIS.md`): convergent feedback applied (inverted framing, split persistent/transient properties, added falsifiability)
- **Five case studies written** (pattern-first, loosely coupled to claim registry)
- **Website built** (`site/`): Astro static site with hand-drawn SVG illustrations, graph-paper background
- **Four additional source projects explored**: llm-distillery, RenkumSpot, ese_bot, ovr.news (not yet case studies, but evidence in proposition)
- **Guide track scaffolded** but not populated (patterns/, anti-patterns/, by-phase/)
- **Research track scaffolded** with README (questions + methodology statement)

## Related Repos — Quick Reference

| Repo | Key file to read first |
|------|----------------------|
| agent-ready-projects | `README.md` (the full guide) |
| agent-ready-papers | `README.md` + `papers/perspective/` (Paper 1) |
| driven-pendulum | `docs/theory/00_index.md` + `claims/claim_registry.md` |
| vmodel.eu | `CLAUDE.md` + `docs/adr/README.md` |
| OPAL (BR head) | `design_review_checklists/00_INDEX.md` |
| llm-distillery | `CLAUDE.md` + `docs/adr/` |
| RenkumSpot | `CLAUDE.md` + `docs/decisions/` |
| ese_bot | `docs/ARCHITECTURE.md` + `docs/decisions/` |
| ovr.news | `CLAUDE.md` + `docs/decisions/` |

## Active Decisions

- **Framing**: "SE is necessary but insufficient" (not "agentic engineering IS systems engineering") — per review feedback
- **Case study style**: Pattern-first, loosely coupled to claim registry — not thesis chapters
- **Material properties split**: Persistent (confidence inflation, observation-calibration gap) vs. transient (scoring regression, plausible-but-wrong severity)
- **Personal project**: No institutional references (HAN removed from all public-facing docs)
- **Adopted agent-ready-projects v1.0.0**: Layered memory system for session continuity
- **Adopted agent-ready-papers claim registry**: Typed verification with confidence tiers
