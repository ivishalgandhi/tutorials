# Lesson 04 — Go Exercises: Wiring Agent + Webhooks

Two exercises that cover the end-to-end agent runtime: separating the HTTP handler from the worker pool, and shutting down cleanly.
Each has a `problem.go` (broken or incomplete code) and a `solution.go`.

## Setup

```bash
# Any recent Go version works; 1.22+ recommended for the standard-library examples.
go version
```

## Exercises

| # | Exercise | Concept tested |
|---|----------|----------------|
| 01 | Webhook to Worker Pool | The handler must ack and enqueue; slow work belongs to the workers |
| 02 | Graceful Shutdown | `http.Server.Shutdown` must be paired with `sync.WaitGroup` to drain workers |

## Lesson connection

These map directly to the blog post's event-driven runtime architecture:
- Exercise 01 → "webhooks are the lingua franca" of an event-driven backbone; the handler accepts the event and returns immediately.
- Exercise 02 → durable logs and bounded queues are only useful if the runtime can finish in-flight work before exit.

Run each `problem.go` first to see the failure mode, then read `solution.go` to understand the fix.
