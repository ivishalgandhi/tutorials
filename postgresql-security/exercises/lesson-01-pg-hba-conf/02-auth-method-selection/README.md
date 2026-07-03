# Exercise 02 — Fix the Auth Methods

## The bug

A new PostgreSQL server has been set up. The DBA came from SQL Server and
configured pg_hba.conf "to get things working quickly". The file has five
security problems — each one a method choice that is either dangerously wrong,
deprecated, or unnecessarily broad.

## Your task

Read `problem.conf`. Identify all five security problems and fix them.
Each problem is on a separate line. The comments tell you what the intent was —
your job is to make the method match the intent securely.

## Scoring

Give yourself 1 point for each correct fix (5 total).

For each line you fix, also answer:
- What is wrong with the current method?
- What should it be, and why?

## Hint

The five methods involved are: `trust`, `md5`, `scram-sha-256`, `peer`, `reject`.
You will not need any others.

## Verify

```sql
-- After reloading, check there are no 'trust' entries on network connections:
SELECT line_number, type, user_name, address, auth_method
FROM pg_hba_file_rules
WHERE auth_method = 'trust' AND type != 'local';
-- Should return 0 rows on a correctly hardened server.

-- Check no md5 entries remain:
SELECT line_number, auth_method FROM pg_hba_file_rules WHERE auth_method = 'md5';
-- Should return 0 rows.
```
