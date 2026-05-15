from fastapi import FastAPI

from ml_service.core.predictor import run_prediction

app = FastAPI(title="ML Service")


@app.get("/")
def home():
    return {"status": "ml service running"}


@app.post("/predict")
def predict(data: dict):

    result = run_prediction(data)

    return result