# Episode 01: Context Engineering — It Didn't Forget. It Never Knew.

**Series:** Agentic Engineering: the craft, not the hype
**Duration:** ~22 minutes
**Cast:** Lisa (host), Marc (expert), Sven (skeptic)

## Summary

Sven's agent deletes the audit log. Again. Marc explains why: the agent never received Sven's instructions from previous sessions. The episode introduces the auto-loading cliff, task-triggered pointers, the four-layer documentation model, and the self-learning loop. Sven raises three real objections. Marc admits his own failures (300-line cage, 75 hidden memory files). Lisa connects the patterns to team onboarding and knowledge management.

## Key claims made in this episode

| # | Claim | Speaker | Line | Confidence | Source |
|---|-------|---------|------|------------|--------|
| C1 | Agent sessions start with zero memory of previous sessions | Marc | 27 | ESTABLISHED | By design: LLM context windows are ephemeral. Confirmed in Anthropic (2026) "Effective Context Engineering for AI Agents" and all major tool documentation. |
| C2 | There's a hard boundary (auto-loading cliff) between auto-loaded and invisible content | Marc | ~39 | ESTABLISHED | Documented in agent-ready-projects v1.2.0 (Veen 2026). Confirmed by tool documentation: Claude Code auto-loads CLAUDE.md and MEMORY.md; Cursor loads .mdc files; Codex loads AGENTS.md. Content not in these files requires explicit agent action to access. |
| C3 | Claude Code loads CLAUDE.md, Cursor uses .mdc files, Codex reads AGENTS.md | Marc | ~47 | ESTABLISHED | Tool documentation: Anthropic Claude Code docs, Cursor docs (.cursor/rules/*.mdc), OpenAI Codex docs (AGENTS.md). Windsurf uses .windsurfrules. |
| C4 | Project file is approximately fifty lines | Marc | ~67-71 | SUPPORTED | agent-ready-projects worked example (docs/EXAMPLE.md): ~50 lines. Template (templates/project-file.md): ~72 lines including comments. Framework recommends 150 lines as warning threshold. "Fifty" is a ballpark, not a specification. |
| C5 | Self-learning loop: capture, surface, promote, retire | Marc | ~87 | ESTABLISHED | Documented in agent-ready-projects v1.0.0+ (README.md, lines 351+). Lifecycle validated across multiple projects (driven-pendulum, agent-ready-papers, ovr.news). |
| C6 | Seventy-five memory files accumulated across twenty-eight projects in hidden auto-memory | Marc | ~new | ESTABLISHED | Author's own experience, documented in agent-ready-projects ADR-001 (2026-03-19). Migration performed and verified in a single session. |
| C7 | Agents sometimes miss instructions, especially under context compression | Marc | ~111 | SUPPORTED | Known behavior documented by Anthropic (2026) "Effective Context Engineering": context compression can cause older content to lose fidelity. Not formally quantified in public literature. Widely reported by practitioners. |
| C8 | Three-hundred-line project file caused agent to become overly cautious | Marc | ~cage section | SUPPORTED | Author's own experience. Consistent with context economics: excessive auto-loaded content reduces available context for the task. Documented in agent-ready-projects README (150-line heuristic). |
| C9 | Forty-seven percent of organizations report negative consequences from AI use | Marc/Lisa | ~new | ESTABLISHED | McKinsey Global Survey 2025. |
| C10 | Only twenty percent of engineering organizations can measure AI's actual impact | Marc | ~new | ESTABLISHED | Jellyfish 2025 "State of Software Engineering Teams". |
| C11 | Code tells the agent what IS, not what must NEVER BE | Marc | ~code objection | SUPPORTED | Logical argument, not empirical claim. Constraints, rationale, and prohibitions are not expressible in source code alone. Consistent with software engineering literature on documentation vs. implementation. |

## Claim verification status

- **ESTABLISHED** (7): C1, C2, C3, C5, C6, C9, C10
- **SUPPORTED** (4): C4, C7, C8, C11
- **EMERGING** (0)
- **SPECULATIVE** (0)

Coverage: 11/11 verified = **100%**

## References

### Tool Documentation
- Anthropic. (2026). *Claude Code Documentation*. CLAUDE.md auto-loading behavior.
- Anthropic. (2026). *Effective Context Engineering for AI Agents*. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic. (2026). *Effective Harnesses for Long-Running Agents*. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Cursor. (2026). *Rules Documentation*. .cursor/rules/*.mdc format.
- OpenAI. (2026). *Codex Documentation*. AGENTS.md convention.

### Industry Surveys
- McKinsey & Company. (2025). *The State of AI: Global Survey*. 47% negative consequences.
- Jellyfish. (2025). *State of Software Engineering Teams*. 20% can measure AI impact.

### Framework (Own Work)
- Veen, J. (2026). *agent-ready-projects* v1.2.0. GitHub. Auto-loading cliff, four-layer model, self-learning loop.
- Veen, J. (2026). *ADR-001: In-Repo Memory Over Auto-Memory*. agent-ready-projects/docs/decisions/.
- Veen, J. (2026). *The AI-Augmented Engineer*. Internal research report v1.2, HAN University.

### Case Studies (Own Work)
- Veen, J. (2026). OPAL: AI-Augmented Design Review. HAN University.
- Veen, J. (2026). agent-ready-projects: adoption across 28 projects. HAN University.

## Show notes (listener-facing)

**What this episode covers:**
- Why your agent "forgets" everything between sessions — and why that's by design
- The auto-loading cliff: the hard boundary between what agents see and what's invisible
- The four layers: project file, runbook, memory index, gotcha log
- Three objections tested: "just write docs," "code should speak for itself," "enterprise overhead"
- Why hidden memory files don't get maintained — visibility forces curation
- The global file cliff: project-specific context burning tokens everywhere

**Key stats mentioned:**
- 47% of organizations report negative consequences from AI use (McKinsey 2025)
- Only 20% can measure AI's actual impact (Jellyfish 2025)

**Try this tomorrow:**
1. Open your tool's auto-loaded file (CLAUDE.md, .cursor/rules, AGENTS.md)
2. Write one line describing your project
3. Add three to five hard constraints — things the agent must never do
4. Add a "before you start" table mapping common tasks to relevant docs
5. Create an empty gotcha log file in your repo (not a hidden directory)

**Links:**
- agent-ready-projects framework: [GitHub link]
- ADR-001: In-Repo Memory Over Auto-Memory: [GitHub link]
- Anthropic: Effective Context Engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- McKinsey State of AI 2025: [link]

**Next episode:** Learn the Material — what happens when the agent reads all your instructions and still gets it confidently wrong.
