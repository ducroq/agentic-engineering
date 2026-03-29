# ADR-006: Only Durable Patterns Qualify as Core

**Date:** 2026-03-29
**Status:** Accepted

## Context

Of the four patterns, two are tied to how tools and verification work (structural) and two are tied to current LLM limitations (model-dependent):

- **Context Is Architecture** — structural. The auto-loading cliff exists because of how agent tools load context, not because of model quality. This won't change when GPT-6 ships.
- **Layer Your Verification** — structural. Cheap V&V is a consequence of compute economics. Independent verification catching what single-pass misses is a principle from safety engineering that predates AI.
- **Learn the Material** — partially model-dependent. Confidence inflation may persist (RLHF incentive), but scoring regression and plausible-but-wrong outputs are improving with each model generation. The specific "material properties" list has a shelf life.
- **Reproduce, Don't Assess** — model-dependent. The technique exploits the gap between LLM assessment (weak) and LLM computation (strong). Reasoning-augmented models are closing this gap. The principle ("verify by computing") is permanent; the specific prompting technique may be unnecessary in 18 months.

## Decision

A pattern belongs under the Augmented Engineering umbrella as a core tool or methodology if it is structural — tied to how tools, verification, or engineering practice works — rather than model-dependent. Model-dependent patterns are useful advisory content ("current known limitations") but not foundational.

**Core (structural):**
- Context Is Architecture → agent-ready-projects
- Layer Your Verification → future verification tooling

**Advisory (model-dependent, useful but expiring):**
- Learn the Material → reference content on current LLM behavioral properties
- Reproduce, Don't Assess → prompting technique for current-generation models

## Consequences

**Positive:**
- The umbrella stays relevant as models improve — it doesn't depend on LLMs being bad at specific things
- Clear criteria for what belongs: "will this still matter when the next model generation ships?"
- Focuses tool-building effort on structural problems

**Negative:**
- Two of the original four patterns are demoted from "core" to "advisory" — this may feel like the project is shrinking
- The website and podcast were structured around four equal patterns; rebalancing is needed
- "Learn the Material" contains the genuinely durable insight that LLMs are a material with properties — the specific property list expires but the framing doesn't. This nuance may get lost in the demotion.

## Alternatives Considered

- **Keep all four as core**: Rejected — investing in tooling around model-dependent patterns is building on sand
- **Drop the model-dependent patterns entirely**: Rejected — they're useful *now* and the shelf-life transparency is honest. Advisory status is the right middle ground.
