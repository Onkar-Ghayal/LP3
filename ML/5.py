
# ==============================================
# SALES DATA CLUSTERING USING K-MEANS AND
# HIERARCHICAL CLUSTERING
# ==============================================

# 1. Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA


# 2. Load Dataset

df = pd.read_csv("sales.csv", encoding="latin1")

print("First Five Rows:")
print(df.head())


# 3. Check Dataset Information

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())


# 4. Select Features

features = [
    "SALES",
    "QUANTITYORDERED",
    "PRICEEACH",
    "MSRP"
]


# 5. Remove Missing Values

df = df.dropna(subset=features)

x = df[features]

print("\nSelected Features:")
print(x.head())

print("\nFeatures Shape:")
print(x.shape)

print("\nMissing Values:")
print(x.isnull().sum())


# 6. Feature Scaling

scaler = StandardScaler()

x_scaled = scaler.fit_transform(x)


# ==============================================
# 7. ELBOW METHOD
# ==============================================

wcss = []

for k in range(1, 11):

    km = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    km.fit(x_scaled)

    wcss.append(km.inertia_)


# 8. Plot Elbow Graph

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, 11),
    wcss,
    marker="o"
)

plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")

plt.xticks(range(1, 11))
plt.grid(True)

plt.show()


# ==============================================
# 9. K-MEANS CLUSTERING
# ==============================================

optimal_k = 3

kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42,
    n_init=10
)

df["KMeans_Cluster"] = kmeans.fit_predict(x_scaled)

print("\nK-Means Cluster Counts:")

print(df["KMeans_Cluster"].value_counts())


# ==============================================
# 10. HIERARCHICAL CLUSTERING
# ==============================================

hc = AgglomerativeClustering(
    n_clusters=optimal_k,
    linkage="ward"
)

df["Hierarchical_Cluster"] = hc.fit_predict(x_scaled)

print("\nHierarchical Cluster Counts:")

print(df["Hierarchical_Cluster"].value_counts())


# ==============================================
# 11. DIMENSIONALITY REDUCTION USING PCA
# ==============================================

pca = PCA(n_components=2)

x_pca = pca.fit_transform(x_scaled)


# ==============================================
# 12. VISUALIZE K-MEANS CLUSTERING
# ==============================================

plt.figure(figsize=(8, 5))

plt.scatter(
    x_pca[:, 0],
    x_pca[:, 1],
    c=df["KMeans_Cluster"]
)

plt.title("K-Means Clustering")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.show()


# ==============================================
# 13. VISUALIZE HIERARCHICAL CLUSTERING
# ==============================================

plt.figure(figsize=(8, 5))

plt.scatter(
    x_pca[:, 0],
    x_pca[:, 1],
    c=df["Hierarchical_Cluster"]
)

plt.title("Hierarchical Clustering")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.show()


# ==============================================
# 14. DISPLAY FINAL DATA
# ==============================================

print("\nFinal Dataset with Clusters:")

print(df.head())

print("\nK-Means Cluster Counts:")
print(df["KMeans_Cluster"].value_counts())

print("\nHierarchical Cluster Counts:")
print(df["Hierarchical_Cluster"].value_counts())
