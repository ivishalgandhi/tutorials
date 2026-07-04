# Go Agents: Concurrency, Webhooks, and Architecture — Resources

## Knowledge

### The Blog Post and Real Agent Runtimes

- [What Coding Agents Teach Us About AI Agent Concurrency, Webhooks, and Design Architecture](http://localhost:3000/what-coding-agents-teach-us-about-concurrency-webhooks-architecture)  
  The anchor for this course. Covers the concurrency spectrum (Pi, Keen Code, OpenHands), why systems languages are taking over agent runtimes, and production webhook design. Refer back to it before every lesson.

- [earendil-works/pi](https://github.com/earendil-works/pi)  
  Process-based orchestration with JSONL/Unix-socket IPC. Use as the example of strong isolation at the cost of per-agent overhead.

- [mochow13/keen-code](https://github.com/mochow13/keen-code)  
  Go-based terminal coding agent. Use as the canonical example of goroutines + streaming channels for agent thought-loops.

- [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)  
  Python `asyncio` + durable event log. Use as the example of long-running sessions and replayable state.

- [Rombaut, “Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures” (arXiv 2026)](https://arxiv.org/abs/2604.03515)  
  Source-code taxonomy of 13 open-source coding agents. Use when you want to ground architectural claims in pinned commits rather than marketing.

### Go Concurrency — Videos

- [Jake Wright — Concurrency in Go](https://www.youtube.com/watch?v=LvgVSSpwND8)  
  Short, visual introduction to goroutines, channels, and `select`. Best first watch for anyone new to Go concurrency.

- [Master Go Programming With These Concurrency Patterns (in 40 minutes)](https://www.youtube.com/watch?v=qyM8Pi1KiiM)  
  Covers goroutines, channels, buffered vs unbuffered channels, the `for-select` loop, done channels, and pipelines. Use when you need a single end-to-end video before writing your own worker pool.

- [WorkerPools in Go Tutorial](https://www.youtube.com/watch?v=1iBj5qVyfQA)  
  Focused walkthrough of a fixed-size worker pool. Use this when you are ready to map the abstract pattern to a concrete Go implementation.

- [Go Context Timeout & Cancellation (Production Example)](https://www.youtube.com/watch?v=ti5tsg5Axcg)  
  Explains why every I/O call in Go should accept `context.Context` and how cancellation prevents resource leaks. Use for the graceful shutdown and timeout sections.

### Go Concurrency — Primary Sources

- [Go by Example: Goroutines](https://gobyexample.com/goroutines) and [Channels](https://gobyexample.com/channels)  
  Canonical, runnable snippets. Use as the reference for syntax and idioms.

- [Go Concurrency Patterns: Context — The Go Blog](https://go.dev/blog/context)  
  The original Google article that introduced `context.Context`. Use for cancellation, deadlines, and propagation across API boundaries.

- [Go standard library: `sync`](https://pkg.go.dev/sync) and [`context`](https://pkg.go.dev/context)  
  Authoritative reference for `WaitGroup`, `Mutex`, `Once`, and context helpers.

### Webhooks in Go — Articles

- [WebhookWhisper — Building a Webhook Receiver in Go](https://webhookwhisper.com/blog/webhook-receiver-go)  
  HMAC-SHA256 verification, goroutine-based async processing, and `sync.Map` idempotency using only the standard library. Use as the primary pattern for the webhook receiver lesson.

- [gethook.to — Writing a Webhook Consumer in Go](https://gethook.to/blog/writing-a-webhook-consumer-in-go)  
  Production checklist: `io.LimitReader`, timestamp windows, idempotency with `ON CONFLICT DO NOTHING`, and structured logging. Use for the operational checklist.

- [BackendBytes — Go Graceful HTTP Shutdown: Zero-Downtime Production Patterns](https://backendbytes.com/articles/go-graceful-shutdown-production/)  
  Explains the Kubernetes race between SIGTERM and endpoint removal, and the two-phase shutdown pattern. Use for the shutdown lesson.

### Agent Architecture — Context

- [Mohammad Khan — Multi-Agent Development Is a Distributed Systems Problem](https://mohammadkhan.dev/blog/multi-agent-distributed-systems-problem)  
  War story about webhook storms, queueing, and invariants. Use to ground the "why" of the course in real-world agent failures.

- [OpenClaw Architecture — Concurrency, Isolation, and Invariants](https://theagentstack.substack.com/p/openclaw-architecture-part-2-concurrency)  
  Discusses the single-writer rule, per-session serialization, global throttling, and queue modes. Use for the agent dispatch section.

- [learnwithparam — Architecting a CodeRabbit-style AI code-review agent at scale](https://www.learnwithparam.com/blog/architecting-coderabbit-ai-agent-at-scale)  
  Webhook spikes, decoupling reception from processing, and retry storms. Use for the webhook → queue → worker flow.

### Agent Architecture — Videos

- [AI agent design patterns](https://www.youtube.com/watch?v=GDm_uH6VxPY)  
  Single agent, sequential agent, and parallel agent patterns. Use to frame the "decide" step of the agent loop.

- [5-Step Framework for Scaling Up Your Coding Agents](https://www.youtube.com/watch?v=ORc7-DeCp2o)  
  Treats software development as a manufacturing pipeline and explains throughput bottlenecks. Use for the concurrency-control motivation.

- [How we built 1,000 AI agents that run a marathon](https://www.youtube.com/watch?v=WSIzai2vq4)  
  Deep dive into Google ADK, Redis pub/sub dispatch, and a Go gateway. Use for the architecture inspiration section.

## Skills

- Go standard library: `net/http`, `crypto/hmac`, `crypto/sha256`, `crypto/subtle`, `encoding/hex`, `sync`, `context`, `os/signal`.
- Reading JSON payloads with `encoding/json` while preserving raw bytes for signature verification.
- Implementing bounded concurrency with `chan struct{}` and `sync.WaitGroup`.
- Writing `http.Handler` tests with `httptest`.
- Using `httptest.Server` to simulate webhook providers in tests.

## Wisdom (Communities)

- [r/golang](https://reddit.com/r/golang) — idiomatic Go and concurrency questions.
- [Go Forum](https://forum.golangbridge.org/) — beginner-friendly, strong moderation.
- [r/MachineLearning](https://reddit.com/r/MachineLearning) and [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) — agent architecture discussions.

## Gaps

- No single video teaches "agents + concurrency + webhooks" together in Go. The course synthesises across Go concurrency videos, webhook best-practice articles, and agent architecture essays.
- Most webhook tutorials are for SaaS providers (Stripe, GitHub); general-purpose receiver patterns must be abstracted from those examples.
- The YouTube agent videos are framework-specific (ADK, Superset, Conductor). The course extracts the transport-agnostic ideas: loop, queue, concurrency cap, idempotency.
