import streamlit as st
import pandas as pd
from model_engine import predict_transaction
from log_utils import log_transaction, read_logs

st.title("Real-Time Fraud Detection System")

menu = ["User Mode", "Admin Panel"]
choice = st.sidebar.selectbox("Select Mode", menu)

if choice == "User Mode":
    st.subheader("Enter Transaction Details")
    amount = st.number_input("Transaction Amount", min_value=0.0, step=10.0)
    old_balance = st.number_input("Old Balance", min_value=0.0, step=10.0)
    new_balance = st.number_input("New Balance", min_value=0.0, step=10.0)
    txn_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT"])

    if st.button("Predict"):
        result = predict_transaction(amount, old_balance, new_balance, txn_type)
        st.success(f"Prediction: {'FRAUD' if result['label']==1 else 'LEGITIMATE'} (Probability: {result['probability']:.2f})")
        log_transaction(amount, old_balance, new_balance, txn_type, result['label'], result['probability'])

elif choice == "Admin Panel":
    st.subheader("Transaction Logs")
    logs_df = read_logs()
    if not logs_df.empty:
        st.dataframe(logs_df)
        st.bar_chart(logs_df["is_fraud"])
    else:
        st.warning("No transactions logged yet.")
