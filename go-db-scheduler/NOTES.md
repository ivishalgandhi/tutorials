# Notes — Go Database Job Scheduler

## User Profile

- Database / infrastructure engineer managing 20,000 databases across 5,000 servers
- Fleet mix: SQL Server + PostgreSQL, preparing for cloud scale
- Go beginner (< 6 months) — goroutines and channels are still new
- Real production system to ship — not a toy project
- Motivation: ship a working scheduler + understand distributed patterns for future Go work

## Teaching Preferences

- Go beginner — annotate every non-obvious Go construct (e.g. explain why a buffered channel is a semaphore, not just show it)
- Ground every lesson in the real fleet: "this prevents two backup jobs running on sql-prod-01 simultaneously"
- Quizzes are essential for storage strength — every lesson must end with an interactive quiz
- Lessons should be short and completable in one sitting
- Code examples should be minimal but compilable — no pseudo-code
- Primary source link required in every lesson

## Teaching the Principles

This workspace was set up mid-course (after lessons 1–4 existed). Lessons 5 and 6 must be built applying all teaching principles from scratch. Existing lessons 1–4 were generated before proper skill was applied — future sessions should audit and fix quiz answer lengths.

## Serving Lessons

Always serve lessons via HTTP (not file://). Relative CSS/JS imports break over file://.

```
cd /Users/vishal/learn/tutorials/go-db-scheduler
python3 -m http.server 8765
```

Then open: http://localhost:8765/

## Vocabulary (Ubiquitous Language)

- **Fleet** — all servers and databases under management (currently 20K DBs / 5K servers)
- **Policy** — a rule that generates jobs dynamically from inventory (template, not instance)
- **Job** — a single scheduled operation against a single database (generated, not stored)
- **Executor** — the engine-specific code that runs a job (SQLServerExecutor, PostgreSQLExecutor)
- **Orchestrator** — the component that drains the job queue, enforces concurrency, detects conflicts
- **Thundering herd** — when thousands of jobs start simultaneously, saturating I/O
- **Stagger** — distributing job start times across a maintenance window using a deterministic hash
- **Exactly-once** — ensuring a job runs exactly once across all scheduler nodes
- **Tick loop** — the periodic scheduling cycle (cron tick → generate jobs → enqueue)

## Fleet Context

- Dual-engine: SQL Server (T-SQL) + PostgreSQL
- Maintenance window: typically 1 AM – 5 AM, IANA timezone-aware
- Concurrency cap: `MaxConcurrentOps` per server (50–200 globally, throttled per server)
- Job duration range: 5 seconds (health check) to 12 hours (CHECKDB on 10 TB)
