# Exercise 01 — Fix the Broken Loop

## The bug

The loop in `problem.py` terminates by checking if Claude's text response contains
the phrase `"Task complete"`. Run it a few times — it sometimes hangs forever.

## What to fix

Replace the text-matching termination with the correct machine-readable signal:
`response.stop_reason == "end_turn"`.

## Why this matters on the exam

This is the #1 tested anti-pattern in Domain 1. The exam describes a loop that
"occasionally hangs in production" and asks for the root cause. The answer is always:
**natural language termination is unreliable — use stop_reason**.

## Run

```bash
python problem.py   # observe: sometimes loops forever
python solution.py  # correct: always terminates cleanly
```
