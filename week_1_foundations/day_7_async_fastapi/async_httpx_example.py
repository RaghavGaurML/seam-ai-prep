# async_httpx_example.py → acts as a client.
# It sends outgoing requests to external APIs (or even to your own FastAPI app),
#  waits for responses efficiently using async I/O,
# and automatically cleans up open connections when done.
import asyncio

import httpx


# Simulate calling multiple APIs in parallel
async def fetch_data(client, url: str):
    response = await client.get(url)
    return {"url": url, "status": response.status_code}


async def main():
    urls = [
        "https://httpbin.org/get",
        "https://api.github.com",
        "https://jsonplaceholder.typicode.com/todos/1",
    ]

    async with httpx.AsyncClient() as client:
        # Launch all requests at once
        tasks = [fetch_data(client, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for r in results:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())

# Real-world production pattern example
# @app.get("/aggregate")
# async def aggregate_data():
#     async with httpx.AsyncClient() as client:
#         tasks = [
#             client.get("https://api.github.com"),
#             client.get("https://jsonplaceholder.typicode.com/todos/1")
#         ]
#         responses = await asyncio.gather(*tasks)
#     return [r.json() for r in responses]
