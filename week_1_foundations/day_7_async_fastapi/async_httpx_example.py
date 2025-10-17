# async_httpx_example.py → acts as a client.
# It sends outgoing requests to external APIs (or even to your own FastAPI app),
#  waits for responses efficiently using async I/O,
# and automatically cleans up open connections when done.
import asyncio

import httpx


# Fetch GET requests (e.g., /hello)
async def fetch_get(client, url):
    response = await client.get(url)
    return {
        "url": url,
        "method": "GET",
        "status": response.status_code,
        "response": response.json(),
    }


# Fetch POST requests (e.g., /predict)
async def fetch_post(client, url, data):
    response = await client.post(url, json=data)
    return {
        "url": url,
        "method": "POST",
        "status": response.status_code,
        "response": response.json(),
    }


async def main():
    async with httpx.AsyncClient() as client:
        # Define GET and POST tasks
        tasks = [
            fetch_get(client, "http://127.0.0.1:8000/hello"),
            fetch_post(client, "http://127.0.0.1:8000/predict", {"a": 2, "b": 3}),
            fetch_post(client, "http://127.0.0.1:8000/predict", {"x": 10, "y": 5}),
        ]

        # Run all tasks concurrently
        results = await asyncio.gather(*tasks)

        # Print results neatly
        for result in results:
            print(result)


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
