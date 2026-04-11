"""Simple retrieval that favors coverage over final decision-making."""

import math
import re
from collections import Counter
from typing import Dict, List

from context_store import get_all_context


def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def text_to_vector(text: str) -> Counter[str]:
    return Counter(tokenize(text))


def cosine_similarity(left: Counter[str], right: Counter[str]) -> float:
    if not left or not right:
        return 0.0

    dot_product = sum(left[token] * right[token] for token in left.keys() & right.keys())
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))

    if left_norm == 0 or right_norm == 0:
        return 0.0

    return dot_product / (left_norm * right_norm)


def retrieve(task: str) -> List[Dict[str, object]]:
    query_vector = text_to_vector(task)
    results = []

    for item in get_all_context():
        searchable_text = " ".join(
            [
                str(item.get("task", "")),
                str(item.get("strategy", "")),
                " ".join(str(tag) for tag in item.get("tags", [])),
            ]
        )
        score = cosine_similarity(query_vector, text_to_vector(searchable_text))
        if score > 0:
            enriched_item = dict(item)
            enriched_item["retrieval_score"] = round(score, 3)
            results.append(enriched_item)

    return sorted(results, key=lambda item: item["retrieval_score"], reverse=True)
