from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import os

app = FastAPI()

# Load model
model_path = os.path.join(os.path.dirname(__file__), "../models/random_forest_model.pkl")
model = joblib.load(model_path)

# Define expected feature order
expected_features = ['longitude', 'latitude', 'housing_median_age', 'median_income',
                     'rooms_per_household', 'bedrooms_per_room', 'population_per_household',
                     'ocean_proximity_INLAND', 'ocean_proximity_ISLAND',
                     'ocean_proximity_NEAR BAY', 'ocean_proximity_NEAR OCEAN']

@app.post("/predict/")
def predict(features: dict):
    try:
        # Convert input to DataFrame
        df = pd.DataFrame([features])

        # Ensure feature order matches model's expected order
        df = df[expected_features]  # Reorder columns

        # Make prediction
        prediction = model.predict(df)[0]

        return {"predicted_house_price": prediction}

    except Exception as e:
        print("Error:", str(e))  # Debugging: Print the error
        raise HTTPException(status_code=500, detail=str(e))  # Return error message
