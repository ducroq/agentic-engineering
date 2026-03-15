# Case Studies — Track 1: Build

Each case study tells the story of a real engineering project where agentic AI workflows were used. The goal is to extract **transferable patterns** — what worked, what didn't, and what a practitioner in a different domain can take away.

## Case Study Index

| Case Study | Domain | Pattern |
|------------|--------|---------|
| [opal.md](opal.md) | Embedded/optical | Recursive V&V — validate the validators |
| [vmodel-eu.md](vmodel-eu.md) | Education/software | Role specialization — separate what's deterministic from what needs judgment |
| [driven-pendulum.md](driven-pendulum.md) | Hardware/physics | Reproduce, don't assess — compute instead of reason about equations |
| [agent-ready-projects.md](agent-ready-projects.md) | Meta/methodology | Context engineering — layered memory with auto-loading cliff |
| [agent-ready-papers.md](agent-ready-papers.md) | Academic writing | Typed verification — different claim types need different checking |

## Template

Target: ~2,000 words. Lead with the story, extract the pattern, be honest about limitations.

---

### The Pattern (title-level)

One-sentence summary of the transferable pattern.

### 1. What Was Built

What the project is, what engineering problem it solves, and why agentic AI was involved. Enough context for a reader from a different discipline to follow. (~200 words)

### 2. How the Agents Were Used

The actual workflow: which agents, what roles, what feedback loops. Include a simple flow or diagram. Focus on the structure of the workflow, not the specific tools. (~400 words)

### 3. What Worked

Concrete results with numbers where available. What did the workflow produce that wouldn't have happened otherwise? (~400 words)

### 4. What Didn't Work

Where agents got things wrong. Specific failure modes, how they were caught, what they reveal. Be concrete — a single good failure example is worth more than a paragraph of hedging. (~300 words)

### 5. The Pattern

The transferable insight, stated concisely:

> **When** {situation},
> **use** {pattern},
> **because** {reason}.

When does this pattern NOT apply? (~300 words)

### 6. Limitations

Single-researcher, single-project, no controlled comparison. What can't this case study tell us? (~150 words)

---

## Conventions

- **Pattern-first:** The pattern is what matters. The engineering narrative serves the pattern, not the other way around.
- **Practitioner-accessible:** A working engineer should be able to read this and try the pattern tomorrow.
- **Honest about failures:** Where agents failed matters as much as where they succeeded.
- **Tool-agnostic:** Describe the pattern so it works with any capable AI system. Mention specific tools used, but don't write patterns that require them.
- **Loosely coupled to the claim registry:** Case studies inform the registry, but they're not structured around it. If a case study provides evidence for a claim, note it naturally — don't force every observation through a claim ID.
- **Calibrated language:** Don't oversell. These are N=1 case studies from one researcher's practice — they demonstrate patterns, they don't prove universality.
