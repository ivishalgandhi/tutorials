# Lesson 03 — Go Exercises: Concurrency Control

Two exercises that cover the two standard ways to cap concurrency in Go: worker pools and semaphores.
Each has a `problem.go` (unbounded concurrency) and a `solution.go`.

## Setup

```bash
# Any recent Go version works; 1.22+ recommended for the standard-library examples.
go version
```

## Exercises

| # | Exercise | Concept tested |
|---|----------|----------------|
| 01 | Worker Pool | A fixed set of long-lived goroutines drains a shared job channel |
| 02 | Semaphore | A bounded `chan struct{}` acts as a token bucket for short-lived goroutines |

## Lesson connection

These map directly to the concurrency spectrum from the blog post:
- Exercise 01 → the Keen Code pattern: pre-warmed workers handle a continuous stream of agent thought-loops.
- Exercise 02 → when work is bursty, a semaphore caps active goroutines without rewriting the whole dispatcher.

Run each `problem.go` first to see the unbounded behavior, then read `solution.go` to understand the fix.
