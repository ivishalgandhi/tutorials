# Coordination — Leader Election, Distributed Locks, Execution Store

The user understands the exactly-once execution problem in distributed systems: leader election (Redis SET NX with heartbeat) prevents duplicate scheduling in the normal case, while a distributed lock (Lua CAS script for atomic acquire) is defense-in-depth for split-brain scenarios. The execution store tracks job state transitions (pending → running → succeeded/failed/timeout/conflict) and is the shared memory that makes deduplication possible.

**Evidence:** Completed Lesson 4 with interactive quiz.

**Implications:** User has now seen `context.Context`, `select` statements, `defer`, `sync.Mutex`, `atomic.Bool`, and ticker patterns in Go. These don't need re-introducing in lessons 5 and 6. The orchestrator lesson can focus on new concepts: buffered channels as semaphores, `sync.WaitGroup`, and `signal.NotifyContext`.
