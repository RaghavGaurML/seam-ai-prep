# Note: this is similar to the synchronous functions implemented in Day 6 - FastAPI Basics
import asyncio

from fastapi import FastAPI

app = FastAPI()


# “Whenever a client makes a GET request to /hello, run this function.”
@app.get("/hello")
async def hello():
    await asyncio.sleep(0.1)
    return {"message": "hello async world!"}


# “When a client sends a POST request to /predict, call this function with the data they sent.”
@app.post("/predict")
async def predict(data: dict):
    await asyncio.sleep(0.2)
    return {"prediction": sum(data.values())}  # dummy prediction
