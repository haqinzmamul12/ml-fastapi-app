from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/health")
def health():
    return {"status": "healthy", "version": "1.0-dev"}

@app.post("/predict")
def predict(data: InputData):
    result = data.feature1 * 3 + data.feature2
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
        "precision": 0.95,
        "recall": 0.87,
        "f1_score": 0.88,
        "roc_auc": 0.96
    }

