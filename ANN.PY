import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample medical data
# Features: Age, Blood Pressure, Sugar Level
X = np.array([
    [25, 120, 90],
    [30, 130, 100],
    [35, 140, 110],
    [40, 150, 130],
    [45, 160, 140],
    [50, 170, 150],
    [55, 180, 160],
    [60, 190, 170]
])

# 0 = No Disease, 1 = Disease
y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create Artificial Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=1000,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Display accuracy
print("Actual Values:", y_test)
print("Predicted Values:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict a new patient
new_patient = [[48, 165, 145]]
prediction = model.predict(new_patient)

if prediction[0] == 1:
    print("Prediction: Disease Detected")
else:
    print("Prediction: No Disease")
