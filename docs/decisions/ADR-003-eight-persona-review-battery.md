# ADR-003: Eight-Persona Review Battery

**Date:** 2026-03-19
**Status:** Accepted

## Context

Podcast scripts need feedback before production. A single reviewer catches what a single perspective sees. The augmented-engineering proposition used a six-agent parallel review (systems engineer, ML researcher, practitioner, epistemologist, educator, devil's advocate) and found that convergent criticism — where multiple independent reviewers flag the same issue — is the strongest signal for what actually needs fixing.

The podcast has a broader audience than the proposition. A script that satisfies a senior engineer may lose a junior developer. A script that excites a content creator may bore a podcast purist. The review process needs to represent the actual listener base.

## Decision

Every episode is reviewed by **eight persona agents** running in parallel, compiled by an **orchestrator agent** into a prioritized action plan.

### The eight personas

| Persona | Represents | Key question they answer |
|---------|-----------|------------------------|
| **Junior developer** | 1-2 years experience, uses AI daily | "Do I understand this? Is it relevant to me?" |
| **Team lead** | Managing 8 devs with mixed AI tools | "Does this work for teams or just individuals?" |
| **Skeptic** | 15-year veteran, doubts AI value | "Where do I call BS? What would change my mind?" |
| **Educator** | CS lecturer integrating AI into curriculum | "Can I teach with this? Does it build transferable skills?" |
| **Podcast listener** | Quality-conscious, subscribes to Changelog/Lex | "Is this a real conversation or a scripted lecture?" |
| **Indie hacker** | Solo builder, ships fast, zero patience | "Does this help me ship or slow me down?" |
| **Content creator** | 50K YouTube subscribers, thinks in clips | "Can I promote this? What's the hook, the clip, the share?" |
| **Non-technical manager** | PM making tooling/budget decisions | "Can I follow? Can I build a business case from this?" |

### Why these eight

They cover the full listener spectrum along three axes:
- **Technical depth**: junior → senior → skeptic
- **Organizational role**: individual → team lead → manager
- **Content relationship**: listener → educator → creator

Missing personas that may be added later: embedded systems engineer, open-source maintainer, student, non-English speaker.

### The orchestrator

After all eight reviews complete, the orchestrator:
1. Identifies **convergent praise** — strengths multiple personas agree on (protect in revision)
2. Identifies **convergent criticism** — problems multiple personas flag (highest priority)
3. Identifies **divergent reactions** — where personas disagree (positioning decisions, not bugs)
4. Extracts the **strongest quote per persona** (one sentence each)
5. Produces a **priority action plan**: P0 (must fix), P1 (should fix), P2 (nice to have)
6. Delivers a **verdict**: ready for production, needs revision, or needs rethinking

### Agent locations

```
augmented-engineering/.claude/agents/
├── ae-review-orchestrator.md
├── ae-review-junior-dev.md
├── ae-review-team-lead.md
├── ae-review-skeptic.md
├── ae-review-educator.md
├── ae-review-podcast-listener.md
├── ae-review-indie-hacker.md
├── ae-review-content-creator.md
└── ae-review-non-technical-manager.md
```

### When to run

- After significant script revisions (not after every edit)
- Before audio production (final quality gate)
- When adding a new episode to the series

### Invocation

From the augmented-engineering repo: `run ae-review-orchestrator on podcast/dialogen/aug_01_context_engineering_dialogue.txt`

## Consequences

### Positive
- Catches issues that a single perspective misses — the first review round found 8 summarization violations, missing team perspective, and no moment of Marc being fallible
- Convergent criticism is high-signal: if four out of eight personas flag the same issue, it's real
- Divergent reactions reveal positioning tensions without forcing a resolution — "too technical" vs "not technical enough" is a choice, not a bug
- The strongest-quote-per-persona table is immediately useful for marketing and positioning
- Reusable across all future episodes

### Negative
- Eight parallel agents take several minutes and significant token usage
- Reviews can be contradictory — the orchestrator resolves this but it requires judgment
- Personas are synthetic, not real listeners — they may miss failure modes that actual humans would catch

### Risks
- Over-optimizing for the review battery instead of for real listeners. The battery is a proxy, not a substitute for actual audience feedback.
- Persona definitions may drift or become stale as the series evolves. Review and update persona prompts periodically.

## Evidence

The battery was run twice during the first session:
- **Round 1** (5 personas on v1 scripts): identified Lisa as summarizer, Marc as infallible, missing team perspective, missing proof points
- **Round 2** (8 personas on v3 scripts): validated P0 fix (Marc being wrong about teams), confirmed improvements, identified remaining trim opportunities

Key finding: convergent criticism was the strongest editing signal. Issues flagged by 4+ personas were always worth fixing. Issues flagged by 1 persona were often positioning choices.

## References

- augmented-engineering `.claude/agents/review-orchestrator.md` — the proposition review orchestrator (6 agents) that inspired this pattern
- augmented-engineering `REVIEW-SYNTHESIS.md` — evidence that parallel review produces high-signal feedback
