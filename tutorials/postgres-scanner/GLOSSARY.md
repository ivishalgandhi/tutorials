# PostgreSQL for Scanner Builders — Glossary

Terms are added here only once the user has demonstrated they can use the concept correctly, not just that they've been introduced to it.

## Connection Model

**backend process**:
The OS process PostgreSQL forks for each client connection. One process per connection, lives until the connection closes.
_Avoid_: connection thread, connection handler

**max_connections**:
The hard server-wide limit on simultaneous client connections. Exceeding it produces `FATAL: sorry, too many clients already`.
_Avoid_: connection limit, connection cap

**postmaster**:
The PostgreSQL supervisor process. Accepts incoming connections and forks a backend process for each one.
_Avoid_: postgres master, main postgres process

## Safety Parameters

**statement_timeout**:
A GUC (session parameter) that cancels any SQL statement running longer than the specified duration (in milliseconds). The primary safety knob for a scanner.
_Avoid_: query timeout

**connect_timeout**:
A DSN parameter (in seconds) that limits how long to wait for a TCP connection to be established. Prevents hanging on dead servers.
_Avoid_: connection timeout (ambiguous)

**lock_timeout**:
A GUC that fails a statement if it cannot acquire a lock within the specified duration. Prevents the scanner from blocking behind production lock holders.

**application_name**:
A GUC that sets a client-visible label shown in `pg_stat_activity`. No functional effect — purely for identification.

## Go Concurrency

**semaphore**:
A concurrency primitive that limits how many goroutines can proceed past a point simultaneously. In Go, implemented as a buffered channel of capacity N.
_Avoid_: throttle, rate limiter (different concept)

**worker pool**:
A fixed set of goroutines that pull work items from a shared channel. Caps memory and concurrency precisely.
_Avoid_: goroutine pool (not standard Go vocabulary)
