# Research — Track 2: Research

Empirical investigation of what makes agentic engineering effective, grounded in case study evidence from Track 1.

## Primary Research Question

> Under what conditions do structured agentic feedback loops improve the quality and reliability of engineering outputs?

## Sub-Questions

| RQ | Question | Key Claims | Evidence Needed |
|----|----------|------------|-----------------|
| RQ1 | Do feedback loops produce better outputs than single-pass generation? | T-1 | Retrospective comparison: same task with/without loop |
| RQ2 | Does multi-agent review outperform single-agent, and when? | T-2 | Formalized comparison (vmodel.eu ADR-016 is starting point) |
| RQ3 | Where in the V-model do feedback loops add the most value? | V-1, V-2 | Cross-case analysis by engineering lifecycle phase |
| RQ4 | What domain expertise does effective human oversight require? | C-1, C-2 | Code "human intervention moments" across case studies |
| RQ5 | Do agentic engineering patterns transfer across engineering domains? | V-2, S-1 | Cross-domain comparison (weakest — needs external validation) |

## Methodology

### Approach: Practice-Based Research

This project documents the researcher's own engineering practice with agentic AI systems. This is a legitimate research methodology (Schon, 1983; Kemmis, 2009) but requires transparency about its limitations.

**What this is:**
- Systematic documentation of five real engineering projects using agentic AI
- Cross-case analysis identifying common patterns and divergences
- Evidence mapped to a typed claim registry with confidence tiers

**What this is not:**
- Controlled experiment with randomization
- Multi-researcher study with inter-rater reliability
- Representative survey of industry practice

### Data Sources

All evidence comes from five case study repositories, each containing verifiable artifacts:

| Source | Domain | Key Artifacts |
|--------|--------|---------------|
| OPAL | Embedded/optical | 14 checklists, 725 items, design review records |
| vmodel.eu | Education/software | 64-report blind validation set, 18 ADRs, scoring pipeline code |
| Driven Pendulum | Hardware/physics | Equation audit documents, claim registry, error logs |
| agent-ready-projects | Meta/methodology | METHODOLOGY.md, tested on 3+ real projects |
| agent-ready-papers | Academic writing | Paper 1 at 100% claim coverage, retrofit audit results |

### Analysis Methods

- **Cross-case analysis:** Systematic comparison of patterns across five case studies (see `cross-case-analysis.md` when completed)
- **Claim registry verification:** Every claim tracked with typed evidence and confidence tiers
- **Pattern extraction:** Transferable patterns documented in guide/ (Track 3)

### Quality Assurance

- **Typed verification:** All claims categorized as CLAIM, ARGUMENT, or PROPOSITION with appropriate evidence requirements
- **Confidence calibration:** Language matched to evidence strength (ESTABLISHED → SPECULATIVE)
- **Falsifiability:** Each claim includes "risk if wrong" — what would disprove it
- **Transparency:** Limitations stated explicitly in every case study and in `evidence-gaps.md`

## Limitations (Stated Up Front)

1. **N=1 researcher.** All case studies are from one practitioner's work. Patterns may reflect individual style rather than generalizable principles.
2. **No randomized comparison.** "With loop vs. without loop" comparisons are retrospective, not controlled experiments.
3. **Five domains, one perspective.** The domains are diverse (embedded hardware, physics, software, methodology, writing) but viewed through one engineer's lens.
4. **Practice-based, not experimental.** Findings indicate what worked in these specific contexts. Generalization requires external validation.
5. **Self-selection bias.** Projects were chosen because agentic approaches seemed promising — we don't document projects where agents weren't useful.

These limitations are real but do not invalidate the research. They constrain the strength of claims (reflected in confidence tiers) and define what additional evidence would be needed to strengthen them.

## Connection to Digital Engineers Research

This project operationalizes concepts from the Digital Engineers research initiative (HAN University of Applied Sciences, 2024-2026):

| Digital Engineers Concept | How It Appears Here |
|--------------------------|-------------------|
| D x V x C framework | "The Human Role" section in every case study |
| Tool Agnosticism Principle | Patterns described tool-agnostically; tools mentioned but not required |
| Validation Primacy (P1) | Core thesis: validation through feedback loops |
| AI Stance Typology | "Augmented" stance = directing multi-agent systems |
| Six Propositions | Reframed as RQ1-RQ5 for agentic systems |

**Bridge statement:** Digital Engineers asked: what makes an engineer effective with AI? It proposed domain expertise x validation capability x context awareness. This project provides the evidence: five case studies showing how structured agentic feedback loops operationalize those competencies across the engineering lifecycle.

## Research Outputs (Planned)

| Document | Purpose | Status |
|----------|---------|--------|
| `cross-case-analysis.md` | Systematic comparison across five case studies | Planned |
| `methodology.md` | Full methodology statement (practice-based / design science) | Planned |
| `evidence-gaps.md` | What would strengthen each P0 claim | Planned |

## File Conventions

- All research documents are written in English
- Claims reference the [claim registry](../claims/claim-registry.md) using `[T-1]` format
- Confidence language follows the registry's tier system
- Limitations are stated, not hidden
