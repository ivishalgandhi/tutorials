# PostgreSQL for Scanner Builders — Resources

## Knowledge

- [Measuring the Memory Overhead of a Postgres Connection — Andres Freund](https://blog.anarazel.de/2020/10/07/measuring-the-memory-overhead-of-a-postgres-connection/)
  Definitive empirical analysis by a Postgres core contributor. Use for: understanding what each connection actually costs in RAM, and why the process model exists.

- [Analyzing the Limits of Connection Scalability in Postgres — Citus Data](https://www.citusdata.com/blog/2020/10/08/analyzing-connection-scalability)
  Why connection count hurts even when you have plenty of RAM — context switching, procarray, lock tables. Use for: explaining to a DBA why you cap your concurrency.

- [Resources Consumed by Idle PostgreSQL Connections — AWS Database Blog](https://aws.amazon.com/blogs/database/resources-consumed-by-idle-postgresql-connections/)
  Empirical measurement: each idle connection uses ~1.5 MB, under load up to ~14.5 MB. Use for: justifying connect-and-close over persistent pooling per server.

- [jackc/pgx — GitHub](https://github.com/jackc/pgx)
  The Go PostgreSQL driver. Use for: all pgx v5 API reference, `RuntimeParams`, `pgxpool` configuration.

- [pgxpool Tuning for High-Concurrency Go Services — Gold Lapel](https://goldlapel.com/grounds/connection-pooling/pgxpool-tuning-high-concurrency)
  Practical guidance on `MaxConns`, `MinConns`, `MaxConnLifetime` for pgxpool. Use for: if scanner ever moves to a persistent-pool model.

- [pgvitals — Production-Tested Health Check Queries](https://github.com/pgvitals/pgvitals)
  Curated SQL across 35+ diagnostic areas: connection saturation, bloat, vacuum lag, replication, wraparound risk. Use for: source of truth for which health-check queries to run and why.

- [fresha/pgdoctor — Read-Only PostgreSQL Health Checks in Go](https://github.com/fresha/pgdoctor)
  Open-source Go health check tool, production-safe, read-only. Use for: reference implementation of safe catalog queries.

- [pg_stat_activity — PostgreSQL Official Docs](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW)
  Official reference for the most important catalog view your scanner will query. Use for: column definitions, what each state means.

- [Runtime Configuration Parameters (GUCs) — PostgreSQL Official Docs](https://www.postgresql.org/docs/current/runtime-config.html)
  Reference for `statement_timeout`, `lock_timeout`, `connect_timeout`, `application_name`, and all other session parameters. Use for: verifying exact behaviour of safety parameters.

- [Predefined Roles (pg_monitor) — PostgreSQL Official Docs](https://www.postgresql.org/docs/current/predefined-roles.html)
  Exact privileges granted by `pg_monitor`. Use for: telling DBAs exactly what role to grant and why.

## Wisdom (Communities)

- [r/PostgreSQL](https://www.reddit.com/r/PostgreSQL/)
  Active community with mix of DBAs and developers. Good for: asking "is this safe to run on production?" questions with real DBA perspectives.

- [Postgres Slack — postgresql.slack.com](https://postgres-slack.herokuapp.com/)
  The largest real-time Postgres community. `#general` and `#performance` channels are high-signal. Use for: getting feedback on scanner design from Postgres internals experts.

## Gaps

- No high-quality resource yet found specifically on **Go concurrency patterns for database scanning at scale** (worker pools, semaphore sizing). May need to derive from first principles and benchmark.
