# classes_practice.py
from typing import List, Tuple

class Product:
    def __init__(self, name: str, price: int, tags: List[str] | None = None) -> None:
        self.name = name
        self.price = price
        self.tags = tags or []

    def discount(self, percent: int) -> float:
        return self.price * (1 - percent / 100)

class Cart:
    def __init__(self) -> None:
        self.items : List[Tuple[Product, int]] = []

    def add(self, product: Product, quantity: int = 1) -> None:
        self.items.append((product, quantity))

    def total(self) -> int:
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

    def get_tagged(self, tag: str) -> List[Product]:
        """Return all products in cart with given tag."""
        return [p for p, _ in self.items if tag in p.tags]
