# Augmented Engineering — Cheat Sheet

**One sentence:** SE principles transfer to AI agents, but four things are genuinely new.

---

## The Four Patterns

### 1. Learn the Material
LLMs have behavioral properties you must design around, like material properties in physical engineering.

- **Confident but wrong.** They say "demonstrates" when they mean "suggests." (agent-ready-papers: 6/22 claims over-confident)
- **Can observe, can't score.** They see the table but score structure=1 anyway. (vmodel.eu: separated scoring → 54.7% to 93.8% agreement)
- **Plausible-but-wrong output.** Right units, right magnitude, wrong answer. (driven-pendulum: 0/3 errors caught by review, 3/3 by reproduction)
- **Scores regress to the mean.** High work scored low, low work scored high. (vmodel.eu: 5 models, all did this)

*First two properties likely persist. Last two may fade as models improve. Design for all four today, hold loosely.*

### 2. Layer Your Verification
V&V is old. V&V that costs minutes instead of months is new. Stack passes — each one catches what the others miss.

- OPAL: 5 layers, 10 defects. Stopping after layer 1 would have missed 8.
- The recursive step — auditing the auditors — found FIX-04 (motor driver logic pin), which the first pass missed entirely.
- Zero false positives in the fix register.

*When does the nth layer stop paying off? Unknown. Five was still productive.*

### 3. Context Is Architecture
Agents have an **auto-loading cliff**: what's loaded automatically gets used; everything else is invisible.

- A well-written doc below the cliff has zero impact.
- **Task-triggered pointers** cross the cliff:
  - Doesn't work: `| API troubleshooting | docs/api-quirks.md |`
  - Works: `| API returns 422 | docs/api-quirks.md |`
- The difference: situations vs. categories. Agents recognize situations.

*Discovered in agent-ready-projects, validated across 100+ sessions.*

### 4. Reproduce, Don't Assess
"Does this look right?" catches nothing. "What answer do I get?" catches everything.

- Driven pendulum: Claude + Gemini assessed 68 equations → 0 errors found.
- Sonnet reproduced step-by-step → 3 errors found:
  1. Table labeled "5 degrees" computed at 1 degree (5x error)
  2. Dwell time formula: predicted 84ms vs. actual 43ms
  3. Correction rate: 12 s/hr stated as 36 s/hr
- All three had correct units and plausible magnitudes. Invisible to assessment.

*The technique may age out. The principle — verify by computing, not by vibes — won't.*

---

## Quick Decision Rules

| Situation | Pattern |
|-----------|---------|
| LLM gave me a number | Reproduce it (Pattern 4) |
| LLM scored or rated something | Don't trust it — separate scoring (Pattern 1) |
| LLM sounds very confident | Check the evidence tier (Pattern 1) |
| Agent isn't using my docs | Check if it's below the cliff (Pattern 3) |
| One review pass found nothing | Run another layer (Pattern 2) |
| Designing agent context files | Use task-triggered pointers (Pattern 3) |

---

## Honest Limits

- N=1 researcher, 9 projects, no controlled comparison
- Survivorship bias — failed attempts are absent
- Two of four LLM properties may be obsolete in 12-24 months
- This is a practitioner's hypothesis, not a validated framework
