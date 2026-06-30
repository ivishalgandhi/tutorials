# Zabbix Webhooks in Go — Resources

## Knowledge

### Zabbix — Primary Sources

- [Zabbix Manual: Webhook media type](https://www.zabbix.com/documentation/current/en/manual/config/notifications/media/webhook)
  Official reference for the webhook media type: parameters, JavaScript script body, macros, return
  values, and the `Process tags` option. Use this when configuring the Zabbix side of the integration.

- [Zabbix Guidelines: Creating webhooks](https://www.zabbix.com/documentation/guidelines/en/webhooks)
  Quality guidelines for webhook scripts: input validation, response validation, required macros
  (`{ALERT.SUBJECT}`, `{ALERT.MESSAGE}`, `{ALERT.SENDTO}`, `{EVENT.SOURCE}`, `{EVENT.VALUE}`), logging,
  and tag handling. Use this to write robust webhook JavaScript and avoid common Zabbix pitfalls.

- [Zabbix Manual: Webhook script examples](https://www.zabbix.com/documentation/current/en/manual/config/notifications/media/webhook/webhook_examples)
  Official Jira, Slack, and other example scripts. Good for seeing how `JSON.parse(value)`,
  `HttpRequest()`, and `Zabbix.log()` are used in practice.

- [Zabbix Manual: Macros supported in notifications](https://www.zabbix.com/documentation/current/en/manual/config/notifications/media)
  Macro reference for message templates and webhook parameters. Essential for mapping event
  fields (event ID, clock, severity, host, trigger name, tags, recovery value) into the JSON payload.

- [Zabbix API: Event object](https://www.zabbix.com/documentation/current/en/manual/api/reference/event/object)
  REST API documentation for the `event` object (`eventid`, `source`, `object`, `clock`, `value`,
  `severity`, `r_eventid`, etc.). Useful because the same fields appear in webhook macros and help
  design the receiver's database schema.

- [Zabbix Manual: Macros supported by location](https://www.zabbix.com/documentation/current/en/manual/appendix/macros/supported_by_location)
  Authoritative list of which macros resolve in which context. Use this to confirm that
  `{EVENT.ID}`, `{EVENT.CLOCK}`, `{EVENT.SEVERITY}`, `{EVENT.TAGSJSON}`, and host/trigger macros are
  available in trigger-based webhook notifications.

- [Zabbix Manual: Sending message](https://www.zabbix.com/documentation/current/en/manual/config/notifications/action/operation/message)
  How action operations send messages to a media type. Explains the link between actions, media
  types, users/user groups, and the Action log.

- [ZBX-16716: Webhook media type test timeout](https://support.zabbix.com/browse/ZBX-16716)
  Known issue: the media type test button uses a hard-coded 3-second connection timeout, independent
  of the media type's configured Timeout. Important when testing slow or remote receivers.

### Go Webhook Receivers — Best Practice Articles

- [gethook.to: Writing a webhook consumer in Go](https://gethook.to/blog/writing-a-webhook-consumer-in-go)
  Practical Go patterns: idempotency with `ON CONFLICT DO NOTHING`, `xmax = 0` trick for
  insert-or-skip, signature verification, and atomic transactions. Strongly recommended for the
  database idempotency section.

- [Hookbase: Idempotency keys for webhooks](https://www.hookbase.app/blog/idempotency-keys-for-webhooks)
  Choosing the right idempotency key, why not to hash the whole body, atomic insert patterns, and
  retention windows. Use this to reason about key choice and cleanup.

- [137Foundry: Building a webhook receiver that handles production traffic](https://137foundry.com/articles/webhook-receiver-production-guide)
  Production checklist: retries, signature verification, timestamp windows, idempotency store, and
  queueing. Good for the operations checklist in the reference document.

- [Sesame Disk: Implementing idempotent webhook receivers in Go](https://sesamedisk.com/implementing-idempotent-webhook-receiver-in-go/)
  Idempotency key strategies, PostgreSQL schema examples, and locking patterns. Useful for
  multi-tenant and state-machine variants.

## Skills

- Go standard library: `net/http`, `crypto/hmac`, `encoding/json`, `database/sql`.
- PostgreSQL: `ON CONFLICT`, `RETURNING`, `xmax` system column, advisory locks (if needed).
- MySQL/MariaDB: `INSERT ... ON DUPLICATE KEY UPDATE` as the equivalent idempotency primitive.
- Zabbix frontend: Alerts → Media types → Webhook, and Configuration → Actions → Operations.

## Wisdom (Communities)

- [r/zabbix](https://reddit.com/r/zabbix) — practical integrations, webhook scripts, and troubleshooting.
- [Zabbix Community Forum](https://www.zabbix.com/forum) — official forum for integration questions.
- [Go Forum](https://forum.golangbridge.org/) — idiomatic Go and `database/sql` questions.
- [Postgres Slack](https://postgres-slack.herokuapp.com/) — PostgreSQL patterns for idempotency and locking.

## Gaps
- Zabbix webhook documentation is mostly about sending *to* external SaaS tools; there is no
  official "how to write a custom receiver" guide, so we synthesize the receiver side from the Go
  webhook best-practice literature.
- The exact payload shape depends on the macros and JavaScript you write in the webhook script; it
  is not fixed by Zabbix. This is a strength (flexibility) and a source of bugs if not documented.
