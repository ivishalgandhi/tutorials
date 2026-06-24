# Notes

## User Profile

- Experienced Go developer, new to PostgreSQL internals
- Already has a working scanner (3000 servers, <1 min, 40-50 checks)
- Learning concurrency concepts for the first time alongside Postgres
- Runs against production systems he does not own — safety is the top concern
- Practical orientation: wants to understand *why*, not just *how*

## Teaching Preferences

- Ground every lesson in the scanner mission — avoid abstract Postgres theory
- Code examples should be in Go (pgx v5)
- Prioritize production safety above performance optimization
- Every lesson should have an interactive quiz — storage strength matters here
- Keep lessons short and completable quickly

## Vocabulary

- "Scanner" = the user's Go tool that connects to many Postgres servers
- "Health checks" = the 40-50 SQL queries run per server
- "Polite guest" = a scanner that leaves no mark on the server it inspects

## Serving Lessons

Always serve lessons via HTTP, not file://. Browsers block relative CSS/JS imports on file:// URLs.

Start the local server from the workspace root:
```
python3 -m http.server 8765
```
Then open: http://localhost:8765/lessons/

## Scanner Architecture

Two-phase design:

**Phase 1 — Inventory lookup**
- `connections.toml` holds the inventory database connection details AND the query to fetch server names
- CLI connects to the inventory DB first, runs that query, gets the list of servers to scan

**Phase 2 — Health checks**
- For each server from the inventory, CLI connects concurrently (semaphore-limited)
- Runs all checks from the other TOML files in `checks/` (replication.toml, vacuum.toml, etc.)
- The TOML filename = the category name

Key point: `connections.toml` is special — it's the bootstrap file (inventory DSN + server discovery query).
All other TOML files under `checks/` are health check categories run against each scanned server.

Exact TOML structure not yet shared — assumed `[[checks]]` with `name`, `description`, `sql` fields. Align when user shares actual format.

## Discovered So Far

- User is using `database/sql` for now, may benefit from migrating to `pgx` native
- Key danger: scanner could exhaust `max_connections` on a production server
- Key tools: `statement_timeout`, `lock_timeout`, `connect_timeout`, `pg_monitor` role, `application_name`
