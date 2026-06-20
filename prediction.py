import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("health_data.csv")

# Features
X = data[["glucose", "haemoglobin", "cholesterol"]]

# Target
y = data["risk"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)


def predict_health(glucose, haemoglobin, cholesterol):

    prediction = model.predict(
        [[glucose, haemoglobin, cholesterol]]
    )[0]

    if prediction == 1:
        return "Health Risk Detected"
    else:
        return "Normal Health Indicators"
