# Exercise 01 — Cancelable Agent

## The bug

The `RunAgent` function in `problem.go` loops up to 100 times and does not check the `context.Context` it receives.
If the caller sets a 50 ms timeout, the agent keeps running until all 100 iterations finish.

## What to fix

Make the agent respect cancellation by checking `ctx.Err()` at the top of the loop.
When the context is cancelled, return the context error instead of continuing.

## Why this matters

In production, your agent will receive a `SIGTERM` when the container shuts down.
Without cancellation checks, the orchestrator will eventually send `SIGKILL` and you may lose in-progress work.

## Run

```bash
cd exercises/lesson-01-agent-loop/01-cancelable-agent
go run problem.go    # should ignore the timeout and run to completion
```

After fixing:

```bash
go run solution.go   # should stop as soon as the context times out
```
