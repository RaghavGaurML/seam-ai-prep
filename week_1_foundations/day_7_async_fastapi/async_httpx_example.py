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
