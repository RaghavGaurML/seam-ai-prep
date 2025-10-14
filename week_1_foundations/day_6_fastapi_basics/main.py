# import logging
# import time

# from fastapi import FastAPI, Request
# from schemas import PredictionRequest, PredictionResponse

# app = FastAPI()

# # Use a separate logger to avoid uvicorn access formatter issues
# logger = logging.getLogger("mylogger")
# logging.basicConfig(level=logging.INFO)


# # Logging middleware wraps around every http request
# @app.middleware("http")  # global decorator
# async def log_requests(request: Request, call_next):
#     start_time = time.time()

#     # Safely get client host (can be None)
#     client_host = request.client.host if request.client else "unknown"

#     response = await call_next(request)
#     duration = (time.time() - start_time) * 1000  # in milliseconds

#     # Log with standard logger
#     logger.info(
#         "%s - %s %s completed in %.2fms (status=%d)",
#         client_host,
#         request.method,
#         request.url.path,
#         duration,
#         response.status_code,
#     )

#     return response


# # “Whenever a client makes a GET request to /hello, run this function.”
# @app.get("/hello")
# async def hello():
#     return {"message": "Hello, Seam AI!"}


# # “When a client sends a POST request to /predict, call this function with the data they sent.”
# @app.post("/predict", response_model=PredictionResponse)
# async def predict(req: PredictionRequest):
#     score = len(req.text) % 10  # dummy model
#     return PredictionResponse(score=score)
