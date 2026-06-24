# Concurrency — Semaphores & Worker Pools

Lesson 5 completed. Naive goroutine fan-out (one goroutine per server, no limit) is dangerous at 3,000 servers — hits max_connections, OS fd limits, and memory from goroutine stacks simultaneously.

Two safe patterns:
- Semaphore: buffered channel make(chan struct{}, N). Send to acquire, receive in defer to release. goroutine-per-server up to N concurrent.
- Worker pool: fixed N goroutines ranging over a work channel. Close the channel before launching workers so range exits cleanly.

Scanner is I/O bound (waiting for network RTT). Goroutines spend most time idle. Formula: concurrency ≈ target_rate × avg_latency. At 3,000 servers / 60s = 50/sec, avg 2s latency → ~100 concurrency. Stay below max_connections on target servers (leave headroom for real traffic).

Context propagation: outer context with 90s scan timeout wraps per-server context with 10s timeout. Cancelling the outer immediately cancels all in-flight per-server contexts.
