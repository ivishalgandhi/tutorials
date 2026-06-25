"""
Exercise 01 — Solution: Won't Delegate
=======================================
FIXED: The coordinator's allowed_tools list now includes "Task", so it can spawn
subagents. The model is given the tool, and it delegates to parallel researchers.

KEY LESSON:
  The tool whitelist is the control surface. If the coordinator can't see "Task",
  it can't delegate, no matter how strong the system prompt is.
"""

from typing import Dict, List
import asyncio

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

    if "solar" in prompt.lower():
        return "Solar: photovoltaic costs fell 14% in 2024; strong policy tailwinds in Spain and Germany."
    if "wind" in prompt.lower():
        return "Wind: offshore capacity doubled in the North Sea; grid integration remains the bottleneck."
    if "hydro" in prompt.lower():
        return "Hydro: run-of-river upgrades dominate; environmental permits slow new large-scale projects."
    return f"{agent_name}: researched '{prompt[:40]}...'"


async def run_coordinator(topic: str) -> str:
    """FIXED: allowed_tools includes 'Task', so delegation works."""

    # FIXED: "Task" is present, so the coordinator can spawn subagents.
    allowed_tools = ["WebSearch", "ReadFile", "WriteFile", "Task"]

    subtopics = ["solar", "wind", "hydro"]

    if "Task" not in allowed_tools:
        return (
            f"Inline answer about {topic}: renewable energy is growing. "
            "Solar and wind are the main drivers. Hydro is also important."
        )

    results = await asyncio.gather(
        *[spawn_subagent("researcher", f"Research {subtopic} for {topic}") for subtopic in subtopics]
    )

    return f"Synthesized report on {topic}:\n" + "\n".join(f"  • {r}" for r in results)


if __name__ == "__main__":
    output = asyncio.run(run_coordinator("renewable energy in Europe"))
    print(output)
