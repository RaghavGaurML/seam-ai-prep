from fastapi import FastAPI
from schemas import PredictionRequest, PredictionResponse

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello, Seam AI!"}


@app.post("/predict", response_model=PredictionResponse)
async def predict(req: PredictionRequest):
    score = len(req.text) % 10  # dummy "model"
    return PredictionResponse(score=score)
