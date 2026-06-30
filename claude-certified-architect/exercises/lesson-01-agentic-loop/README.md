# Lesson 01 — Python Exercises: The Agentic Loop

Three exercises that cover the three most-tested concepts from Domain 1.
Each has a `problem/` (broken or incomplete code) and a `solution/`.

## Setup

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"
```

## Exercises

| # | Exercise | Concept tested |
|---|----------|---------------|
| 01 | Fix the broken loop | Loop termination must use `stop_reason`, not text matching |
| 02 | PreToolUse hook | Deterministic gates for financial operations |
| 03 | Stop-reason handler | Correct handling of all four `stop_reason` values |

## Exam connection

These map directly to the anti-patterns tested in Domain 1 (27% of exam):
- Exercise 01 → "parsing natural language to determine termination" anti-pattern
- Exercise 02 → "prompts are probabilistic / hooks are deterministic" frame
- Exercise 03 → stop_reason table (end_turn / tool_use / max_tokens / stop_sequence)

Run each `problem.py` first to see it fail, then read `solution.py` to understand why.
