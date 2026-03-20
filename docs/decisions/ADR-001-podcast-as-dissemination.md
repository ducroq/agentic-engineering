# ADR-001: Podcast as Dissemination Channel

**Date:** 2026-03-19
**Status:** Accepted

## Context

The agentic-engineering project contains a research proposition ("what's genuinely new when engineers work with AI agents"), five case studies, a claim registry, and a six-agent review synthesis. The work is grounded in nine real projects but limited to one practitioner (N=1). It needs to reach practitioners, educators, and teams — not just readers of long markdown documents.

Options considered:
1. **Blog posts** — Addy Osmani's approach. Good reach, but saturated space and lacks the conversational depth to explore nuance.
2. **Academic paper** — already in progress via agent-ready-papers. Slow, limited audience, doesn't reach practitioners.
3. **Conference talks** — one-shot, no continuity, no community building.
4. **Podcast series** — sustained engagement, narrative format, builds audience over time, natural funnel for tandemize.ai.

## Decision

Create a podcast series: **Agentic Engineering: the craft, not the hype.**

### Format: three voices

| Role | Character | Function |
|------|-----------|----------|
| Host / audience proxy | Lisa | Asks the questions listeners are thinking. Brings team/management perspective. Bridges to universal human experience. |
| Expert / practitioner | Marc | Carries the knowledge. Admits limitations. Shares failures. |
| Skeptic / student | Sven | Pushes back. Raises objections. Represents junior developers and doubters. |

**Why three voices, not two or one:**
- Two-voice (interview) collapses into softball questions. The host has no reason to push back.
- One-voice (monologue) is a lecture. No friction, no surprise.
- Three voices create a natural triangle: Marc explains, Sven challenges, Lisa contextualizes. The listener identifies with whichever role matches their mood.

### Scripts live in this repo, not podcast-generator

The scripts are part of the agentic-engineering project — they're a way of presenting the research, not a separate podcast project. Production tooling (TTS engines, voice library, mastering pipeline) lives in podcast-generator. Content (scripts, show notes, claim verification, research) lives here.

```
agentic-engineering/
├── podcast/
│   ├── dialogen/      # Scripts
│   ├── shownotes/     # Claim verification + references + listener-facing notes
│   ├── productie/     # Generated audio
│   └── onderzoek/     # Episode research
```

### Funnel for tandemize.ai

The podcast serves as top-of-funnel for tandemize.ai, a planned consulting business around agentic engineering. The funnel is natural, not forced: episodes that expose problems individuals can't solve alone (team scaling, verification at scale) lead listeners toward wanting professional help.

### Growth path

- **N=1 now**: Marc and Sven are the creator split into two voices. Authentic starting point.
- **N=3-5 soon**: Friends and collaborators join as guests with their own projects and failures.
- **N=many later**: Listener stories, community contributions, the podcast becomes a platform.

## Consequences

### Positive
- Reaches practitioners who won't read a 10,000-word proposition
- Sustained engagement across episodes — each one builds on the last
- Three-voice format allows nuance, disagreement, and honesty
- Natural content marketing for tandemize.ai without being a sales pitch
- The review battery (8 personas) ensures quality before production

### Negative
- Production overhead: scripting, TTS generation, DAW mixing, mastering per episode
- Three-voice scripting is harder than blog posts — every line must serve character AND content
- Audio format can't be skimmed — listeners commit 20 minutes or skip entirely

### Risks
- N=1 limits credibility long-term. Mitigated by the growth path (guests, community).
- TTS-generated audio may not match the quality expectations of podcast listeners used to human hosts. Mitigated by strong scripting and post-production (overlap markers, silence trimming, mastering).

## References

- agentic-engineering `PROPOSITION.md` — the research this podcast disseminates
- agentic-engineering `memory/project_ae_podcast_marketing.md` — positioning and competitive landscape
- podcast-generator ADR-001: Dialogue writing style for local TTS
- podcast-generator ADR-002: Local TTS for Agentic Engineering series
