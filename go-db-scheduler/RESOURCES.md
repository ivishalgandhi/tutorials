# Go Database Job Scheduler — Resources

## Knowledge

- [Effective Go — Concurrency section — golang.org](https://go.dev/doc/effective_go#concurrency)
  The canonical Go reference for goroutines, channels, and the buffered channel semaphore pattern. Use for: understanding _why_ buffered channels work as semaphores before using them in the worker pool.

- [Go Concurrency Patterns: Pipelines and Cancellation — Go Blog](https://go.dev/blog/pipelines)
  Official Go Blog deep-dive on channels, cancellation via `done` channels, and pipeline fan-in/fan-out. Use for: designing the job channel and drain logic in the orchestrator.

- [GopherCon 2018: Rethinking Classical Concurrency Patterns — Bryan C. Mills](https://sourcegraph.com/blog/go/gophercon-2018-rethinking-classical-concurrency-patterns)
  Rigorous treatment of worker pools, semaphores, and why "goroutine per task" is often wrong. Use for: choosing between worker pool and dynamic goroutine approaches.

- [Go Worker Pool Pattern: Production-Ready Concurrency — BackendBytes](https://backendbytes.com/articles/go-worker-pool-concurrency/)
  Practical guide: buffer sizing, backpressure, context cancellation, WaitGroup drain. Use for: implementing the worker pool in lesson 5.

- [os/signal — NotifyContext — pkg.go.dev](https://pkg.go.dev/os/signal#NotifyContext)
  Official API reference for `signal.NotifyContext`. Use for: implementing graceful shutdown (SIGTERM → drain → exit) in lesson 5.

- [Graceful Shutdown in Go: Practical Patterns — VictoriaMetrics](https://victoriametrics.com/blog/go-graceful-shutdown/)
  Production patterns for SIGTERM, context propagation, and draining in-flight work. Use for: the graceful shutdown section of the orchestrator.

- [Instrumenting a Go application for Prometheus — Prometheus Docs](https://prometheus.io/docs/guides/go-application/)
  Official step-by-step guide: Counter, Gauge, Histogram, promauto, /metrics endpoint. Use for: all Prometheus instrumentation in lesson 6.

- [prometheus package — pkg.go.dev](https://pkg.go.dev/github.com/prometheus/client_golang/prometheus)
  Complete API reference for the Go Prometheus client library. Use for: exact method signatures, metric type selection.

- [BACKUP (Transact-SQL) — Microsoft Learn](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-transact-sql?view=sql-server-ver16)
  Authoritative syntax reference for `BACKUP DATABASE` and `BACKUP LOG`. Use for: the SQL Server executor's T-SQL in lesson 6.

- [DBCC CHECKDB — Microsoft Learn](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-checkdb-transact-sql?view=sql-server-ver16)
  Official reference for `DBCC CHECKDB` options (`WITH NO_INFOMSGS`, `PHYSICAL_ONLY`, `ESTIMATEONLY`). Use for: the integrity check executor.

- [ALTER INDEX REBUILD — Microsoft Learn](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-index-transact-sql?view=sql-server-ver16)
  Reference for `ALTER INDEX ALL ON ... REBUILD WITH (ONLINE=ON)`. Use for: the index rebuild executor.

- [VACUUM — PostgreSQL Documentation](https://www.postgresql.org/docs/current/sql-vacuum.html)
  Authoritative reference for `VACUUM`, `VACUUM FULL`, `VACUUM ANALYZE`, options and locking behaviour. Use for: the PostgreSQL vacuum executor.

- [REINDEX — PostgreSQL Documentation](https://www.postgresql.org/docs/current/sql-reindex.html)
  Syntax and CONCURRENTLY option for `REINDEX DATABASE`. Use for: the PostgreSQL index rebuild executor.

- [Routine Vacuuming — PostgreSQL Documentation](https://www.postgresql.org/docs/current/routine-vacuuming.html)
  Why autovacuum isn't enough for high-churn tables, and how to manually supplement it. Use for: explaining why the scheduler runs VACUUM at all.

## Wisdom (Communities)

- [r/golang](https://www.reddit.com/r/golang/)
  Active community for Go questions. Good for: asking about concurrency patterns, channel sizing, real-world scheduler implementations.

- [Gophers Slack — gophers.slack.com](https://invite.slack.golangbridge.org/)
  The largest Go community. `#general`, `#concurrency`, and `#performance` are high-signal. Use for: reviewing the worker pool design before shipping.

- [r/SQLServer](https://www.reddit.com/r/SQLServer/)
  DBA community for SQL Server questions. Use for: asking about backup T-SQL edge cases, CHECKDB timeout recommendations for large databases.

## Gaps

- No high-quality resource yet found on **per-server semaphore sizing in production database schedulers** (how to calibrate `MaxConcurrentOps` per server type/hardware). May need to derive from benchmarks on real fleet.
- No comprehensive resource on **Go scheduler patterns for dual-engine (SQL Server + PostgreSQL) fleets**. Most examples are single-engine.
