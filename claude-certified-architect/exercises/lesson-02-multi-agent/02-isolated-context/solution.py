"""
Exercise 02 — Solution: Isolated Context
========================================
FIXED: The coordinator passes the full document, prior search results, and an
explicit output schema to the subagent. The subagent now has everything it needs.

KEY LESSON:
  Subagents inherit nothing. The prompt is the only channel. If a required fact,
  document, or format is not in the prompt, the subagent cannot produce it.
"""

from typing import Dict


def spawn_subagent(agent_name: str, prompt: str) -> str:
    """Simulates the Task tool: runs in isolation with only the prompt it receives."""

    if "Document:" not in prompt:
        return (
            "Generic analysis: This document appears to discuss a technical topic. "
            "It contains multiple sections and uses specialized terminology."
        )

    document_mentioned = "per-token latency" in prompt
    if document_mentioned:
        return (
            "Structured analysis:\n"
            "  Claim: Token-level latency spikes correlate with prompt-cache misses.\n"
            "  Evidence: Section 3.2 shows p99 latency increased 34 ms after cache eviction.\n"
            "  Output: latency report"
        )

    return f"{agent_name}: processed prompt '{prompt[:50]}...'"


def run_coordinator(document: str, search_results: list[str]) -> str:
    """FIXED: passes the full universe the subagent needs."""

    # FIXED: every required fact is explicitly in the prompt.
    subagent_prompt = f"""Analyze the following document and produce a structured analysis.

Document:
{document}

Prior search results:
{chr(10).join(f"- {r}" for r in search_results)}

Output requirements:
- Return exactly one claim.
- Cite the specific section or evidence from the document.
- End with "Output: <report type>".
"""

    return spawn_subagent("document-analyst", subagent_prompt)


if __name__ == "__main__":
    doc = """
    Title: Latency Analysis of Anthropic API Cache Eviction

    Section 3.2 — Cache-miss correlation
    We observed that per-token latency spikes correlate with prompt-cache misses.
    After the cache was evicted, p99 latency increased by 34 ms on average.
    """

    prior_results = [
        "Source A: prompt caching reduces cost by up to 90% for long prompts.",
        "Source B: cache eviction occurs when TTL expires or prefix no longer matches.",
    ]

    result = run_coordinator(doc, prior_results)
    print("Subagent result:")
    print(result)
