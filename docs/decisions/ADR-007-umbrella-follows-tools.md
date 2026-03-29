# ADR-007: Don't Build the Umbrella Ahead of the Tools

**Date:** 2026-03-29
**Status:** Accepted

## Context

With "Augmented Engineering" reframed as a tool umbrella (ADR-005), there's a natural temptation to invest in the umbrella itself: consistent branding across repos, a GitHub org, a polished landing page, an "about augmented engineering" narrative, visual identity guidelines.

The current state: one flagship tool (agent-ready-projects), one credible second candidate (layered verification tooling, not yet built), a website, a podcast, and a lot of research scaffolding.

## Decision

The umbrella stays minimal until a second flagship tool exists. Specifically:

- **Now:** The umbrella is a name, a repo, a landing page that points to agent-ready-projects, and advisory content on the model-dependent patterns. No GitHub org, no cross-repo branding, no visual identity system.
- **When there's a second tool:** Revisit the landing page structure, consider a GitHub org, update the site to showcase both tools.
- **Signal to watch:** If time spent on umbrella infrastructure exceeds time spent building tools, stop and recalibrate.

## Consequences

**Positive:**
- All energy goes into making agent-ready-projects better and building the next tool
- Avoids the "impressive brand, no product" trap
- Cheap to maintain — the umbrella is just a pointer

**Negative:**
- The website, podcast, and repo may look under-invested compared to the ambition of the name
- Visitors may not understand the relationship between agent-ready-projects and augmented-engineering until the umbrella has more content

## Alternatives Considered

- **Build the umbrella now while energy is high**: Rejected — umbrella without tools is a branding exercise. The energy is better spent on the layered verification tooling or improving agent-ready-projects.
- **Merge everything into agent-ready-projects**: Rejected — the umbrella name is already established and the podcast uses it. Having a thin umbrella costs almost nothing.
