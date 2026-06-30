# Mission: Concurrent Database Job Scheduler in Go

## Why
I manage a fleet of 20,000 databases across 5,000 servers (SQL Server and PostgreSQL) and am preparing for cloud scale. I am building a production-grade, policy-driven maintenance scheduler in Go — a real system that must coordinate backups, integrity checks, index maintenance, and vacuums across this fleet without duplicated jobs, thundering herds, or missed maintenance windows. Go is new to me (under 6 months). I am learning the distributed systems patterns _and_ the Go idioms at the same time, with a real system to ship.

## Success looks like
- I can implement a worker pool in Go using buffered channels as semaphores and explain why it works
- I can write a conflict-detection loop that prevents a backup and an integrity check from running on the same database simultaneously
- I can implement graceful shutdown (SIGTERM → drain → exit) without killing an in-progress backup
- I can instrument a Go scheduler with Prometheus counters, gauges, and histograms and read a Grafana dashboard of the output
- I can write the SQL Server T-SQL and PostgreSQL SQL for each maintenance operation (backup, integrity check, index rebuild, vacuum)
- I can deploy the scheduler to Kubernetes and explain what the leader-election and distributed-lock primitives are doing in production

## Constraints
- Go beginner (< 6 months) — every Go-specific pattern needs explanation, not just code
- Running against production databases I own — correctness and safety trump cleverness
- Dual-engine (SQL Server + PostgreSQL) — solutions must work for both
- Fleet is already at 20K databases / 5K servers, targeting cloud scale

## Out of scope
- Building the inventory / discovery layer (already exists)
- PostgreSQL administration beyond what the executor needs (backups, upgrades)
- Full observability platform (Prometheus + Grafana basics only, not alertmanager, tracing)
