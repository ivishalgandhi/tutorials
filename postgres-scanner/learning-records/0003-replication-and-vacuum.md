# Replication Lag & Vacuum Health

Lesson 3 teaches two scanner checks beyond connection activity.

**Replication:** pg_is_in_recovery() tells you the server's role (primary=false, replica=true). The key pattern is one query that handles both roles, using NULL for columns that don't apply. The LSN equality check (pg_last_wal_receive_lsn() = pg_last_wal_replay_lsn()) prevents false-positive lag on idle primaries. Thresholds: <10s healthy, 10–60s warning, >60s critical.

**Vacuum:** pg_stat_user_tables.n_dead_tup tracks dead tuple accumulation left by UPDATE/DELETE under MVCC. Dead_pct = 100 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0). NULLIF protects division by zero on empty tables. Thresholds: <5% healthy, 5–20% warning, >20% critical. Zero rows from the check = healthy result.

**TOML files:** checks/replication.toml (replication_status), checks/vacuum.toml (vacuum_health). Both follow the zero-rows-is-pass pattern from Lesson 2.

**Full scanner loop:** one connection per server, three TOML category files (activity, replication, vacuum), runCategory for each, close connection. Ready for Lesson 4: error handling and timeout patterns.
