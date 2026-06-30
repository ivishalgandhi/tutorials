# PostgreSQL for Scanner Builders

A 6-lesson course on PostgreSQL internals for engineers building Go health-check scanners.

**Goal:** understand PostgreSQL deeply enough to safely scan thousands of production servers you don't own — and know exactly why your scanner behaves the way it does.

## Lessons

| # | Title | Topics |
|---|---|---|
| 1 | What is a PostgreSQL Connection | Process model, cost per connection, safety GUCs, semaphore pattern |
| 2 | pg_stat_activity | Connection saturation, long-running queries, stuck transactions |
| 3 | Replication & Vacuum | Role detection, replication lag, dead tuple accumulation |
| 4 | Error Handling | SQLSTATE codes, `errors.As()`, per-server isolation, error budget |
| 5 | Concurrency | Naive fan-out danger, semaphore, worker pool, pool sizing |
| 6 | pgx v5 | `rows.Values()`, `ConnectConfig`, migration from `database/sql` |

## Browsing

Lessons use relative asset paths — serve over HTTP, not `file://`:

```bash
python3 -m http.server 8765 --directory .
# open http://localhost:8765/lessons/0001-what-is-a-postgres-connection.html
```

## Structure

```
lessons/          HTML lesson files
assets/           Shared CSS, quiz JS, Mermaid init
reference/        Glossary
learning-records/ Post-lesson notes (one per lesson)
MISSION.md        Learning goals and constraints
RESOURCES.md      Reference links
```
