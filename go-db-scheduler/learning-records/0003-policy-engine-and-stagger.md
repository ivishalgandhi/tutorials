# Policy Engine, TargetSelector, and Stagger Algorithm

The user understands how `MaintenancePolicy` acts as a template that generates concrete jobs by joining against live inventory, how `TargetSelector` filters the fleet by engine, tier, region, tags, and size range, and how `StaggerByHash` distributes jobs across a maintenance window to prevent the thundering herd. Dynamic timeouts (`base + sizeGB × perGB`, capped at `MaxTimeout`) were introduced here.

**Evidence:** Completed Lesson 3 with interactive quiz.

**Implications:** The policy engine is "done" from a teaching perspective. Lesson 5 can assume `PolicyGenerator.GenerateAll()` produces a `[]ScheduledJob` slice — we don't need to show how those jobs were generated, only how the orchestrator dispatches them.
