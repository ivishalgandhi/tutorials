# 01 — Fix the Swap

## Problem

`Swap` receives two `int` values by value. It swaps the local copies, but the original variables in `main` are unchanged.

## Goal

Modify `Swap` so that it takes pointers and swaps the values at those addresses.

## Run

```bash
go run problem.go
```

Expected output after the fix:

```
x = 20, y = 10
```

## Hint

- `*int` is the type of a pointer to an `int`.
- `*a` reads the value at the address stored in `a`.
- Pass `&x` and `&y` from `main`.
