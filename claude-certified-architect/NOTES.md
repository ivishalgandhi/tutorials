# Teaching Notes

## User profile
- Director-level, database reliability background
- "Vibe coder" — has hands-on Claude experience but gaps in formal vocabulary
- Career-driven: wants the credential to unstick stagnated career trajectory
- Learning style: prefers reasoning from first principles, not memorization

## Preferences
- All diagrams must be Mermaid (in-browser rendering)
- Deep web research required before each lesson — never rely on parametric knowledge alone
- Lesson content must be exam-grounded (cite domain weights and gotchas explicitly)
- Materials live at: `/Users/vishal/learn/tutorials/claude-certified-architect/`
- Reference materials also wanted on M4 at: `/Users/vishal/claude-certified-architect-book/` (may need syncing)

## Exam snapshot (as of June 2026)
- 60 questions, 120 min, scaled 100–1000, pass at 720
- **4 of 6 official scenarios** per sitting (Ankit's README built from official PDF v0.1)
  - paullarionov (★3,002) claims 4 of 8 — 2 extra may be newer additions, treat as bonus prep
- **No penalty for guessing — answer every question**
- Free for Claude Partner Network members
- Delivered via Anthropic Academy (Skilljar)

## THE ONE FRAME (put this in every lesson)
> **Prompts are probabilistic. Hooks are deterministic.**
>
> Single failure causes financial loss, security breach, or compliance violation → **hooks / programmatic gates**.
> Single failure causes bad-but-recoverable UX → **prompts**.

## The exam is NOT API memorization — it tests judgment
From an actual passer (Ankit Raheja, ankitrahejagatech):
- Questions test: what should happen when a tool call fails, when context runs out, when a subagent goes off-track
- Most distractors "sound right but aren't best" — practise wrong-answer elimination
- Production design frame: What is brittle? Deterministic? Fails silently? Needs isolation? Escalation?

## What is NOT on the exam (do not waste time on these)
Constitutional AI, RLHF, fine-tuning, embedding models, computer use, vision API, streaming/SSE,
OAuth/API key rotation, rate limiting, quotas, pricing, prompt caching implementation details,
specific cloud provider configs, token counting.

## Critical gotcha: partial prefill deprecated
- Trailing assistant messages in the `messages` array → **validation error** on Claude 4.6+
- Replacement: `output_config.format` (JSON schema), forced tool_choice, or system prompt style instructions

## Source material on M4
- Raw GitHub repo content: `/Users/vishal/claude-certified-architect-book/`
- ankitrahejagatech-domain1.md — best D1 cheat sheet (distractor cribsheet + mnemonics)
- ankitrahejagatech-sample-questions.md — 12 official sample questions verbatim
- paullarionov-guide-en.md (★3,002) — most comprehensive community guide
- daronyondem-exam-prep-guide.md (★944) — framing and anti-patterns

## Domain weights (for lesson prioritisation)
| Domain | Weight | Color tag |
|--------|--------|-----------|
| D1: Agentic Architecture & Orchestration | 27% | amber (domain-1) |
| D2: Tool Design & MCP Integration        | 18% | indigo (domain-2) |
| D3: Claude Code Configuration & Workflows| 20% | cyan (domain-3) |
| D4: Prompt Engineering & Structured Output| 20% | green (domain-4) |
| D5: Context Management & Reliability     | 15% | purple (domain-5) |

## Lesson sequencing rationale
- Start with D1 (highest weight, most gotchas for vibe coders)
- Interleave D3 + D4 (everyday developer patterns, build confidence)
- Cover D2 (MCP architecture, distinct vocabulary)
- Finish with D5 (context + caching, lower weight but high integration value)
