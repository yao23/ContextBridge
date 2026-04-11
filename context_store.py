"""In-memory context storage for the minimal ContextBridge demo."""

from typing import Dict, List, Optional


ContextItem = Dict[str, object]


context_store: List[ContextItem] = [
    {
        "task": "debug API timeout",
        "strategy": "check logs",
        "result": "success",
        "tags": ["backend", "latency"],
    },
    {
        "task": "fix slow API response",
        "strategy": "increase timeout",
        "result": "failure",
        "tags": ["backend"],
    },
]


def add_context(
    task: str,
    strategy: str,
    result: str,
    tags: Optional[List[str]] = None,
) -> None:
    context_store.append(
        {
            "task": task,
            "strategy": strategy,
            "result": result,
            "tags": tags or [],
        }
    )


def get_all_context() -> List[ContextItem]:
    return context_store
