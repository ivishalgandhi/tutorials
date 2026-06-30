# Mission: Zabbix Webhooks in Go for Database Reliability

## Why
My team is responsible for database administration. We run Zabbix for monitoring and want to push
alert events into a custom Go application instead of polling the Zabbix API or scraping the frontend.
Webhooks let us react to problems (and recoveries) in near real time, keep a durable audit trail in a
database, and build downstream automation such as paging, runbook links, and correlation with other
event sources.

## Success looks like
- I can explain the difference between push (webhooks) and pull (polling) for monitoring events and pick the right one for a given situation.
- I can configure a Zabbix webhook media type and action that POSTs structured event data to a custom endpoint.
- I can write a Go HTTP server that receives the webhook, validates it, and stores the event in a database.
- I can make the receiver idempotent so retries, duplicate alerts, and concurrent deliveries do not corrupt the event log.
- I can read the Zabbix event macros and map them to a database schema the DBA team can query.

## Constraints
- Zabbix is already running; the focus is on the integration, not installing Zabbix itself.
- The Go application must be small, testable, and operable by a DBA team without a full platform engineering stack.
- Storage must be durable and auditable (a relational database such as PostgreSQL or MySQL/MariaDB).
- Network boundaries, proxies, and TLS are realistic concerns; the examples should address them.
- Prefer code and patterns that work with standard library `database/sql` plus `pgx`/`lib/pq` or `go-sql-driver/mysql`, not a custom framework.

## Out of scope
- Installing or tuning the Zabbix server itself.
- Replacing Zabbix's internal alerting; this is about augmenting it with a custom receiver.
- Building a full incident-management workflow (paging, escalation, on-call scheduling).
- Advanced authentication schemes beyond a shared secret / bearer token and TLS; OAuth and mTLS are noted but not primary.
- WebSocket, SSE, or other streaming event transports.
