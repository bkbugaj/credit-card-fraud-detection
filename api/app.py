import os
import pickle

import numpy as np
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = os.path.join("models", "rnd_forest_clf.pkl")

app = FastAPI()

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


class PredictionRequest(BaseModel):
    inputs: list


@app.post("/predict")
async def predict(request: PredictionRequest):
    inputs = np.array(request.inputs)
    predictions = model.predict(inputs)
    return {"predictions": predictions.tolist()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
