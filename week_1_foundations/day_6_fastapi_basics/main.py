from fastapi import FastAPI
from schemas import PredictionRequest, PredictionResponse

app = FastAPI()


# “Whenever a client makes a GET request to /hello, run this function.”
@app.get("/hello")
async def hello():
    return {"message": "Hello, Seam AI!"}


# “When a client sends a POST request to /predict, call this function with the data they sent.”
@app.post("/predict", response_model=PredictionResponse)
async def predict(req: PredictionRequest):
    score = len(req.text) % 10  # dummy "model"
    return PredictionResponse(score=score)
