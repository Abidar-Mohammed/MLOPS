from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.svm import SVC

# Load the SVM model
svm_model = joblib.load('svm_model1.joblib')

# Create a FastAPI app
app = FastAPI()

# Define the input data model
class InputData(BaseModel):
    air_temperature: float
    process_temperature: float
    rotational_speed: int
    torque: float
    tool_wear: int

# Define the prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    # Convert input data to a DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Make a prediction using the loaded SVM model
    prediction = svm_model.predict(input_df)[0]

    # Return the prediction
    return {"prediction": prediction}

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
