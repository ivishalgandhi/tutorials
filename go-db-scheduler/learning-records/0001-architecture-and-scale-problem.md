# Architecture and the Scale Problem

The user understands why a cron-based approach fails at fleet scale (thundering herd, no conflict detection, no window awareness, static definitions can't survive fleet churn) and can explain the policy-driven alternative. They can describe the 6-layer architecture (Inventory → Policy Generation → Scheduling → Execution → Coordination → Observability) and why each layer exists.

**Evidence:** Completed Lesson 1 with interactive quiz.

**Implications:** Can skip re-introducing the "why" in future lessons. Build on policy-driven framing when explaining the orchestrator — "the orchestrator is what separates generated jobs from executed jobs."
