# Lesson 02 — Python Exercises: Orchestrator & Subagent Patterns

Three exercises that cover the most-tested multi-agent anti-patterns from Domain 1.
Each has a `problem.py` (broken or incomplete code) and a `solution.py`.

## Setup

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"
```

These exercises simulate the Claude Agent SDK patterns using plain Python so they
are runnable without needing the private Agent SDK package.

## Exercises

| # | Exercise | Concept tested |
|---|----------|----------------|
| 01 | Won't delegate | Coordinator must include `"Task"` in `allowed_tools` to spawn subagents |
| 02 | Isolated context | Subagent prompt must include document, prior results, and output format |
| 03 | Failure propagation | Subagent should return structured error context, not empty success |

## Exam connection

These map directly to the multi-agent failure-tracing table from Domain 1:
- Exercise 01 → "won't delegate" symptom (missing `Task` in `allowed_tools`)
- Exercise 02 → shallow output caused by incomplete context passing
- Exercise 03 → Official Sample Q8 error-propagation pattern

Run each `problem.py` first to see it fail, then read `solution.py` to understand why.
