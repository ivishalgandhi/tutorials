# Mission: PostgreSQL for Scanner Builders

## Why
I am building a Go tool that scans thousands of PostgreSQL servers concurrently, running 40–50 health-check queries per server. I can already hit ~3,000 servers in under a minute. I need to understand the internals deeply enough to guarantee I never harm a production system I don't own — and to know exactly why my scanner behaves the way it does.

## Success looks like
- I can explain to a skeptical DBA why my scanner is safe to run on their production server
- I know which connection parameters to set before a single query runs, and why each one matters
- I can choose and tune a concurrency pattern (worker pool / semaphore) without guessing
- I can read `pg_stat_activity` and other catalog views and know what they're telling me
- I can diagnose a slow or misbehaving scan from first principles

## Constraints
- New to PostgreSQL internals (connection model, catalog views, GUCs)
- New to concurrency concepts (goroutines, semaphores, worker pools)
- Runs against production databases he does not own — safety trumps everything
- Existing tool uses `database/sql`; moving toward `pgx` v5

## Out of scope
- PostgreSQL administration (backups, upgrades, tuning shared_buffers)
- Writing application queries / ORM usage
- Building a full observability platform (just health checks)
