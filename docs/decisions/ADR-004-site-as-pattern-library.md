# ADR-004: Reframe Website as Pattern Library

**Date:** 2026-03-28
**Status:** Accepted

## Context

The current site (ducroq.github.io/augmented-engineering) is structured as a research portfolio: thesis statement, four patterns with evidence from nine projects, project cards, and an about section. The "Try This Monday" boxes are the most actionable content but are buried inside evidence-heavy pages.

The nine project cards on the homepage serve the author's credibility narrative but not the reader. A visitor working on a Django app has no reason to care about OPAL's PCB review. The site asks people to trust the research before they can apply anything.

Meanwhile, agent-ready-projects (the framework) is already the actionable artifact — concrete, adopted, versioned. The CHEATSHEET.md with situation-triggered decision rules is closer to what practitioners actually want.

## Decision

Reframe the site as a **pattern library**: each page leads with the problem and the fix, not the evidence. Evidence becomes supporting material, not the headline. The nine projects become attribution ("observed across 9 projects"), not a homepage section.

Structure: problem → pattern → concrete example → "try this" → evidence (collapsed or linked).

## Consequences

**Positive:**
- Visitors get value on first page load without reading research context
- Patterns become independently shareable (link someone to "reproduce don't assess" directly)
- agent-ready-projects becomes the natural next step, not a separate thing to discover
- Aligns with the project's own hard constraint: "practitioner-accessible — a working engineer should try the pattern Monday morning"

**Negative:**
- The research depth that makes the proposition rigorous becomes less visible
- Case studies and claim registry serve the proposition, not the pattern library — their role shifts to background material
- Need to rethink the PROPOSITION.md ↔ site relationship (proposition is the research artifact; site is the practitioner artifact)

## Alternatives Considered

- **Keep current structure, improve copy**: Rejected — the problem is structural (leads with journey, not reader's problem), not editorial
- **Two separate sites** (research + practice): Rejected — splits a small audience further and doubles maintenance
- **Just link to agent-ready-projects**: Rejected — the four patterns are broader than context architecture; agent-ready-projects is one pattern's implementation
