
# ==============================================
# CUSTOMER CHURN PREDICTION USING ANN
# ==============================================

# 1. Import Libraries

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# 2. Load Dataset

df = pd.read_csv("Churn_Modelling.csv")

print("First Five Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())


# 3. Drop Unnecessary Columns

df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)


# 4. Encode Categorical Columns

label_encoder = LabelEncoder()

df["Gender"] = label_encoder.fit_transform(df["Gender"])

df["Geography"] = label_encoder.fit_transform(df["Geography"])


# 5. Separate Features and Target

X = df.drop("Exited", axis=1)

y = df["Exited"]


# 6. Split Dataset into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 7. Feature Scaling

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


# 8. Build ANN Model

model = Sequential()

# Input Layer and First Hidden Layer
model.add(Dense(
    16,
    activation="relu",
    input_shape=(X_train.shape[1],)
))

# Second Hidden Layer
model.add(Dense(8, activation="relu"))

# Output Layer
model.add(Dense(1, activation="sigmoid"))


# 9. Compile Model

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# 10. Train Model

history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2
)


# 11. Make Predictions

y_pred = model.predict(X_test)

# Convert probabilities into 0 or 1
y_pred = (y_pred > 0.5).astype(int)


# 12. Evaluate Model

print("\n========== ANN MODEL RESULTS ==========")

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 13. Plot Training Accuracy

import matplotlib.pyplot as plt

plt.plot(history.history["accuracy"], label="Training Accuracy")

plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("ANN Model Accuracy")

plt.legend()
plt.show()


# 14. Plot Training Loss

plt.plot(history.history["loss"], label="Training Loss")

plt.plot(history.history["val_loss"], label="Validation Loss")

plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("ANN Model Loss")

plt.legend()
plt.show()
