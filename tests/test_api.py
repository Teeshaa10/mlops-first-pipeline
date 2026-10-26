# import testclient from fastapi.testclient
from fastapi.testclient import TestClient
#Import the app from main.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import app
# Create a reusable test client using the app for all test functions
client = TestClient(app)

def test_health_endpoint():
    """Verify that the application is running and can respond to a health check request."""
    # Send a GET request to the /health endpoint
    response = client.get("/health")
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response JSON matches the expected output
    assert response.json() == {"status": "healthy"}

def test_valid_iris_prediction():
    """Test the prediction endpoint with valid input data."""
    # Define valid input data for the prediction
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    # Send a POST request to the /predict endpoint with the input data
    response = client.post("/predict", json=payload)
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    #Convert the json response to a d python ictionary
    result = response.json()
    # Assert that the response JSON contains the expected keys
    assert "prediction" in result
    assert "class_name" in result

    #The predicted class name should be one of the expected  iris class names
    assert result["class_name"] in ["setosa", "versicolor", "virginica"]
    assert result["prediction"] in [0, 1, 2]

def test_invalid_iris_input():
    """Test the prediction endpoint with invalid input data."""
    # Define invalid input data for the prediction
    payload = {
        "sepal_length": -1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    # Send a POST request to the /predict endpoint with the invalid input data
    response = client.post("/predict", json=payload)
    # Assert that the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422