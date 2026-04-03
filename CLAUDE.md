# Augmented Engineering

Durable tools and patterns for engineers working with AI agents.

- **Type**: Tool umbrella — tools, durable patterns, advisory content
- **Status**: Active (March 2026)
- **Flagship tool**: agent-ready-projects (v1.4.0)
- **agent-ready-projects**: v1.4.0

## Before You Start

| When | Read |
|------|------|
| Understanding the core argument | `PROPOSITION.md` — the four patterns and what's genuinely new |
| Reviewing critical feedback | `REVIEW-SYNTHESIS.md` — six reviews + priority action plan |
| Making any factual claim | `claims/claim-registry.md` — 17 claims, confidence tiers, calibrated language |
| Working on a case study | `case-studies/README.md` — template and conventions |
| Working on research content | `research/README.md` — research questions and methodology |
| Working on the guide | `guide/README.md` — pattern library structure |
| Working on the website | `site/` + `docs/VIBE.md` — Astro static site, visual identity guide, `npm run dev` to preview |
| Stuck or debugging | `memory/gotcha-log.md` — problem-fix archive |
| Making an architectural decision | `docs/decisions/README.md` — ADR index and template |
| Working on the podcast | `podcast/` + `memory/project_aug_podcast_marketing.md` — scripts, production, strategy |
| Ending a session | Run `/curate` — reviews gotcha log, promotes patterns, updates memory index |

## Hard Constraints

- **Pattern-first**: Lead with the transferable pattern, not with thesis/framework evidence
- **Evidence-based**: Claims backed by case studies or cited sources — no speculation as fact
- **Tool-agnostic**: Patterns work with any AI system — mention tools used but don't require them
- **Honest about limitations**: N=1 researcher, no controlled comparison, survivorship bias — say so
- **Confidence-calibrated**: Match language to evidence strength (ESTABLISHED → "shows"; EMERGING → "may")
- **No institutional references**: This is a personal project, not institutional
- **Negative results are knowledge**: Document what didn't work, with quantified results and why — prevents agents from retrying dead ends
- **Ground truth**: When multiple artifacts describe the same thing, one is canonical — others defer to it
- **Never create config-format docs**: No wrangler.toml, docker-compose.yml, or .npmrc as documentation — build tools auto-discover and execute them

## Decision Framework

| Verdict | Criteria |
|---------|----------|
| **PASS** | Pattern-first, evidence-backed, confidence-calibrated, no institutional refs |
| **REVIEW** | New claim without registry entry, case study touching multiple patterns, website copy |
| **FAIL** | Speculation presented as fact, missing evidence for ESTABLISHED claim, institutional language |

## Core Patterns (durable, structural)

1. **Context Is Architecture** — Auto-loading cliff, task-triggered pointers → implemented in agent-ready-projects
2. **Layer Your Verification** — Cheap V&V enables routine multi-layer verification → future tooling (issue #4)

## Advisory Patterns (useful now, model-dependent, 12-24 month shelf life)

3. **Learn the Material** — LLM behavioral properties (some persistent, some transient)
4. **Reproduce, Don't Assess** — Compute instead of reasoning about equations

## Architecture

```
augmented-engineering/
├── PROPOSITION.md           # Core argument — read first (ground truth for the four patterns)
├── REVIEW-SYNTHESIS.md      # Critical reviews from 6 perspectives
├── CHEATSHEET.md            # Practitioner-friendly decision rules
├── case-studies/            # Five case studies (pattern-first)
│   ├── README.md            # Template + conventions
│   ├── opal.md              # Recursive V&V
│   ├── vmodel-eu.md         # Role specialization
│   ├── driven-pendulum.md   # Reproduce, don't assess
│   ├── agent-ready-projects.md  # Auto-loading cliff
│   └── agent-ready-papers.md    # Typed verification
├── research/                # Research questions + methodology
├── guide/                   # Pattern library
│   ├── patterns/            # Scaffolded, not yet populated
│   ├── anti-patterns/       # Scaffolded, not yet populated
│   └── by-phase/            # V-model phase mapping (populated)
├── claims/
│   └── claim-registry.md    # 17 claims, 59% coverage
├── podcast/                 # Augmented Engineering podcast
│   ├── dialogen/            # Episode scripts
│   ├── shownotes/           # Show notes with claim verification
│   ├── productie/           # Production pipeline
│   └── onderzoek/           # Research material
├── presentations/           # Slide decks and talk materials
├── docs/
│   ├── decisions/           # ADRs — 7 decisions (index in README.md)
│   └── VIBE.md              # Visual identity direction
├── site/                    # Astro website (dark mode, Inter, semantic color)
│   └── src/
│       ├── layouts/         # Base layout
│       ├── components/      # Pattern page template
│       └── pages/           # Landing, 4 patterns, tool page with Mermaid
├── .claude/
│   ├── agents/              # Review agents (7 core + 8 podcast personas)
│   └── skills/curate/       # End-of-session curation skill
└── memory/                  # In-repo memory (not auto-memory, per ADR-001)
    ├── MEMORY.md            # Index — loaded every session
    └── gotcha-log.md        # Problem → Root Cause → Fix archive
```

## How to Work Here

```bash
# Website
cd site && npm install && npm run dev    # Dev server at localhost:4321

# Review the proposition (6-agent parallel review)
# Use review-orchestrator agent — it launches all 6 personas

# Review a podcast script (8-persona battery)
# Use ae-review-orchestrator agent

# Check claim coverage
# Read claims/claim-registry.md — look for P0 claims below 100%
```

## Ground Truth Designations

| Topic | Canonical artifact | Others defer to it |
|-------|-------------------|-------------------|
| The four patterns | `PROPOSITION.md` | Case studies, guide, website, podcast |
| Claim confidence levels | `claims/claim-registry.md` | Prose in case studies and proposition |
| Case study template | `case-studies/README.md` | Individual case studies |
| Podcast strategy | `memory/project_aug_podcast_marketing.md` | Session notes |
| Visual identity | `docs/VIBE.md` | Site CSS, component styles |
| Strategic direction | `docs/decisions/ADR-005,006,007` | CLAUDE.md framing, site structure |

## Nine Source Projects

| Repo | Domain | Pattern |
|------|--------|---------|
| OPAL | Embedded/optical | Recursive V&V, layered verification |
| vmodel.eu | Education/software | Role specialization, separated scoring |
| Driven Pendulum | Physics/hardware | Reproduce-don't-assess |
| agent-ready-projects | Methodology | Auto-loading cliff, context architecture |
| agent-ready-papers | Academic writing | Typed verification, confidence calibration |
| llm-distillery | ML/content filtering | Config-driven generics, oracle discipline |
| RenkumSpot | Community platform | Schema as source of truth |
| ese_bot | Document retrieval | Sovereignty as architecture constraint |
| ovr.news | News curation | Multi-provider fallbacks, quality gates |

## Cross-Repo Evidence

This repo is the synthesis layer for nine source projects. When working in a source project and you discover evidence relevant to the four patterns (verification findings, context architecture lessons, reproduce-don't-assess examples, LLM behavioral properties), file an issue at `ducroq/augmented-engineering` with the pattern name, quantified results, and which claims it supports.

## Writing Style

- Pattern-first: the pattern is what matters, engineering narrative serves it
- Practitioner-accessible: a working engineer should try the pattern Monday morning
- Honest about failures: where agents failed matters as much as where they succeeded
- Loosely coupled to claim registry: note evidence naturally, don't force claim IDs into every paragraph
- No emojis unless explicitly requested
