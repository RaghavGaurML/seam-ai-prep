# functions_practice.py
from typing import Sequence, Callable

def average(numbers: Sequence[int]) -> float:
    return sum(numbers) / len(numbers)

def top_three(items: list, key: Callable) -> list:
    """Return the top 3 items by key function."""
    return sorted(items, key=key, reverse=True)[:3]

def safe_divide(a: int, b: int, default: float = 0.0) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return default

def concat(strings: list[str], sep: str) -> str:
    return sep.join(strings)

def word_frequencies(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
