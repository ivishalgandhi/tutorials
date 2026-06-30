"""
Exercise 03 — Handle All Four stop_reason Values
==================================================
PROBLEM: The agent only handles "end_turn" and "tool_use".
"max_tokens" is silently treated as end_turn (returns truncated text as if it's complete).
"stop_sequence" is ignored (loop continues when it shouldn't).

YOUR TASK:
  Complete the handle_stop_reason() function with correct behaviour for all four values:

  | stop_reason     | Correct action                                          |
  |-----------------|--------------------------------------------------------|
  | "end_turn"      | Extract and return the final text — loop exits         |
  | "tool_use"      | Execute tools, append results, continue loop           |
  | "max_tokens"    | Raise RuntimeError — output is truncated, not complete |
  | "stop_sequence" | Log which sequence fired, return partial result cleanly |

  Do NOT return partial text silently on max_tokens.
  That's the anti-pattern: callers think they got a complete response when they didn't.
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
        """
        TODO: handle all four stop_reason values correctly.
        Set self.done = True when the loop should exit.
        Set self.result to the final answer when done.
        Append to self.messages when the loop should continue.
        """
        if response.stop_reason == "end_turn":
            self.result = "".join(
                b.text for b in response.content if hasattr(b, "text")
            )
            self.done = True

        elif response.stop_reason == "tool_use":
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

        # TODO: handle "max_tokens"
        # Currently falls through and the loop continues on truncated output — wrong.

        # TODO: handle "stop_sequence"
        # Currently falls through silently — wrong.


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

    return "Max iterations reached."


if __name__ == "__main__":
    # Normal case — should work fine
    print("=== Normal call ===")
    print(run_agent("What is 42 + 58?"))

    # Truncated case — max_tokens=5 forces a max_tokens stop
    # With the bug: returns partial text silently (looks like a complete answer)
    # With the fix: raises RuntimeError
    print("\n=== Truncated call (max_tokens=5) ===")
    try:
        print(run_agent("Write a detailed paragraph about Python.", max_tokens=5))
    except RuntimeError as e:
        print(f"RuntimeError (correct): {e}")
