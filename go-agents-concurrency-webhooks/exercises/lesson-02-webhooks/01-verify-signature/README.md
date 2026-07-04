# Exercise 01 — Verify Signature

## The bug

The webhook handler in `problem.go` compares the received signature with the
computed one using `==`. String comparison short-circuits on the first different
byte, so an attacker can measure response times to reconstruct the signature.

## What to fix

Use `hmac.Equal` to compare the decoded signature bytes against the recomputed
bytes. Also parse the `sha256=` prefix from the header instead of comparing
raw hex strings.

## Why this matters

HMAC is a shared secret. A constant-time comparison is the only way to check it
without leaking information through timing. Production webhook providers expect
receivers to implement this correctly.

## Run

```bash
cd exercises/lesson-02-webhooks/01-verify-signature
go run problem.go    # compiles but uses an insecure comparison
```

After fixing:

```bash
go run solution.go   # uses hmac.Equal and parses the raw body correctly
```
