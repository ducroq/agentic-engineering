# Architecture Decision Records

Significant choices between approaches, with context, consequences, and alternatives.

## Index

| ADR | Status | Decision |
|-----|--------|----------|
| [ADR-001](ADR-001-podcast-as-dissemination.md) | Accepted | Podcast as primary dissemination channel for the four patterns |
| [ADR-002](ADR-002-claim-verification-for-podcast.md) | Accepted | Claim verification gates before podcast scripts go to production |
| [ADR-003](ADR-003-eight-persona-review-battery.md) | Accepted | Eight-persona review battery for podcast script quality |
| [ADR-004](ADR-004-site-as-pattern-library.md) | Accepted | Reframe website as pattern library, not research portfolio |
| [ADR-005](ADR-005-umbrella-not-proposition.md) | Accepted | Augmented Engineering is a tool umbrella, not a research proposition |
| [ADR-006](ADR-006-only-durable-patterns.md) | Accepted | Only structural (durable) patterns are core; model-dependent ones are advisory |
| [ADR-007](ADR-007-umbrella-follows-tools.md) | Accepted | Don't build the umbrella ahead of the tools |

## When to Write an ADR

- Choosing between two or more viable approaches
- Adopting a convention that isn't obvious from the code
- Rejecting an approach that seems natural (document why not)

## Template

```markdown
# ADR-NNN: [Title]

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Superseded by ADR-NNN

## Context
Why we faced this choice.

## Decision
What we chose.

## Consequences
Positive and negative effects.

## Alternatives Considered
What else we considered and why we rejected it.
```
