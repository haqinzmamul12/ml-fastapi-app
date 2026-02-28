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
    return {"prediction": result}