# Agentic Engineering

**What's new when engineers work with AI agents?**

Systems engineering is a necessary but insufficient foundation. V&V, decomposition, feedback loops, and risk management all transfer directly. But AI agents introduce four genuinely novel challenges that existing frameworks don't address.

## The Four Patterns

1. **Learn the Material** — LLMs have behavioral properties (confidence inflation, observation-calibration gap, plausible-but-wrong outputs). Some are permanent. Some are being fixed.
2. **Layer Your Verification** — V&V became cheap enough to apply routinely. Five layers found 10 defects; stopping at one would have missed eight.
3. **Context Is Architecture** — Agents only see what's auto-loaded. Task-triggered pointers cross the cliff.
4. **Reproduce, Don't Assess** — When checking equations, compute the answer independently. Assessment found 0/3 errors. Reproduction found 3/3.

## Nine Projects

| Project | Domain | Key pattern |
|---------|--------|-------------|
| OPAL | Embedded/optical | Recursive V&V across 5 layers |
| vmodel.eu | Education/software | Role specialization, separated scoring |
| Driven Pendulum | Physics/hardware | Reproduce-don't-assess |
| agent-ready-projects | Methodology | Auto-loading cliff, task-triggered pointers |
| agent-ready-papers | Academic writing | Typed verification (CLAIM/ARGUMENT/PROPOSITION) |
| llm-distillery | ML/content filtering | Config-driven generics, oracle output discipline |
| RenkumSpot | Community platform | Schema as source of truth |
| ese_bot | Document retrieval | EU sovereignty as architecture constraint |
| ovr.news | News curation | Multi-provider tiered fallbacks |

## Repository Structure

```
agentic-engineering/
├── PROPOSITION.md          # The core argument (read this first)
├── REVIEW-SYNTHESIS.md     # Six critical reviews + action plan
├── case-studies/           # Five detailed case studies
├── research/               # Research questions + methodology
├── guide/                  # Pattern library (planned)
├── claims/                 # Claim registry (17 claims, 59% coverage)
├── site/                   # Astro website (the public output)
│   └── src/
│       ├── pages/          # Landing page + 4 pattern pages
│       └── components/     # Hand-drawn SVG illustrations
└── .claude/agents/         # Review agent prompts (6 perspectives)
```

## Website

The site is built with Astro and features hand-drawn SVG illustrations on a graph-paper background. It presents the four patterns with evidence from the nine projects.

To run locally:
```bash
cd site && npm install && npx astro dev
```

## The Evidence Base

Nine projects, one researcher, 2025-2026. Practice-based evidence — not experimental. The patterns are worth trying. The framing is worth debating. Neither is established. See `PROPOSITION.md` for the full argument and `REVIEW-SYNTHESIS.md` for critical review.

## License

TBD
