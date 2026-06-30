# Exercise 02 — Isolated Context

## Concept

Subagents do not inherit the coordinator's conversation history, system prompt, or
tool results. Every byte the subagent needs must be in the prompt passed to the
`Task` tool.

## The bug

The `problem.py` calls a subagent with a vague prompt: "Analyze the document".
The subagent has no document, no prior search results, and no output format. It
hallucinates or produces a generic answer.

## Your task

1. Run `problem.py` and see the subagent produce a generic response.
2. Find the `spawn_subagent` call in the coordinator.
3. Rewrite the prompt to include:
   - the full document text,
   - any prior context (e.g., search results),
   - explicit output-format requirements.
4. Run again and confirm the subagent produces a structured, document-grounded answer.

## Exam connection

This is the most common subagent failure mode: the subagent runs correctly, but
its universe is too small because the coordinator's context-passing was incomplete.
