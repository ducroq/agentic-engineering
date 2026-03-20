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
- **Driven-pendulum case study updated** (2026-03-16): Session 7 added — V&V on informal messages (5 errors caught in WhatsApp drafts), 6-agent parallel review (14 issues), human-in-the-loop "short solenoid" terminology catch. Claims E-1, T-1, T-2, C-1, C-2 evidence updated.
- **Guide by-phase/ populated** (2026-03-17): V-model phase mapping with feedback loop framing and evidence links
- **Guide patterns/ and anti-patterns/ scaffolded** but not yet populated
- **Research track scaffolded** with README (questions + methodology statement)
- **ADR-001 written in agent-ready-projects** (2026-03-19): In-repo memory over auto-memory — moved 28 projects (~75 files) from hidden auto-memory to visible in-repo `memory/` directories. Framework guidance updated.
- **Agentic Engineering podcast created** (2026-03-19): Series "Agentic Engineering: the craft, not the hype" — ep 0 (introduction) and ep 1 (context engineering) scripted. 8-persona review battery created. ADR-001 written for dialogue writing style in podcast-generator.
- **Global CLAUDE.md cliff discovered and fixed** (2026-03-19): Project-specific content (voice library, TTS engines) moved from global instructions to podcast-generator's CLAUDE.md. Added "global file cliff" guidance to framework.

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

## Podcast — Agentic Engineering: the craft, not the hype

| File | Contents |
|------|----------|
| `memory/project_ae_podcast_marketing.md` | Series identity, competitive landscape, proposition, growth path, cognitive load insight, tandemize.ai funnel strategy |
| `memory/reference_tandemize.md` | Friend's planned agentic engineering business, potential podcast synergy |
| `memory/feedback_echo_chamber.md` | Circular evidence risk — case studies verifying themselves |
| `memory/session_2026-03-19_podcast_launch.md` | Marathon session: podcast creation, memory migration, framework v1.2.0, personal insights |

- Scripts live in `podcast/dialogen/` (ep 00 intro + ep 01 context engineering)
- Show notes with claim verification live in `podcast/shownotes/`
- Review agents (8 personas + orchestrator) live in `.claude/agents/ae-review-*.md`
- ADR-001 (dialogue writing style for local TTS) lives in podcast-generator: `docs/decisions/`
- Digital Engineers research (`C:\Users\scbry\OneDrive - HAN\Research\Digital engineers\`) is the source for podcast stats — extraction report produced with ~30 findings mapped to episodes

## Active Decisions

- **Framing**: "SE is necessary but insufficient" (not "agentic engineering IS systems engineering") — per review feedback
- **Case study style**: Pattern-first, loosely coupled to claim registry — not thesis chapters
- **Material properties split**: Persistent (confidence inflation, observation-calibration gap) vs. transient (scoring regression, plausible-but-wrong severity)
- **Personal project**: No institutional references (HAN removed from all public-facing docs)
- **Adopted agent-ready-projects v1.1.0**: Layered memory system for session continuity (v1.1.0: tool-agnostic, agent-assisted, worked examples, adoption feedback loop)
- **Adopted agent-ready-papers claim registry**: Typed verification with confidence tiers
- **Feedback loop framing adopted** (2026-03-17): "agent generates → agent reviews → agent validates → engineer decides" — borrowed from practitioner discourse, grounded in our evidence
- **In-repo memory by default**: Memory files live in `memory/` inside the repo, not in tool auto-memory. Exception only for content that should never be committed. Per ADR-001 in agent-ready-projects.
