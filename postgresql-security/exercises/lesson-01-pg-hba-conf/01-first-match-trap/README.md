# Exercise 01 — Spot the First-Match Trap

## The bug

A DBA added a rule to allow the `audit_user` role to connect from the auditor's
laptop (10.0.5.20) using `scram-sha-256`. But `audit_user` can still connect
from *any* IP address without a password. The rule "isn't working".

## Your task

Read `problem.conf`. Find exactly which rule is swallowing the `audit_user` entry
and explain why. Then reorder the rules in `solution.conf` so that:

1. `audit_user` can only connect from 10.0.5.20 with scram-sha-256
2. All other users on the internal network (10.0.0.0/8) still connect with scram-sha-256
3. The local postgres superuser still uses peer
4. Everything else is rejected

## Why this matters

This is the #1 pg_hba.conf mistake for SQL Server DBAs. In SQL Server, you add
a LOGIN rule and it applies regardless of order. In PostgreSQL, the FIRST matching
rule wins — a broad rule higher in the file silently swallows all specific rules below it.

## Verify your answer

```bash
# After reordering, reload and check parsed rules:
SELECT type, database, user_name, address, auth_method
FROM pg_hba_file_rules
ORDER BY line_number;
```
