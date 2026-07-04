# Exercise 02 — Stop a Goroutine with a Done Channel

## The bug

`printer` in `problem.go` prints numbers forever. There is no way for `main` to ask it to stop,
so the program runs until you press Ctrl+C.

## What to fix

Add a `done chan struct{}` parameter to `printer`. In `main`, close the channel after 100 ms.
Inside `printer`, use a `select` that exits when `done` is closed.

## Why this matters

You will see this pattern again when we build the worker pool and the dispatcher. A closed channel
is the cleanest signal for "no more work" or "stop now".

## Run

```bash
cd exercises/lesson-01-agent-loop/02-done-channel
go run problem.go    # prints forever
```

After fixing:

```bash
go run solution.go   # prints for ~100 ms, then stops
```
