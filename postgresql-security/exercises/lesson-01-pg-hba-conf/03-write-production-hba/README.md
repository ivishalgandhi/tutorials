# Exercise 03 — Write a Production pg_hba.conf from Requirements

## The scenario

You are hardening a new PostgreSQL 16 cluster for a SaaS application.
The architect has given you these requirements:

```
Cluster: myapp (single database named myapp)

Roles:
  postgres       — superuser, only accessed from the local OS
  app_user       — application service account, connects from 10.0.1.0/24
  ci_migrate     — CI/CD migration runner, connects from 10.0.2.50 only
  readonly_user  — analytics/reporting, connects from 10.0.3.0/24
  dba_admin      — DBA admin, connects from 10.0.4.10 only

Security requirements:
  - All network connections must use TLS (no plaintext TCP)
  - All network connections must use scram-sha-256
  - The postgres superuser must NOT be reachable over the network
  - The CI/CD runner must be locked to its exact IP — not a subnet
  - Everything not explicitly allowed must be rejected
  - Local (Unix socket) connections for postgres use peer auth
```

## Your task

Write the complete `pg_hba.conf` in `answer.conf`.
There is no skeleton — start from scratch.

When you are done, check `solution.conf` to compare.

## Checklist before you submit

- [ ] Local postgres peer rule present
- [ ] postgres has NO network (host/hostssl) entry
- [ ] All host entries use hostssl, not host
- [ ] All host entries use scram-sha-256
- [ ] ci_migrate rule uses /32 (single IP), not a subnet
- [ ] Catch-all reject rule is the LAST entry
- [ ] Rules are ordered: most specific first, broadest last

## Verify (if you have a live cluster)

```sql
-- Check no network entry allows postgres:
SELECT * FROM pg_hba_file_rules
WHERE 'postgres' = ANY(user_name) AND type IN ('host','hostssl','hostnossl');
-- Should return 0 rows.

-- Check all network entries use scram-sha-256:
SELECT line_number, type, user_name, address, auth_method
FROM pg_hba_file_rules
WHERE type IN ('host','hostssl') AND auth_method != 'scram-sha-256';
-- Should return 0 rows (reject entries have no auth_method, ignore those).
```
