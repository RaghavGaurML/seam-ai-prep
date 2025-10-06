# Use this to sort, auto-format, and lint everything in your current folder
# isort .; black .; ruff check .
def messy_function(a, b, c=5):
    result = a + b + c
    if result > 10:
        print("Big")
    else:
        print("Small")
    for i in range(3):
        print(i)
    return result


def another_function(x, y):
    print(x * y)
    return x * y


def unused_function():
    x = 123
    y = 456
    return x + y


def main():
    pass
