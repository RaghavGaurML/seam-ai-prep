import asyncio

from fastapi import FastAPI, HTTPException

app = FastAPI()

# ---------------------------
# Data layer (simulated DB)
# ---------------------------
fake_db: dict = {}  # Simulated database


# Splitting into fetch_user and get_user separates data retrieval from the API route,
# making the code more reusable, testable, and maintainable.
# Actually retrieves user data from a database, API, or external source.
async def fetch_user(user_id: int):
    """Fetch user data from the 'database'."""
    # Simulate a slow database or API call
    await asyncio.sleep(0.3)
    return fake_db.get(user_id)


async def insert_user(user_data: dict):
    """Insert new user data into the 'database'."""
    await asyncio.sleep(0.1)  # simulate async DB write
    new_id = len(fake_db) + 1
    fake_db[new_id] = {"id": new_id, **user_data}
    return fake_db[new_id]


# ---------------------------
# API layer
# ---------------------------
# “Whenever a client makes a GET request to /hello, run this function.”
# We return dictionaries with FastAPI because it automatically
# serializes responses to JSON, and JSON must have a top-level object (dictionary or list).
# We use asyncio.sleep() instead of time.sleep() as it models tasks running parallel
@app.get("/hello")
async def hello():
    await asyncio.sleep(0.1)
    return {"message": "hello async world!"}


# “When a client sends a POST request to /predict,
# call this function with the data they sent.”
@app.post("/predict")
async def predict(data: dict):
    await asyncio.sleep(0.2)
    return {"prediction": sum(data.values())}  # dummy prediction


# Handles incoming requests and uses fetch_user() to get the data;
# may add validation or formatting.
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    """
    API endpoint for getting a user's info.
    Calls fetch_user() to retrieve data from the DB.
    """
    user = await fetch_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/user")
async def create_user(user_data: dict):
    """
    API endpoint for creating a new user.
    Validates input and calls insert_user() to save it.
    """
    if "name" not in user_data:
        raise HTTPException(status_code=400, detail="Name is required")

    user = await insert_user(user_data)
    return {"message": "User created successfully", "user": user}
