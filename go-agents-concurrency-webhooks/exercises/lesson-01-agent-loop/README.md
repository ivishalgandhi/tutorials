# Lesson 01 — Go Exercises: The Agent Loop

Two exercises that cover the core Go primitives behind any agent loop: cancellation and goroutine lifecycle.
Each has a `problem.go` (broken or incomplete code) and a `solution.go`.

## Setup

```bash
# Any recent Go version works; 1.22+ recommended for the standard-library examples.
go version
```

## Exercises

| # | Exercise | Concept tested |
|---|----------|----------------|
| 01 | Cancelable Agent | `context.Context` must be checked inside long-running loops |
| 02 | Stop with a Done Channel | A closed channel is the cleanest signal for "stop now" |

## Lesson connection

These map directly to the control-flow patterns behind real agent runtimes:
- Exercise 01 → a loop that ignores `SIGTERM` keeps running until the orchestrator kills it.
- Exercise 02 → a goroutine without a cancellation path leaks until the process exits.

Run each `problem.go` first to see the bug, then read `solution.go` to understand the fix.
