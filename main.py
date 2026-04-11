"""Minimal ContextBridge demo: retrieval -> selection -> evaluation -> memory."""

from typing import Dict, Optional

from context_store import add_context
from evaluator import evaluate
from retrieval import retrieve
from selector import select


def run_agent(task: str, context: Optional[Dict[str, object]]) -> str:
    if context:
        return f"Try this: {context['strategy']}"
    return f"Try general debugging steps for: {task}"


def run(task: str) -> None:
    candidates = retrieve(task)
    print("Retrieved:")
    if candidates:
        for item in candidates:
            print(f"- {item['strategy']} ({item['result']})")
    else:
        print("- No matching context")

    selected = select(candidates)
    print("\nSelected:")
    if selected:
        print(f"- {selected['strategy']}")
    else:
        print("- None")

    output = run_agent(task, selected)
    print("\nOutput:")
    print(output)

    result = evaluate(output)
    print("\nEvaluation:")
    print(result)

    stored_strategy = selected["strategy"] if selected else output
    add_context(task, stored_strategy, result)
    print("\nMemory updated.")


def main() -> None:
    task = input("Enter task: ").strip() or "fix slow API timeout"
    run(task)


if __name__ == "__main__":
    main()
