# Exercise 02 — Idempotent Handler

## The bug

The handler in `problem.go` processes every request it receives. When a webhook
provider retries the same event, the handler runs the work twice. Duplicate
charges, duplicate deployments, and duplicate notifications are all possible.

## What to fix

Track the set of seen event IDs in a map protected by a `sync.Mutex`. When a
request arrives, check whether the ID is already in the map. If it is, return a
successful response and skip the work. If it is not, add the ID and process the
event.

## Why this matters

Webhook providers retry on timeouts and errors. The receiver must be
idempotent: processing the same event many times should have the same effect as
processing it once.

## Run

```bash
cd exercises/lesson-02-webhooks/02-idempotent-handler
go run problem.go    # prints "processed" twice for the same event ID
```

After fixing:

```bash
go run solution.go   # prints "processed" once and "skipped" once
```
