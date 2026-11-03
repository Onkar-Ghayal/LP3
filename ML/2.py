
# ============================================
# EMAIL SPAM CLASSIFICATION USING KNN AND SVM
# ============================================

# 1. Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# 2. Load Dataset

df = pd.read_csv("emails.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())


# 3. Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values if present
df = df.dropna()


# 4. Check Spam and Not Spam Count

print("\nPrediction Counts:")
print(df["Prediction"].value_counts())


# 5. Data Visualization

sns.countplot(x="Prediction", data=df)

plt.xlabel("Spam or Not Spam")
plt.ylabel("Count")
plt.title("Email Spam Classification")
plt.show()


# 6. Separate Features and Target

X = df.drop(["Prediction", "Email No."], axis=1)
y = df["Prediction"]


# 7. Split Dataset into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ============================================
# 8. K-NEAREST NEIGHBORS (KNN)
# ============================================

knn = KNeighborsClassifier(n_neighbors=5)

# Train Model
knn.fit(X_train, y_train)

# Prediction
pred_knn = knn.predict(X_test)

# Accuracy
acc_knn = accuracy_score(y_test, pred_knn)

print("\n========== KNN RESULTS ==========")

print("Accuracy:", acc_knn)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred_knn))

print("\nClassification Report:")
print(classification_report(y_test, pred_knn))


# ============================================
# 9. SUPPORT VECTOR MACHINE (SVM)
# ============================================

svm = SVC(kernel="linear")

# Train Model
svm.fit(X_train, y_train)

# Prediction
pred_svm = svm.predict(X_test)

# Accuracy
acc_svm = accuracy_score(y_test, pred_svm)

print("\n========== SVM RESULTS ==========")

print("Accuracy:", acc_svm)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred_svm))

print("\nClassification Report:")
print(classification_report(y_test, pred_svm))


# ============================================
# 10. COMPARE BOTH MODELS
# ============================================

print("\n========== MODEL COMPARISON ==========")

print("KNN Accuracy:", acc_knn)
print("SVM Accuracy:", acc_svm)

if acc_knn > acc_svm:
    print("\nKNN performs better.")
elif acc_svm > acc_knn:
    print("\nSVM performs better.")
else:
    print("\nBoth models perform equally.")


# ============================================
# 11. ACCURACY COMPARISON GRAPH
# ============================================

models = ["KNN", "SVM"]
accuracies = [acc_knn, acc_svm]

plt.bar(models, accuracies)

plt.xlabel("Classification Models")
plt.ylabel("Accuracy")
plt.title("KNN vs SVM Accuracy Comparison")

plt.ylim(0, 1)
plt.show()
