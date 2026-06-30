# Prior knowledge: hands-on Claude experience, formal gaps

Vishal has been actively building with Claude ("vibe coding") as a Director for database reliability.
He has working intuitions about prompting and tool use but has not studied the formal vocabulary of
agentic architecture, MCP, or Claude Code configuration systematically. This means:

- **Strengths:** practical feel for what Claude can do, familiarity with the API at a usage level
- **Gaps:** stop_reason semantics, multi-agent topology patterns, MCP primitives (tools vs resources vs prompts),
  CLAUDE.md hierarchy, hooks vs prompt-based guardrails, prompt caching mechanics

## Implications
- Skip beginner "what is an LLM" content entirely
- Ground every lesson in production design decisions, not toy examples
- Surface anti-patterns prominently — vibe-coders are most likely to have internalized these by accident
- First lesson should tackle the most common vibe-coder mistake: terminating agentic loops by parsing
  Claude's text instead of reading `stop_reason`
