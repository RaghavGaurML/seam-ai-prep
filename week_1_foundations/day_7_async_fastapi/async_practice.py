# Note: this is similar to the synchronous functions implemented in Day 6 - FastAPI Basics
import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    await asyncio.sleep(0.1)
    return {"message": "hello async world!"}
