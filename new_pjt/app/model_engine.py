import joblib
import numpy as np

model, encoder = joblib.load("models/fraud_model.pkl")

def predict_transaction(amount, old_balance, new_balance, txn_type):
    txn_type_encoded = encoder.transform([txn_type])[0]
    features = np.array([[amount, old_balance, new_balance, txn_type_encoded]])
    prob = model.predict_proba(features)[0][1]
    label = int(prob >= 0.5)
    return {"label": label, "probability": prob}
