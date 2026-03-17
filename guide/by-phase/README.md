# V-Model Phase Mapping

How the four patterns apply across engineering phases. Each phase entry links to the patterns and case studies that provide evidence for agentic workflows at that stage.

## Overview

| Phase | Primary Pattern | Feedback Loop | Source Evidence |
|-------|----------------|---------------|-----------------|
| Requirements | Layer Your Verification | Agent drafts requirements → agent checks consistency → agent validates testability → engineer decides | vmodel.eu: 93.8% within-1 agreement on 64 blind reports |
| Architecture | Layer Your Verification | Agent reviews interfaces → agent audits review → agent spot-checks high-risk items → engineer decides | OPAL: recursive V&V found motor driver pin missing |
| Detailed Design | Reproduce, Don't Assess | Agent derives equations independently → agent compares results → discrepancies flagged → engineer resolves | Driven Pendulum: reproduction found 3 errors that assessment missed |
| Implementation | Context Is Architecture | Auto-loaded context drives agent behavior → task-triggered pointers cross the cliff → engineer structures context | agent-ready-projects: auto-loading cliff discovery |
| Testing | Layer Your Verification | Agent generates test cases → agent reviews coverage → agent validates against requirements → engineer prioritizes | vmodel.eu + OPAL: multi-layer verification across disciplines |
| Documentation | Layer Your Verification | Agent traces claims to evidence → agent calibrates confidence language → agent checks compliance → engineer approves | agent-ready-papers: 100% claim coverage, typed verification |

## The Common Structure

Every phase follows the same feedback loop:

**Agent generates → Agent reviews → Agent validates → Engineer decides**

What varies by phase:
- **What** is being generated (requirements, designs, equations, tests, docs)
- **Which agents** are specialized for the task (reviewer, reproducer, auditor)
- **What verification means** (consistency at requirements level, reproduction at design level, coverage at testing level)

## Phase Files (Planned)

Each file below will contain the full pattern card(s), anti-pattern warnings, and worked examples for that V-model phase.

- `requirements.md` — consistency, testability, conflict detection
- `architecture.md` — interface verification, performance estimation
- `detailed-design.md` — equation reproduction, safety analysis, manufacturability
- `implementation.md` — context architecture, auto-loading, session continuity
- `testing.md` — coverage, test generation, log mining
- `documentation.md` — claim tracing, confidence calibration, compliance
