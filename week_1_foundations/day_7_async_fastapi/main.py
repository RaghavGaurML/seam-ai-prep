# Note: this is similar to the synchronous functions implemented in Day 6 - FastAPI Basics
import asyncio

from fastapi import FastAPI

app = FastAPI()


# “Whenever a client makes a GET request to /hello, run this function.”
# We return dictionaries with FastAPI because it automatically serializes responses to JSON, and JSON must have a top-level object (dictionary or list).
# We use asyncio.sleep() instead of time.sleep() as it models tasks running parallel
@app.get("/hello")
async def hello():
    await asyncio.sleep(0.1)
    return {"message": "hello async world!"}


# “When a client sends a POST request to /predict, call this function with the data they sent.”
@app.post("/predict")
async def predict(data: dict):
    await asyncio.sleep(0.2)
    return {"prediction": sum(data.values())}  # dummy prediction
