# Exercise 02 — Graceful Shutdown

## The bug

`problem.go` starts an HTTP server with `http.ListenAndServe`. When you press Ctrl+C, the program exits
immediately, killing any in-flight request or worker without giving it time to finish.

## What to fix

Replace `http.ListenAndServe` with an `http.Server` value. Use `signal.NotifyContext` to catch
`SIGINT`. On shutdown, call `srv.Shutdown` with a timeout, then close the work channel and wait for the
workers with `sync.WaitGroup`.

## Why this matters

Production systems receive `SIGTERM` during deploys or autoscaling events. A graceful shutdown finishes
in-flight work, closes the listener so no new requests arrive, and then exits cleanly.

## Run

```bash
cd exercises/lesson-04-wiring/02-graceful-shutdown
go run problem.go
# Press Ctrl+C — the process exits immediately, possibly mid-request.
```

After fixing:

```bash
go run solution.go
# Press Ctrl+C — the server prints "shutting down", waits for workers to finish, then exits.
```
