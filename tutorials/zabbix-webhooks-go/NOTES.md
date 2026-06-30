# Teaching Notes

## User preferences
- Course pages and lessons should visually match the existing tutorial folders (`postgres-scanner`, `claude-certified-architect`).
  - Use the shared `assets/style.css` and the same lesson-meta / card list patterns.
- Lessons must include the interactive `quiz.js` widget used by the other courses (not static numbered quizzes).
- Do detailed web research before writing content; ground claims in Zabbix docs, Zabbix Jira issues, and Go best-practice articles.
- Cite sources inline with links so the lesson is trustworthy.

## Course conventions
- Course index: `index.html` with `assets/style.css`, `.lesson-list` cards, `.lesson-num`, `.lesson-title`, `.lesson-topics`.
- Lessons: `../assets/style.css`, `../assets/quiz.js`, `../assets/mermaid-init.js`, Mermaid sequence diagrams, callouts, and a `.quiz-section` at the end.
- References: `../assets/style.css`, glossary tables, and quick lookup tables.
