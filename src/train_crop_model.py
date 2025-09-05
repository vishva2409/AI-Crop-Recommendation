import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("data/soil_data.csv")

X = data[["Nitrogen", "Phosphorus", "Potassium", "pH", "Moisture"]]
y = data["Label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("models/crop_prediction_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Crop recommendation model saved in models/crop_prediction_model.pkl")
