# Exercise 03 — Handle All Four stop_reason Values

## The scenario

A production agent only handles `end_turn` and `tool_use`. In load testing:
- `max_tokens` responses are silently returned as partial text (users get cut-off answers)
- `stop_sequence` is never handled (falls through to an unintended code path)

## What to build

Complete the `handle_stop_reason()` function so it:
1. Returns text on `end_turn`
2. Executes tools and continues on `tool_use`
3. Raises a clear error on `max_tokens` (truncated — don't return partial output silently)
4. Logs and stops cleanly on `stop_sequence`

## Why this matters on the exam

The exam tests that you know each stop_reason's meaning and the correct action for each.
`max_tokens` and `end_turn` look similar (both have text content) but require different handling.
Treating `max_tokens` as `end_turn` is an anti-pattern: it returns truncated output silently.

## Run

```bash
python problem.py   # missing cases fall through silently
python solution.py  # all four cases handled correctly
```
