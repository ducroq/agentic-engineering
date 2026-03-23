# Review Synthesis: "What's New When Engineers Work with AI Agents"

Six review agents with distinct perspectives reviewed `PROPOSITION.md`. This document compiles convergent criticism, divergent views, and a priority action plan.

---

## Convergent Criticism (Multiple Reviewers Agree)

| Issue | Flagged By | Severity | Fixable? |
|-------|-----------|----------|----------|
| **The thesis is trivially true / unfalsifiable** — "SE applies" has no discriminating power; everything is SE if you squint | Devil, Epistemologist, Practitioner | HIGH | Yes — invert the framing |
| **Material properties analogy is overloaded** — LLM behaviors are stochastic, version-dependent, context-sensitive; not like steel fatigue | ML Researcher, Epistemologist, Devil, Systems Engineer | HIGH | Yes — split into persistent vs. transient |
| **N=1 is more serious than acknowledged** — can't distinguish "SE works with AI" from "this SE-trained engineer applies SE to everything" | All six reviewers | HIGH | Partially — reframe as hypothesis, seek external validation |
| **"What's the Same" section is filler** — practitioners already know this; academics find it superficial | Practitioner, Systems Engineer, Devil | MEDIUM | Yes — compress to one paragraph |
| **The "For Educators" section is too thin** — three sentences, no learning outcomes, no assessment, no sequencing, no prerequisites | Educator | MEDIUM | Yes — expand or explicitly defer |
| **Temporal stability problem** — some "material properties" are active research areas being solved (scoring calibration, hallucination rates) | ML Researcher, Devil | HIGH | Yes — split persistent from transient |
| **Missing metrics and cost data** — "each layer found defects" but no false positive rates, time costs, or effort quantification | Practitioner, Systems Engineer | MEDIUM | Yes — add from case studies |
| **Circularity is acknowledged but not resolved** — author uses SE to build projects, finds SE patterns, reports SE works | Epistemologist, Devil | HIGH | Partially — reframe prescriptive claims as hypotheses |

---

## Divergent Criticism (Reviewers Disagree)

| Issue | Position A | Position B | Tension |
|-------|-----------|-----------|---------|
| **Is "context architecture" genuinely new?** | Devil, ML Researcher: Yes, has no SE equivalent, may seed a new discipline | Systems Engineer: No, it's interface management / interrupt-driven interfaces | Reveals depth of SE knowledge needed to resolve |
| **Will "reproduce, don't assess" survive?** | Practitioner: Most actionable pattern, use it now | ML Researcher: Workaround for current reasoning limits, obsolete in 18 months | Depends on model improvement trajectory |
| **Is the human oversight claim permanent?** | Educator, Systems Engineer: Yes, domain judgment is irreplaceable | Devil: Transitional pattern; autonomous agents are advancing | Fundamental tension in the proposition |
| **Should it be framed as SE or as something new?** | Author, Systems Engineer: SE with additions | Devil: "SE is necessary but insufficient" — lead with what's new | The framing question IS the proposition |

---

## Priority Action Plan

### P0 — Must address (changes the core argument)

1. **Invert the framing.** Lead with what's genuinely new (the four novel patterns). Treat the SE parallels as expected background, not the headline. The current structure buries the contribution behind a tautology. The Devil's steel man nails it: **"SE is a necessary but insufficient foundation for augmented engineering."**

2. **Split material properties into persistent vs. transient.** Create two categories:
   - *Likely persistent:* confidence inflation (tied to RLHF), auto-loading cliff (structural to agent architecture), observation-calibration gap (working memory limitation)
   - *Under active research:* hallucination rates (declining), scoring calibration (improving), mathematical reasoning (advancing rapidly)
   - Adjust downstream recommendations accordingly — patterns built on transient properties should be framed as "current best practice" not permanent principles.

3. **State what would falsify the thesis.** The epistemologist is right: the proposition is currently unfalsifiable. Define what evidence would disprove it. Candidates: a successful agentic approach that violates SE principles; a situation where SE framing actively misleads; a genuinely novel principle with no SE analogue that the author missed.

4. **Reframe prescriptive claims as hypotheses.** "Stop looking for AI-native methodologies" and "the students who understand SE will adapt" are presented as conclusions but the evidence only supports them as hypotheses. Match the claim strength to the evidence base.

### P1 — Should address (strengthens the work)

5. **Compress "What's the Same" to one paragraph.** List the SE principles that apply (V&V, decomposition, feedback loops, risk classification, configuration). Don't elaborate — the audience either knows them or can look them up. Use the freed space for what's actually interesting.

6. **Add metrics from case studies.** For OPAL: defects per verification layer, unique defects per layer. For vmodel.eu: the five specific single-agent failure modes with parse rates. For driven-pendulum: the three specific errors with before/after values. Numbers are more convincing than "each layer found defects."

7. **Expand or explicitly defer the education section.** Either write learning outcomes, assessment methods, sequencing, and the chicken-and-egg problem (domain expertise needed for validation, but students are building domain expertise) — or state clearly that translating these principles into curriculum is a separate task requiring collaboration with engineering educators.

8. **Engage with the streetlight fallacy.** Acknowledge that an ML researcher or cognitive scientist examining the same projects would find different patterns. State whether the SE lens is claimed to be the *correct* frame or merely *a useful* frame. The honest answer ("a useful frame, not the only one") is fine but should be explicit.

9. **Address the autonomy trajectory.** What happens to the proposition if human oversight becomes optional? Does the framework survive? The "human in the loop" claim has a confidence of SUPPORTED, not ESTABLISHED. Be explicit about its shelf life.

### P2 — Nice to have (polish)

10. **Add a failure case.** Describe a project or task where agentic approaches didn't work, or where the SE framing wasn't helpful. This is the single strongest thing the author could add to counter the survivorship bias criticism.

11. **Engage with SE depth.** The systems engineer reviewer correctly notes that the V-model mapping is superficial — no traceability matrices, derived requirements, tool qualification (DO-330), or assurance levels. Either engage with these seriously or explicitly scope the proposition to "SE principles at the practitioner level, not at the certification level."

12. **Reformat for the actual audience.** The practitioner reviewer nailed it: if this were an 800-word blog post titled "Four Things I Learned About LLMs From Nine Engineering Projects," it would spread on Slack. The academic packaging limits the audience. Consider two versions: a short practitioner piece and a longer reflective account.

---

## Verdict

The proposition contains a genuine insight trapped inside the wrong framing. The interesting contribution — four novel patterns emerging from the specific properties of LLMs — is buried under a tautological headline ("SE still works!") and undermined by an overloaded material properties analogy.

The Devil's steel man states the proposition better than the proposition states itself:

> **SE is a necessary but insufficient foundation for augmented engineering. The engineering principles you already know transfer directly and provide a strong starting framework. But AI agents also introduce genuinely novel challenges — context architecture, reproduction-based verification, cheap layered V&V, and substrate-specific failure modes — that existing SE frameworks do not address.**

Revise around this framing, split persistent from transient properties, add metrics, and compress the "What's the Same" section. The result would be worth publishing — as a practitioner reflection, not as an academic claim, given the N=1 evidence base.
