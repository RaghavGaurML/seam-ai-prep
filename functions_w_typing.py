# Implement simple functions with type hints
from typing import List, Tuple

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

def average(numbers: List[float]) -> float:
    """Return the average of a list of floats."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def get_coordinates() -> Tuple[float, float]:
    """Return a tuple representing coordinates (x, y)."""
    return (0.0, 0.0)

def is_even(n: int) -> bool:
    """Return True if the number is even, False otherwise."""
    return n % 2 == 0