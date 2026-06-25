"""
Exercise 03 — Solution: Failure Propagation
============================================
FIXED: The subagent returns structured error context on timeout. The coordinator
detects the error and retries with a narrower query. The final report is either
complete or explicitly notes the missing dimension.

KEY LESSON:
  Silently returning empty results marks failure as success. Always return
  structured error context so the coordinator can recover intelligently.
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
        raise TimeoutError(f"API call timed out for query: {query}")

    return {
        "status": "success",
        "results": [f"{query}: result 1", f"{query}: result 2"],
    }


async def run_subagent_research(topic: str) -> dict:
    """
    FIXED: on timeout, returns structured error context instead of a fake success.
    """
    query = f"{topic} hydro capacity"
    try:
        return await search_internal_api(query)
    except TimeoutError as e:
        return {
            "status": "error",
            "failure_type": "transient_timeout",
            "attempted_query": query,
            "partial_results": [],
            "alternatives": [
                f"Retry with narrower query: '{topic} hydro run-of-river'",
                "Use cached snapshot from previous run",
            ],
        }


async def run_coordinator(topic: str) -> str:
    """
    FIXED: coordinator checks for error status and applies an alternative strategy.
    """
    hydro_data = await run_subagent_research(topic)

    # If the subagent failed, retry with a narrower query.
    if hydro_data.get("status") == "error":
        fallback_query = f"{topic} hydro run-of-river"
        try:
            fallback = await search_internal_api(fallback_query)
        except TimeoutError:
            fallback = None

        if fallback and fallback.get("status") == "success":
            hydro_data = fallback
        else:
            return (
                "Final report:\n"
                "  • Solar: [stable data from cache]\n"
                "  • Wind: [stable data from cache]\n"
                "  • Hydro: [DATA UNAVAILABLE — internal API timed out after retry; escalate to human]"
            )

    sections = [
        "Solar: [stable data from cache]",
        "Wind: [stable data from cache]",
        f"Hydro: {hydro_data['results']}",
    ]

    return "Final report:\n" + "\n".join(f"  • {s}" for s in sections)


if __name__ == "__main__":
    for i in range(5):
        report = asyncio.run(run_coordinator("renewable energy in Europe"))
        print(f"\nRun {i + 1}:")
        print(report)
