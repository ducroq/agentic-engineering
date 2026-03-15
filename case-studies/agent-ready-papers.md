# agent-ready-papers: Different Claims Need Different Checking

**Domain:** Academic writing — AI-augmented research papers
**Pattern:** Typed verification — not all claims are the same; facts, arguments, and novel contributions each have distinct failure modes and need distinct verification procedures

---

## 1. What Was Built

agent-ready-papers is verification infrastructure for writing academic papers with AI assistance. The problem it solves isn't citation hallucination specifically (tools exist for that) — it's the broader verification challenge: AI writing assistants produce fluent, well-structured output that *reads* correct, masking failures that are invisible to casual inspection.

Four failure modes appeared consistently across three real paper projects (targeting IEEE TIM, Measurement Science and Technology, and Learned Publishing):

1. **Citation hallucination** — fabricated references with plausible-sounding titles and DOIs
2. **Confidence inflation** — speculative claims stated with the certainty of established findings
3. **Scope creep** — arguments expanded beyond evidence support without structural constraints
4. **Calculation errors** — arithmetic mistakes hidden in plausible-looking results

Existing tools (RefChecker, scite.ai, RAG systems) address citation hallucination at the model or tool level. None address confidence inflation, scope creep, or the process-level question: how do you systematically verify different *types* of claims?

---

## 2. How the Agents Were Used

The workflow centers on a **claim registry** — every substantive statement in the paper is registered, typed, and verified according to type-specific procedures:

**CLAIM** (factual statement with a source):
- Verification: Does the source exist and say this?
- Procedure: 6-step anti-hallucination checklist (is the paper real? is the author real? is the journal real? does the claim match the paper's scope? exact location cited? have I read the relevant section?)

**ARGUMENT** (interpretive conclusion combining evidence + reasoning):
- Verification: Is the reasoning valid? Are premises verified? Is the warrant explicit?
- Procedure: Adapted Toulmin (1958) analysis — claim, grounds, warrant, qualifier, counter-arguments

**PROPOSITION** (novel recommendation or contribution):
- Verification: Are constructs defined? Boundary conditions specified? Alternatives engaged?
- Procedure: Adapted Whetten (1989) analysis — what, how, why, when/where/who, so what

**CALCULATION** (derived numerical value):
- Verification: Does the stated result follow from the stated formula and inputs?
- Procedure: Mechanical reproduction (same pattern as the driven-pendulum case study)

The agent drafts content, the human registers claims as they appear, and verification follows type-specific checklists. The registry tracks priority (P0/P1/P2), confidence tier (ESTABLISHED through SPECULATIVE), and verification status.

---

## 3. What Worked

**Typed verification catches what generic review misses.** The key finding from three retrospective audits across different paper types:

In the Proposition paper audit, entry H4 ("Invalid feedback undermines the primary benefit") was initially registered as a CLAIM with no source — scored SPECULATIVE (0.25 confidence). When retyped as an ARGUMENT, its three premises were each independently verified, and the warrant (systematically biased measurement leads to systematically invalid feedback) was logically valid. Re-assessed as EMERGING. The typing changed the verdict because it changed the verification procedure — you don't check an argument the same way you check a fact.

All three audits revealed entries misclassified as CLAIMs that were actually ARGUMENTs or PROPOSITIONs, leading to false-low confidence scores.

**Confidence-to-language mapping prevents inflation.** The framework enforces a prescriptive mapping:

| Tier | Language |
|------|----------|
| ESTABLISHED | "demonstrates", "shows" |
| SUPPORTED | "indicates", "evidence suggests" |
| EMERGING | "may", "preliminary evidence" |
| SPECULATIVE | "warrants investigation", "we hypothesize" |

In the Technology Paper audit, six of 22 claims used language more confident than evidence warranted — "demonstrates" for single-unit findings, "extends to" for extrapolations. The mapping catches these mechanically.

**100% claim coverage is achievable and useful.** Paper 1 (perspective paper on the verification gap) achieved 19/19 claims verified, all references checked against DOIs, all AI-introduced citations passed the anti-hallucination checklist. The overhead was ~5-10 minutes per claim, which is significant but comparable to careful manual fact-checking.

**Page budgets prevent scope creep.** Defining section-level page budgets before writing begins — and tracking "content moved" and "content cut" decisions — structurally prevents the AI's tendency to expand sections without limit.

---

## 4. What Didn't Work

**The tag/tier conflation.** One source project independently developed a 7-level tag system (VERIFIED, HIGH CONF, MED CONF, etc.) that conflated verification status (has someone checked?) with confidence assessment (how strong is the evidence?). Retrofitting to the framework's separated model (Status: checked/unchecked; Confidence: ESTABLISHED/SUPPORTED/EMERGING/SPECULATIVE) required systematic migration. The distinction matters because a claim can be *checked* and still *speculative* — or *unchecked* and actually well-established.

**Unregistered Discussion claims.** One paper draft contained six substantive claims in Discussion sections that appeared nowhere in the registry. Discussion sections — the most reviewer-scrutinized part of papers — went unverified because the registration discipline focused on Introduction and Results. The framework now explicitly requires Discussion claims to be registered.

**Self-review doesn't catch confidence inflation.** The model that writes "this demonstrates" for a speculative claim doesn't flag its own language as overconfident in review mode. The confidence mapping works because it's a structural constraint (tier determines permissible language), not a judgment call during review.

**The verification overhead is real.** 5-10 minutes per claim, 20+ claims per paper, plus anti-hallucination checks on every reference — this adds hours to the writing process. For papers where verification cost exceeds the cost of being wrong, the full framework is overkill.

---

## 5. The Pattern

> **When** writing technical or academic documents with AI assistance where correctness matters,
> **use** typed verification: register every substantive claim, classify it by type (fact, argument, recommendation, calculation), and apply type-specific verification procedures — because each type has different failure modes and "check the source" doesn't work for interpretive conclusions or novel contributions.

The deeper insight: **fluent output is not verified output.** AI writing assistants produce text that reads well, cites plausibly, and argues coherently — regardless of whether the facts are real, the reasoning is valid, or the confidence is calibrated. The framework's contribution isn't catching hallucinations (tools do that) — it's systematizing the full range of verification that academic writing requires.

The Toulmin and Whetten frameworks aren't novel — they're standard tools in academic argumentation theory. What's new is operationalizing them as type-specific checklists within an AI-augmented writing workflow, so the verification procedure matches the claim type automatically.

**When this pattern doesn't apply:**
- Informal or exploratory writing where verification overhead isn't justified
- Short documents with few claims where the overhead exceeds the benefit
- Domains where all claims are purely factual — the typing adds value when you have a mix of facts, arguments, and proposals

---

## 6. Limitations

All three source projects share the same author team and domain cluster (engineering/medical technology). Whether the typed verification approach generalizes to other fields — humanities, social sciences, pure mathematics — is plausible but unverified. The Toulmin and Whetten frameworks themselves are grounded in Western academic argumentation traditions.

The "100% claim coverage" achievement on Paper 1 is encouraging but the paper is a perspective piece (19 claims), not a large empirical study. Scaling to papers with 50+ claims, complex statistical analyses, and multi-author workflows has not been tested.

The confidence-to-language mapping is prescriptive by design, but calibrating what constitutes "ESTABLISHED" vs. "SUPPORTED" requires domain judgment. The framework systematizes the mapping but doesn't eliminate the subjective assessment of evidence strength.
