# Claude Certified Architect Resources

## Knowledge

### Official — Primary Sources

- [Anthropic Academy](https://anthropic.skilljar.com/)
  The four official free courses the exam is built on: Agent Skills, Building with the Claude API,
  Introduction to MCP, Claude Code in Action. Complete all four before sitting the exam.

- [Anthropic Docs: Build with Claude](https://docs.anthropic.com/en/docs/build-with-claude/overview)
  Canonical reference for the Messages API, tool use, extended thinking, prompt caching,
  and structured outputs. Primary source for D1, D4, D5.

- [Anthropic Docs: Tool Use Overview](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview)
  Covers tool definitions, `tool_choice`, `strict` mode, parallel tool use. Authoritative for D2.

- [Anthropic Docs: Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
  Cache write/read pricing, TTLs, prefix matching rules, `defer_loading`. Core to D5.

- [Anthropic Docs: Extended Thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
  `budget_tokens`, `display: summarized | omitted`, interaction with tool_choice. Core to D4.

- [Anthropic Docs: Structured Outputs](https://docs.anthropic.com/en/docs/build-with-claude/structured-outputs)
  `output_config.format`, JSON schema constrained decoding. Core to D4.

- [Model Context Protocol — Introduction](https://modelcontextprotocol.io/introduction)
  Official MCP spec. Tools vs Resources vs Prompts, transports (stdio, Streamable HTTP, SSE).
  Primary source for D2.

- [MCP Architecture Guide](https://modelcontextprotocol.io/docs/learn/architecture)
  Host / Client / Server model, message flow, capability negotiation.

- [Claude Code Docs: Hooks Guide](https://docs.anthropic.com/en/docs/claude-code/hooks)
  Hook events, configuration locations, lifecycle. Core to D3.

- [Claude Code Docs: CLAUDE.md](https://docs.anthropic.com/en/docs/claude-code/memory)
  Project constitution hierarchy, what to include/exclude, nested files.

- [Claude Code Docs: Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
  Built-in subagents (Explore, Plan), custom agents, context isolation vs fork.

### Community Study Guides (ranked by GitHub stars)

- [paullarionov/claude-certified-architect ★3,002](https://github.com/paullarionov/claude-certified-architect)
  **Highest-starred community guide.** Covers all 8 exam scenarios with practice questions sourced
  from real exam takers. Multi-language (EN, ES, RU, ZH, JA, KO, IT, AR…). PDF available.
  Raw content saved locally: `/Users/vishal/claude-certified-architect-book/paullarionov-guide-en.md`
  Use for: primary exam drill, authoritative practice questions.

- [daronyondem/claude-architect-exam-guide ★944](https://github.com/daronyondem/claude-architect-exam-guide)
  Scenario-oriented. Central framing: *"where should responsibility live — model or code?"*
  Covers API fundamentals, tool design, MCP, Claude Code, context management. PDF + EPUB.
  Raw content saved locally: `/Users/vishal/claude-certified-architect-book/daronyondem-exam-prep-guide.md`
  Use for: understanding the model-vs-code design principle, anti-pattern checklist.

- [avidevelops/claude-architect-exam-prep ★474](https://github.com/avidevelops/claude-architect-exam-prep)
  Q&A-style breakdown of multi-agent architectures, context management, tool/schema design,
  and batch processing. Best for: Lesson 2 (orchestrator/subagent patterns) and architectural
  tradeoff questions. Raw content saved locally:
  `/Users/vishal/claude-certified-architect-book/avidevelops-exam-prep.md`

- [dnacenta/claude-certified-architect ★24](https://github.com/dnacenta/claude-certified-architect)
  Per-domain deep dives (5 files). Good for: targeted domain review.
  Raw content saved locally: `/Users/vishal/claude-certified-architect-book/dnacenta-d*.md`

- [OlivierAlter/Claude-Certified-Architect-Foundations-Certification-Exam ★125](https://github.com/OlivierAlter/Claude-Certified-Architect-Foundations-Certification-Exam)
  77 scenario-based questions reverse-engineered from the official exam guide. Includes a
  Claude Code skill for interactive exam sessions. Use for: high-volume question drill.

- [NaveenBabuBommisetty/claude-architect-notes](https://github.com/naveenbabubommisetty/claude-architect-notes)
  Domain tutorials, anti-patterns guide, 60 practice questions.

- [amitgambhir/claude-certified-architect-guide](https://github.com/amitgambhir/claude-certified-architect-guide)
  Interactive quiz, traps & gotchas, cheat sheet. Use for: self-testing.

- [Claude Certifications Study Guide](https://claudecertifications.com/claude-certified-architect)
  In-depth guides for all 5 domains, 25 practice questions, 12-week study plan.
  Use for: structured drills, anti-pattern cheatsheets.

- [ankitrahejagatech/claude-certified-architect-prep ★7](https://github.com/ankitrahejagatech/claude-certified-architect-prep)
  **Built by an actual exam passer from the official Anthropic PDF.** Contains 12 official sample
  questions verbatim, domain cheat sheets with distractor-recognition cribsheets, and a browser-based
  interactive practice exam. Central frame: "Prompts are probabilistic. Hooks are deterministic."
  Raw content: `/Users/vishal/claude-certified-architect-book/ankitrahejagatech-*.md`
  Live practice exam: https://ankitrahejagatech.github.io/claude-certified-architect-prep/practice-exam.html
  Use for: **the 12 official sample questions — primary drill tool**.

- [hamzafarooq/claude-certified-architect ★102](https://github.com/hamzafarooq/claude-certified-architect)
  64-question practice exam, domain cheat sheets, sample questions. Live: https://practice-exam-deploy.vercel.app
  Use for: high-volume practice questions.

- [jaysevak/ccaf-practice-exam](https://github.com/jaysevak/ccaf-practice-exam)
  Timed exam + practice mode + domain drill. Single HTML file, works fully offline.
  Live: https://jaysevak.github.io/ccaf-practice-exam/
  Use for: timed simulation closest to exam conditions.

- [aderegil/claude-certified-architect](https://github.com/aderegil/claude-certified-architect)
  6 scenarios, 5 domains, 30 hands-on Python tasks. Closest to the actual production setup the exam describes.
  Use for: hands-on scenario practice.

- [mominurr/cca-f-mock-exam](https://github.com/mominurr/cca-f-mock-exam)
  Full 60-question mock, 120-min timer, per-domain performance analytics.
  Use for: full timed mock before sitting the real exam.

- [SpillwaveSolutions/cca-exam-prep-customer-support](https://github.com/SpillwaveSolutions/cca-exam-prep-customer-support)
  9 Jupyter notebooks, 234 tests, architectural patterns by scenario.
  Use for: deep dive on the Customer Support scenario (most common on the exam).

- [claudecertprep.com](https://claudecertprep.com)
  Free full study guide across all 5 domains, cheat sheet, quiz, mock exam, and flashcards.
  Use for: flashcard-style spaced repetition.

- [Learn with Darin — CCA Lab](https://learn.techwithdarin.com/certs/claude-architect/)
  10-hour hands-on lab plan. Use for: practical exercises beyond these lessons.

- [Zen van Riel: CCA Certification Guide](https://zenvanriel.com/ai-engineer-blog/claude-certified-architect-anthropic-certification-guide/)
  Exam logistics (format, scoring, access), implementation patterns overview.

- [LowCode Agency: How to Become CCA](https://www.lowcode.agency/blog/how-to-become-claude-certified-architect)
  Step-by-step certification process, Partner Network access.

- [Amit Kothari: The Four Academy Courses](https://amitkoth.com/claude-certified-architect-foundations-path/)
  Thoughtful breakdown of the Academy path — argues the courses matter more than the exam.

## Wisdom (Communities)

- [Anthropic Discord](https://discord.gg/anthropic)
  Active developer community. Good for MCP implementation questions and Claude Code edge cases.

- [r/ClaudeAI (Reddit)](https://reddit.com/r/ClaudeAI)
  Community discussion, exam experience reports, study tips.

- [Claude Partner Network](https://www.anthropic.com/partners)
  Required for exam access (free). Join here to unlock Anthropic Academy certification path.

## Gaps
- No official exam blueprint published by Anthropic — all domain weights are third-party reported
- Official practice exam / sample questions: not yet published as of June 2026
- Advanced certifications (Developer, advanced Architect): announced but not yet released
