# Notes — Go Agents: Concurrency, Webhooks, and Architecture

## User Profile

- Database/infrastructure engineer with limited Go experience (< 6 months).
- Already wrote a blog post on coding agents, concurrency, and webhooks.
- Goal is interview confidence: be able to explain a real-world Go implementation of the ideas in the post.
- Wants lessons grounded in real-world examples, not toy code.

## Teaching Preferences

- Explain every non-obvious Go construct (e.g., why `chan struct{}` is a semaphore, not just show it).
- Match the visual style of the existing tutorial folders (`go-db-scheduler`, `postgres-scanner`, `zabbix-webhooks-go`).
- Every lesson must include an interactive `quiz.js` quiz and at least one exercise.
- Include popular, relevant YouTube videos in the resources and inline citations.
- Keep code examples compilable with only the Go standard library.
- Use the same glossary and reference conventions as the existing courses.

## Course Conventions

- Course index: `index.html` with `assets/style.css`, `.lesson-list` cards, `.lesson-num`, `.lesson-title`, `.lesson-topics`.
- Lessons: `../assets/style.css`, `../assets/quiz.js`, `../assets/mermaid-init.js`, Mermaid diagrams, callouts, and a `.quiz-section` at the end.
- Exercises: `exercises/lesson-NN-slug/NN-exercise-name/{README.md,problem.go,solution.go}`.
- References: `../assets/style.css`, glossary tables, and quick lookup tables.

## Vocabulary (Ubiquitous Language)

- **Agent loop** — `sense → decide → act` cycle repeated until a terminal condition.
- **Webhook** — an HTTP callback pushed by a provider when an event occurs.
- **Idempotency key** — a unique identifier that lets the receiver safely process retries as no-ops.
- **Worker pool** — a fixed set of long-lived goroutines that drain jobs from a shared channel.
- **Semaphore** — a bounded channel used to limit the number of goroutines in a critical section.
- **Graceful shutdown** — stop accepting new work, drain in-flight work, then exit.
- **Backpressure** — signaling the sender to slow down when the receiver is overloaded.

## Serving Lessons

Always serve via HTTP (not `file://`) so relative CSS/JS imports resolve:

```bash
cd /Users/vishal/learn/tutorials/go-agents-concurrency-webhooks
python3 -m http.server 8765
```

Then open: http://localhost:8765/
