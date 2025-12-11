# app/main.py
from fastapi import FastAPI
from .model import load_model, predict_example

app = FastAPI()
model = load_model()  # load on startup once

@app.get("/")
def root():
    return {"message": "ML service is running"}

@app.get("/predict")
def predict():
    prediction = predict_example(model)
    return {"prediction": prediction}