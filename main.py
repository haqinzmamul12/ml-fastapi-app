from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/health")
def health():
    return {"status": "healthy", "version": "1.0-dev"}

@app.post("/predict")
def predict(data: InputData):
    result = data.feature1 * 10 + data.feature2
    print(f"Prediction requested: {data}")   # 👈 new logging
    return {"prediction": result}


@app.get("/model-info")
def model_info():
    return {
        "model_name": "demo-model",
        "version": "1.0",
        "accuracy": 0.91
    }


@app.get("/model-metrics")
def model_metrics():
    return {
        "precision": 0.89,
        "recall": 0.87,
        "f1_score": 0.88,
        "roc_auc": 0.92
    }

@app.post("/predict-batch")
def predict_batch(data: List[InputData]):
    results = []
    for item in data:
        result = item.feature1 * 5 + item.feature2
        results.append({"prediction": result})
    return {"results": results}
