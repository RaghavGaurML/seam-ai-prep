# debug_demo.py
import asyncio


def greet(name: str) -> str:
    # BREAKPOINT 1: Inspect 'name' and 'message'
    message = f"Hello, {name}!"
    print(message)
    return message


async def async_greet(name: str):
    # BREAKPOINT 2: Before sleeping
    print(f"Starting async greet for {name}...")
    await asyncio.sleep(1)
    # BREAKPOINT 3: After sleep, before calling greet
    return greet(name)


if __name__ == "__main__":
    # BREAKPOINT 4: Before running the event loop
    asyncio.run(async_greet("Raghav"))
    asyncio.run(async_greet("Raghav"))
