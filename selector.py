"""Selection logic for choosing the best retrieved context."""

from typing import Dict, List, Optional


def select(candidates: List[Dict[str, object]]) -> Optional[Dict[str, object]]:
    if not candidates:
        return None

    def score(item: Dict[str, object]) -> int:
        value = 0
        if item.get("result") == "success":
            value += 10
        value += len(str(item.get("task", "")))
        return value

    return sorted(candidates, key=score, reverse=True)[0]
