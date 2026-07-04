# Lesson 02 — Go Exercises: Receiving Webhooks

Two exercises that cover the two hard parts of a production webhook receiver: authentication and idempotency.
Each has a `problem.go` (broken or insecure code) and a `solution.go`.

## Setup

```bash
# Any recent Go version works; 1.22+ recommended for the standard-library examples.
go version
```

## Exercises

| # | Exercise | Concept tested |
|---|----------|----------------|
| 01 | Verify Signature | HMAC comparison must be constant-time (`hmac.Equal`, not `==`) |
| 02 | Idempotent Handler | Duplicate event IDs must be skipped, not reprocessed |

## Lesson connection

These map directly to the webhook design principles from the blog post:
- Exercise 01 → "Authentication and Validation" — a public endpoint that triggers agent work must verify signatures.
- Exercise 02 → "Idempotency" — external systems retry, so the runtime must record processed keys before dispatching work.

Run each `problem.go` first to see the failure mode, then read `solution.go` to understand the fix.
