# Lesson 01 — Exercises: pg_hba.conf

Three exercises covering the three most-tested concepts from Lesson 1.
Each has a `problem.conf` (broken or incomplete) and a `solution.conf`.

## How to work through these

1. Read the README in each exercise directory.
2. Open `problem.conf` — diagnose or complete it without looking at the solution.
3. Write your answer, then open `solution.conf` to compare.
4. Read the explanation in the solution file header — the *why* matters more than the *what*.

## Exercises

| # | Exercise | Concept tested |
|---|----------|---------------|
| 01 | Spot the first-match trap | Rule ordering silently swallows specific rules |
| 02 | Fix the auth methods | trust/md5/scram-sha-256 — which and when |
| 03 | Write a production hba | Build a correct, complete pg_hba.conf from requirements |

## Exam connection (DBA competency check)

These map directly to the mistakes a SQL Server DBA makes when first encountering pg_hba.conf:

- Exercise 01 → "I added a rule but it doesn't seem to apply" — first-match semantics
- Exercise 02 → "I'll just use trust internally" — understanding auth method blast radius
- Exercise 03 → Synthesising all rules into a coherent, secure, ordered policy

## Setup

No server required. These are static file exercises — read, diagnose, rewrite.
If you want to test live, any PostgreSQL instance works:

```bash
psql -c "SHOW hba_file;"        # find your pg_hba.conf
psql -c "SELECT pg_reload_conf();"  # reload after edits (no restart)
psql -c "SELECT * FROM pg_hba_file_rules;"  # verify parsed rules
```
