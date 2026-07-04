# Exercise 01 — Webhook to Worker Pool

## The bug

`problem.go` starts an HTTP server that processes each webhook synchronously inside the handler.
The handler sleeps for 200 ms before returning, which can cause the provider to time out and retry.

## What to fix

Move the slow work out of the handler. Create a buffered `events` channel, enqueue the event in the
handler with a non-blocking send, and start a worker pool that processes events asynchronously.
If the queue is full, return `503 Service Unavailable`.

## Why this matters

Webhook providers expect a fast response. The handler's job is to verify and accept the event; the
worker pool's job is to do the work. Separating them lets you add concurrency limits and backpressure.

## Run

```bash
cd exercises/lesson-04-wiring/01-webhook-to-pool
go run problem.go
# In another terminal:
curl -X POST http://localhost:8080/webhook -H 'X-Event-ID: 1'
```

The request will take 200 ms. After fixing:

```bash
go run solution.go
# In another terminal:
curl -X POST http://localhost:8080/webhook -H 'X-Event-ID: 1'
```

The request returns immediately with HTTP 202 while the worker processes the event in the background.
