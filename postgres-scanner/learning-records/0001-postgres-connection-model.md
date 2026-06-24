# PostgreSQL connection model and scanner safety parameters

User disclosed strong prior knowledge: already scans ~3,000 servers/minute with 40–50 checks each, using `database/sql` in Go. Core concepts covered and lesson completed: each connection forks a real OS process, `max_connections` is a hard ceiling, and the five safety parameters (`connect_timeout`, `statement_timeout`, `lock_timeout`, `application_name`, `idle_in_transaction_session_timeout`) must be set via `RuntimeParams` before any query runs. Ready for Lesson 2 — which catalog views to query and how to read them.
