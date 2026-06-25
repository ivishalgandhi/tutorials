# Learning record 0002 — Multi-agent orchestration patterns

## What was learned

After Lesson 1 established the agentic loop and the prompts-vs-hooks frame, Lesson 2 extended
that frame to multi-agent systems. The central insight:

> Subagents execute in isolation. The coordinator owns decomposition, partitioning, and context passing.
> If subagents complete successfully but the output is wrong, blame the coordinator, not the agents.

Key concepts that stuck:

- **Hub-and-spoke topology** — all inter-subagent communication routes through the coordinator.
  Direct agent-to-agent links break observability and error recovery.
- **Subagent context isolation** — subagents do not inherit the coordinator's conversation history,
  system prompt, or tool results. The prompt is the only channel.
- **The `Task` tool** — the coordinator must have `"Task"` in `allowedTools` or it will never delegate.
- **Parallel spawning** — one coordinator response can emit multiple `Task` calls; the SDK runs them
  concurrently.
- **Failure tracing** — missing topics = decomposition too narrow; duplicated work = partitioning
  sloppy; shallow output = subagent prompts/tools; won't delegate = missing `Task` tool.
- **Least privilege** — give subagents only the tools they need (e.g., `verify_fact` for synthesis,
  full web search kept at the coordinator level).
- **Evaluator–optimiser** — only works when the evaluator has objectively checkable criteria;
  subjective criteria cause infinite loops.

## Mistakes corrected

The user got two official sample questions wrong before this lesson:

1. **Heterogeneous timestamps** — Lesson 1 was already updated with a Wrong Answer Autopsy explaining
   why PostToolUse is required when the upstream API response format is outside the agent's control.
2. **Multi-agent coverage gap** — this lesson directly addresses the root cause: the coordinator's
   decomposition was too narrow, not the subagents' execution quality.

## Implications for future lessons

- Lesson 3 (lifecycle hooks) will build on this: subagents run in isolation, but hooks are the
  deterministic layer that can enforce rules across the whole system.
- Lesson 9 (MCP architecture) will revisit tool boundaries: each subagent can have its own MCP server
  scope, which is another reason for isolation.
- Continue using the failure-tracing table as a mental model for every multi-agent scenario.
