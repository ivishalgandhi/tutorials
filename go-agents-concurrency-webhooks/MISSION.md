# Mission: Go Agents — Concurrency, Webhooks, and Architecture

## Why
I published a blog post about what coding agents teach us about concurrency and webhooks. In interviews, I want to back up the ideas with a real, idiomatic Go implementation that I can explain line by line. I am new to Go, so I need to learn the language while building the same agent-style patterns I wrote about.

## Success looks like
- I can explain the agent loop in Go (`sense → decide → act`) and point to a working implementation.
- I can write a Go webhook receiver that verifies signatures, stores events idempotently, and processes them asynchronously.
- I can implement a bounded worker pool in Go using channels and `sync.WaitGroup`, and explain when to use it over a semaphore.
- I can wire webhooks into an agent dispatcher: one HTTP handler receives events, a queue fans them out to workers, and `context.Context` carries cancellation through the whole path.
- I can describe graceful shutdown, observability, and retry behaviour in production terms.

## Constraints
- Go beginner (< 6 months) — every non-obvious Go construct must be explained, not just shown.
- Goal is interview fluency and a real implementation, not shipping a product.
- Examples must compile with the standard library only (no external frameworks).
- Every lesson must include a short exercise and cite at least one primary source or popular video.

## Out of scope
- Calling real LLM APIs or building a full coding agent.
- Kubernetes deployment, distributed locks, or leader election.
- Advanced Go: generics, cgo, unsafe, reflection.
- OAuth, mTLS, or complex authentication beyond shared-secret HMAC.
