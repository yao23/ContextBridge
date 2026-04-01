"""
ContextBridge Demo - main.py

A simple CLI demo showing:
- Context storage
- Retrieval
- Selection
- Evaluation loop

Run:
python main.py
"""

import json
from typing import List, Dict


# -----------------------------
# Context Store (in-memory for demo)
# -----------------------------
context_store: List[Dict] = [
    {
        "task": "debug API timeout",
        "strategy": "check logs and trace latency",
        "result": "success",
        "tags": ["backend", "latency"]
    },
    {
        "task": "fix slow API response",
        "strategy": "increase timeout",
        "result": "failure",
        "tags": ["backend"]
    }
]


# -----------------------------
# Retrieval
# -----------------------------
def retrieve_context(task: str):
    results = []
    for item in context_store:
        if any(word in item["task"] for word in task.split()):
            results.append(item)
    return results


# -----------------------------
# Selection (simple scoring)
# -----------------------------
def select_context(candidates: List[Dict]):
    if not candidates:
        return None

    # prioritize success > recency
    scored = sorted(
        candidates,
        key=lambda x: (x["result"] == "success"),
        reverse=True
    )
    return scored[0]


# -----------------------------
# Mock Agent (LLM placeholder)
# -----------------------------
def run_agent(task: str, context: Dict):
    if context:
        return f"Using past strategy: {context['strategy']}"
    return "No context found, try general debugging."


# -----------------------------
# Evaluation
# -----------------------------
def evaluate(output: str):
    # simple mock: if mentions logs, success
    if "logs" in output:
        return "success"
    return "failure"


# -----------------------------
# Main flow
# -----------------------------
def main():
    task = input("Enter task: ")

    # Step 1: Retrieve
    candidates = retrieve_context(task)
    print("\nRetrieved:")
    for c in candidates:
        print(f"- {c['strategy']} ({c['result']})")

    # Step 2: Select
    selected = select_context(candidates)
    print("\nSelected:")
    if selected:
        print(f"- {selected['strategy']}")
    else:
        print("None")

    # Step 3: Run agent
    output = run_agent(task, selected)
    print("\nAgent Output:")
    print(output)

    # Step 4: Evaluate
    result = evaluate(output)
    print("\nEvaluation:")
    print(result)

    # Step 5: Update memory
    context_store.append({
        "task": task,
        "strategy": output,
        "result": result,
        "tags": []
    })

    print("\nMemory updated.")


if __name__ == "__main__":
    main()
