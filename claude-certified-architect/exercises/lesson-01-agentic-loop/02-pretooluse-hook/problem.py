"""
Exercise 02 — PreToolUse Hook: Deterministic Gate
===================================================
PROBLEM: The refund agent dispatches tools based on Claude's requests — but there is
no prerequisite check. Claude can (and sometimes does) call process_refund before
ever calling get_customer, leading to refunds on unverified accounts.

YOUR TASK:
  Add a PreToolUse gate inside `dispatch_tool()` that blocks `process_refund`
  (and `lookup_order`) unless `get_customer` has already returned a verified
  customer ID in this session.

  Specifically:
    1. Track whether get_customer has been called and returned a valid ID.
    2. Before executing process_refund or lookup_order, check that state.
    3. If the prerequisite is not met, return an error result instead of executing.

This is a programmatic hook — it does NOT modify the system prompt or add examples.
"""

import anthropic

client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"

# ── Tool definitions ──────────────────────────────────────────────────────────
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

# ── Mock tool implementations ─────────────────────────────────────────────────
def _get_customer(email: str) -> dict:
    db = {"alice@example.com": {"customer_id": "C-001", "name": "Alice"}}
    return db.get(email, {"error": "Customer not found"})

def _lookup_order(order_id: str, customer_id: str) -> dict:
    orders = {"O-999": {"order_id": "O-999", "amount": 49.99, "status": "delivered"}}
    order = orders.get(order_id)
    if not order:
        return {"error": "Order not found"}
    return order

def _process_refund(order_id: str, customer_id: str, amount: float) -> dict:
    return {"status": "refund_processed", "order_id": order_id, "amount": amount}


# ── Tool dispatcher — THIS IS WHERE THE HOOK SHOULD LIVE ─────────────────────
def dispatch_tool(tool_name: str, tool_input: dict, session_state: dict) -> str:
    """
    Dispatches a tool call. session_state carries cross-call state for this session.

    TODO: Add a PreToolUse gate here that blocks process_refund and lookup_order
    unless session_state["verified_customer_id"] is set.
    """
    # No gate — any tool fires in any order (BUG)
    if tool_name == "get_customer":
        result = _get_customer(tool_input["email"])
        if "customer_id" in result:
            session_state["verified_customer_id"] = result["customer_id"]
        return str(result)

    if tool_name == "lookup_order":
        # BUG: no check that get_customer was called first
        return str(_lookup_order(tool_input["order_id"], tool_input["customer_id"]))

    if tool_name == "process_refund":
        # BUG: no check that get_customer was called first
        return str(_process_refund(
            tool_input["order_id"],
            tool_input["customer_id"],
            tool_input["amount"],
        ))

    return f"Unknown tool: {tool_name}"


# ── Agent loop ────────────────────────────────────────────────────────────────
def run_agent(user_message: str) -> str:
    session_state = {}  # carries verified_customer_id once get_customer succeeds
    messages = [{"role": "user", "content": user_message}]

    # Intentionally weak system prompt — relies only on Claude's judgment
    system = (
        "You are a customer support agent. "
        "Help customers with refunds and order lookups."
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
    # This might process a refund without identity verification
    result = run_agent(
        "Please refund $49.99 for order O-999 for customer ID C-001."
    )
    print(result)
