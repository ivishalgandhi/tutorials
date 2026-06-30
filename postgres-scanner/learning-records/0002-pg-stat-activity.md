# pg_stat_activity — three scanner queries introduced

Lesson 2 completed. pg_stat_activity: the state column (active / idle / idle in transaction), why idle-in-transaction is dangerous (blocks autovacuum via snapshot retention), and three queries — connection saturation, long-running queries, stuck transactions. Two-phase scanner architecture established: connections.toml bootstraps inventory lookup (Phase 1), checks/*.toml fan out concurrently per server (Phase 2). rows.Values() vs Scan() distinction understood. Ready for Lesson 3: replication lag and vacuum health.
