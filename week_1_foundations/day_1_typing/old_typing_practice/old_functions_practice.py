# Implement simple functions with type hints


def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of two integers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the division of two integers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please provide a function name and arguments")
        sys.exit(1)

    func = sys.argv[1]
    args: list[str] = sys.argv[2:]

    match func:
        case "greet":
            print(greet(*args))
        case "add":
            print(add(int(args[0]), int(args[1])))
        case "subtract":
            print(subtract(int(args[0]), int(args[1])))
        case "multiply":
            print(multiply(int(args[0]), int(args[1])))
        case "divide":
            print(divide(int(args[0]), int(args[1])))
        case _:
            print(f"Unknown function: {func}")
