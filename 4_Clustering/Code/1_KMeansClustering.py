import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

dataset = pd.read_csv('4_Clustering\Datasets\Mall_Customers.csv')
x = dataset.iloc[:, [3, 4]].values

from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters= i, init= 'k-means++', random_state= 42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title("The Elbow Method")
plt.xlabel("Nb of clusters")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters= 5, init= 'k-means++', random_state= 42)
y_kmeans = kmeans.fit_predict(x)
print(y_kmeans)

plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c= 'red', label= 'cluster1')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c= 'blue', label= 'cluster2')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c= 'green', label= 'cluster3')
plt.scatter(x[y_kmeans == 3, 0], x[y_kmeans == 3, 1], s = 100, c= 'cyan', label= 'cluster4')
plt.scatter(x[y_kmeans == 4, 0], x[y_kmeans == 4, 1], s = 100, c= 'magenta', label= 'cluster5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s= 300, c= 'yellow', label= 'Centroids')
plt.title("Clusters")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()