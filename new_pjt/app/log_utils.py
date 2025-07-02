import pandas as pd
from datetime import datetime
import os

LOG_FILE = "logs/fraud_logs.csv"

def log_transaction(amount, old_balance, new_balance, txn_type, is_fraud, probability):
    row = {
        "timestamp": datetime.now(),
        "amount": amount,
        "old_balance": old_balance,
        "new_balance": new_balance,
        "type": txn_type,
        "is_fraud": is_fraud,
        "probability": probability
    }
    df = pd.DataFrame([row])
    if os.path.exists(LOG_FILE):
        df.to_csv(LOG_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(LOG_FILE, index=False)

def read_logs():
    if os.path.exists(LOG_FILE):
        return pd.read_csv(LOG_FILE)
    else:
        return pd.DataFrame()
