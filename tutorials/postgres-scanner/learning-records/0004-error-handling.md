# Error Handling & Timeouts

Lesson 4 completed. Four error classes: network (*net.OpError), server (*pgconn.PgError with SQLSTATE), context deadline (context.DeadlineExceeded), statement timeout (SQLSTATE 57014). Always use errors.As() not type assertions — pgx wraps errors in chains.

Key SQLSTATE codes: 28000/28P01 = auth failure (no retry), 3D000 = db not found, 42501 = permission denied, 57014 = statement_timeout fired, 55P03 = lock_timeout.

Per-server isolation: each goroutine returns a named ScanResult, deferred recover() catches panics, named returns let the recover block write into the result. Category-level errors (one TOML check timing out) should not abort other categories for the same server — continue with next category.

Error budget: track error rates by class after each scan. >5% unreachable = systemic (inventory stale, network segment). >1% auth_failure = credential rotation problem. Never retry auth failures — they fill pg_log and can trigger account lockout.
