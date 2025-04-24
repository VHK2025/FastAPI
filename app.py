from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

# Chargement du modèle
with open("getaround_price_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(
    title="GetAround Price Predictor",
    description="API pour predire le prix d'une location de voiture via un modele ML",
    version="1.0"
)

class RentalFeatures(BaseModel):
    feature_1: float
    feature_2: float
    feature_3: float

@app.post("/predict")
def predict_price(data: RentalFeatures):
    input_data = np.array([[data.feature_1, data.feature_2, data.feature_3]])
    prediction = model.predict(input_data)[0]
    return {
        "predicted_price": round(prediction, 2)
    }
