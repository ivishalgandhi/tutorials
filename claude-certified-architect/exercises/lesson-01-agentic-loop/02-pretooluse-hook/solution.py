"""
Exercise 02 — Solution: PreToolUse Hook
========================================
FIXED: dispatch_tool() now has a PreToolUse gate that blocks process_refund and
lookup_order unless get_customer has already returned a verified customer ID.

This is 100% deterministic — no prompt change, no few-shot examples.
The gate fires in application code before the tool executes.

EXAM PATTERN:
  Q: "Production data shows the agent skips get_customer in 12% of cases,
      leading to incorrect refunds. What change most effectively addresses this?"
  A: Programmatic prerequisite that blocks lookup_order and process_refund until
     get_customer returns a verified customer ID.
  Wrong answers: stronger system prompt, more few-shot examples, routing classifier.
"""

import anthropic

client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"

tools = [
    {
        "name": "get_customer",
        "description": (
            "Looks up a customer by email and returns their verified customer ID and name. "
            "Must be called before any order lookups or refunds."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Customer email address"}
            },
            "required": ["email"],
        },
    },
    {
        "name": "lookup_order",
        "description": "Looks up an order by order ID. Requires a verified customer ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string"},
                "customer_id": {"type": "string"},
            },
            "required": ["order_id", "customer_id"],
        },
    },
    {
        "name": "process_refund",
        "description": "Processes a refund for an order. Requires a verified customer ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string"},
                "customer_id": {"type": "string"},
                "amount": {"type": "number"},
            },
            "required": ["order_id", "customer_id", "amount"],
        },
    },
]

def _get_customer(email: str) -> dict:
    db = {"alice@example.com": {"customer_id": "C-001", "name": "Alice"}}
    return db.get(email, {"error": "Customer not found"})

def _lookup_order(order_id: str, customer_id: str) -> dict:
    orders = {"O-999": {"order_id": "O-999", "amount": 49.99, "status": "delivered"}}
    return orders.get(order_id, {"error": "Order not found"})

def _process_refund(order_id: str, customer_id: str, amount: float) -> dict:
    return {"status": "refund_processed", "order_id": order_id, "amount": amount}


# ── FIXED: PreToolUse gate ────────────────────────────────────────────────────
def dispatch_tool(tool_name: str, tool_input: dict, session_state: dict) -> str:
    """
    PreToolUse gate: blocks financial operations until identity is verified.
    This is deterministic — 100% compliance, unlike any prompt-based approach.
    """
    # ── PreToolUse hook ───────────────────────────────────────────────────────
    IDENTITY_REQUIRED = {"lookup_order", "process_refund"}
    if tool_name in IDENTITY_REQUIRED and not session_state.get("verified_customer_id"):
        # Block execution — return structured error the model can reason about
        return (
            f"BLOCKED: {tool_name} requires identity verification first. "
            "Call get_customer with the customer's email before proceeding."
        )
    # ─────────────────────────────────────────────────────────────────────────

    if tool_name == "get_customer":
        result = _get_customer(tool_input["email"])
        if "customer_id" in result:
            # Record verified identity in session state
            session_state["verified_customer_id"] = result["customer_id"]
        return str(result)

    if tool_name == "lookup_order":
        return str(_lookup_order(tool_input["order_id"], tool_input["customer_id"]))

    if tool_name == "process_refund":
        return str(_process_refund(
            tool_input["order_id"],
            tool_input["customer_id"],
            tool_input["amount"],
        ))

    return f"Unknown tool: {tool_name}"


def run_agent(user_message: str) -> str:
    session_state = {}
    messages = [{"role": "user", "content": user_message}]
    system = (
        "You are a customer support agent. "
        "Help customers with refunds and order lookups. "
        "Always verify the customer's identity with get_customer before any other operations."
    )

    for _ in range(10):
        response = client.messages.create(
            model=MODEL,
            max_tokens=512,
            system=system,
            tools=tools,
            messages=messages,
        )

        if response.stop_reason == "end_turn":
            return "".join(
                block.text for block in response.content if hasattr(block, "text")
            )

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = dispatch_tool(block.name, block.input, session_state)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})

    return "Max iterations reached."


if __name__ == "__main__":
    print("=== Test 1: Attempt refund without identity verification ===")
    result = run_agent(
        "Please refund $49.99 for order O-999 for customer ID C-001."
    )
    print(result)

    print("\n=== Test 2: Proper flow with identity verification ===")
    result = run_agent(
        "Customer email is alice@example.com. "
        "Please refund $49.99 for order O-999."
    )
    print(result)
