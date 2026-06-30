"""
Exercise 02 — Isolated Context
==============================
BUG: The coordinator asks a subagent to "Analyze the document" but never passes the
document text, prior search results, or output format. The subagent has no context
and returns a generic, useless summary.

YOUR TASK:
  1. Run this file and see the generic subagent output.
  2. Find the spawn_subagent call in the coordinator.
  3. Rewrite the prompt to pass the document, prior results, and a structured
     output requirement.
  4. Run again and confirm the subagent output is grounded in the document.

Hint: The subagent's prompt is its universe. If information isn't there, the
subagent cannot use it.
"""

from typing import Dict


def spawn_subagent(agent_name: str, prompt: str) -> str:
    """Simulates the Task tool: runs in isolation with only the prompt it receives."""

    # The subagent only sees what is in the prompt. If the prompt is vague,
    # the best it can do is return a generic answer.
    if "Document:" not in prompt:
        return (
            "Generic analysis: This document appears to discuss a technical topic. "
            "It contains multiple sections and uses specialized terminology. "
            "(No specific claims can be made because the document text was not provided.)"
        )

    # If the document text is present, the subagent can produce a real answer.
    document_mentioned = False
    if "per-token latency" in prompt:
        document_mentioned = True

    if document_mentioned:
        return (
            "Structured analysis:\n"
            "  Claim: Token-level latency spikes correlate with prompt-cache misses.\n"
            "  Evidence: Section 3.2 shows p99 latency increased 34 ms after cache eviction.\n"
            "  Output: latency report"
        )

    return f"{agent_name}: processed prompt '{prompt[:50]}...'"


def run_coordinator(document: str, search_results: list[str]) -> str:
    """BUG: the subagent prompt is missing the document and context it needs."""

    # ------------------------------------------------------------------
    # BUG: this prompt is empty. The subagent has no document and no context.
    # ------------------------------------------------------------------
    subagent_prompt = "Analyze the document and summarize the key findings."
    # ------------------------------------------------------------------

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
