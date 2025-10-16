# Note: this is similar to the synchronous functions implemented in Day 6 - FastAPI Basics
import asyncio

from fastapi import FastAPI, HTTPException

app = FastAPI()


# Splitting into fetch_user and get_user separates data retrieval from the API route, making the code more reusable, testable, and maintainable.
# Actually retrieves user data from a database, API, or external source.
async def fetch_user(user_id: int):
    # Simulate a slow database or API call
    await asyncio.sleep(0.3)
    names = ["Alice", "Bob", "Carol", "Dave"]
    return {"id": user_id, "name": names[user_id % 4], "role": "Engineer"}


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


# Handles incoming requests and uses fetch_user() to get the data; may add validation or formatting.
@app.get("/user/user_id")
async def get_user(user_id: int):
    user = await fetch_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
