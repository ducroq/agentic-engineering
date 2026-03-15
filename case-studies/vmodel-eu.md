# vmodel.eu: Separate What's Deterministic from What Needs Judgment

**Domain:** Education — automated formative feedback on student requirements specifications
**Pattern:** Role specialization — don't ask one agent to do everything; separate deterministic checks, qualitative analysis, and calibrated scoring into dedicated roles

---

## 1. What Was Built

vmodel.eu gives engineering students automated formative feedback on their requirements specifications. Students submit a document; within minutes they get structured feedback on structure, quality, domain coverage, and V-model alignment. It runs entirely on local hardware (RTX 4080, Ollama) with zero cloud dependencies — GDPR by design.

The initial approach was obvious: one large prompt, one model, do everything. It didn't work. The interesting part of this case study is *why* it failed and what the replacement architecture looks like.

---

## 2. How the Agents Were Used

The production pipeline has seven agents in sequence:

```
Agent 0: Extraction (heuristic)         — parse PDF/DOCX into text
Agent 1: Structure (heuristic)          — 6 boolean floor_checks
Agent 2: Quality Review (Gemma 3 27B)   — findings, contradictions, issues
Agent 3: Coverage (Phi-4 14B)           — per-requirement gap analysis
Agent 4: Problem Statement (Gemma 3)    — separate problem statement review
Agent 5: Traceability (Phi-4)           — V-model verification gaps
Agent 6: Scoring (embedding + Ridge ML) — predicted score 1-5
Merge: deduplicate findings, render feedback email
```

End-to-end: ~3-4 minutes. The processing time is deliberate — ADR-015 documents why instant feedback creates optimization loops where students fix symptoms without understanding causes (grounded in Nicol & Macfarlane-Dick 2006, Sadler 1989).

The key architectural choices:

**Deterministic first.** Agents 0 and 1 are heuristics — no LLM involved. They extract structure and compute six boolean checks (table present? IDs present? MoSCoW? measurable thresholds?). These feed into binding scoring rules that prevent later agents from contradicting observable facts.

**Complementary models.** Gemma 3 27B excels at structural insight — compound requirements, contradictions, redundancy. Phi-4 14B systematically enumerates every individual requirement. Manual comparison: Gemma wins 8/10 reports, Phi-4 wins 1/10, tie 1/10. Neither covers what the other does.

**Scoring removed from LLMs entirely.** Agent 6 uses mpnet embeddings (768 dimensions) plus 12 hand-engineered structural features, fed into a Ridge regression trained on 122 baseline reports with human-validated ground truth.

---

## 3. What Worked

**Multi-agent solved five specific failures of single-agent.** ADR-016 documents each:

1. Gemma parsed the full prompt only 72% of the time. Adding scoring logic dropped it to 50%.
2. Every model tested (five total) exhibited regression to the mean on scoring — high-quality reports scored too low, some low-quality reports inflated.
3. Gemma and Phi-4 have complementary blind spots — together they cover what neither does alone.
4. Structure detection (is there a table?) is deterministic. Asking an LLM is wasteful and unreliable.
5. Each new review dimension (verification methods, V-model alignment) required rewriting an already-stretched prompt.

Separating concerns let each component operate within its reliable range.

**Blind validation on held-out data.** Trained on 122 baseline reports, tested on 64 unseen reports from three domains (AI, embedded vision, mechatronics):

| Metric | Training (LOOCV) | Held-out (64) |
|--------|-----------------|---------------|
| MAE | 0.443 | 0.734 |
| Within-1 agreement | 96.7% | 93.8% |

Per-domain: AI 100%, mechatronics 97%, embedded vision 85%. The system generalizes across engineering domains without domain-specific tuning.

**Structural features saved domain transfer.** Pure embeddings encode *topic* (ML vocabulary vs. mechatronics vocabulary), not *quality* (presence of tables, prioritization, measurable criteria). When mechatronics reports entered the held-out set, pure embeddings collapsed to 54.7% within-1 agreement. Adding 12 structural features recovered it to 93.8%. The lesson: separate semantic understanding from structural quality indicators.

---

## 4. What Didn't Work

**Every LLM failed at calibrated numeric scoring.** Five models tested, all exhibited regression to the mean. The best (Gemma 3 27B) still scored high-quality reports 2.0 points below target. Root cause: 14-27B parameter models can't simultaneously internalize a rubric, evaluate domain content, and calibrate numeric output. They handle any two, not all three. This appears to be a fundamental limitation at current model scale — not a prompting problem.

**LLMs contradicted their own observations.** Qwen reported `has_table=true` in analysis, then scored structure=1. Binding floor_check rules were needed to prevent this. The general lesson: LLMs can observe accurately but struggle to consistently translate observations into calibrated scores.

**Invisible inflation at the low end.** Velvet 14B looked good on high-quality reports but inflated low-quality scores from 1-2 to 3.0. This is only visible when you test the full quality spectrum. Testing only on "good" examples masks systematic failure.

**Prompt engineering hit a wall.** Four major iterations improved high-quality report scores from 2.0 to 2.6 — meaningful but still 2.2 points short. The gap was architectural, not linguistic.

---

## 5. The Pattern

> **When** a task requires simultaneous judgment across multiple dimensions (here: structure + quality + coverage + scoring) and a single agent fails at the combination,
> **use** role specialization: separate deterministic checks from qualitative analysis from calibrated scoring, using the best tool for each — heuristics where things are objectively verifiable, LLMs where judgment is needed, ML classifiers where calibration matters,
> **because** each component type has different failure modes, and combining them in one prompt forces the model to do things it's bad at alongside things it's good at.

The deeper insight: **know what LLMs are bad at and don't ask them to do it.** Numeric scoring, self-consistency between observations and conclusions, parsing complex procedural instructions — these fail reliably. Once you identify the failure mode, move that specific capability to a component designed for it.

This is the same principle behind Unix pipelines and microservice architectures: do one thing well, compose the results. What's specific to agentic AI is identifying *which* things LLMs do well (qualitative analysis, finding contradictions, domain-aware enumeration) and which they don't (calibrated scoring, deterministic structure detection).

**When this pattern doesn't apply:**
- Simple tasks where a single agent performs reliably — multi-agent adds latency and complexity for no benefit
- When you lack ground truth data for calibration (here: 122 graded reports) — without calibration anchors, you can't verify the pipeline works
- When the task is primarily generative rather than evaluative — the failure modes documented here are specific to assessment/review tasks

---

## 6. Limitations

This documents one system built for one educational context. The 93.8% within-1 agreement is strong but the held-out set is 64 reports. The "multi-agent beats single-agent" finding is specific to this task and these models — a more capable future model might handle everything in one pass. The evidence shows multi-agent is better given current model limitations, which is a snapshot, not a permanent truth.

The deliberate-slowness design (rate-limited feedback to prevent optimization loops) is grounded in educational assessment literature but has not been tested in a controlled experiment against instant feedback.

The system achieves EU AI Act Article 6(3) non-high-risk classification and follows a 10-principle constitution (ADR-009) with lecturer review before release — but these governance choices are context-specific and may not transfer to other assessment settings.
