# ADR-002: Claim Verification for Podcast Scripts

**Date:** 2026-03-19
**Status:** Accepted

## Context

Podcast scripts contain factual claims — statistics, research findings, case study results. Unlike blog posts or papers, audio content can't be footnoted inline. A listener hearing "forty-seven percent of organizations report negative consequences" has no way to verify that claim in the moment. If the number is wrong, the podcast loses credibility. If it's right but unsourced, it's indistinguishable from made-up statistics.

The augmented-engineering project already uses typed claim verification (via agent-ready-papers) for written work. The podcast needs an equivalent system adapted for audio.

## Decision

Every podcast episode has a **show notes file** that serves as the verification record. The show notes contain:

### 1. Claim verification table

Every factual claim in the script is tracked:

| # | Claim | Speaker | Confidence | Source |
|---|-------|---------|------------|--------|
| C1 | 90% of dev teams use AI daily | Lisa | ESTABLISHED | Stack Overflow 2025 (65K), JetBrains 2025 (24.5K), Jellyfish 2025 |
| C2 | Only 3-8% fully trust output | Lisa | ESTABLISHED | Stack Overflow 2025: 3%; JetBrains 2025: 8% |

**Confidence tiers** (from agent-ready-papers):
- **ESTABLISHED** — multiple independent sources or directly verifiable
- **SUPPORTED** — strong single source with corroborating evidence
- **EMERGING** — preliminary evidence, stated with appropriate hedging
- **SPECULATIVE** — hypothesis, clearly flagged

**Coverage target**: 100% of factual claims verified before production. No unverified statistics in produced audio.

### 2. Full reference list

Every source cited in the verification table gets a proper reference: author, year, title, URL or DOI where available. Organized by type (industry surveys, academic sources, case studies).

### 3. Listener-facing show notes

A plain-language summary for listeners: what the episode covers, key stats mentioned with sources, actionable next steps, and links to referenced materials.

### File location

```
augmented-engineering/podcast/shownotes/
├── aug_00_introduction.md
├── aug_01_context_engineering.md
└── aug_02_material_properties.md   # (future)
```

### Workflow

1. **During scripting**: when a stat is added to the script, add it to the claim table immediately with its source.
2. **Before production**: verify 100% coverage. No claim without a source.
3. **After production**: publish show notes alongside the episode.

## Consequences

### Positive
- Every claim is traceable — if challenged, the source is one click away
- Forces discipline during scripting: you can't casually drop a number without knowing where it came from
- Show notes become a valuable resource on their own — listeners bookmark them
- Prevents the most common AI podcast failure: confident-sounding unsourced claims

### Negative
- Adds time to the scripting process — every stat needs to be looked up and verified
- Some powerful claims may be dropped because the source doesn't meet the confidence threshold
- Show notes require maintenance if sources update or retract

### Risks
- Claim verification creates a false sense of rigor if applied mechanically. "ESTABLISHED" means "multiple sources say this" — not "this is definitely true." The confidence tiers communicate certainty, they don't guarantee it.

## References

- agent-ready-papers `templates/claim-registry.md` — the source pattern for typed verification
- agent-ready-papers `templates/writing-guide.md` — confidence tier to language mapping
- augmented-engineering `podcast/shownotes/aug_00_introduction.md` — first implementation
- augmented-engineering `podcast/shownotes/aug_01_context_engineering.md` — second implementation
