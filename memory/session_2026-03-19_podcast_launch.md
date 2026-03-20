---
name: Session 2026-03-19 — Podcast launch, memory migration, framework update
description: Major session covering podcast creation, 8-persona review battery, ADRs, memory migration across 28 projects, competitive analysis, and personal insights about AI-augmented engineering
type: project
---

## What happened

Single marathon session that covered podcast creation, framework evolution, and infrastructure cleanup.

### Podcast: Agentic Engineering — the craft, not the hype

1. **Explored both repos** (agent-ready-projects + podcast-generator) to scope the podcast
2. **Wrote ADR-001** for podcast-generator: dialogue writing style for local TTS engines (28 rules covering sentence structure, word choice, emotion through structure, LLM anti-patterns, overlap markers, self-corrections)
3. **Wrote episode 0** (introduction, ~8 min) and **episode 1** (context engineering, ~19 min)
4. **Ran 5-persona review battery** (first round): fact-check, ADR-001 compliance, narrative design, TTS readability, persuasiveness
5. **Rewrote both episodes** based on feedback — added Lisa's team perspective, Sven's harder objections, the "turn" (Marc's 300-line cage), self-corrections, overlap markers
6. **Created series identity**: "Agentic Engineering: the craft, not the hype"
7. **Explored TADA (HumeAI)** as potential new TTS engine
8. **Mined Digital Engineers research** for podcast stats — extracted ~30 usable findings with sources
9. **Wrote show notes with claim verification** for both episodes (8 + 11 claims, 100% verified)
10. **Wove stats into scripts**: trust gap (90%/<10%), senior trust paradox, McKinsey 47%, Jellyfish 20%
11. **Created 8-persona review battery** as reusable agents + orchestrator in `.claude/agents/`
12. **Ran full 8-persona review** (second round) — all feedback compiled into orchestrator report
13. **Applied all P0/P1/P2 fixes**: Marc fallible on teams, trimmed 18%, explained compression, swapped steel analogy, added "won't tools fix this?" question, Lisa pushback on teams
14. **Competitive landscape research**: identified gap (topic crowded, angle wide open)

### Framework: agent-ready-projects v1.2.0

1. **Discovered auto-memory problem**: 75 hidden files across 28 projects nobody maintained
2. **Wrote ADR-001**: in-repo memory over auto-memory
3. **Updated README**: Layer 3 location, new in-repo vs auto-memory table, global file cliff section
4. **Updated CHANGELOG**: v1.2.0 entry
5. **Fed back into agentic-engineering**: case study updated, gotcha log entry, memory index updated

### Infrastructure: memory migration

1. **Audited all 28 project memory directories** in `~/.claude/projects/`
2. **Migrated ~75 files** from hidden auto-memory to visible in-repo `memory/` directories
3. **Covered**: local_dev projects (14), smaller projects (6), HAN OneDrive projects (6), other drives (2)
4. **Slimmed global CLAUDE.md**: moved voice library + TTS engines + workflow to podcast-generator's CLAUDE.md

### Personal insights captured

- "I built things I couldn't have built at all without AI" — capability shift, not productivity metric
- "The cognitive load is the highest it's ever been" — five projects, five mental models, the weight of verification
- Both true simultaneously: catapulted AND loaded. This duality is the emotional core of the series.
- N=1 is starting point, not destination. Friends coming on board. Growth through community.

## Files created/modified

### agentic-engineering repo
- `podcast/dialogen/ae_00_introduction_dialogue.txt` — created + 3 revisions
- `podcast/dialogen/ae_01_context_engineering_dialogue.txt` — created + 3 revisions
- `podcast/shownotes/ae_00_introduction.md` — claim verification + references
- `podcast/shownotes/ae_01_context_engineering.md` — claim verification + references
- `.claude/agents/ae-review-*.md` — 8 persona agents + orchestrator (9 files)
- `case-studies/agent-ready-projects.md` — Phase 5 added
- `memory/gotcha-log.md` — auto-memory entry added
- `memory/MEMORY.md` — updated with podcast + ADR-001 + decisions
- `memory/project_ae_podcast_marketing.md` — created + updated
- `memory/reference_tandemize.md` — created
- `memory/session_2026-03-19_podcast_launch.md` — this file

### agent-ready-projects repo
- `docs/decisions/ADR-001-in-repo-memory-over-auto-memory.md` — created
- `README.md` — Layer 3 location, tables, global cliff section updated
- `CHANGELOG.md` — v1.2.0 entry added

### podcast-generator repo
- `docs/decisions/ADR-001-dialogue-writing-style-local-tts.md` — created (33 rules)
- `CLAUDE.md` — voice library, TTS engines, workflow added from global

### Global
- `~/.claude/CLAUDE.md` — slimmed (podcast content removed)
- `~/.claude/projects/*/memory/` — 28 projects migrated to in-repo
