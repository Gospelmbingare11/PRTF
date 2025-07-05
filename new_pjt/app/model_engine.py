import joblib
import pandas as pd
import numpy as np

# ✅ Adjusted path to find the model correctly on Streamlit Cloud
model, encoder = joblib.load("../models/fraud_model.pkl")

def predict_transaction(input_data):
    """
    Takes input_data as a dictionary and returns fraud prediction.
    """
    # Convert input data to DataFrame
    df = pd.DataFrame([input_data])

    # Encode categorical variables if needed
    if encoder:
        for column in encoder:
            if column in df.columns:
                df[column] = encoder[column].transform(df[column])

    # Predict with the model
    prediction = model.predict(df)
    prediction_proba = model.predict_proba(df)

    return prediction[0], prediction_proba[0][1]
