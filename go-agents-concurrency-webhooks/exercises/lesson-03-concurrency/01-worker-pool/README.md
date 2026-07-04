# Exercise 01 — Worker Pool

## The bug

`problem.go` receives a list of jobs and starts one goroutine for each job. If the list is large, the program can create thousands of goroutines at once, exhaust memory, and open too many connections or file descriptors.

## What to fix

Rewrite the program as a fixed worker pool:

1. Create a `jobs` channel and a `results` channel.
2. Start a fixed number of worker goroutines that read from `jobs` and write to `results`.
3. Use `sync.WaitGroup` to wait for all workers to finish.
4. Close the `jobs` channel after sending all work.
5. Collect results from the `results` channel until it is closed.

## Why this matters

A webhook agent that receives a burst of events can easily spawn one goroutine per event. A worker pool caps the number of concurrent workers, keeps memory usage predictable, and makes graceful shutdown simpler.

## Run

```bash
cd exercises/lesson-03-concurrency/01-worker-pool
go run problem.go    # creates many goroutines at once
```

After fixing:

```bash
go run solution.go   # uses a fixed pool of 3 workers
```
