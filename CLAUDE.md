# Agentic Engineering

Documenting, demonstrating, and researching the use of multi-agent AI systems with structured feedback loops across the engineering V-model.

- **Type**: Research + case studies + practical guide (three tracks)
- **Status**: Initial setup (March 2026)
- **Institution**: HAN University of Applied Sciences
- **agent-ready-projects**: v1.0.0

## Before You Start

| When | Read |
|------|------|
| Making any factual claim | `claims/claim-registry.md` — check if claim exists, verify confidence tier, use calibrated language |
| Adding or updating a case study | `case-studies/README.md` — case study template and conventions |
| Writing research content | `research/README.md` — research questions and methodology |
| Working on the guide/framework | `guide/README.md` — pattern library structure |
| Stuck or debugging something weird | `memory/gotcha-log.md` — problem-fix archive |
| Understanding a related repo | See "Related Repositories" below — read that repo's CLAUDE.md first |

## Hard Constraints

- **Evidence-based**: Every claim must be backed by a case study or cited source — no speculation presented as fact
- **V-model grounded**: Map all patterns and examples to engineering lifecycle phases
- **Engineer-in-the-loop**: Agents augment, never replace, engineering judgment — never frame agents as autonomous replacements
- **Tool-agnostic**: Competencies transcend specific AI tools — don't write patterns that only work with one tool
- **Domain-agnostic**: Patterns must work across mechanical, electrical, software, and systems engineering — don't assume software-only
- **No company names**: Use generic references ("regional high-tech industry") — industry partners are not confirmed
- **Show, don't tell**: Case studies before theory — demonstrate, then extract the pattern
- **Confidence-calibrated language**: Match language to evidence strength — see claim registry for tiers (ESTABLISHED → "shows"; EMERGING → "may"; SPECULATIVE → "warrants investigation")

## Architecture

Three tracks, one thesis:

```
agentic-engineering/
├── CLAUDE.md                # This file (Layer 1: identity + orientation)
├── README.md                # Public-facing project overview
├── case-studies/            # Track 1: Build — working demonstrations
│   └── [per-project case study documents]
├── research/                # Track 2: Research — empirical investigation
│   └── [research questions, methodology, findings]
├── guide/                   # Track 3: Guide — practical framework
│   └── [pattern library, anti-patterns, V-model mapping]
└── memory/                  # Layers 3-4: session memory + gotcha log
    ├── MEMORY.md            # Memory index (auto-loaded)
    └── gotcha-log.md        # Problem-fix archive
```

## Related Repositories (Case Studies)

These external repos provide the empirical evidence. Each is an independent project; this repo synthesizes and analyzes them.

| Repo | Domain | What it demonstrates |
|------|--------|---------------------|
| `C:\local_dev\agent-ready-projects` | Meta/methodology | How to structure projects for effective AI agent collaboration |
| `C:\local_dev\agent-ready-papers` | Academic writing | Verification infrastructure for AI-augmented papers |
| `C:\local_dev\driven-pendulum` | Hardware/physics | Agentic V&V for electromagnetic pendulum sync (68 equations, claim registry) |
| `C:\local_dev\vmodel.eu` | Education/software | Multi-agent pipeline reviewing requirements docs (Gemma + Phi-4) |
| OPAL (BR head) | Embedded/optical | AI-augmented PCB design review (14 checklists, 725 items) |

## The Core Thesis

Agentic AI works in engineering through structured feedback loops:
```
AI generates → AI reviews → AI validates → Human oversees
```

The engineer's role: directing, validating, taking responsibility — requiring domain expertise × validation capability × context awareness.

## Key Paths

| Path | What it is |
|------|-----------|
| `README.md` | Public-facing overview with V-model mapping |
| `case-studies/` | Track 1: case study documents |
| `research/` | Track 2: research materials |
| `guide/` | Track 3: practical framework |
| `memory/MEMORY.md` | Session memory index |
| `memory/gotcha-log.md` | Problem-fix archive |
| `claims/claim-registry.md` | Verification registry — all claims with evidence status |

## Writing Style

- Accessible but rigorous — practitioners and researchers both in audience
- Show, don't tell — case studies before theory
- Honest about limitations — where agents fail matters as much as where they succeed
- No emojis unless explicitly requested
