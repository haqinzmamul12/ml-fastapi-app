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
    result = data.feature1 * 5 + data.feature2
    return {"prediction": result}


@app.get("/model-info")
def model_info():
    return {
        "model_name": "demo-model",
        "version": "1.0",
        "accuracy": 0.91
    }