"""
Exercise 01 — Fix the Broken Loop
===================================
BUG: This loop terminates by looking for the phrase "Task complete" in Claude's
response text. It works most of the time, but occasionally hangs forever because
Claude phrases its completion differently depending on context and temperature.

YOUR TASK:
  1. Find the two lines that implement text-matching termination.
  2. Replace them with the correct stop_reason check.
  3. Also handle the max_tokens case — the current code ignores it entirely.

Hint: every Messages API response has a `response.stop_reason` field.
The value "end_turn" means Claude is done. That's the only signal you need.
"""

import anthropic

client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"

# A minimal tool so the loop actually exercises tool_use stop_reason
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
    iteration = 0
    max_iterations = 10  # safety backstop only — NOT the primary exit

    while iteration < max_iterations:
        iteration += 1
        response = client.messages.create(
            model=MODEL,
            max_tokens=256,
            tools=tools,
            messages=messages,
        )

        # ─────────────────────────────────────────────────────────────────
        # BUG: text-matching termination — unreliable, sometimes hangs
        # ─────────────────────────────────────────────────────────────────
        response_text = "".join(
            block.text for block in response.content if hasattr(block, "text")
        )
        if "Task complete" in response_text or "task complete" in response_text:
            return response_text  # ← wrong: depends on Claude's exact phrasing
        # ─────────────────────────────────────────────────────────────────

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
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
            continue

        # TODO: what about stop_reason == "max_tokens"?
        # Currently this falls through to the next iteration silently.

    return "Max iterations reached — loop did not terminate cleanly."


if __name__ == "__main__":
    result = run_agent(
        "Count the words in this sentence: 'The quick brown fox jumps over the lazy dog'. "
        "Then tell me the result."
    )
    print("Agent result:", result)
