import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import os

# Load your PaySim dataset
df = pd.read_csv("data/psv_data.csv")
print(df.head())

# Encode 'type' column
le = LabelEncoder()
df['type_encoded'] = le.fit_transform(df['type'])

# Select relevant features
features = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'type_encoded']
X = df[features]
y = df['isFraud']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and encoder
os.makedirs("models", exist_ok=True)
joblib.dump((model, le), "models/fraud_model.pkl")

print("Model trained and saved to models/fraud_model.pkl")
