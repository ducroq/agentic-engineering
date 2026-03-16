# Claim Registry

<!-- Verification registry for the Agentic Engineering project.
     Adapted from agent-ready-papers v1.0.0.
     Every factual claim, argument, and proposition tracked here. -->

**Project:** Agentic Engineering
**Last Updated:** 2026-03-15
**Thesis:** Agentic AI becomes powerful in engineering when we build structured feedback loops that let agents improve each other — with the engineer firmly in the loop.

---

## Coverage Summary

| Priority | Total | Verified | Needs Evidence | Coverage |
|----------|-------|----------|----------------|----------|
| P0 | 5 | 2 | 3 | 40% |
| P1 | 8 | 5 | 3 | 63% |
| P2 | 4 | 3 | 1 | 75% |
| **Total** | **17** | **10** | **7** | **59%** |

**Targets:** ≥85% overall, 100% P0, 90% P1, 70% P2

---

## Priority Guide

### P0 (Critical) — thesis fails without these

| ID | Claim | Risk if Wrong |
|----|-------|---------------|
| T-1 | Structured feedback loops improve agent output quality in engineering | Core thesis collapses — loops might add overhead without benefit |
| T-2 | Multi-agent review produces better results than single-agent | Could be that one good agent + good prompt is sufficient |
| T-3 | Human-in-the-loop oversight remains necessary (agents can't fully self-validate) | If agents can self-validate, the engineer's role claim is wrong |
| V-1 | Agentic feedback loops apply across V-model phases (not just software) | Could be limited to certain phases; V-model mapping overpromises |
| V-2 | The generate→review→validate→oversee pattern transfers from software to other engineering | Could be software-specific; other engineering domains may need different patterns |

### P1 (Important) — target 90%

| ID | Claim | Risk if Wrong |
|----|-------|---------------|
| C-1 | Domain expertise is required for effective human oversight of agents | Could be that general AI literacy suffices |
| C-2 | Validation capability (not tool proficiency) is the critical competency | Could be that tool skill matters more than judgment |
| C-3 | These competencies transfer across AI tools (tool-agnostic) | Could be that each tool requires tool-specific competencies |
| E-1 | Equation-checking agents catch errors that standard LLM review misses | Could be a fluke or limited to simple arithmetic |
| E-2 | Multi-agent requirements review achieves comparable quality to human review | Could be that agreement metrics mask systematic blind spots |
| E-3 | AI-augmented design review covers disciplines a single engineer would miss | Could be that checklists are shallow and miss real issues |
| S-1 | Software engineering's feedback loop patterns are transferring into other engineering domains | Could be aspirational rather than observed |
| S-2 | This transfer is happening now (2025-2026), not hypothetically | Could be premature — real adoption may be years away |

### P2 (Supporting) — target 70%

| ID | Claim | Risk if Wrong |
|----|-------|---------------|
| B-1 | 90% of engineering teams now use AI tools | Minor — general adoption context |
| B-2 | Current approaches treat agents as isolated tools, not feedback loops | Minor — framing claim |
| B-3 | The agentic pattern originated in software development (CI/CD, code review) | Minor — historical context |
| B-4 | Agent-ready project structure improves multi-session agent effectiveness | Minor — methodology claim |

---

## Registry

### Core Thesis

| ID | Statement | Type | Priority | Confidence | Source | Source Tier | Status |
|----|-----------|------|----------|------------|--------|-------------|--------|
| T-1 | Structured feedback loops (generate→review→validate→oversee) improve the quality and reliability of agent-generated engineering outputs | PROPOSITION | P0 | EMERGING | OWN WORK: case studies (OPAL, driven-pendulum, vmodel.eu); driven-pendulum 2026-03-16: 6-agent parallel review found 14 issues that single-pass work missed | E | [ ] |
| T-2 | Multi-agent architectures (separate generate/review/validate agents) produce better results than single-agent approaches | CLAIM | P0 | EMERGING | OWN WORK: vmodel.eu (multi-agent vs single-agent comparison); driven-pendulum (equation-checker vs standard review); driven-pendulum 2026-03-16: 6 specialized agents in parallel found 14 cross-cutting issues | E | [ ] |
| T-3 | Human-in-the-loop oversight remains necessary — agents cannot fully self-validate engineering outputs | ARGUMENT | P0 | SUPPORTED | OWN WORK: case studies show agents miss domain-specific issues; aligned with validation competency research (Digital Engineers) | E+F | [~] |

**T-3 warrant:** Engineering outputs have safety, regulatory, and physics constraints that require domain judgment to evaluate. Case studies show agents generating plausible-but-incorrect outputs that pass agent-level review but fail human inspection.

### V-Model Coverage

| ID | Statement | Type | Priority | Confidence | Source | Source Tier | Status |
|----|-----------|------|----------|------------|--------|-------------|--------|
| V-1 | Agentic feedback loops have been demonstrated across at least 5 of 6 V-model phases (requirements, architecture, design, implementation, testing) | CLAIM | P0 | EMERGING | OWN WORK: case studies cover these phases | E | [~] |
| V-2 | The generate→review→validate→oversee pattern, originating in software engineering, transfers to mechanical, electrical, and systems engineering | PROPOSITION | P0 | SPECULATIVE | OWN WORK: OPAL (electrical/optical), driven-pendulum (mechanical/physics) — limited sample | E | [ ] |

### Competency Claims

| ID | Statement | Type | Priority | Confidence | Source | Source Tier | Status |
|----|-----------|------|----------|------------|--------|-------------|--------|
| C-1 | Effective oversight of agentic engineering requires domain expertise — general AI literacy is insufficient | ARGUMENT | P1 | SUPPORTED | Digital Engineers research (proposition P2: Domain Prerequisite); OPAL case study (optical/analog domain knowledge needed to evaluate checklists); driven-pendulum 2026-03-16: human caught "pancake coil" terminology error that 6 review agents + equation-checker all missed — requires knowing what the physical component is | E | [~] |
| C-2 | Validation capability (critical assessment of AI outputs) matters more than tool proficiency for effective agentic engineering | ARGUMENT | P1 | SUPPORTED | Digital Engineers research (proposition P1: Validation Primacy); vmodel.eu (scoring quality depends on understanding requirements, not LLM operation); driven-pendulum 2026-03-16: physics V&V passed but domain expert caught naming error | E | [~] |
| C-3 | Engineering competencies for working with AI agents transfer across specific AI tools | ARGUMENT | P1 | EMERGING | Digital Engineers research (Tool Agnosticism Principle); limited direct evidence from case studies | E+F | [ ] |

### Evidence from Case Studies

| ID | Statement | Type | Priority | Confidence | Source | Source Tier | Status |
|----|-----------|------|----------|------------|--------|-------------|--------|
| E-1 | Mechanical equation verification (reproduce-don't-assess) catches numerical errors that plausibility-based LLM review misses: 5/5 errors caught in formal docs + 5/5 in informal messages (driven-pendulum) that standard review missed | CLAIM | P1 | SUPPORTED | OWN WORK: driven-pendulum equation-checker audit; agent-ready-papers driven-pendulum-retrofit audit; 2026-03-16 WhatsApp message V&V (5 errors in informal comms) | E | [x] |
| E-2 | Multi-agent requirements review (vmodel.eu) achieves ≥80% within-1 agreement with human grading on a 64-report blind validation set | CLAIM | P1 | SUPPORTED | OWN WORK: vmodel.eu held-out validation | E | [x] |
| E-3 | AI-augmented design review (OPAL) produced 14 discipline-specific checklists totaling 725 items, covering disciplines beyond the lead engineer's expertise | CLAIM | P1 | ESTABLISHED | OWN WORK: OPAL design_review_checklists/ — directly verifiable in repo | E | [x] |

### Software-to-Engineering Transfer

| ID | Statement | Type | Priority | Confidence | Source | Source Tier | Status |
|----|-----------|------|----------|------------|--------|-------------|--------|
| S-1 | The feedback loop pattern (CI/CD, code review, automated testing) that transformed software engineering is being adopted in other engineering domains via agentic AI | CLAIM | P1 | EMERGING | Industry observations (LinkedIn discourse, tool announcements); no systematic study | F | [ ] |
| S-2 | This adoption is actively happening in 2025-2026, not hypothetically | CLAIM | P1 | EMERGING | Industry observations; own practice; no survey data | F | [ ] |

### Background

| ID | Statement | Type | Priority | Confidence | Source | Source Tier | Status |
|----|-----------|------|----------|------------|--------|-------------|--------|
| B-1 | ~90% of engineering teams now use AI tools | CLAIM | P2 | SUPPORTED | Jellyfish 2025; Stack Overflow 2024; JetBrains 2024 | D | [x] |
| B-2 | Current industry practice predominantly treats AI agents as isolated tools rather than as components of structured feedback loops | CLAIM | P2 | EMERGING | Industry observation; no systematic study | F | [ ] |
| B-3 | The agentic feedback pattern has roots in software engineering practices (CI/CD pipelines, automated code review, test-driven development) | CLAIM | P2 | ESTABLISHED | Software engineering literature; widely accepted | C | [x] |
| B-4 | Structured project context (layered memory, task-triggered pointers) improves AI agent effectiveness across sessions | CLAIM | P2 | SUPPORTED | OWN WORK: agent-ready-projects methodology testing on 3+ projects | E | [x] |

---

## Source Verification Checklist

### Own Work (Case Studies)

| Source | Claims | What to Check | Status |
|--------|--------|---------------|--------|
| OPAL design review | E-3, V-1 | Checklists exist in repo; count items; verify discipline coverage | [x] |
| Driven Pendulum equation-checker | E-1, V-1 | Audit documents exist; error count verified; Gemini comparison documented | [x] |
| vmodel.eu held-out validation | E-2, V-1 | Validation scripts + results in repo; 64-report set; agreement metrics | [x] |
| agent-ready-projects methodology | B-4 | METHODOLOGY.md documents testing on real projects | [x] |
| Digital Engineers research | C-1, C-2, C-3, T-3 | Propositions P1, P2 in propositions/ folder; claim registry v0.13 | [~] |

### External Sources

| Source | Claims | What to Check | Status |
|--------|--------|---------------|--------|
| Jellyfish 2025 | B-1 | 90% team adoption figure | [x] |
| Stack Overflow 2024 + JetBrains 2024 | B-1 | 84-85% individual adoption (convergent) | [x] |

### Evidence Gaps

| Claim | What's Missing | How to Fill |
|-------|---------------|-------------|
| T-1 (feedback loops improve quality) | Controlled comparison: with-loop vs without-loop | Design experiment or retrospective analysis |
| T-2 (multi-agent > single-agent) | Systematic comparison across tasks | vmodel.eu has some data; need to formalize |
| V-2 (pattern transfers across domains) | More case studies in diverse engineering domains | Recruit partner projects or extend own practice |
| S-1, S-2 (adoption is happening now) | Systematic survey or literature review | Industry survey or systematic review of tool adoption |
| B-2 (tools not loops is current practice) | Survey of current industry practice | Could be part of S-1/S-2 investigation |

---

## Unit Type Reference

| Type | When to use | Verification |
|------|------------|--------------|
| **CLAIM** (default) | Factual statement with a source | Does the source exist and say this? |
| **ARGUMENT** | Interpretive conclusion combining evidence + reasoning | Warrant valid? Evidence sufficient? Counter-arguments addressed? |
| **PROPOSITION** | Novel recommendation or contribution | Premises verified? Reasoning valid? Boundary conditions stated? |

## Confidence Tier Reference

| Tier | Language |
|------|----------|
| **ESTABLISHED** | "demonstrates", "shows", "confirms" |
| **SUPPORTED** | "indicates", "supports", "evidence suggests" |
| **EMERGING** | "may", "preliminary evidence", "initial findings suggest" |
| **SPECULATIVE** | "warrants investigation", "remains unclear", "we hypothesize" |

## Source Tier Reference

| Tier | Type |
|------|------|
| A | Peer-reviewed primary research |
| B | Peer-reviewed review article |
| C | Textbook / established reference |
| D | Industry report / guidelines |
| E | Own unpublished work |
| F | Logical inference |

---

*Registry created: 2026-03-15*
