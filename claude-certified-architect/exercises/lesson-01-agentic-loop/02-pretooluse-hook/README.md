# Exercise 02 — PreToolUse Hook: Deterministic Gate

## The scenario

A customer support agent has three tools: `get_customer`, `lookup_order`, `process_refund`.
Production data shows it occasionally calls `process_refund` without first verifying the
customer via `get_customer` — causing incorrect refunds.

A stronger system prompt was tried. Few-shot examples were added. The error rate dropped
from 12% to 2% but never to 0%.

## What to build

Add a `PreToolUse` hook (implemented as a prerequisite check in the tool dispatcher)
that **blocks** `process_refund` from running unless `get_customer` has already been
called and returned a verified customer ID in this session.

## Why this matters on the exam

This is Official Sample Question #1 verbatim. The answer is always:
**programmatic prerequisite → 100% deterministic, not ~98% probabilistic**.

The exam will offer "stronger system prompt" and "more few-shot examples" as distractors.
Those are wrong because 2% failure on a financial operation = real customers get wrong refunds.

## Run

```bash
python problem.py   # observe: refund can fire without identity verification
python solution.py  # correct: refund is blocked until get_customer succeeds
```
