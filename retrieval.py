"""Simple retrieval that favors coverage over final decision-making."""

from typing import Dict, List

from context_store import get_all_context


def retrieve(task: str) -> List[Dict[str, object]]:
    task_words = [word.lower() for word in task.split()]
    results = []

    for item in get_all_context():
        item_task = str(item["task"]).lower()
        if any(word in item_task for word in task_words):
            results.append(item)

    return results
