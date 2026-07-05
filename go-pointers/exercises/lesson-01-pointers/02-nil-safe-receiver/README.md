# 02 — Nil-Safe Receiver

## Problem

Calling `Log` on a nil `*Logger` causes a panic because the method dereferences `l.Prefix` without checking `l` first.

## Goal

Make the method nil-safe. It should print the message without a prefix when the receiver is nil, and print normally when it is not.

## Run

```bash
go run problem.go
```

Expected output after the fix:

```
hello
app: world
```

## Hint

- A pointer receiver can be `nil`.
- Add `if l == nil { ...; return }` at the start of the method.
- Keep the method useful for both nil and non-nil receivers.
