# Agentic Engineering

**Agentic AI becomes powerful in engineering when we build structured feedback loops that let agents improve each other — with the engineer firmly in the loop.**

This repository documents, demonstrates, and researches the emerging practice of agentic engineering: using multi-agent AI systems with structured feedback loops across the full engineering V-model.

## Three Tracks

### Track 1: Build
Working demonstrations of agentic engineering across domains — from embedded hardware to requirements verification.

**Case studies:**
- **OPAL** — AI-augmented design review of a confocal backscatter detector (PCB, firmware, analog, optical physics). 14 checklists, 725 items, multi-discipline V&V.
- **Driven Pendulum** — Agentic workflow for electromagnetic clock synchronization: claim registries, equation-checking agents, requirements-to-prototype V&V.
- **vmodel.eu** — Multi-agent pipeline (Gemma 3 + Phi-4) reviewing student requirements documents against IEEE 29148 and V-model standards. Production deployment.
- **agent-ready-projects** — Framework for structuring any project for effective AI agent collaboration (layered memory, auto-loading cliff, task-triggered pointers).
- **agent-ready-papers** — Verification infrastructure for AI-augmented academic writing (typed claims, anti-hallucination, confidence calibration).

### Track 2: Research
Empirical investigation of what makes agentic engineering effective.

Key questions:
- What feedback loop structures produce reliable engineering outputs?
- Where does human-in-the-loop oversight actually matter vs. where can agents self-validate?
- What domain expertise is required to oversee agent-generated engineering work?
- How do validation competencies transfer across tools and domains?

### Track 3: Guide
A practical framework for designing agentic engineering workflows.

- Pattern library: which V-model phases, which loop architectures
- Anti-patterns: where agents fail without proper oversight
- The feedback loop thesis: generate → review → validate → human oversees

## The V-Model Mapping

Agentic feedback loops are emerging across the entire product development lifecycle:

| V-Model Phase | Agent Capabilities | Case Study |
|---------------|-------------------|------------|
| **Requirements** | Consistency checks, testability analysis, conflict detection, standards compliance | vmodel.eu |
| **Architecture** | Interface verification, design rule checking, performance estimation | OPAL (design review checklists) |
| **Detailed Design** | Equation verification, parameter validation, claim tracking | Driven Pendulum |
| **Implementation** | Code generation with verification, firmware development | OPAL (ESP32 firmware) |
| **Testing** | Coverage analysis, test case generation, V&V automation | OPAL, vmodel.eu |
| **Documentation** | Claim registries, anti-hallucination checks, confidence calibration | agent-ready-papers |

## The Core Thesis

The pattern that makes agentic AI work in engineering is not "AI does a task" but structured feedback loops:

```
AI generates → AI reviews → AI validates → Human oversees
```

This is the same dynamic that transformed software engineering — constant learning from failures, debugging, reviewing constraints — now applied to mechanical, electrical, and systems engineering.

The engineer's role shifts from doing to directing, validating, and taking responsibility. This requires **domain expertise** (to know what's right), **validation capability** (to catch what's wrong), and **context awareness** (to judge what matters).

## Origin

This project grows from two years of research into AI-augmented engineering at HAN University of Applied Sciences, including:
- Empirical research on how professional engineers use AI tools
- Development of a conceptual framework for the "AI-augmented engineer"
- Hands-on experience building agentic systems for real engineering problems

## Repository Structure

```
agentic-engineering/
├── README.md               # This file
├── case-studies/            # Track 1: Documented case studies
├── research/                # Track 2: Research materials
├── guide/                   # Track 3: Practical framework
└── CLAUDE.md                # Agent orientation
```

## License

TBD

## Contact

HAN University of Applied Sciences — Academy for Engineering Applications
