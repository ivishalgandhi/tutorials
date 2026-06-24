"""
Exercise 03 — Solution: Handle All Four stop_reason Values
============================================================
FIXED: All four stop_reason values handled correctly.

EXAM TABLE (memorise this):
  end_turn      → extract text, exit loop — model finished naturally
  tool_use      → execute tools, append results, continue loop
  max_tokens    → raise error — truncated, NOT a complete response
  stop_sequence → log which sequence fired, exit cleanly

The critical distinction: max_tokens and end_turn can both produce text content,
but only end_turn means the response is complete. Silently returning max_tokens
output as if it's complete is an anti-pattern — callers get partial answers.
"""

import anthropic

client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"

tools = [
    {
        "name": "add",
        "description": "Adds two numbers together.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"},
            },
            "required": ["a", "b"],
        },
    }
]

def execute_tool(name: str, inputs: dict) -> str:
    if name == "add":
        return str(inputs["a"] + inputs["b"])
    return f"Unknown: {name}"


class StopReasonHandler:
    def __init__(self):
        self.messages = []
        self.result = None
        self.done = False

    def handle_stop_reason(self, response) -> None:
        if response.stop_reason == "end_turn":
            # ✓ Model finished — return the complete text
            self.result = "".join(
                b.text for b in response.content if hasattr(b, "text")
            )
            self.done = True

        elif response.stop_reason == "tool_use":
            # ✓ Execute all tool_use blocks, continue the loop
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": execute_tool(block.name, block.input),
                    })
            self.messages.append({"role": "assistant", "content": response.content})
            self.messages.append({"role": "user", "content": tool_results})

        elif response.stop_reason == "max_tokens":
            # ✓ FIXED: truncated output — raise, don't silently return partial text
            partial = "".join(
                b.text for b in response.content if hasattr(b, "text")
            )
            raise RuntimeError(
                f"Response truncated at max_tokens limit. "
                f"Partial output ({len(partial)} chars): '{partial[:80]}...'. "
                "Increase max_tokens or split the task."
            )

        elif response.stop_reason == "stop_sequence":
            # ✓ FIXED: a stop sequence fired — log it, exit cleanly
            seq = getattr(response, "stop_sequence", "<unknown>")
            print(f"[stop_sequence fired: {seq!r}]")
            self.result = "".join(
                b.text for b in response.content if hasattr(b, "text")
            )
            self.done = True

        else:
            # Future-proof: unknown stop_reason — fail loudly, not silently
            raise RuntimeError(f"Unhandled stop_reason: {response.stop_reason!r}")


def run_agent(user_message: str, max_tokens: int = 512) -> str:
    handler = StopReasonHandler()
    handler.messages = [{"role": "user", "content": user_message}]

    for _ in range(10):
        response = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            tools=tools,
            messages=handler.messages,
        )
        handler.handle_stop_reason(response)
        if handler.done:
            return handler.result

    return "Safety cap reached."


if __name__ == "__main__":
    print("=== Normal call ===")
    print(run_agent("What is 42 + 58?"))

    print("\n=== Truncated call (max_tokens=5) — expect RuntimeError ===")
    try:
        print(run_agent("Write a detailed paragraph about Python.", max_tokens=5))
    except RuntimeError as e:
        print(f"RuntimeError caught (correct behaviour): {e}")
