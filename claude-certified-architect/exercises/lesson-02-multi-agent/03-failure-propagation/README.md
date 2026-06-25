# Exercise 03 — Failure Propagation

## Concept

When a subagent fails, it must return structured error context so the coordinator
can decide whether to retry, route around, or escalate. Returning empty results
marked as success masks the failure and corrupts the final report.

## The bug

The `problem.py` simulates an internal API search that times out. The subagent
catches the timeout and returns an empty list with a status of `"success"`. The
coordinator publishes a report that silently omits that dimension.

## Your task

1. Run `problem.py` and see the final report published with missing data.
2. Find the `search_internal_api` subagent.
3. Change the return value on timeout to a structured error dict with:
   - `failure_type`,
   - `attempted_query`,
   - `partial_results`,
   - `alternatives`.
4. Update the coordinator to detect the error and retry with an alternative query.

## Exam connection

This is Official Sample Q8: the best error propagation approach returns
structured context to the coordinator so it can make an intelligent recovery decision.
