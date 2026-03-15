# agent-ready-projects: The Auto-Loading Cliff

**Domain:** Meta/methodology — structuring projects for effective AI agent collaboration
**Pattern:** Context engineering — what agents load automatically determines what they know; everything below the auto-loading cliff is effectively invisible unless triggered

---

## 1. What Was Built

agent-ready-projects is a prescriptive guide for structuring software projects so AI coding agents (Claude Code, Cursor, Windsurf, Copilot, etc.) work effectively across sessions. The core problem: agents restart cold every session. They don't remember yesterday's architectural decisions, failed approaches, or corner cases already discovered. Developers end up repeating context, redirecting agents to critical files, or watching them redo mistakes.

The guide emerged from 100+ agent sessions across multiple real projects, refined through multi-agent audits where independent agents reviewed different projects against the framework and provided converging feedback.

---

## 2. How the Agents Were Used

This case study is different from the others — the "agentic workflow" here is the agents using the framework, not agents building something. The development process itself was agentic:

**Phase 1: Pattern extraction.** Observations from 100+ sessions distilled into an initial model. Common complaints: "I already told you this," "go read X first," "we decided not to do that last session."

**Phase 2: Apply to real projects.** The model was tested on a real project. Key discovery: the **auto-loading cliff** — the hard boundary between content agents load automatically (CLAUDE.md, project instructions) and content that's effectively invisible unless explicitly triggered. "Linked prominently from CLAUDE.md" is *not* a trigger. Agents skim past links unless a task-specific need activates them.

**Phase 3: Multi-agent audit.** Three independent agents audited three different project types (editorial platform, data pipeline, deployment platform) against the guide. Converging feedback:

- Duplication isn't always bad — same fact framed differently for different purposes (a constraint in CLAUDE.md, an operational reminder in the runbook) serves different cognitive moments
- Line-count targets are wrong — what matters is context budget per session, not line count
- Cross-project knowledge has no natural home — interface docs should live where they're needed, not where they originate
- The guide's own example violated its own advice (used descriptive labels instead of task triggers)

All feedback was applied to v1.0.0.

---

## 3. What Worked

**Task-triggered pointers cross the cliff.** The breakthrough was replacing descriptive labels with task-specific triggers:

```
Bad:  | API troubleshooting | docs/api-quirks.md |
Good: | API returns 422     | docs/api-quirks.md — validation edge cases |
```

The difference: "API troubleshooting" is a category the agent has to decide is relevant. "API returns 422" is a situation the agent recognizes it's in. This is the difference between a library index and a decision table.

**The self-learning loop keeps context fresh.** Four phases: Capture (log problems as they happen) → Surface (identify recurring patterns at end of session) → Promote (move frequent gotchas up the visibility stack) → Retire (mark resolved issues, prune stale knowledge). This turns context management from a one-time documentation effort into a living process.

Example lifecycle: "Staging migrations time out" logged in gotcha-log → recurs twice → promoted to infrastructure topic file as "if staging migrations time out, run with `--lock-timeout=60s`" → database moved to dedicated instance → marked [RESOLVED].

**The processor memory hierarchy analogy clicked.** Mapping agent context to CPU memory hierarchy (registers = project file, L1 = memory index, L2/L3 = topic files, RAM = gotcha log, disk = git history) gave practitioners an intuitive framework for deciding where information should live. The key principle transfers: **miss cost asymmetry** — a lesson missing from auto-loaded context costs the full debugging time to rediscover.

**Layered model scales with project complexity.** Four layers, each added when the previous one gets crowded:
1. Project file (always) — identity, hard constraints, task-triggered pointers
2. Runbook (most projects) — operational detail that would clutter the project file
3. Memory + topic files (complex projects) — deep knowledge organized by domain
4. Gotcha log (always) — problem/solution journal

---

## 4. What Didn't Work

**Static documentation fails silently.** The initial model treated context as a documentation problem — write good docs and agents will use them. Wrong. Good docs that are never loaded are worthless. The auto-loading cliff was discovered because a thorough, well-written runbook was being completely ignored by agents. The problem wasn't content quality; it was content *placement*.

**Over-promoting creates noise.** Early versions promoted gotchas too aggressively — every recurring issue moved to always-loaded context. This polluted the project file with low-relevance warnings. The fix: require 2-3 recurrences before promotion, and add a retirement pattern (promotion without retirement turns the project file into a museum).

**"Constitution" without operational context is ignored.** High-level principles ("we value simplicity," "pipeline reliability > feature richness") have no effect unless connected to operational decisions. An agent reading "we value simplicity" won't change its behavior. An agent reading "when choosing between approaches, pick the one with fewer moving parts — we got burned by over-engineering the auth layer" will.

**Cross-repo knowledge has no natural home.** When repos have producer/consumer relationships, interface documentation drifts. Two audit agents independently flagged this. The pragmatic answer: store facts where they're needed, not where they originate — even if this creates duplication.

---

## 5. The Pattern

> **When** working with AI agents across multiple sessions on a codebase,
> **use** layered context with task-triggered pointers: put identity and hard constraints in the auto-loaded project file, put operational detail in on-demand documents, and bridge them with pointers that activate when the agent recognizes a specific task — not descriptive labels it has to interpret,
> **because** agents don't browse documentation; they respond to situational triggers — and everything below the auto-loading cliff is invisible unless something pulls it into context.

The auto-loading cliff is structural, not tool-specific. Every AI coding tool has it: CLAUDE.md for Claude Code, .cursor/rules for Cursor, AGENTS.md for Codex. The specific boundary differs but the dynamic is the same.

The deeper insight: **documentation quality for AI agents is measured by self-navigation, not accuracy.** A perfectly accurate doc that no agent ever reads is worse than an approximate pointer that triggers the right lookup at the right time.

**When this pattern doesn't apply:**
- One-off scripts or throwaway projects where session continuity doesn't matter
- Projects small enough that the entire codebase fits in context — no need for progressive disclosure if everything is always visible
- Teams where human developers do all the context management and agents are used for isolated tasks

---

## 6. Limitations

The framework was developed and tested by one researcher across their own projects. "Projects adopting the framework report productive sessions" is observational — there's no controlled comparison between projects with and without context engineering. The multi-agent audit provides some external validation (three independent agents converged on similar feedback) but all agents were prompted by the same researcher.

The auto-loading cliff concept is consistent with cognitive science work on environmental cues and situated cognition (Suchman, 1987; Hutchins, 1995) and with the information foraging literature on how agents decide which information to pursue (Pirolli & Card, 1999). The processor memory hierarchy analogy maps to established computer architecture principles. But the specific application to AI coding agents is novel and has not been independently studied.
