"""
Exercise 01 — Solution: Fix the Broken Loop
=============================================
FIXED: The loop now uses stop_reason == "end_turn" as the only termination signal.
max_tokens is handled explicitly as an error condition, not silently ignored.

KEY LESSON:
  stop_reason is a machine-readable contract between the API and your code.
  Text matching is probabilistic. stop_reason is deterministic.
  The exam tests this distinction in every Domain 1 scenario about loop hangs.
"""

import anthropic

client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"

tools = [
    {
        "name": "get_word_count",
        "description": "Counts the number of words in a string.",
        "input_schema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "The text to count words in."}
            },
            "required": ["text"],
        },
    }
]

def get_word_count(text: str) -> str:
    count = len(text.split())
    return f"{count} words"

def run_agent(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]
    max_iterations = 10  # safety backstop — NOT the primary exit condition

    for _ in range(max_iterations):
        response = client.messages.create(
            model=MODEL,
            max_tokens=256,
            tools=tools,
            messages=messages,
        )

        # ── FIXED: use stop_reason, not text matching ──────────────────
        if response.stop_reason == "end_turn":
            # Model finished — extract and return the final text
            return "".join(
                block.text for block in response.content if hasattr(block, "text")
            )

        if response.stop_reason == "max_tokens":
            # Response was truncated — treat as an error, not success
            raise RuntimeError(
                "Response truncated by max_tokens. Increase max_tokens or split the task."
            )

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    if block.name == "get_word_count":
                        result = get_word_count(block.input["text"])
                    else:
                        result = f"Unknown tool: {block.name}"
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })
            # Always append both the assistant response AND the tool results
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
            continue
        # ───────────────────────────────────────────────────────────────

    return "Safety cap reached — check for runaway tool calls."


if __name__ == "__main__":
    result = run_agent(
        "Count the words in this sentence: 'The quick brown fox jumps over the lazy dog'. "
        "Then tell me the result."
    )
    print("Agent result:", result)
