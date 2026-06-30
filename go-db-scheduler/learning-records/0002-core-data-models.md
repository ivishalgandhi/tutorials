# Core Data Models — DBServer, Database, OperationType

The user can read and understand Go struct definitions with field tags, and knows the three core domain types: `DBServer` (host metadata + concurrency cap + maintenance windows), `Database` (fleet inventory item with size, recovery model, exclusions), and `OperationType` (the conflict matrix that prevents incompatible operations from running simultaneously on the same database).

**Evidence:** Completed Lesson 2 with interactive quiz.

**Implications:** Can use `DBServer.MaxConcurrentOps` and `OperationType` conflict matrix without re-explaining in lesson 5. User is comfortable with Go struct syntax. Maintenance window timezone awareness was introduced here — reference it in lesson 5's window-check code.
