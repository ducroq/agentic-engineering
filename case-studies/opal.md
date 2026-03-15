# OPAL: Validate the Validators

**Domain:** Embedded systems — mixed-signal optical instrument
**Pattern:** Recursive V&V — each verification layer finds defects the previous one missed, so verify the verification itself

---

## 1. What Was Built

OPAL is a prototype confocal backscatter detector that measures pharmaceutical concentrations via bead agglutination. It uses a repurposed Blu-ray pickup (Class 3B 405nm laser), a mixed-signal signal chain with millivolt-level precision, voice coil actuators, and five voltage domains — all controlled by an ESP32.

A working breadboard had been validated, and the next step was a custom PCB. The problem: the KiCad schematic had never been systematically reviewed. The design crosses disciplines — optical physics, analog electronics, firmware, thermal management, laser safety — that no single engineer typically covers. A traditional design review would require multiple specialists. The question was whether an agentic workflow could substitute.

---

## 2. How the Agents Were Used

The review ran over three days in February 2026, in phases that built on each other:

```
Checklist Generation (14 checklists, ~725 items)
    ↓
Risk Classification (P0: safety-critical / P1: design / P2: best-practice)
    ↓
P0 Verification (77 issues checked against schematic + standards)
    ↓  found 2 defects
V&V Audit ("can we trust the verifiers?")
    ↓  found 1 more defect
P1 Spot-Check (50 items from 220 P1 pool)
    ↓  found 4 firmware bugs
Full P1 Campaign
    ↓  found 3 more bugs
Standards Grounding + Signal Integrity Analysis
```

The engineer directed each phase transition. Agents generated checklists, classified items, and verified issues against the schematic and datasheets. The engineer made scope decisions (which items are P0?), provided resources agents couldn't access (NDA-protected datasheets), and initiated the recursive V&V step.

The critical structural choice: after Phase G (P0 verification) appeared complete, the engineer asked "can we trust our agents?" and launched three parallel audit agents to verify the verifiers. This is the recursive V&V pattern.

---

## 3. What Worked

**Each layer found defects the others missed.** Ten verified fixes were implemented before fabrication, with zero false positives reaching the fix register. The key finding is not the count but the distribution:

| Layer | Found |
|-------|-------|
| P0 verification | FIX-01 (laser GPIO pull-downs missing — boot-time eye hazard), FIX-02 (LDO undersized for motor driver) |
| V&V audit | FIX-04 (motor driver logic supply pin entirely absent from schematic) |
| P1 spot-check | FIX-05 (ADC timing), FIX-06 (PWM resolution), FIX-07 (thermal) |
| Full P1 campaign | FIX-08 (reference impedance), FIX-09 (DAC initialization), FIX-10 (laser safety in firmware) |
| + local datasheets | ISS-103, ISS-130 (two hardware bugs from NDA-protected specs) |

Stopping after P0 verification would have left 8 of 10 fixes undiscovered. Most concerning: FIX-06, where an ESP32 PWM resolution limit caused the safety voltage cap from FIX-03 to silently map to 4.1V instead of the intended 2.0V — a safety regression hidden inside an apparent fix.

**Cross-discipline coverage.** The 14 checklists spanned disciplines (optical, analog, digital, thermal, EMC, laser safety, power integrity) that a single-engineer review would cover unevenly. The checklists were grounded in real standards (IPC-2221B, IEC 60825-1, JEDEC JESD51, IEEE 1012).

**Risk stratification made the review tractable.** 725 items is unmanageable as a flat list. The P0/P1/P2 classification directed thorough verification at the 126 safety-critical items and lighter treatment of the 355 best-practice items.

---

## 4. What Didn't Work

**Systematic standard misapplication.** Checklists consistently cited IEC 62368-1 (consumer electronics) instead of IEC 61010-1 (laboratory instruments). This wasn't random — it was training data bias toward consumer products. Every standards citation from AI should be verified against the actual product category.

**Physically impossible solutions.** During signal integrity analysis, the agent proposed "parking" voice coils (PWM=0) to reduce electromagnetic interference. This would destroy the instrument — voice coils need continuous current to hold focal position; zero current releases the lens to its spring rest position, losing focus entirely. The agent had no model of actuator physics.

**NDA barrier.** Two issues remained INCONCLUSIVE until the engineer provided local copies of NDA-protected datasheets. One revealed a 10x resistance error (500 ohm recorded as 5k ohm) that had silently propagated through all calculations since early design. Agents can only verify against information they can access.

**No spontaneous propagation.** When fixes were applied, stale values persisted in five dependent documents. Agents don't maintain system-wide consistency unless explicitly prompted.

---

## 5. The Pattern

> **When** reviewing a complex engineering design across disciplines where defects have high consequences,
> **use** recursive V&V: verify the design in layers, then verify the verification itself — apply the same skepticism to your checking process that you apply to the design,
> **because** each verification layer has blind spots, and only by auditing the auditors do you discover what was missed.

The deeper insight is about **meta-cognition in verification workflows**. The engineer's most consequential decision wasn't technical — it was asking "should we trust what we just did?" after the first verification pass appeared clean. That question, applied recursively, is what separates a thorough review from a single-pass sanity check.

This pattern resonates with established engineering practice. Independent verification and validation (IV&V) is standard in safety-critical systems (DO-178C in avionics, IEC 61508 in functional safety). What's new is that agentic AI makes multi-layer verification cheap enough to apply routinely, not just on safety-critical projects with dedicated V&V budgets.

**When this pattern doesn't apply:**
- Low-consequence designs where a missed defect costs less than the review effort
- Single-discipline designs where one engineer has full domain coverage
- When you lack the domain expertise to evaluate whether the verification is asking the right questions — the recursive step requires knowing what "good" looks like

---

## 6. Limitations

This is one design review by one engineer who both designed the instrument and conducted the AI-augmented review. The "8 of 10 missed by single-pass" result is specific to this design — it demonstrates the principle but doesn't quantify a general rate. No independent engineering review was conducted for comparison, so we can't say whether AI-augmented review was better or worse than a traditional multi-engineer review — only that it found real defects that would have reached fabrication.

All case studies in this collection share the same researcher, which limits generalizability. The recursive V&V pattern is consistent with established IV&V practice in safety-critical systems (IEEE 1012, IEC 61508), which provides some external grounding, but the specific agentic implementation has not been independently replicated.
