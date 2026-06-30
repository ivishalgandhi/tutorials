# Exercise 01 — Won't Delegate

## Concept

A coordinator agent can only spawn subagents if it has the right tool available.
In the Claude Agent SDK, the coordinator must include `"Task"` in its `allowed_tools`
list. Without it, the model has no way to delegate and will try to do everything inline.

## The bug

The `problem.py` defines a `researcher` subagent and a `run_coordinator` function,
but the coordinator's `allowed_tools` list omits `"Task"`. When the coordinator
should spawn parallel research subagents, it instead generates a single inline answer.

## Your task

1. Run `problem.py` and see the coordinator return an inline answer instead of delegating.
2. Find the `allowed_tools` list in the coordinator definition.
3. Add `"Task"` so the coordinator can invoke the `spawn_subagent` tool.
4. Confirm the output now shows two subagents running in parallel and a synthesized report.

## Exam connection

This maps directly to the "won't delegate" symptom from the failure-tracing table:
coordinator completes, subagents are defined, but they are never invoked because the
tool harness doesn't allow it.
