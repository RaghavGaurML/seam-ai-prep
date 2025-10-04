# functions_practice.py
from typing import List, Tuple, Callable, Any

def average(numbers: Tuple[int]) -> float:
    total = sum(numbers)
    return total / len(numbers)

def top_three(items: List[str], key: Callable[[str], Any]) -> List[str]:
    """Return the top 3 items by key function."""
    sorted_items = sorted(items, key=key, reverse=True)
    return sorted_items[:3]

def safe_divide(a: int, b: int, default: float = 0.0) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return default

def concat(strings: List[str], sep: str) -> str:
    """Join list of strings with separator."""
    return sep.join(strings)

def word_frequencies(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
