# AI for Engineers: Understanding Before Using
## Test-speech outline -- 30 minutes

---

## Part 0: What Are We Actually Talking About? (3 min)

A 60-second stack, bottom to top -- just enough so everyone has the same mental model:

1. **Machine Learning** -- software that learns patterns from data instead of following hand-written rules. Not new (1990s onward), but compute and data made it practical.
2. **Deep Learning** -- ML with many layers of neurons. Enabled image recognition, speech, translation. The "deep" in deep learning is literally "more layers."
3. **Large Language Models (LLMs)** -- deep learning trained on text. Predict the next word, billions of times, on most of the internet. That's it. No reasoning engine, no knowledge database -- a very sophisticated pattern completer.
4. **AI Agents** -- LLMs wrapped in a loop: read context, decide what to do, use tools (search, code, APIs), check the result, repeat. This is what ChatGPT, Copilot, Claude Code etc. actually are when you use them for work.

> **Key point:** An agent is only as good as the model inside it, and the model is a pattern completer trained on text. Everything that follows -- the failures, the patterns, the practices -- flows from this.

**AUDIENCE QUESTION:** "Quick check -- who here has used ChatGPT or Copilot? Who has used it for something beyond a simple question -- generating code, writing a report, analyzing data?"

---

## Part 1: The Problem (10 min)

### 1.1 Opening: The Uncomfortable Numbers (2 min)

- 84-90% of software dev teams use AI daily
- But: 47% experienced negative consequences (McKinsey 2025)
- 96% don't fully trust AI, yet only 48% verify before committing (Sonar 2026)
- Senior devs trust AI *less* than juniors -- experience reveals problems

> **Key line:** Experience reveals problems rather than building confidence. The opposite of normal technology adoption.

### 1.2 The Productivity Paradox (2 min)

| Context | Impact | Source |
|---------|--------|--------|
| Lab (simple tasks) | **+55.8%** faster | Peng et al. 2023 |
| Enterprise deployment | **+8.69%** (+ 16% more build failures) | Accenture 2024 |
| Experienced devs, real codebases | **-19%** slower | METR 2025 |

> **Key line:** Experienced developers were 19% slower with AI while *perceiving* themselves 20% faster. A 39-point perception gap.

> **Punchline:** AI makes easy things easier. But engineering is rarely easy.

**AUDIENCE QUESTION:** "Show of hands -- who uses AI tools in their daily work? And who has a systematic way of checking whether the output is correct?"

### 1.3 Beyond Software: What About "Real" Engineering? (3 min)

Pick 2-3 for the audience:

- **Chemical (HAZOP):** >86% textual similarity to expert work, but only 19-37% semantically valid. Looks right, isn't.
- **Civil (FE exam):** 0% on Structural Design, 100% on Ethics. Catastrophic domain failure.
- **Mechanical:** 47-60% on core ME problems. Nearly 40% failure on the best tool.
- **Electrical (PCB):** AI hallucinated electronic components -- invented resistors, wrong suggestions.

> **Pattern:** AI produces outputs that *look* professionally competent but contain errors only domain experts catch.

**AUDIENCE QUESTION:** "Has anyone here encountered AI output that looked correct at first glance but turned out to be wrong? What tipped you off?"

---

## Part 2: The Four Patterns -- What's Actually New (15 min)

> **Transition:** "So the problem is clear. Now -- what do we do about it? I've been working with AI agents across nine engineering projects over the past year. Here are four patterns that are genuinely new."

### 2.1 Learn the Material (3 min)

LLMs have behavioral properties, like material properties in physical engineering. You must design around them.

| Property | Example | Likely persistent? |
|----------|---------|-------------------|
| Confident but wrong | 6/22 claims over-confident in one paper | Yes |
| Can observe, can't score | Sees the table, scores structure=1 anyway | Yes |
| Plausible-but-wrong output | Right units, right magnitude, wrong answer | Fading |
| Scores regress to mean | High work scored low, low work scored high | Fading |

> **Key line:** You wouldn't use steel without knowing its fatigue properties. Don't use LLMs without knowing theirs.

**AUDIENCE QUESTION:** "When you use a new material or tool for the first time -- how do you learn its limits? Do you do the same with AI?"

### 2.2 Layer Your Verification (4 min)

V&V is old. V&V that costs *minutes* instead of months is new.

- OPAL PCB review: 5 verification layers, 10 defects found
- Stopping after layer 1 would have missed 8 of 10
- The recursive step -- auditing the auditors -- found a motor driver logic pin error the first pass missed entirely
- Zero false positives

> **Key line:** When verification is cheap, layer it. Run another pass. Audit the auditors.

**AUDIENCE QUESTION:** "In your domain, how many independent checks does a design go through before it ships? What if you could add five more checks for the cost of a coffee?"

### 2.3 Context Is Architecture (4 min)

Agents have an **auto-loading cliff**: what's loaded gets used; everything else is invisible.

```
Doesn't work:  | API troubleshooting | docs/api-quirks.md |
Works:          | API returns 422     | docs/api-quirks.md |
```

- The difference: categories vs. situations. Agents recognize situations.
- A beautifully written document below the cliff has zero impact on agent behavior.
- Validated across 100+ sessions on real projects.

> **Key line:** If you don't architect what the agent sees, you don't control what the agent does.

### 2.4 Reproduce, Don't Assess (4 min)

"Does this look right?" catches nothing. "What answer do I get?" catches everything.

**Live example (driven pendulum project):**
- Claude + Gemini assessed 68 equations for correctness --> 0 errors found
- Same model, asked to reproduce step-by-step --> 3 errors found:
  1. Table labeled "5 degrees" computed at 1 degree (5x error)
  2. Dwell time formula: predicted 84ms vs actual 43ms
  3. Correction rate: 12 s/hr stated as 36 s/hr
- All three had correct units and plausible magnitudes -- invisible to "assessment"

> **Key line:** Don't ask AI "is this right?" Ask it "what do *you* get?" Then compare.

**AUDIENCE QUESTION:** "Think about how you review a colleague's calculations. Do you check the answer, or do you redo the calculation? What changes when the 'colleague' is an AI?"

---

## Part 3: What This Means For You (5 min)

### 3.1 Quick Decision Rules (2 min)

| Situation | What to do |
|-----------|-----------|
| LLM gave me a number | Reproduce it (Pattern 4) |
| LLM scored or rated something | Don't trust it -- separate scoring (Pattern 1) |
| LLM sounds very confident | Check the evidence tier (Pattern 1) |
| Agent isn't using my docs | Check if it's below the cliff (Pattern 3) |
| One review pass found nothing | Run another layer (Pattern 2) |

### 3.2 The Honest Limits (1 min)

Be upfront:
- This is N=1 researcher, 9 projects, no controlled comparison
- Two of four LLM properties may fade in 12-24 months
- This is a practitioner's hypothesis, not a validated framework

> **But:** The underlying principles -- verify, layer, design context, know your materials -- are permanent. The specific techniques will evolve.

### 3.3 Closing (2 min)

> The hard part is no longer producing engineering work. The hard part is knowing whether the work is any good.

> Teaching engineers to use AI without teaching them to evaluate AI outputs is like teaching them to read test results without teaching them what the results mean.

**FINAL AUDIENCE QUESTION:** "Starting tomorrow -- which one of these four patterns could you apply to your current project?"

---

## Timing Summary

| Section | Minutes | Cumulative |
|---------|---------|------------|
| 0. What are we talking about | 3 | 3 |
| 1.1 Opening stats | 2 | 5 |
| 1.2 Productivity paradox | 2 | 7 |
| 1.3 Beyond software | 3 | 10 |
| 2.1 Learn the material | 3 | 13 |
| 2.2 Layer verification | 4 | 17 |
| 2.3 Context is architecture | 4 | 21 |
| 2.4 Reproduce don't assess | 4 | 25 |
| 3.1 Decision rules | 2 | 27 |
| 3.2 Honest limits | 1 | 28 |
| 3.3 Closing | 2 | 30 |

## Notes

- Audience questions are placed at natural transition points and serve as breathers between dense content
- Part 1 establishes credibility through external evidence (not your own work)
- Part 2 brings in your original contribution -- the four patterns
- Part 3 gives them something actionable to take away
- The "honest limits" section builds trust -- don't skip it
