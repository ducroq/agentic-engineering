# Augmented Engineering

What's new when engineers work with AI agents? Four patterns from nine real projects.

- **Type**: Proposition + case studies + website
- **Status**: Active (March 2026)
- **agent-ready-projects**: v1.1.0

## Before You Start

| When | Read |
|------|------|
| Understanding the core argument | `PROPOSITION.md` — the four patterns and what's genuinely new |
| Reviewing critical feedback | `REVIEW-SYNTHESIS.md` — six reviews + priority action plan |
| Making any factual claim | `claims/claim-registry.md` — 17 claims, confidence tiers, calibrated language |
| Working on a case study | `case-studies/README.md` — template and conventions |
| Working on research content | `research/README.md` — research questions and methodology |
| Working on the guide | `guide/README.md` — pattern library structure |
| Working on the website | `site/` — Astro static site, `npm run dev` to preview |
| Stuck or debugging | `memory/gotcha-log.md` — problem-fix archive |

## Hard Constraints

- **Pattern-first**: Lead with the transferable pattern, not with thesis/framework evidence
- **Evidence-based**: Claims backed by case studies or cited sources — no speculation as fact
- **Tool-agnostic**: Patterns work with any AI system — mention tools used but don't require them
- **Honest about limitations**: N=1 researcher, no controlled comparison, survivorship bias — say so
- **Confidence-calibrated**: Match language to evidence strength (ESTABLISHED → "shows"; EMERGING → "may")
- **No institutional references**: This is a personal project, not institutional

## The Four Patterns

1. **Learn the Material** — LLM behavioral properties (some persistent, some transient)
2. **Layer Your Verification** — Cheap V&V enables routine multi-layer verification
3. **Context Is Architecture** — Auto-loading cliff, task-triggered pointers
4. **Reproduce, Don't Assess** — Compute instead of reasoning about equations

## Architecture

```
augmented-engineering/
├── PROPOSITION.md           # Core argument — read first
├── REVIEW-SYNTHESIS.md      # Critical reviews from 6 perspectives
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
├── site/                    # Astro website
│   └── src/
│       ├── layouts/         # Base layout with graph-paper grid
│       ├── components/      # SVG illustrations + pattern page template
│       └── pages/           # Landing + 4 pattern pages
├── .claude/agents/          # Review agent prompts
│   ├── review-systems-engineer.md
│   ├── review-ml-researcher.md
│   ├── review-practitioner.md
│   ├── review-epistemologist.md
│   ├── review-educator.md
│   ├── review-devil.md
│   └── review-orchestrator.md
└── memory/
    ├── MEMORY.md
    └── gotcha-log.md
```

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
