# classes_practice.py

class Product:
    def __init__(self, name: str, price: float, tags: list[str] | None = None) -> None:
        self.name = name
        self.price = price
        self.tags = tags or []

    def discount(self, percent: float) -> float:
        """Return the price after applying a percentage discount."""
        return self.price * (1 - percent / 100)


class Cart:
    def __init__(self) -> None:
        self.items: list[tuple[Product, int]] = []

    def add(self, product: Product, quantity: int = 1) -> None:
        self.items.append((product, quantity))

    def total(self) -> float:
        """Calculate total cost of items in the cart."""
        return sum(product.price * quantity for product, quantity in self.items)

    def get_tagged(self, tag: str) -> list[Product]:
        """Return all products in cart with given tag."""
        return [p for p, _ in self.items if tag in p.tags]
