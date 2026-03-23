# Episode 00: Introduction — What's Genuinely New?

**Series:** Augmented Engineering: the craft, not the hype
**Duration:** ~8 minutes
**Cast:** Lisa (host), Marc (expert), Sven (skeptic)

## Summary

The series opener. Three voices introduce the central question: what's genuinely new when humans and AI agents build things together — and what's just old engineering in a new hat? Marc previews four patterns from nine projects. Lisa pushes back on the N=1 limitation. Sven appoints himself skeptic-in-chief.

## Key claims made in this episode

| # | Claim | Speaker | Line | Confidence | Source |
|---|-------|---------|------|------------|--------|
| C1 | Nine out of ten software development teams use AI tools daily | Lisa | ~new | ESTABLISHED | Stack Overflow 2025 (65K respondents): 84%; JetBrains 2025 (24.5K): 85%; Jellyfish 2025: 90%. Three independent surveys, 90K+ combined. |
| C2 | Only three to eight percent fully trust AI output | Lisa | ~new | ESTABLISHED | Stack Overflow 2025: 3% "highly trust"; JetBrains 2025: 8% "trust completely". |
| C3 | Senior developers trust AI less than juniors | Marc | ~new | SUPPORTED | JetBrains 2025: seniors (10+ yr) 61% low trust vs juniors (0-2 yr) 48%. Stack Overflow trend: trust declining from 52% (2023) to 46% (2025). |
| C4 | AI material properties: more confident than warranted | Marc | 33 | SUPPORTED | Documented across multiple domains. Chemical HAZOP: >86% textual similarity but 19-37% semantic validity (Park et al. 2025). Structural: 0% on core design questions (Naser et al. 2023). |
| C5 | Five verification layers found ten defects, one layer found two | Marc | 42 | ESTABLISHED | OPAL case study (Veen 2026), HAN University. Five-layer review of ESP32-based optical instrument. Documented in augmented-engineering case-studies/opal.md. |
| C6 | Sixty-eight equations reviewed, three errors found only by reproduction | Marc | 59 | ESTABLISHED | Driven-pendulum case study (Veen 2026). Same model, different prompt (assess vs reproduce). Documented in augmented-engineering case-studies/driven-pendulum.md. |
| C7 | Nine projects across different domains | Marc | 17 | ESTABLISHED | Author's own work. Projects enumerated in PROPOSITION.md: OPAL, vmodel.eu, driven-pendulum, agent-ready-projects, agent-ready-papers, llm-distillery, RenkumSpot, ese_bot, ovr.news. |
| C8 | Forty-seven percent of organizations report negative consequences from AI | Lisa | ~new | ESTABLISHED | McKinsey Global Survey 2025. |

## Claim verification status

- **ESTABLISHED** (5): C1, C5, C6, C7, C8 — multiple sources or directly verifiable
- **SUPPORTED** (3): C2, C3, C4 — strong single sources with corroborating evidence
- **EMERGING** (0)
- **SPECULATIVE** (0)

Coverage: 8/8 verified = **100%**

## References

### Industry Surveys
- Stack Overflow. (2025). *Developer Survey 2025*. 65,000+ respondents. https://survey.stackoverflow.co/2025/
- JetBrains. (2025). *The State of Developer Ecosystem 2025*. 24,534 respondents.
- Jellyfish. (2025). *State of Software Engineering Teams*. Global engineering management survey.
- McKinsey & Company. (2025). *The State of AI: Global Survey*.

### Academic Sources
- Park, S. et al. (2025). AI-generated HAZOP analysis. *Safety Science*.
- Naser, M.Z. et al. (2023). Can AI Chatbots Pass the Fundamentals of Engineering Exam? *Journal of Civil Engineering Education*.
- Peng, S. et al. (2023). The Impact of AI on Developer Productivity. (Lab study, +55.8%)
- METR Research. (2025). Measuring AI Impact on Developer Productivity. (Field study, -19%)
- Accenture. (2024). Enterprise AI Deployment Impact. (+8.69%, +16% build failures)

### Case Studies (Own Work)
- Veen, J. (2026). OPAL: AI-Augmented Design Review of an Optical Instrument. HAN University.
- Veen, J. (2026). Driven Pendulum: Equation Verification by Reproduction. HAN University.
- Veen, J. (2026). *The AI-Augmented Engineer*. Internal research report v1.2, HAN University.

## Show notes (listener-facing)

**What this episode covers:**
- Why "what's genuinely new?" is the question that matters
- Four patterns that don't fit existing engineering frameworks
- Nine out of ten teams use AI daily — but fewer than one in ten trust it
- The honest limitation: this is one engineer's experience, not universal law

**Links:**
- agent-ready-projects framework: [GitHub link]
- The AI-Augmented Engineer report: [link when published]
- Stack Overflow Developer Survey 2025: https://survey.stackoverflow.co/2025/

**Next episode:** Context Engineering — what happens when your agent starts every session as a complete stranger.
