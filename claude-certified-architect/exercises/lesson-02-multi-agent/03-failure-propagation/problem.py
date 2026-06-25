"""
Exercise 03 — Failure Propagation
=================================
BUG: An internal API search subagent times out. It catches the exception and
returns an empty result list with status "success". The coordinator trusts the
status and publishes a report with missing data.

YOUR TASK:
  1. Run this file and see the final report contain "Hydro: []" — a silent gap.
  2. Find the `search_internal_api` function.
  3. On timeout, return a structured error dict instead of empty results.
  4. Update the coordinator to detect the error and retry with a narrower query.

Hint: Masks empty as success → bad. Structured error context → good.
"""

import asyncio
import random


async def search_internal_api(query: str) -> dict:
    """
    Simulates a query to an internal knowledge API.
    Randomly times out to demonstrate failure handling.
    """
    if random.random() < 0.6:
        await asyncio.sleep(0.05)
        # Simulate a network timeout.
        raise TimeoutError(f"API call timed out for query: {query}")

    return {
        "status": "success",
        "results": [f"{query}: result 1", f"{query}: result 2"],
    }


async def run_subagent_research(topic: str) -> dict:
    """
    BUG: catches the timeout and returns an empty success response.
    The coordinator cannot tell that a failure occurred.
    """
    try:
        return await search_internal_api(f"{topic} hydro capacity")
    except TimeoutError:
        # ------------------------------------------------------------------
        # BUG: masks failure as success. The coordinator will trust this.
        # ------------------------------------------------------------------
        return {"status": "success", "results": []}
        # ------------------------------------------------------------------


async def run_coordinator(topic: str) -> str:
    """Coordinator that trusts subagent results and synthesizes a report."""
    hydro_data = await run_subagent_research(topic)

    sections = []
    sections.append(f"Solar: [stable data from cache]")
    sections.append(f"Wind: [stable data from cache]")
    sections.append(f"Hydro: {hydro_data['results']}")

    return "Final report:\n" + "\n".join(f"  • {s}" for s in sections)


if __name__ == "__main__":
    # Run a few times to hit the timeout.
    for i in range(5):
        report = asyncio.run(run_coordinator("renewable energy in Europe"))
        print(f"\nRun {i + 1}:")
        print(report)
        if "Hydro: []" in report:
            print("  -> BUG: hydro data is silently missing from the report!")
            break
