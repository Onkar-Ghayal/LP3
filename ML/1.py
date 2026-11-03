
# ==========================================
# UBER FARE PREDICTION USING MACHINE LEARNING
# ==========================================

# 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


# 2. Load Dataset

df = pd.read_csv("uber.csv")

print("First Five Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# 3. Data Preprocessing

# Remove unnecessary columns
df = df.drop(["Unnamed: 0", "key"], axis=1, errors="ignore")

# Convert pickup_datetime into datetime format
df["pickup_datetime"] = pd.to_datetime(
    df["pickup_datetime"], errors="coerce", utc=True
)

# Extract hour from pickup_datetime
df["hour"] = df["pickup_datetime"].dt.hour

# Remove original datetime column
df = df.drop("pickup_datetime", axis=1)

# Handle missing values
df = df.dropna()

# Calculate distance between pickup and dropoff
df["Distance"] = np.sqrt(
    (df["dropoff_longitude"] - df["pickup_longitude"])**2 +
    (df["dropoff_latitude"] - df["pickup_latitude"])**2
)

print("\nAfter Preprocessing:")
print(df.head())


# 4. Identify Outliers Before Removal

plt.figure(figsize=(8, 4))
sns.boxplot(x=df["fare_amount"])
plt.title("Fare Amount Before Removing Outliers")
plt.show()


# 5. Remove Invalid Data

df = df[df["fare_amount"] > 0]

df = df[df["passenger_count"].between(1, 6)]

df = df[
    df["pickup_latitude"].between(-90, 90) &
    df["dropoff_latitude"].between(-90, 90)
]

df = df[
    df["pickup_longitude"].between(-180, 180) &
    df["dropoff_longitude"].between(-180, 180)
]

df = df[df["Distance"] > 0]


# 6. Detect and Remove Outliers Using IQR

Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("\nNumber of Outliers:",
      ((df["fare_amount"] < lower) |
       (df["fare_amount"] > upper)).sum())

# Remove outliers
df = df[
    (df["fare_amount"] >= lower) &
    (df["fare_amount"] <= upper)
]


# 7. Boxplot After Removing Outliers

plt.figure(figsize=(8, 4))
sns.boxplot(x=df["fare_amount"])
plt.title("Fare Amount After Removing Outliers")
plt.show()


# 8. Correlation Analysis

corr = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(corr)

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# 9. Split Features and Target

X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]


# 10. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 11. Linear Regression Model

lr = LinearRegression()

lr.fit(X_train, y_train)

pred_lr = lr.predict(X_test)

r2_lr = r2_score(y_test, pred_lr)

rmse_lr = np.sqrt(mean_squared_error(y_test, pred_lr))


# 12. Random Forest Regression Model

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

pred_rf = rf.predict(X_test)

r2_rf = r2_score(y_test, pred_rf)

rmse_rf = np.sqrt(mean_squared_error(y_test, pred_rf))


# 13. Compare Both Models

result = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "R2 Score": [r2_lr, r2_rf],
    "RMSE": [rmse_lr, rmse_rf]
})

print("\nModel Performance Comparison:")
print(result)


# 14. Display Better Performing Model

if r2_rf > r2_lr and rmse_rf < rmse_lr:
    print("\nRandom Forest performs better.")
else:
    print("\nLinear Regression performs better.")


# 15. Actual vs Predicted Values

comparison = pd.DataFrame({
    "Actual Fare": y_test.values[:10],
    "Linear Regression": pred_lr[:10],
    "Random Forest": pred_rf[:10]
})

print("\nActual vs Predicted Fare:")
print(comparison)
