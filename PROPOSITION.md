# What's New When Engineers Work with AI Agents

**Proposition:** Systems engineering provides a necessary but insufficient foundation for working with AI agents. The established principles — V&V, decomposition, feedback loops, risk management — transfer directly. But AI agents also introduce genuinely novel challenges that existing frameworks do not address. This document focuses on what's actually new, because the familiar parts take care of themselves.

---

## The Familiar Foundation (Brief)

Nine engineering projects built with AI agents over 2025-2026 confirm what you'd expect: established engineering principles still work. V&V catches defects. Decomposition beats monoliths. Risk classification focuses effort. Feedback loops improve quality. Configuration separates what changes from what doesn't. None of this is surprising, and none of it requires elaboration for a working engineer.

The more interesting question is: **what did we encounter that existing principles didn't prepare us for?**

---

## Four Things That Are Actually New

### 1. Learn the Material: LLM Behavioral Properties

Every engineering substrate has properties you must design around. LLMs have behavioral properties that, like material properties, require engineering responses — but unlike steel fatigue or semiconductor junction behavior, these properties vary in stability. Some appear deeply tied to how LLMs work. Others are current limitations under active research.

#### Properties likely to persist

These emerge from the architecture and training of current LLMs, not from insufficient scale or immature research:

- **Confidence inflation.** LLMs default to assertive language regardless of evidence strength — "demonstrates" where "suggests" would be appropriate. This is tied to RLHF training objectives that reward confident, complete answers. In the agent-ready-papers project, six of 22 claims in one paper used language more confident than evidence warranted. The structural countermeasure — enforcing a confidence-to-language mapping externally — is a design response to a property of the substrate, not a prompting failure. Even with calibration improvements, the tendency toward overassertion is likely to persist in some form because the training signal rewards it.

- **The observation-calibration gap.** LLMs can observe accurately ("this document has a table") but struggle to translate observations into calibrated quantitative conclusions. In vmodel.eu, a model would report `has_table=true` then score structure=1. Binding rules — where deterministic checks constrain LLM outputs — are needed to prevent self-contradiction. This gap reflects a working-memory problem: simultaneously holding a rubric, content, and a calibration distribution scales poorly with rubric complexity. The gap will narrow but is unlikely to close entirely for complex multi-dimensional assessments.

#### Properties under active research (current best practice, not permanent)

These are real limitations today but are on improvement trajectories that may make current workarounds unnecessary:

- **Plausible-but-wrong outputs.** LLMs generate results that look correct — right units, right order of magnitude, coherent reasoning — but contain errors invisible to surface review. In the driven-pendulum project, both Claude and Gemini reviewed 68 equations for "physics soundness" and found zero errors. When prompted to reproduce each calculation step-by-step, Sonnet found three. Hallucination rates are declining with each model generation, and reasoning-augmented models (o1-class, extended thinking) show substantially better performance on mathematical verification. The *rate* of this failure mode is dropping; the *existence* of it — that fluent output is not verified output — may persist.

- **Regression to the mean on scoring.** In vmodel.eu, every model tested (five, 14B-27B parameters) scored high-quality documents too low and inflated low-quality ones. The architectural response — removing scoring from LLMs and using an embedding+structural features classifier instead — recovered within-1 agreement from 54.7% to 93.8%. This is current best practice for sub-30B models on complex rubrics, but calibration research is advancing. Frontier reasoning models already show measurably better calibration. This workaround may have a shelf life of 12-24 months.

**What this means for practitioners:** Design around these properties today — but hold the architectural responses loosely. The structural countermeasures (confidence mapping, binding rules, separated scoring) are the right patterns now. Revisit when models change. The principle "know what your tools are bad at and don't ask them to do it" is permanent; the specific list of what they're bad at is not.

### 2. Verification Became Cheap Enough to Layer

Independent verification and validation (IV&V) has existed since the 1970s. In safety-critical systems (avionics, nuclear, medical devices), it's mandatory. In most other engineering, it's too expensive.

AI agents change the economics. In the OPAL PCB design review, five distinct verification layers each found defects the others missed:

| Layer | Found | Would have been missed by previous layers |
|-------|-------|--------------------------------------------|
| P0 verification (77 safety-critical items) | FIX-01 (laser boot hazard), FIX-02 (LDO undersized) | — |
| V&V audit ("can we trust our verifiers?") | FIX-04 (motor driver logic pin missing) | Yes — P0 verification missed it |
| P1 spot-check (50 of 220 items) | FIX-05 (ADC timing), FIX-06 (PWM safety regression), FIX-07 (thermal) | Yes — not in P0 scope |
| Full P1 campaign | FIX-08 (reference impedance), FIX-09 (DAC init), FIX-10 (firmware safety) | Yes — different P1 subset |
| + local datasheets | ISS-103 (voltage drop), ISS-130 (10x resistance error) | Yes — required NDA-protected data |

Ten verified fixes before fabrication, zero false positives in the fix register. Stopping after the first verification pass would have left 8 of 10 fixes undiscovered — including FIX-06, where an ESP32 PWM resolution limit silently undermined a safety fix, causing a voltage cap to map to 4.1V instead of the intended 2.0V.

The principle (V&V works) is old. The practice (V&V is now cheap enough to apply routinely to everyday engineering, not just projects with dedicated V&V budgets) is new. The recursive step — auditing the auditors — cost minutes of compute time. In traditional engineering, it costs months and dedicated teams.

**Open question:** When does the nth verification layer stop finding defects? We don't have enough data to answer this. In OPAL, five layers were productive. Whether this generalizes, and what the cost-benefit curve looks like, requires more evidence than nine projects from one researcher can provide.

### 3. Context Is Architecture

AI agents have a fundamentally different relationship with project knowledge than human engineers. A human browses, scans, follows references, builds a mental model. An AI agent loads what's auto-loaded and ignores everything else.

This creates the **auto-loading cliff** — a hard boundary between information the agent sees automatically and information that's effectively invisible. A well-written document below the cliff has zero impact on agent behavior. "Linked prominently from the project file" is not a trigger — agents skim past links unless a task-specific need activates them.

The pattern that crosses the cliff is the **task-triggered pointer**:

```
Doesn't work:  | API troubleshooting | docs/api-quirks.md |
Works:          | API returns 422     | docs/api-quirks.md |
```

The difference: "API troubleshooting" is a category the agent has to decide is relevant. "API returns 422" is a situation the agent recognizes it's in.

This was discovered in the agent-ready-projects framework, tested across 100+ sessions on multiple real projects, and validated by a multi-agent audit where three independent agents reviewed three different project types and converged on the same findings about context management.

**Is this really new?** The systems engineer reviewer argued this is just interface management — ICDs, bus protocols, shared memory maps all deal with what's visible to a component. There's truth to that analogy, but it breaks down on a key point: ICDs assume a consumer that processes everything it receives. Agent context management deals with a consumer that has soft attention boundaries and actively ignores information that doesn't match its current task. The "task-triggered pointer" is closer to an interrupt than a polling interface — but even that analogy is imperfect. This may be a genuinely new architectural concern, or it may be a known concern in a new costume. We're honest that we're not sure.

### 4. Reproduce, Don't Assess

When verifying numerical or mathematical content:

- **Assessment** asks "does this look right?" — check dimensions, plausibility, theoretical consistency. This is what human reviewers do, and what LLMs default to.
- **Reproduction** asks "what answer do I get?" — substitute values, compute step-by-step, compare to the stated result.

In the driven-pendulum project, assessment (by both Claude and Gemini) found zero errors in 68 equations. Reproduction (by Sonnet, prompted to show all work) found three:

1. A table labeled "5 degrees amplitude" contained values computed at 1 degree — 5x coupling strength error
2. A dwell time formula had a spurious factor of 2 and missing theta_max term — predicted 84ms vs. actual 43ms
3. A correction rate of "3.3 ms/swing × 3600 swings/hr" should give ~12 s/hr, but the document stated 36 s/hr

All three errors produced plausible results with correct units and reasonable magnitudes. They were invisible to assessment and immediately visible to arithmetic.

**Shelf life of this pattern:** The ML researcher reviewer argued this may be obsolete within 18 months as reasoning-augmented models improve mathematical judgment. That's possible. But the underlying principle — "don't trust that something is correct because it looks correct; independently verify the result" — is permanent. It's the same principle behind independent calculation checks in structural engineering. What's specific to LLMs is that you can exploit their computational ability (strong when forced to show work) to compensate for their judgment limitation (weak on holistic "does this seem right?"). If future models close this gap, the specific prompting technique becomes unnecessary but the verification principle remains.

---

## What Would Disprove This

A proposition that can't be wrong isn't useful. Here's what would challenge these claims:

- **A successful augmented engineering approach that works better WITHOUT established engineering principles** — e.g., a team that achieves superior results by ignoring V&V, decomposition, and risk classification in favor of a genuinely novel methodology. This would challenge the "SE is necessary" claim.
- **Evidence that the "material properties" are pure artifacts of model scale** — if a 10x larger model exhibits none of the four behavioral properties listed above, they aren't substrate properties but limitations of current scale. The scoring regression and mathematical assessment limitations are the most vulnerable to this.
- **A demonstration that context architecture is fully handled by existing interface management methods** — if standard ICDs and configuration management, applied without modification, produce equivalent agent behavior to task-triggered pointers and cliff-aware design. This would challenge the "genuinely new" claim for context architecture.
- **Evidence that the patterns don't transfer beyond this researcher** — if other engineers applying these patterns in different domains find them unhelpful or misleading. N=1 is acknowledged; N=10 from different practitioners with different training would either strengthen or falsify the claims.

---

## What This Means

### For Practitioners

Your engineering training transfers. V&V, decomposition, risk management, feedback loops — use them. They work with AI agents for the same reasons they work everywhere else.

Then learn four new things:
1. LLMs produce confident, plausible, wrong output. **Reproduce results rather than reviewing them** where correctness matters.
2. LLMs can observe but struggle to score. **Separate calibrated scoring from qualitative analysis** — use ML classifiers or deterministic rules for numeric judgments, LLMs for qualitative review.
3. Agent context is architecture. **Design what's above and below the auto-loading cliff.** Use task-triggered pointers, not descriptive labels.
4. Verification is now cheap. **Layer it.** Run multiple verification passes. Audit the auditors. The marginal cost is minutes.

Items 1 and 2 are current best practice that may become unnecessary as models improve. Items 3 and 4 are likely durable. Hold all four loosely and update as the substrate changes.

### For Educators

The core recommendation — teach engineering principles, not AI-specific tools — is a hypothesis grounded in one practitioner's experience, not a validated curriculum design. Translating it into learning outcomes, assessment methods, and sequencing is a separate task that requires collaboration with engineering educators, not a three-sentence prescription.

That said, some elements are immediately teachable:
- **"Reproduce, don't assess"** works even for novice students — you don't need domain expertise to substitute values and check arithmetic
- **The four behavioral properties** can be taught as a "things to watch for" checklist, similar to how material failure modes are taught
- **The auto-loading cliff** is a 20-minute demonstration with immediate practical impact for students using AI coding assistants

The harder problem: validation requires domain expertise, but students are still building domain expertise. How to scaffold AI verification skills alongside domain knowledge development is an open question this document cannot answer.

### For Researchers

The interesting questions, given this evidence:

- **Which behavioral properties are stable across model generations?** Track the four properties identified here as models improve. If confidence inflation persists but scoring calibration is solved, the pattern landscape changes.
- **Does layered V&V generalize?** Five layers were productive in one PCB design review. What's the cost-benefit curve across different engineering domains and project types?
- **Is context architecture a new discipline or a known one?** Test whether standard interface management methods, applied without modification, produce equivalent results to cliff-aware context design.
- **Do these patterns transfer beyond N=1?** The strongest next step: have engineers with different backgrounds (not systems engineering) apply these patterns and report what works, what doesn't, and what they'd frame differently.

---

## The Evidence Base

Nine projects, one researcher, 2025-2026. Practice-based evidence (documenting one practitioner's work), not experimental.

| Project | Domain | Key evidence |
|---------|--------|-------------|
| OPAL | Embedded/optical | 10 defects found across 5 verification layers; 8 would have been missed by single-pass review |
| vmodel.eu | Education/software | 93.8% within-1 agreement on 64 blind reports; 5 documented single-agent failure modes |
| Driven Pendulum | Physics/hardware | 3/3 equation errors caught by reproduction, 0/3 by assessment |
| agent-ready-projects | Methodology | Auto-loading cliff discovered across 100+ sessions; validated by 3-agent audit |
| agent-ready-papers | Academic writing | 6/22 claims over-confident in one paper; 100% claim coverage achievable at ~5-10 min/claim |
| llm-distillery | ML/content filtering | 6 production filters, config-driven; oracle consistency > data volume (ADR-010) |
| RenkumSpot | Community platform | Schema-driven CMS with defensive loading patterns |
| ese_bot | Document retrieval | EU-sovereign RAG without frameworks; chunking strategy > model quality |
| ovr.news | News curation | Multi-provider tiered fallback; predictive budget management |

### Limitations (These Actually Constrain the Claims)

These are not hedges. They define the boundary of what this document can claim:

- **N=1 researcher.** All nine projects share one practitioner and one set of methodological commitments. The proposition cannot distinguish "these patterns work for augmented engineering" from "this engineer applies these patterns to everything." External validation from engineers with different training is required before generalizing.

- **No controlled comparison.** There is no baseline. We don't know that alternative approaches (no SE framing, different framing, pure intuition) would have performed worse. The patterns produced good results — but so might others.

- **Survivorship bias.** Projects where agentic approaches weren't tried, or were tried and abandoned, are absent. The evidence base structurally cannot show when the approach fails.

- **Temporal snapshot.** Two of the four "behavioral properties" (scoring calibration, plausible-but-wrong outputs) are under active research with visible improvement trajectories. Patterns built on these may have a shelf life of 12-24 months. The document distinguishes persistent from transient where possible, but the distinction itself is a hypothesis.

- **Self-referential.** This document was written with AI assistance, argues that AI assistance works when guided by engineering principles, and cites the author's own projects. The argument may be sound despite the circularity — but the circularity means the evidence is weaker than it appears. A reviewer finding SE patterns in their own SE-designed projects is confirming their design choices, not discovering a law of nature.

- **Alternative lenses exist.** An ML researcher would frame the scoring regression as a calibration problem (Platt scaling, temperature tuning), not a material property. A cognitive scientist would frame the auto-loading cliff as an attention and working memory phenomenon. This document uses a systems engineering lens because that's the author's training — it does not claim this is the only useful lens, or even the best one.

Given these constraints, this document should be read as **a practitioner's hypothesis, not a validated framework.** The patterns are worth trying. The framing is worth debating. Neither is established.

---

## One Sentence

> Systems engineering is a necessary but insufficient foundation for working with AI agents — the established principles transfer directly, but agents introduce genuinely novel challenges in context architecture, verification economics, and substrate-specific behavioral properties that existing frameworks don't address.
