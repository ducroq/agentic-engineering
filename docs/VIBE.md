# VIBE — Augmented Engineering

Visual identity and design direction for the Augmented Engineering umbrella.

## Identity

Augmented Engineering is a tool umbrella for engineers working with AI agents. The brand communicates: **these are well-made tools you can trust, built by a practitioner who uses them.**

Not a research project. Not a startup. Not a framework vendor. A working engineer sharing durable tools.

## Three Pillars

**Engineered.** The design reflects the content — structured, precise, no wasted elements. Every visual choice has a reason. Color means something. Layout mirrors the thing it describes.

**Honest.** Limitations are visible, not hidden. Methodology is transparent. Evidence is shown, not claimed. The design doesn't oversell — it presents.

**Practitioner-first.** A working engineer should find what they need in seconds. Scannable tables over flowing prose. Situation-triggered navigation ("when X, do Y") over descriptive categories.

## Visual Direction

### Typography
- **Headings:** Clean sans-serif (Inter, system-ui). No display fonts, no handwriting fonts.
- **Body:** System serif or sans-serif. Readable at 16-18px, generous line height (1.6-1.7).
- **Code & data:** JetBrains Mono or similar monospace. Used for code blocks, CLI examples, and data values.
- **Hierarchy through weight and size, not font variety.** Two font families maximum.

### Color Palette
Semantic only — color always means something, never decorates.

| Role | Color | Usage |
|------|-------|-------|
| Text | Near-black on light background | Primary content |
| Secondary text | Muted gray | Subtitles, caveats, supporting content |
| Actionable | Green | "Try This Monday" boxes, things you can do now |
| Evidence | Blue | Data, findings, links |
| Caution | Amber/muted orange | Limitations, shelf-life warnings, caveats |
| Surface | White or near-white | Clean background, no texture |
| Borders | Light gray | Subtle structure, card edges, table lines |

No decorative color. No gradients. No colored backgrounds for sections.

### Layout
- **Max width:** 48-54rem for content. Generous margins.
- **Structure mirrors content:** Tables for decision rules. Cards for pattern summaries. Linear flow for methodology.
- **Whitespace is the primary design element.** Spacious but information-rich.
- **Mobile-first:** Single column that reads well on a phone.

### Visual Elements
- **No background textures.** Clean surface. The content is the texture.
- **No illustrations unless they carry information.** The SVG illustrations can stay if they communicate something a paragraph can't. But they should feel like diagrams, not drawings.
- **Minimal borders and shadows.** Structure through spacing, not decoration.
- **Tables are a first-class element.** Situation → pattern tables, evidence tables, comparison tables. Style them well — they do heavy lifting.

## Voice (Design Complement)

The writing voice is already right. The design should match it:

- **Direct.** Lead with the answer, not the context.
- **Evidence-visible.** Show the data that supports the claim, don't just assert.
- **Honest about scope.** Limitations and shelf-life stated plainly, not buried.
- **No marketing language.** No "revolutionary," "game-changing," "unlock." The tools speak through use.

## Reference Vibes

| Reference | What to take |
|-----------|-------------|
| Aegis (own) | Semantic color, monospace data, layered structure |
| Podcast-generator (own) | Linear flow, methodology-first, audio demos as proof |
| Energy/Augur (own) | Data transparency, honest limitations, technical credibility |
| Tailwind docs | Practitioner-friendly, pattern-first, scannable |
| Linear | Engineering-forward, clean, respects your time |

## Anti-Patterns

- **No handwriting fonts.** Warmth comes from voice, not typography.
- **No paper/notebook metaphors.** This is a workshop, not a journal.
- **No decorative color.** If a color doesn't encode meaning, remove it.
- **No hero images or banners.** Content starts immediately.
- **No "about the author" prominence.** The tools are the point, not the person.
- **No animations beyond subtle hover states.** Engineers distrust motion.

## Migration from Current Site

The current site (graph paper, Caveat font, pencil colors) served the "one researcher's field notes" phase. The new direction:

| Current | New |
|---------|-----|
| Caveat handwriting headings | Inter/system sans-serif |
| Graph paper background | Clean white surface |
| Pencil color palette (red, blue, green, orange) | Semantic-only palette |
| Evidence-box with blue left border | Keep — works well, just update colors |
| Monday-box with green border | Keep — the actionable highlight pattern is right |
| Caveat-box with dashed border | Keep — honest limitations pattern is right |
| Pattern cards with illustrations | Simplify — diagram-style or remove |
| "Nine projects" showcase | Gone (per ADR-005) |

The content structure (pattern library, quick reference table, problem → fix → evidence) is right. The visual skin needs to grow up to match the new identity.
