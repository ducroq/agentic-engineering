# Guide — Track 3: Practical Framework

A pattern library for designing agentic engineering workflows. Every pattern is extracted from a real case study (Track 1) and mapped to the engineering V-model.

## Pattern Library Structure

```
guide/
├── README.md               # This file
├── patterns/               # What works — transferable patterns
│   ├── multi-agent-review.md
│   ├── equation-verification.md
│   ├── recursive-vv.md
│   ├── context-engineering.md
│   ├── typed-verification.md
│   └── confidence-calibration.md
├── anti-patterns/          # What fails — common traps
│   ├── plausibility-trap.md
│   ├── checklist-without-vv.md
│   └── single-agent-everything.md
└── by-phase/               # V-model phase mapping
    ├── requirements.md
    ├── architecture.md
    ├── detailed-design.md
    ├── implementation.md
    ├── testing.md
    └── documentation.md
```

## Pattern Card Format

Every pattern follows this structure:

---

### Pattern Name

**Problem:** What engineering challenge does this address?

**Pattern:** The specific workflow structure, stated as:
> **When** {context/situation},
> **use** {pattern: workflow, roles, feedback loop},
> **because** {reason: why this works}.

**Example:** Concrete instance from a case study, with enough detail to replicate.

**When NOT to use:** Boundary conditions — situations where this pattern fails or is unnecessary.

**Evidence strength:** ESTABLISHED / SUPPORTED / EMERGING / SPECULATIVE (matches claim registry tiers)

**Source case study:** Link to the case study this was extracted from.

**Related claims:** Claim IDs from the registry that this pattern supports.

---

## Anti-Pattern Card Format

---

### Anti-Pattern Name

**The trap:** What practitioners do wrong and why it seems reasonable.

**Why it fails:** What goes wrong, with evidence from case studies.

**What to do instead:** Link to the corresponding pattern(s).

**Source case study:** Where this failure was observed.

---

## Planned Patterns

| Pattern | Source Case Study | Key Insight | Status |
|---------|------------------|-------------|--------|
| Multi-agent review | vmodel.eu | Separate generate/review/validate roles outperform single-agent | Planned |
| Equation verification | Driven Pendulum | Reproduce-don't-assess for numerical/mathematical work | Planned |
| Recursive V&V | OPAL | Validate the validators — apply V&V to your V&V process | Planned |
| Context engineering | agent-ready-projects | Layered memory for multi-session agent effectiveness | Planned |
| Typed verification | agent-ready-papers | CLAIM/ARGUMENT/PROPOSITION typing with confidence tiers | Planned |
| Confidence calibration | agent-ready-papers | Match language strength to evidence strength | Planned |

## Planned Anti-Patterns

| Anti-Pattern | Source | The Trap |
|-------------|--------|----------|
| Plausibility trap | Driven Pendulum, OPAL | Reviewing for "looks right" instead of reproducing/verifying |
| Checklist without V&V | OPAL | Generating comprehensive checklists without validating the checklists themselves |
| Single-agent everything | vmodel.eu | One prompt/agent for the entire task instead of specialized roles |

## V-Model Phase Mapping

Each `by-phase/` file maps relevant patterns and anti-patterns to a specific V-model phase, with links to case studies demonstrating agentic workflows at that phase.

| V-Model Phase | Primary Case Study | Patterns |
|---------------|-------------------|----------|
| Requirements | vmodel.eu | Multi-agent review |
| Architecture | OPAL | Recursive V&V |
| Detailed Design | Driven Pendulum | Equation verification |
| Implementation | OPAL, Driven Pendulum | Context engineering |
| Testing | vmodel.eu, OPAL | Multi-agent review, Recursive V&V |
| Documentation | agent-ready-papers | Typed verification, Confidence calibration |

## Design Principles

### Tool-Agnostic

Patterns describe workflow structures, not specific tools. Case studies mention which tools were used (Claude, Gemma, Phi-4, etc.) but patterns are framed so they work with any capable AI agent.

### Domain-Agnostic

Patterns must work across engineering disciplines. If a pattern only works in software, say so explicitly in "When NOT to use."

### Evidence-Grounded

Every pattern links to at least one case study and one claim registry entry. No patterns from theory alone — demonstrate first, then extract.

### Practitioner-Oriented

Written for working engineers who want to try agentic workflows. Enough theory to understand why, enough practice to know how.
