# Memory

## Topic Files

| File | When to load | Key insight |
|------|-------------|-------------|
| `memory/gotcha-log.md` | Stuck or debugging | Problem-fix archive |
| `claims/claim-registry.md` | Writing any content with factual claims | 17 claims tracked; 59% coverage; P0 at 40% |
| `memory/project_aug_podcast_marketing.md` | Working on podcast | Series identity, competitive landscape, growth path |
| `memory/feedback_echo_chamber.md` | Adding new evidence | Circular evidence risk — case studies verifying themselves |
| `memory/reference_tandemize.md` | Discussing external partnerships | Tandemize.ai potential synergy |
| `memory/session_2026-03-19_podcast_launch.md` | Context on podcast creation decisions | Marathon session: memory migration, framework v1.2.0 |
| `docs/decisions/README.md` | Making an architectural decision | ADR index — 7 decisions (podcast, site reframe, umbrella pivot) |
| `docs/VIBE.md` | Working on site design | Visual identity: engineered, honest, practitioner-first |

## Recently Promoted

<!-- Gotchas promoted to topic files or CLAUDE.md. Format:
     "if [situation], then [what to do]" — promoted from gotcha-log YYYY-MM-DD -->

- If memory accumulates in auto-memory (~/.claude/projects/), move it in-repo to `memory/` — promoted from gotcha-log 2026-03-19

## Current State

- **Proposition written** (`PROPOSITION.md`): "What's new when engineers work with AI agents" — four patterns from nine projects
- **Reviewed by 6 agents** (`REVIEW-SYNTHESIS.md`): convergent feedback applied (inverted framing, split persistent/transient properties, added falsifiability)
- **Five case studies written** (pattern-first, loosely coupled to claim registry)
- **Website reframed as pattern library** (`site/`, 2026-03-28): Killed nine-projects section, leads with reader's problem not research. Quick reference decision table on homepage. Pattern pages restructured: problem → fix → try this → evidence. Per ADR-004.
- **Four additional source projects explored**: llm-distillery, RenkumSpot, ese_bot, ovr.news (not yet case studies, but evidence in proposition)
- **Driven-pendulum case study updated** (2026-03-16): Session 7 added — V&V on informal messages (5 errors caught in WhatsApp drafts), 6-agent parallel review (14 issues), human-in-the-loop "short solenoid" terminology catch. Claims E-1, T-1, T-2, C-1, C-2 evidence updated.
- **Guide by-phase/ populated** (2026-03-17): V-model phase mapping with feedback loop framing and evidence links
- **Guide patterns/ and anti-patterns/ scaffolded** but not yet populated
- **Research track scaffolded** with README (questions + methodology statement)
- **ADR-001 written in agent-ready-projects** (2026-03-19): In-repo memory over auto-memory — moved 28 projects (~75 files) from hidden auto-memory to visible in-repo `memory/` directories. Framework guidance updated.
- **Augmented Engineering podcast created** (2026-03-19): Series "Augmented Engineering: the craft, not the hype" — ep 0 (introduction) and ep 1 (context engineering) scripted. 8-persona review battery created. ADR-001 written for dialogue writing style in podcast-generator.
- **Global CLAUDE.md cliff discovered and fixed** (2026-03-19): Project-specific content (voice library, TTS engines) moved from global instructions to podcast-generator's CLAUDE.md. Added "global file cliff" guidance to framework.
- **Full agent-ready-projects adoption** (2026-03-28): Upgraded v1.1.0 → v1.3.4. Added decision framework, ground truth designations, negative-results constraint, ADR index with README, /curate skill. CLAUDE.md architecture tree updated to match actual repo.
- **Site reframed as pattern library** (2026-03-28): Per ADR-004. Leads with reader's problem, quick reference decision table, pattern pages restructured. Nine-projects section removed.
- **Site base path links fixed** (2026-03-29): All internal hrefs now use import.meta.env.BASE_URL. See gotcha-log.
- **Strategic pivot: tool umbrella** (2026-03-29): ADR-005/006/007. Augmented Engineering is a tool umbrella, not a research proposition. Only durable (structural) patterns are core. Don't build umbrella ahead of tools.
- **VIBE.md created** (2026-03-29): Visual identity — Inter font, semantic-only color, clean surfaces. Replaces notebook/pencil aesthetic.
- **Site redesigned per VIBE** (2026-03-29): Dark mode, Inter typography, clean surfaces. Core/advisory pattern split. agent-ready-projects tool page with tabbed Mermaid visual walkthrough (cliff, layers, loop, rhythm). Pill tabs, stadium-shaped nodes, dark-mode-aware classDef colors.
- **Visual guide added to agent-ready-projects** (2026-03-29): 4-page Mermaid guide in docs/guide/ — linked from README. Also rendered on augmented-engineering site tool page.
- **Issues filed**: #3 (extend review agents for umbrella), #4 (layered verification tooling as second flagship).

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

## Podcast — Augmented Engineering: the craft, not the hype

| File | Contents |
|------|----------|
| `memory/project_aug_podcast_marketing.md` | Series identity, competitive landscape, proposition, growth path, cognitive load insight, tandemize.ai funnel strategy |
| `memory/reference_tandemize.md` | Friend's planned augmented engineering business, potential podcast synergy |
| `memory/feedback_echo_chamber.md` | Circular evidence risk — case studies verifying themselves |
| `memory/session_2026-03-19_podcast_launch.md` | Marathon session: podcast creation, memory migration, framework v1.2.0, personal insights |

- Scripts live in `podcast/dialogen/` (ep 00 intro + ep 01 context engineering)
- Show notes with claim verification live in `podcast/shownotes/`
- Review agents (8 personas + orchestrator) live in `.claude/agents/ae-review-*.md`
- ADR-001 (dialogue writing style for local TTS) lives in podcast-generator: `docs/decisions/`
- Digital Engineers research (`C:\Users\scbry\OneDrive - HAN\Research\Digital engineers\`) is the source for podcast stats — extraction report produced with ~30 findings mapped to episodes

## Active Decisions

- **Framing**: "SE is necessary but insufficient" (not "augmented engineering IS systems engineering") — per review feedback
- **Case study style**: Pattern-first, loosely coupled to claim registry — not thesis chapters
- **Material properties split**: Persistent (confidence inflation, observation-calibration gap) vs. transient (scoring regression, plausible-but-wrong severity)
- **Personal project**: No institutional references (HAN removed from all public-facing docs)
- **Adopted agent-ready-projects v1.3.4**: Layered memory system for session continuity. v1.3.4 adds: /curate skill for end-of-session curation, negative results as knowledge, ground truth principle, review agent skeleton
- **Adopted agent-ready-papers claim registry**: Typed verification with confidence tiers
- **Feedback loop framing adopted** (2026-03-17): "agent generates → agent reviews → agent validates → engineer decides" — borrowed from practitioner discourse, grounded in our evidence
- **In-repo memory by default**: Memory files live in `memory/` inside the repo, not in tool auto-memory. Exception only for content that should never be committed. Per ADR-001 in agent-ready-projects.
- **Site is a pattern library, not research portfolio** (ADR-004): Lead with the reader's problem, not the research journey. Evidence supports but doesn't lead. Nine projects are attribution, not content.
- **Augmented Engineering is a tool umbrella** (ADR-005): The proposition becomes backstory. Tools are the point.
- **Only durable patterns are core** (ADR-006): Context Is Architecture and Layer Your Verification are core (structural). Learn the Material and Reproduce Don't Assess are advisory (model-dependent, 12-24 month shelf life).
- **Don't build umbrella ahead of tools** (ADR-007): Minimal umbrella until second flagship exists. agent-ready-projects is the flagship. Layered verification tooling is the candidate second tool (issue #4).
