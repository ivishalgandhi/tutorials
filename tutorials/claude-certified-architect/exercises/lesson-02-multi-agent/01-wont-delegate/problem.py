"""
Exercise 01 — Won't Delegate
==========================
BUG: The coordinator has a `researcher` subagent defined, but its `allowed_tools`
list does not include "Task". The model has no way to delegate, so it answers inline
and the report covers only one dimension.

YOUR TASK:
  1. Run this file and see the inline answer.
  2. Find the coordinator's allowed_tools list.
  3. Add "Task" so the coordinator can invoke spawn_subagent.
  4. Run again and confirm the coordinator spawns parallel subagents.

Hint: The tool harness is the only thing that prevents delegation here.
"""

from typing import Dict, List
import asyncio

# Simulated subagent roster. In a real Agent SDK this is the `agents` dict.
AGENTS = {
    "researcher": {
        "description": "Research a sub-topic and return a concise summary with sources.",
        "tools": ["WebSearch"],
    }
}


async def spawn_subagent(agent_name: str, prompt: str) -> str:
    """Simulates the Task tool: runs a subagent in isolation and returns its result."""
    if agent_name not in AGENTS:
        return f"Error: unknown agent '{agent_name}'"

    # Simulate the subagent doing real work.
    if "solar" in prompt.lower():
        return "Solar: photovoltaic costs fell 14% in 2024; strong policy tailwinds in Spain and Germany."
    if "wind" in prompt.lower():
        return "Wind: offshore capacity doubled in the North Sea; grid integration remains the bottleneck."
    if "hydro" in prompt.lower():
        return "Hydro: run-of-river upgrades dominate; environmental permits slow new large-scale projects."
    return f"{agent_name}: researched '{prompt[:40]}...'"


async def run_coordinator(topic: str) -> str:
    """BUG: allowed_tools is missing 'Task', so the coordinator cannot delegate."""

    # ------------------------------------------------------------------
    # BUG: "Task" is missing from this list. The model cannot spawn subagents.
    # ------------------------------------------------------------------
    allowed_tools = ["WebSearch", "ReadFile", "WriteFile"]
    # ------------------------------------------------------------------

    subtopics = ["solar", "wind", "hydro"]

    if "Task" not in allowed_tools:
        # Without the Task tool, the coordinator has no mechanism to delegate.
        # It falls back to an inline answer, which is shallow and misses dimensions.
        return (
            f"Inline answer about {topic}: renewable energy is growing. "
            "Solar and wind are the main drivers. Hydro is also important. "
            "(No subagents were spawned because 'Task' is not in allowed_tools.)"
        )

    # This path is unreachable until the bug above is fixed.
    results = await asyncio.gather(
        *[spawn_subagent("researcher", f"Research {subtopic} for {topic}") for subtopic in subtopics]
    )

    return f"Synthesized report on {topic}:\n" + "\n".join(f"  • {r}" for r in results)


if __name__ == "__main__":
    output = asyncio.run(run_coordinator("renewable energy in Europe"))
    print(output)
