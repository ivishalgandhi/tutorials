# CCA Lesson Plan — Per-Lesson Blueprint

> This file is the session-to-session handoff.
> Every next session should read this first before writing any lesson.
> Update the status column and "Last worked on" date after each session.

---

## Standing instructions for every lesson

1. **Read NOTES.md first** — has the one frame, out-of-scope list, user profile, source paths.
2. **Read the relevant ankitrahejagatech cheat sheet** from `/Users/vishal/claude-certified-architect-book/` before writing. These are the ground-truth distractor cribsheets built from the official Anthropic PDF.
3. **Pull official sample questions** from `ankitrahejagatech-sample-questions.md` — use verbatim where they map to the lesson topic.
4. **Put "Prompts are probabilistic. Hooks are deterministic." in every lesson** — as a callout or mnemonic. It belongs everywhere.
5. **Include a "Not on this exam" box** in every lesson — keeps the user from wasting time.
6. **Quiz questions must follow official format** — 4 options, one correct, explain why each wrong answer is wrong (not just why the right answer is right).
7. **Every lesson ends with a "What's next" + link to Ankit's live practice exam.**

---

## Lesson status

| # | Title | Domain | Status | File |
|---|-------|--------|--------|------|
| 01 | The Agentic Loop & The One Frame | D1 | ✅ Done | `lessons/0001-agentic-loop.html` |
| 02 | Orchestrator & Subagent Patterns | D1 | ⬜ Next | `lessons/0002-multi-agent-patterns.html` |
| 03 | Lifecycle Hooks & Agent SDK | D1 | ⬜ | `lessons/0003-lifecycle-hooks.html` |
| 04 | CLAUDE.md — The Project Constitution | D3 | ⬜ | `lessons/0004-claude-md.html` |
| 05 | Hooks: Deterministic Guarantees | D3 | ⬜ | `lessons/0005-hooks-deterministic.html` |
| 06 | Plan Mode vs Direct Execution | D3 | ⬜ | `lessons/0006-plan-mode.html` |
| 07 | Structured Output — JSON Schema & tool_use | D4 | ⬜ | `lessons/0007-structured-output.html` |
| 08 | Extended Thinking — Budget Tokens & Display | D4 | ⬜ | `lessons/0008-extended-thinking.html` |
| 09 | MCP Architecture — Host, Client, Server | D2 | ⬜ | `lessons/0009-mcp-architecture.html` |
| 10 | MCP Primitives — Tools vs Resources vs Prompts | D2 | ⬜ | `lessons/0010-mcp-primitives.html` |
| 11 | Tool Error Handling — Structured Errors | D2 | ⬜ | `lessons/0011-tool-errors.html` |
| 12 | Prompt Caching — Cost, Latency, Prefix Rules | D5 | ⬜ | `lessons/0012-prompt-caching.html` |
| 13 | Context Window Management & Compaction | D5 | ⬜ | `lessons/0013-context-management.html` |

---

## Lesson 02 — Orchestrator & Subagent Patterns

**Domain:** D1 (Agentic Architecture & Orchestration) — 27%
**File to create:** `lessons/0002-multi-agent-patterns.html`

### Key concepts to cover
- Hub-and-spoke topology: ALL inter-subagent communication routes through coordinator
- **Subagent context isolation**: subagents do NOT inherit coordinator history — every byte must be explicitly passed in their prompt. Nothing carries over.
- The `Task` tool: coordinator's `allowedTools` must include `"Task"` — otherwise the coordinator won't delegate (common bug on the exam)
- Parallel subagents: multiple `Task` calls in ONE coordinator response — SDK runs them concurrently
- `fork_session`: independent branches from a shared expensive baseline (for parallel exploration)
- Task decomposition patterns (fixed sequential / dynamic decomposition / orchestrator-worker / evaluator-optimiser)
- Evaluator-optimiser: fails when criteria aren't objectively checkable — loop spins indefinitely

### Official sample questions that map here (from `ankitrahejagatech-sample-questions.md`)
- **Q7** (Multi-Agent Research): coordinator decomposition too narrow → missing topics. Answer: B. Root cause is the coordinator's decomposition, not the subagents.
- **Q8** (Multi-Agent Research): subagent timeout error propagation. Answer: A — return structured error context (failure type, query, partial results, alternatives). NOT a generic "search unavailable".
- **Q9** (Multi-Agent Research): synthesis agent needs to verify facts → 40% latency overhead. Answer: A — give synthesis agent a scoped `verify_fact` tool for simple lookups (85%), keep complex ones routed through coordinator (15%). Principle of least privilege.

### Distractor patterns for this lesson (from `ankitrahejagatech-domain1.md`)
**Reject:**
- "Have subagent A pass results directly to subagent B" → breaks hub-and-spoke, kills observability
- "Forward the full conversation transcript to the human reviewer" → not structured error context
- "Catch errors and return an empty string silently" → masks failure as success

**Lean toward:**
- "Pass structured data with claim → source mappings" (for missing citations)
- "Coordinator's decomposition is too narrow" (for missing-topic scenarios)
- "Add `Task` to coordinator's `allowedTools`" (for won't-delegate bugs)
- "Give the synthesis agent a scoped tool" (principle of least privilege)

### Source files to read before writing
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain1.md
  → lines: Task Decomposition Patterns table, Failure Tracing Rules, Hub-and-Spoke section
/Users/vishal/claude-certified-architect-book/paullarionov-guide-en.md
  → lines ~308–420: Chapter 3 (Agent SDK), section 3.3 (Hub-and-Spoke), section 3.4 (Task Tool)
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-sample-questions.md
  → Q7, Q8, Q9 verbatim
```

### Mermaid diagrams to include
1. Hub-and-spoke topology (coordinator in center, subagents radiating out, all comms through hub)
2. Parallel Task calls diagram (one coordinator response → 3 simultaneous subagent calls)
3. Evaluator-optimiser loop (with the "objectively checkable criteria" break condition)

### Failure tracing table (must include)
| Symptom | Root cause |
|---------|-----------|
| Missing topics in output | Coordinator's decomposition too narrow |
| Duplicated work / redundant sources | Coordinator's scope partitioning sloppy |
| Shallow on every topic | Subagent prompts or tool budgets |
| Missing source attribution | Context-passing format (prose instead of claim→source) |
| "Won't delegate" | Coordinator's `allowedTools` missing `"Task"` |

---

## Lesson 03 — Lifecycle Hooks & Agent SDK

**Domain:** D1 / D3 overlap
**File to create:** `lessons/0003-lifecycle-hooks.html`

### Key concepts to cover
- PreToolUse hook: fires before tool executes — gates, authorisation, prerequisite checks, prior state hash
- PostToolUse hook: fires after tool, before model sees result — normalise, redact, truncate, enrich
- Idempotency keys: UUID generated on FIRST attempt, passed on every retry — server-side dedup prevents double-charge
- Error classification: transient (retry) vs permanent (don't retry) vs logical (feed back to model)
- Circuit breaker pattern
- Hooks do NOT rank tools — use prompts/descriptions for that

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain1.md
  → Hooks: PreToolUse vs PostToolUse table, Error Classification table, Idempotency Key section
/Users/vishal/claude-certified-architect-book/daronyondem-exam-prep-guide.md
  → Section on hooks and safety
```

---

## Lesson 04 — CLAUDE.md: The Project Constitution

**Domain:** D3 (Claude Code Configuration & Workflows) — 20%
**File to create:** `lessons/0004-claude-md.html`

### Key concepts to cover
- Path prefix is the whole answer:
  - `~/.claude/` = personal, NEVER git-tracked (user-level config)
  - `.claude/` in project = shared via git (project-level config)
- Divergent team behavior = user-level config that was never committed
- `.claude/commands/` = project slash commands (version-controlled, available to all on clone)
- `~/.claude/commands/` = personal commands (never shared)
- `.claude/rules/` with YAML frontmatter + glob patterns = automatic file-path-based convention enforcement
- CLAUDE.md = project instructions, NOT command definitions

### Official sample questions
- **Q4**: where to put `/review` slash command for whole team → `.claude/commands/` in repo (A). NOT `~/.claude/commands/` (personal).
- **Q6**: codebase with different conventions per area, tests spread throughout → `.claude/rules/` with glob patterns (A). NOT root CLAUDE.md (infers wrong section), NOT `~/.claude/skills/` (manual invocation), NOT CLAUDE.md in every dir (can't handle spread files).

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain3.md → path prefix section
/Users/vishal/claude-certified-architect-book/daronyondem-exam-prep-guide.md → Claude Code section
```

---

## Lesson 05 — Hooks in Claude Code: Deterministic Guarantees

**Domain:** D3
**File to create:** `lessons/0005-hooks-deterministic.html`

### Key concepts to cover
- Claude Code hooks vs Agent SDK hooks (same principle, different context)
- `context: fork` for noisy skills (isolates context, prevents bleed)
- `-p` flag for CI/headless mode — `claude -p "prompt"` prints and exits. NOT `--batch`, NOT `CLAUDE_HEADLESS=true`
- Batch API: 50% cost savings, no latency SLA, no multi-turn tool calling — only for async workloads

### Official sample questions
- **Q10** (CI/CD): pipeline hangs waiting for interactive input → `-p` flag (A). Options B/C/D are non-existent or workarounds.
- **Q11** (CI/CD): Batch API for pre-merge checks vs overnight reports → use batch only for tech-debt reports (A). Pre-merge checks need real-time — Batch has no latency SLA.

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain3.md → CI/CD section, -p flag
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-sample-questions.md → Q10, Q11
```

---

## Lesson 06 — Plan Mode vs Direct Execution

**Domain:** D3
**File to create:** `lessons/0006-plan-mode.html`

### Key concepts
- Plan mode: for large changes, multiple valid approaches, architectural decisions, exploration before commit
- Direct execution: for well-understood, bounded tasks
- Official Q5: monolith → microservices → Plan mode (A). NOT incremental direct execution (risks rework).

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain3.md
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-sample-questions.md → Q5
```

---

## Lesson 07 — Structured Output: JSON Schema & tool_use

**Domain:** D4 (Prompt Engineering & Structured Output) — 20%
**File to create:** `lessons/0007-structured-output.html`

### Key concepts
- `tool_use` eliminates SYNTAX errors, NOT semantic errors (values can still be wrong)
- `tool_choice: "any"` = guaranteed tool call, model picks which one
- `tool_choice: "auto"` = may or may not call a tool — NOT guaranteed
- `tool_choice: "tool"` = forced specific tool call (for pipeline ordering)
- `tool_choice: "none"` = no tool call allowed
- Retry fails when the information isn't in the source document — feed back validation errors instead
- Partial assistant prefill → DEPRECATED on Claude 4.6+, causes validation error
- Schema design: required vs nullable fields, enums with "other", enums with "unclear"

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain4.md
/Users/vishal/claude-certified-architect-book/daronyondem-exam-prep-guide.md → Section 1 (API Fundamentals)
/Users/vishal/claude-certified-architect-book/paullarionov-guide-en.md → Chapter 2 (Tools and tool_use)
```

---

## Lesson 08 — Extended Thinking

**Domain:** D4
**File to create:** `lessons/0008-extended-thinking.html`

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain4.md → extended thinking section
https://platform.claude.com/docs/en/build-with-claude/extended-thinking
```

---

## Lesson 09 — MCP Architecture: Host, Client, Server

**Domain:** D2 (Tool Design & MCP Integration) — 18%
**File to create:** `lessons/0009-mcp-architecture.html`

### Key concepts
- Three-layer model: Host (e.g. Claude Code) → Client (per-server connection) → Server (tool executor)
- `.mcp.json` = project-level MCP config (git-tracked, shared with team)
- `~/.claude.json` = user-level MCP config (personal, never git-tracked)
- Scoped tool access: 4–5 tools per agent, NOT 18 — large tool sets degrade selection accuracy
- MCP annotations are NOT a security boundary — treat as untrusted hints
- `isError: false` for zero results (valid empty) vs `isError: true` for actual failures

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain2.md
/Users/vishal/claude-certified-architect-book/dnacenta-d2-mcp.md
/Users/vishal/claude-certified-architect-book/daronyondem-exam-prep-guide.md → MCP section
```

---

## Lesson 10 — MCP Primitives: Tools vs Resources vs Prompts

**Domain:** D2
**File to create:** `lessons/0010-mcp-primitives.html`

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain2.md
https://modelcontextprotocol.io/docs/concepts/tools
https://modelcontextprotocol.io/docs/concepts/resources
```

---

## Lesson 11 — Tool Error Handling

**Domain:** D2
**File to create:** `lessons/0011-tool-errors.html`

### Key concepts
- Minimal tool descriptions = primary root cause of tool misuse (before adding routing layers)
- Tool descriptions must include: what it does, input formats, when to use vs alternatives
- `isError` field: use correctly — empty result ≠ error

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain2.md
/Users/vishal/claude-certified-architect-book/daronyondem-exam-prep-guide.md → Section 2 (Tool Design)
/Users/vishal/claude-certified-architect-book/paullarionov-guide-en.md → Chapter 2
```

---

## Lesson 12 — Prompt Caching

**Domain:** D5 (Context Management & Reliability) — 15%
**File to create:** `lessons/0012-prompt-caching.html`

### Key concepts
- Cache prefix rules, 50% cost reduction, latency implications
- NOT on the exam: implementation details of caching internals

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain5.md
/Users/vishal/claude-certified-architect-book/dnacenta-d5-context.md
```

---

## Lesson 13 — Context Window Management & Compaction

**Domain:** D5
**File to create:** `lessons/0013-context-management.html`

### Key concepts
- Lost-in-the-middle: put key findings at the start or end, not buried in the middle
- Case facts block: preserves specific values (numbers, dates) outside summarised history
- Conflicting sources: annotate BOTH, flag as contested — do NOT pick one
- Three escalation triggers: explicit human request, policy gap, can't make progress
- Progressive summarisation: loses numeric values, percentages, dates — use case facts block

### Source files
```
/Users/vishal/claude-certified-architect-book/ankitrahejagatech-domain5.md
/Users/vishal/claude-certified-architect-book/dnacenta-d5-context.md
/Users/vishal/claude-certified-architect-book/daronyondem-exam-prep-guide.md → Context section
```

---

## What was learned this session (from LinkedIn post + research)

Date: June 24 2026

- **Source**: LinkedIn post by Ankit Raheja (actual CCA passer). Certificate verified at https://verify.skilljar.com/c/xkszur8rzk44
- **GitHub**: https://github.com/ankitrahejagatech/claude-certified-architect-prep
- **Key lesson**: The exam tests judgment under production constraints, not API memorisation
- **The one frame**: Prompts are probabilistic. Hooks are deterministic. (appears in every domain)
- **Scenario count**: 4 of 6 official (from Anthropic PDF v0.1). paullarionov claims 8 — may be newer additions.
- **Top repos pulled locally**:
  - `paullarionov-guide-en.md` (★3,002) — 188 KB comprehensive guide
  - `daronyondem-exam-prep-guide.md` (★944) — scenario-oriented, 177 KB
  - `ankitrahejagatech-domain1..5.md` — distractor cribsheets, built from official PDF
  - `ankitrahejagatech-sample-questions.md` — 12 official Anthropic sample questions verbatim
  - `dnacenta-d1..d5.md` — domain deep-dives
- **Lesson 1 fully rewritten** with enforcement spectrum, three global rules, distractor cribsheet, production design mindset diagram, official sample question, 4 exam-format quiz questions
