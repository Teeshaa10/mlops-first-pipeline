
from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field


MODEL_PATH = Path(__file__).parent / "models" / "iris_random_forest.joblib"
model = joblib.load(MODEL_PATH)


# Create FastAPI application
app = FastAPI(title="Iris Random Forest API")


# Define input schema
class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Prediction endpoint
@app.post("/predict")
def predict(input_data: IrisInput):
    features = [[
        input_data.sepal_length,
        input_data.sepal_width,
        input_data.petal_length,
        input_data.petal_width
    ]]

    prediction = int(model.predict(features)[0])

    class_names = ["setosa", "versicolor", "virginica"]

    return {
        "prediction": prediction,
        "class_name": class_names[prediction]
    }
