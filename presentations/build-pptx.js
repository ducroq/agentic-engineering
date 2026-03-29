const pptxgen = require("pptxgenjs");
const path = require("path");

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Scott Bryan";
pres.title = "AI for Engineers: Understanding Before Using";

// HAN brand colors from theme
const C = {
  black: "000000",
  white: "FFFFFF",
  bg: "F8F8F8",       // light gray background
  magenta: "E50056",   // HAN accent
  dk_gray: "454545",
  md_gray: "757575",
  lt_gray: "E3E3E3",
  card_gray: "F2F2F2",
};

// HAN fonts
const HEADER_FONT = "Avenir Next Condensed Medium";
const BODY_FONT = "Arial";

// Helper: section divider slide (dark bg)
function addSectionSlide(title, subtitle) {
  const slide = pres.addSlide();
  slide.background = { color: C.black };
  // Magenta accent bar at top
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.06, fill: { color: C.magenta }
  });
  slide.addText(title, {
    x: 0.8, y: 1.5, w: 8.4, h: 1.5,
    fontFace: HEADER_FONT, fontSize: 40, color: C.white, bold: true
  });
  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.8, y: 3.0, w: 8.4, h: 1.0,
      fontFace: BODY_FONT, fontSize: 18, color: C.md_gray
    });
  }
}

// Helper: content slide with title
function addContentSlide(title) {
  const slide = pres.addSlide();
  slide.background = { color: C.bg };
  // Magenta accent bar at top
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.04, fill: { color: C.magenta }
  });
  // Title
  slide.addText(title, {
    x: 0.8, y: 0.3, w: 8.4, h: 0.7,
    fontFace: HEADER_FONT, fontSize: 28, color: C.black, bold: true
  });
  return slide;
}

// Helper: audience question slide
function addQuestionSlide(question) {
  const slide = pres.addSlide();
  slide.background = { color: C.white };
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.04, fill: { color: C.magenta }
  });
  slide.addText("?", {
    x: 0.8, y: 0.8, w: 1.2, h: 1.2,
    fontFace: HEADER_FONT, fontSize: 72, color: C.magenta, bold: true, align: "center"
  });
  slide.addText(question, {
    x: 2.2, y: 0.8, w: 7.0, h: 1.5,
    fontFace: BODY_FONT, fontSize: 20, color: C.dk_gray, italic: true, valign: "middle"
  });
  slide.addText("AUDIENCE QUESTION", {
    x: 0.8, y: 4.8, w: 3, h: 0.4,
    fontFace: BODY_FONT, fontSize: 10, color: C.md_gray, bold: true
  });
}

// Helper: key line / quote slide
function addQuoteSlide(quote, source) {
  const slide = pres.addSlide();
  slide.background = { color: C.black };
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.06, fill: { color: C.magenta }
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.8, y: 1.8, w: 0.06, h: 2.0, fill: { color: C.magenta }
  });
  slide.addText(quote, {
    x: 1.2, y: 1.8, w: 7.8, h: 2.0,
    fontFace: BODY_FONT, fontSize: 22, color: C.white, italic: true, valign: "middle"
  });
  if (source) {
    slide.addText(source, {
      x: 1.2, y: 4.0, w: 7.8, h: 0.5,
      fontFace: BODY_FONT, fontSize: 12, color: C.md_gray
    });
  }
}

// ======================================================================
// SLIDE 1: TITLE
// ======================================================================
const s1 = pres.addSlide();
s1.background = { color: C.black };
s1.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0, w: 10, h: 0.06, fill: { color: C.magenta }
});
s1.addText("AI for Engineers", {
  x: 0.8, y: 1.2, w: 8.4, h: 1.2,
  fontFace: HEADER_FONT, fontSize: 48, color: C.white, bold: true
});
s1.addText("Understanding Before Using", {
  x: 0.8, y: 2.3, w: 8.4, h: 0.8,
  fontFace: HEADER_FONT, fontSize: 32, color: C.magenta
});
s1.addText("Digital Engineers Research Team | March 2026", {
  x: 0.8, y: 4.5, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 14, color: C.md_gray
});

// ======================================================================
// PART 0: What Are We Actually Talking About?
// ======================================================================
addSectionSlide("What Are We Actually\nTalking About?", "A 60-second stack, bottom to top");

// Slide: The AI Stack
const s_stack = addContentSlide("The AI Stack");
const stackItems = [
  { label: "Machine Learning", desc: "Software that learns patterns from data instead of following hand-written rules", y: 3.8, color: C.lt_gray },
  { label: "Deep Learning", desc: "ML with many layers of neurons. The 'deep' is literally 'more layers'", y: 2.8, color: C.lt_gray },
  { label: "Large Language Models", desc: "Deep learning trained on text. A very sophisticated pattern completer", y: 1.8, color: C.card_gray },
  { label: "AI Agents", desc: "LLMs in a loop: read context, decide, use tools, check result, repeat", y: 0.8, color: C.card_gray },
];
// Draw stacked boxes bottom to top
stackItems.forEach((item, i) => {
  const boxY = 1.2 + (3 - i) * 1.05;
  s_stack.addShape(pres.shapes.RECTANGLE, {
    x: 0.8, y: boxY, w: 4.0, h: 0.9,
    fill: { color: item.color },
    line: { color: C.lt_gray, width: 1 }
  });
  s_stack.addText(item.label, {
    x: 1.0, y: boxY + 0.05, w: 3.6, h: 0.4,
    fontFace: HEADER_FONT, fontSize: 16, color: C.black, bold: true, margin: 0
  });
  s_stack.addText(item.desc, {
    x: 5.2, y: boxY, w: 4.4, h: 0.9,
    fontFace: BODY_FONT, fontSize: 13, color: C.dk_gray, valign: "middle"
  });
});

// Key point
s_stack.addText("An agent is only as good as the model inside it, and the model is a pattern completer.", {
  x: 0.8, y: 5.0, w: 8.4, h: 0.4,
  fontFace: BODY_FONT, fontSize: 12, color: C.magenta, bold: true
});

addQuestionSlide("Who here has used ChatGPT or Copilot? Who has used it for something beyond a simple question \u2014 generating code, writing a report, analyzing data?");

// ======================================================================
// PART 1: THE PROBLEM
// ======================================================================
addSectionSlide("Part 1: The Problem", "What happens when engineers use AI?");

// Slide: The Uncomfortable Numbers
const s_nums = addContentSlide("The Uncomfortable Numbers");
const stats = [
  { num: "84-90%", label: "of software dev teams\nuse AI daily" },
  { num: "47%", label: "experienced negative\nconsequences" },
  { num: "96%", label: "don't fully trust AI,\nyet only 48% verify" },
];
stats.forEach((stat, i) => {
  const x = 0.8 + i * 3.1;
  s_nums.addShape(pres.shapes.RECTANGLE, {
    x: x, y: 1.3, w: 2.8, h: 2.4,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.08 }
  });
  s_nums.addText(stat.num, {
    x: x, y: 1.5, w: 2.8, h: 1.0,
    fontFace: HEADER_FONT, fontSize: 36, color: C.magenta, bold: true, align: "center"
  });
  s_nums.addText(stat.label, {
    x: x + 0.2, y: 2.6, w: 2.4, h: 0.9,
    fontFace: BODY_FONT, fontSize: 13, color: C.dk_gray, align: "center"
  });
});
s_nums.addText("Experience reveals problems rather than building confidence. The opposite of normal technology adoption.", {
  x: 0.8, y: 4.2, w: 8.4, h: 0.6,
  fontFace: BODY_FONT, fontSize: 14, color: C.black, bold: true
});
s_nums.addText("Sources: Stack Overflow, JetBrains, McKinsey 2025, Sonar 2026", {
  x: 0.8, y: 5.0, w: 8.4, h: 0.3,
  fontFace: BODY_FONT, fontSize: 10, color: C.md_gray
});

// Slide: The Productivity Paradox
const s_paradox = addContentSlide("The Productivity Paradox");
const paradoxData = [
  [
    { text: "Context", options: { bold: true, color: C.white, fill: { color: C.black } } },
    { text: "Impact", options: { bold: true, color: C.white, fill: { color: C.black } } },
    { text: "Source", options: { bold: true, color: C.white, fill: { color: C.black } } },
  ],
  [
    { text: "Lab (simple tasks)" },
    { text: "+55.8% faster", options: { bold: true, color: "2E7D32" } },
    { text: "Peng et al. 2023" },
  ],
  [
    { text: "Enterprise deployment" },
    { text: "+8.69%\n(+16% more build failures)", options: { bold: true, color: "E65100" } },
    { text: "Accenture 2024" },
  ],
  [
    { text: "Experienced devs, real codebases" },
    { text: "-19% slower", options: { bold: true, color: C.magenta } },
    { text: "METR 2025" },
  ],
];
s_paradox.addTable(paradoxData, {
  x: 0.8, y: 1.3, w: 8.4,
  colW: [3.5, 2.8, 2.1],
  border: { pt: 0.5, color: C.lt_gray },
  fontFace: BODY_FONT, fontSize: 14,
  rowH: [0.5, 0.5, 0.7, 0.5],
});
s_paradox.addText("19% slower with AI while perceiving themselves 20% faster.", {
  x: 0.8, y: 3.8, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 16, color: C.black, bold: true
});
s_paradox.addText("A 39-percentage-point perception gap.", {
  x: 0.8, y: 4.2, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 16, color: C.magenta, bold: true
});

addQuoteSlide("AI makes easy things easier.\nBut engineering is rarely easy.", null);

addQuestionSlide("Show of hands \u2014 who uses AI tools in their daily work? And who has a systematic way of checking whether the output is correct?");

// Slide: Beyond Software
const s_beyond = addContentSlide("Beyond Software: \"Real\" Engineering");
const domains = [
  { domain: "Chemical (HAZOP)", result: ">86% textual similarity but only 19-37% semantically valid", source: "Park et al. 2025" },
  { domain: "Civil (FE exam)", result: "0% on Structural Design, 100% on Ethics", source: "Naser et al. 2023" },
  { domain: "Mechanical", result: "47-60% on core ME problems", source: "Akolekar et al. 2025" },
  { domain: "Electrical (PCB)", result: "AI hallucinated electronic components", source: "JITX 2024" },
];
domains.forEach((d, i) => {
  const y = 1.3 + i * 0.95;
  // Left accent bar
  s_beyond.addShape(pres.shapes.RECTANGLE, {
    x: 0.8, y: y, w: 0.06, h: 0.8, fill: { color: C.magenta }
  });
  s_beyond.addText(d.domain, {
    x: 1.1, y: y, w: 2.6, h: 0.8,
    fontFace: HEADER_FONT, fontSize: 14, color: C.black, bold: true, valign: "middle"
  });
  s_beyond.addText(d.result, {
    x: 3.8, y: y, w: 4.5, h: 0.55,
    fontFace: BODY_FONT, fontSize: 13, color: C.dk_gray, valign: "middle"
  });
  s_beyond.addText(d.source, {
    x: 3.8, y: y + 0.5, w: 4.5, h: 0.3,
    fontFace: BODY_FONT, fontSize: 10, color: C.md_gray
  });
});
s_beyond.addText("Pattern: AI produces outputs that look professionally competent but contain errors only domain experts catch.", {
  x: 0.8, y: 5.0, w: 8.4, h: 0.4,
  fontFace: BODY_FONT, fontSize: 12, color: C.magenta, bold: true
});

addQuestionSlide("Has anyone here encountered AI output that looked correct at first glance but turned out to be wrong? What tipped you off?");

// ======================================================================
// PART 2: THE FOUR PATTERNS
// ======================================================================
addSectionSlide("Part 2: Four Patterns", "What's genuinely new when engineers work with AI agents?");

// Slide: Pattern 1 - Learn the Material
const s_p1 = addContentSlide("Pattern 1: Learn the Material");
s_p1.addText("LLMs have behavioral properties, like material properties in physical engineering.", {
  x: 0.8, y: 1.2, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 15, color: C.dk_gray
});
const props = [
  [
    { text: "Property", options: { bold: true, color: C.white, fill: { color: C.black } } },
    { text: "Example", options: { bold: true, color: C.white, fill: { color: C.black } } },
    { text: "Persistent?", options: { bold: true, color: C.white, fill: { color: C.black } } },
  ],
  ["Confident but wrong", "6/22 claims over-confident", { text: "Yes", options: { bold: true } }],
  ["Can observe, can't score", "Sees table, scores structure=1", { text: "Yes", options: { bold: true } }],
  ["Plausible-but-wrong output", "Right units, right magnitude, wrong answer", { text: "Fading", options: { color: C.md_gray } }],
  ["Scores regress to mean", "High work scored low, low scored high", { text: "Fading", options: { color: C.md_gray } }],
];
s_p1.addTable(props, {
  x: 0.8, y: 1.9, w: 8.4,
  colW: [2.8, 3.6, 2.0],
  border: { pt: 0.5, color: C.lt_gray },
  fontFace: BODY_FONT, fontSize: 13,
  rowH: [0.45, 0.45, 0.45, 0.45, 0.45],
});
s_p1.addText([
  { text: "You wouldn't use steel without knowing its fatigue properties. ", options: {} },
  { text: "Don't use LLMs without knowing theirs.", options: { bold: true, color: C.magenta } }
], {
  x: 0.8, y: 4.6, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 15
});

addQuestionSlide("When you use a new material or tool for the first time \u2014 how do you learn its limits? Do you do the same with AI?");

// Slide: Pattern 2 - Layer Your Verification
const s_p2 = addContentSlide("Pattern 2: Layer Your Verification");
s_p2.addText("V&V is old. V&V that costs minutes instead of months is new.", {
  x: 0.8, y: 1.2, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 15, color: C.dk_gray
});
// Big numbers
const vvStats = [
  { num: "5", label: "verification\nlayers" },
  { num: "10", label: "defects\nfound" },
  { num: "8", label: "missed by\nlayer 1 alone" },
  { num: "0", label: "false\npositives" },
];
vvStats.forEach((s, i) => {
  const x = 0.8 + i * 2.2;
  s_p2.addShape(pres.shapes.RECTANGLE, {
    x: x, y: 1.9, w: 2.0, h: 2.0,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.08 }
  });
  s_p2.addText(s.num, {
    x: x, y: 2.0, w: 2.0, h: 1.0,
    fontFace: HEADER_FONT, fontSize: 48, color: C.magenta, bold: true, align: "center"
  });
  s_p2.addText(s.label, {
    x: x + 0.1, y: 3.0, w: 1.8, h: 0.7,
    fontFace: BODY_FONT, fontSize: 12, color: C.dk_gray, align: "center"
  });
});
s_p2.addText("OPAL PCB Design Review", {
  x: 0.8, y: 4.1, w: 8.4, h: 0.3,
  fontFace: BODY_FONT, fontSize: 10, color: C.md_gray
});
s_p2.addText("When verification is cheap, layer it. Run another pass. Audit the auditors.", {
  x: 0.8, y: 4.5, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 15, color: C.black, bold: true
});

addQuestionSlide("In your domain, how many independent checks does a design go through before it ships? What if you could add five more checks for the cost of a coffee?");

// Slide: Pattern 3 - Context Is Architecture
const s_p3 = addContentSlide("Pattern 3: Context Is Architecture");
s_p3.addText("Agents have an auto-loading cliff: what's loaded gets used; everything else is invisible.", {
  x: 0.8, y: 1.2, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 15, color: C.dk_gray
});
// Visual: cliff diagram
s_p3.addShape(pres.shapes.RECTANGLE, {
  x: 0.8, y: 2.0, w: 4.0, h: 1.2,
  fill: { color: C.white },
  line: { color: C.lt_gray, width: 1 }
});
s_p3.addText("Above the cliff (auto-loaded)", {
  x: 1.0, y: 2.0, w: 3.6, h: 0.4,
  fontFace: BODY_FONT, fontSize: 11, color: C.magenta, bold: true
});
s_p3.addText("Agent sees this, acts on it", {
  x: 1.0, y: 2.4, w: 3.6, h: 0.6,
  fontFace: BODY_FONT, fontSize: 13, color: C.dk_gray
});
// Cliff line
s_p3.addShape(pres.shapes.LINE, {
  x: 0.8, y: 3.3, w: 4.0, h: 0,
  line: { color: C.magenta, width: 3, dashType: "dash" }
});
s_p3.addShape(pres.shapes.RECTANGLE, {
  x: 0.8, y: 3.4, w: 4.0, h: 1.2,
  fill: { color: C.lt_gray },
  line: { color: C.lt_gray, width: 1 }
});
s_p3.addText("Below the cliff", {
  x: 1.0, y: 3.4, w: 3.6, h: 0.4,
  fontFace: BODY_FONT, fontSize: 11, color: C.md_gray, bold: true
});
s_p3.addText("Invisible. Zero impact on behavior.", {
  x: 1.0, y: 3.8, w: 3.6, h: 0.6,
  fontFace: BODY_FONT, fontSize: 13, color: C.md_gray
});
// Right side: examples
s_p3.addShape(pres.shapes.RECTANGLE, {
  x: 5.2, y: 2.0, w: 4.4, h: 1.1,
  fill: { color: "FFEBEE" }
});
s_p3.addText([
  { text: "Doesn't work:\n", options: { bold: true, color: C.magenta, fontSize: 11 } },
  { text: "| API troubleshooting | docs/api-quirks.md |", options: { fontSize: 12, fontFace: "Consolas", color: C.dk_gray } },
], {
  x: 5.4, y: 2.1, w: 4.0, h: 0.9
});
s_p3.addShape(pres.shapes.RECTANGLE, {
  x: 5.2, y: 3.3, w: 4.4, h: 1.1,
  fill: { color: "E8F5E9" }
});
s_p3.addText([
  { text: "Works:\n", options: { bold: true, color: "2E7D32", fontSize: 11 } },
  { text: "| API returns 422 | docs/api-quirks.md |", options: { fontSize: 12, fontFace: "Consolas", color: C.dk_gray } },
], {
  x: 5.4, y: 3.4, w: 4.0, h: 0.9
});
s_p3.addText("Categories vs. situations. Agents recognize situations.", {
  x: 0.8, y: 4.8, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 15, color: C.black, bold: true
});

// Slide: Pattern 4 - Reproduce, Don't Assess
const s_p4 = addContentSlide("Pattern 4: Reproduce, Don't Assess");
s_p4.addText([
  { text: "\"Does this look right?\" ", options: { color: C.md_gray } },
  { text: "catches nothing. ", options: { color: C.md_gray } },
  { text: "\"What answer do I get?\" ", options: { color: C.black, bold: true } },
  { text: "catches everything.", options: { color: C.black, bold: true } },
], {
  x: 0.8, y: 1.2, w: 8.4, h: 0.5,
  fontFace: BODY_FONT, fontSize: 15
});
// Two-column comparison
// Left: Assessment
s_p4.addShape(pres.shapes.RECTANGLE, {
  x: 0.8, y: 2.0, w: 4.0, h: 2.8,
  fill: { color: "FFEBEE" }
});
s_p4.addText("Assessment", {
  x: 0.8, y: 2.1, w: 4.0, h: 0.5,
  fontFace: HEADER_FONT, fontSize: 20, color: C.magenta, bold: true, align: "center"
});
s_p4.addText([
  { text: "Claude + Gemini reviewed\n68 equations\n\n", options: { breakLine: true } },
  { text: "Errors found: ", options: { bold: true, breakLine: true } },
  { text: "0", options: { bold: true, fontSize: 36, color: C.magenta } },
], {
  x: 1.0, y: 2.6, w: 3.6, h: 2.0,
  fontFace: BODY_FONT, fontSize: 14, color: C.dk_gray, align: "center", valign: "middle"
});
// Right: Reproduction
s_p4.addShape(pres.shapes.RECTANGLE, {
  x: 5.2, y: 2.0, w: 4.4, h: 2.8,
  fill: { color: "E8F5E9" }
});
s_p4.addText("Reproduction", {
  x: 5.2, y: 2.1, w: 4.4, h: 0.5,
  fontFace: HEADER_FONT, fontSize: 20, color: "2E7D32", bold: true, align: "center"
});
s_p4.addText([
  { text: "Same model, step-by-step\n\n", options: { breakLine: true } },
  { text: "Errors found: ", options: { bold: true, breakLine: true } },
  { text: "3", options: { bold: true, fontSize: 36, color: "2E7D32" } },
  { text: "\n5x coupling error\n84ms vs 43ms dwell time\n12 s/hr stated as 36 s/hr", options: { fontSize: 11, color: C.dk_gray, breakLine: true } },
], {
  x: 5.4, y: 2.6, w: 4.0, h: 2.0,
  fontFace: BODY_FONT, fontSize: 14, color: C.dk_gray, align: "center", valign: "middle"
});
s_p4.addText("All three errors had correct units and plausible magnitudes \u2014 invisible to assessment.", {
  x: 0.8, y: 5.0, w: 8.4, h: 0.4,
  fontFace: BODY_FONT, fontSize: 12, color: C.magenta, bold: true
});

addQuestionSlide("Think about how you review a colleague's calculations. Do you check the answer, or do you redo the calculation? What changes when the 'colleague' is an AI?");

// ======================================================================
// PART 3: WHAT THIS MEANS FOR YOU
// ======================================================================
addSectionSlide("Part 3: What This Means\nFor You", "Quick decision rules and honest limits");

// Slide: Quick Decision Rules
const s_rules = addContentSlide("Quick Decision Rules");
const rules = [
  { situation: "LLM gave me a number", action: "Reproduce it", pattern: "Pattern 4" },
  { situation: "LLM scored or rated something", action: "Don't trust it \u2014 separate scoring", pattern: "Pattern 1" },
  { situation: "LLM sounds very confident", action: "Check the evidence tier", pattern: "Pattern 1" },
  { situation: "Agent isn't using my docs", action: "Check if it's below the cliff", pattern: "Pattern 3" },
  { situation: "One review pass found nothing", action: "Run another layer", pattern: "Pattern 2" },
];
rules.forEach((r, i) => {
  const y = 1.3 + i * 0.8;
  s_rules.addShape(pres.shapes.RECTANGLE, {
    x: 0.8, y: y, w: 8.4, h: 0.7,
    fill: { color: i % 2 === 0 ? C.white : C.card_gray }
  });
  s_rules.addText(r.situation, {
    x: 1.0, y: y, w: 3.5, h: 0.7,
    fontFace: BODY_FONT, fontSize: 14, color: C.black, bold: true, valign: "middle"
  });
  s_rules.addText(r.action, {
    x: 4.6, y: y, w: 3.2, h: 0.7,
    fontFace: BODY_FONT, fontSize: 14, color: C.dk_gray, valign: "middle"
  });
  s_rules.addText(r.pattern, {
    x: 7.8, y: y, w: 1.4, h: 0.7,
    fontFace: BODY_FONT, fontSize: 11, color: C.magenta, bold: true, valign: "middle", align: "right"
  });
});

// Slide: Honest Limits
const s_limits = addContentSlide("Honest Limits");
s_limits.addText([
  { text: "N=1 researcher, 9 projects, no controlled comparison\n\n", options: { bullet: true, breakLine: true } },
  { text: "Two of four LLM properties may fade in 12-24 months\n\n", options: { bullet: true, breakLine: true } },
  { text: "This is a practitioner's hypothesis, not a validated framework\n\n", options: { bullet: true, breakLine: true } },
  { text: "Survivorship bias \u2014 failed attempts are absent", options: { bullet: true } },
], {
  x: 0.8, y: 1.3, w: 8.4, h: 2.5,
  fontFace: BODY_FONT, fontSize: 16, color: C.dk_gray, paraSpaceAfter: 6
});
s_limits.addShape(pres.shapes.RECTANGLE, {
  x: 0.8, y: 4.0, w: 8.4, h: 1.2,
  fill: { color: C.white },
  line: { color: C.magenta, width: 2 }
});
s_limits.addText("But: the underlying principles \u2014 verify, layer, design context, know your materials \u2014 are permanent. The specific techniques will evolve.", {
  x: 1.0, y: 4.1, w: 8.0, h: 1.0,
  fontFace: BODY_FONT, fontSize: 15, color: C.black, bold: true, valign: "middle"
});

// ======================================================================
// CLOSING
// ======================================================================
addQuoteSlide(
  "The hard part is no longer producing engineering work.\nThe hard part is knowing whether the work is any good.",
  null
);

addQuoteSlide(
  "Teaching engineers to use AI without teaching them to evaluate AI outputs is like teaching them to read test results without teaching them what the results mean.",
  null
);

addQuestionSlide("Starting tomorrow \u2014 which one of these four patterns could you apply to your current project?");

// Final thank you slide
const sEnd = pres.addSlide();
sEnd.background = { color: C.black };
sEnd.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0, w: 10, h: 0.06, fill: { color: C.magenta }
});
sEnd.addText("Thank You", {
  x: 0.8, y: 1.5, w: 8.4, h: 1.2,
  fontFace: HEADER_FONT, fontSize: 48, color: C.white, bold: true, align: "center"
});
sEnd.addText("Four Patterns for AI-Augmented Engineering", {
  x: 0.8, y: 2.8, w: 8.4, h: 0.6,
  fontFace: BODY_FONT, fontSize: 18, color: C.md_gray, align: "center"
});
sEnd.addText([
  { text: "1. Learn the Material", options: { breakLine: true } },
  { text: "2. Layer Your Verification", options: { breakLine: true } },
  { text: "3. Context Is Architecture", options: { breakLine: true } },
  { text: "4. Reproduce, Don't Assess", options: {} },
], {
  x: 2.5, y: 3.5, w: 5.0, h: 1.8,
  fontFace: HEADER_FONT, fontSize: 16, color: C.magenta, align: "center",
  paraSpaceAfter: 8
});

// Write
const outPath = path.resolve("C:/local_dev/augmented-engineering/presentations/AI-for-Engineers-2026-03-25.pptx");
pres.writeFile({ fileName: outPath }).then(() => {
  console.log("Created: " + outPath);
}).catch(err => {
  console.error("Error:", err);
  process.exit(1);
});
