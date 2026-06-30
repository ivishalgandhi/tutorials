# 0001: Mission and Webhook Basics

## Context
User is on a database administration team. They want to push Zabbix monitoring events into a custom Go application instead of polling the Zabbix API or scraping the frontend. The stored events must be durable and auditable in a relational database.

## Mission
Capture the "why" and "success" criteria in `MISSION.md`:

- Explain push vs. pull for monitoring events.
- Configure a Zabbix webhook media type and action.
- Write a Go HTTP receiver that validates, stores, and responds to webhook deliveries.
- Store events idempotently so retries do not corrupt the audit log.
- Map Zabbix macros to a database schema the DBA team can query.

## Lesson 1: Receiving Zabbix Alerts with a Go Webhook
Updated `lessons/0001-webhook-vs-polling.html` to match the other course folders and include detailed research:

- Webhooks vs. polling decision table.
- Zabbix webhook media type parameters, JavaScript script, timeout/attempt settings, and retry behavior.
- Testing the webhook, including the test-button 3-second timeout trap (ZBX-16716).
- Local Go echo server for testing.
- PostgreSQL schema with `event_id` as primary key.
- Go receiver using `net/http`, `pgx/v5`, and `ON CONFLICT DO NOTHING` with `xmax = 0` to detect duplicates.
- Production checklist: timeouts, TLS, async processing, retention, metrics.
- Interactive `quiz.js` quiz section with 5 retrieval-practice questions.

## Reference
Created `reference/webhook-patterns.html` with glossary, webhooks vs. polling table, macro mapping, and idempotency primitives for PostgreSQL and MySQL/MariaDB.

Created `reference/handoff-checklist.html` with questions to ask when another team manages Zabbix: endpoint/networking, authentication, event scope, payload/macros, retry behavior, testing, and observability.

## Assets
Copied shared `quiz.js` and `mermaid-init.js` from `postgres-scanner` so the new course uses the same interactive components as the existing courses.

## Next possible lessons
- Testing the webhook receiver (unit tests for idempotency and auth).
- Handling Zabbix recovery events and update operations.
- Building a small dashboard or correlation query from `zabbix_events`.
- MySQL/MariaDB variant of the schema and idempotency query.

## Resources used
- Zabbix Manual: Webhook media type (primary source).
- Zabbix Guidelines: Creating webhooks (primary source).
- Zabbix Manual: Macros supported by location (macro availability).
- Zabbix Manual: Sending message (action/media type link).
- ZBX-16716: Webhook media type test timeout (test-button timeout trap).
- gethook.to: Writing a webhook consumer in Go (idempotency pattern).
- Hookbase: Idempotency keys for webhooks (key choice and retention).

## Date
2026-06-24
