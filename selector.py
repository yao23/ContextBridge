"""Selection logic for choosing the best retrieved context."""

from typing import Dict, List, Optional, Tuple


def select(
    candidates: List[Dict[str, object]],
) -> Tuple[Optional[Dict[str, object]], List[str]]:
    if not candidates:
        return None, ["no candidate context matched the task"]

    def score(item: Dict[str, object]) -> float:
        value = float(item.get("retrieval_score", 0.0))
        if item.get("result") == "success":
            value += 1.0
        return value

    ranked = sorted(candidates, key=score, reverse=True)
    selected = ranked[0]

    reasons = []
    if selected.get("result") == "success":
        reasons.append("higher success rate from past outcome")
    else:
        reasons.append("selected despite no successful history because it was the best match")

    reasons.append(f"more relevant to the task (score={score(selected):.3f})")
    return selected, reasons
