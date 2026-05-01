from fastapi import FastAPI
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI(
    title="Regression Project API",
    description="Basic Regression Model using FastAPI",
    version="1.0"
)

# Load trained model
model = joblib.load("regression_model.pkl")

# Home route
@app.get("/")
def home():
    return {
        "message": "Regression API is running"
    }

# Prediction route
@app.get("/predict")
def predict(value: float):

    prediction = model.predict(
        np.array([[value]])
    )

    return {
        "input": value,
        "prediction": prediction.tolist()
    }