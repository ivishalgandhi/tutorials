# Exercise 02 — Semaphore

## The bug

`problem.go` fetches a list of URLs concurrently. It starts one goroutine per URL, so a long list can open too many network connections at once and exhaust file descriptors or get the program throttled.

## What to fix

Use a buffered channel as a semaphore to cap the number of concurrent fetches:

1. Create a `chan struct{}` with a buffer equal to the desired concurrency limit.
2. Before each fetch, send a token to the channel to acquire it.
3. After the fetch, receive from the channel to release the token.
4. Use a `defer` to guarantee the token is released even if the fetch fails.

## Why this matters

Agents often call external APIs in parallel. Without a concurrency cap, a burst of work can trigger rate limits or connection errors. A semaphore is the lightest way to add a cap when you still want one goroutine per task.

## Run

```bash
cd exercises/lesson-03-concurrency/02-semaphore
go run problem.go    # unbounded concurrent fetches
```

After fixing:

```bash
go run solution.go   # cap concurrent fetches at 3
```
