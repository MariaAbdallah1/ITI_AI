import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def manhattan_distance(point1, point2):
    return np.sum(np.abs(point1 - point2))

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def init_centroids(data, k):
    np.random.seed(42)
    indices = np.random.choice(data.shape[0], size=k, replace=False)
    return data[indices]

def assign_clusters(data, centroids, distance_func):
    clusters = []
    for point in data:
        distances = [distance_func(point, centroid) for centroid in centroids]
        clusters.append(np.argmin(distances))
    return clusters

def update_centroids(data, clusters, k):
    new_centroids = []
    for i in range(k):
        cluster_points = data[np.array(clusters) == i]
        if len(cluster_points) > 0:
            new_centroids.append(np.mean(cluster_points, axis=0))
    return np.array(new_centroids)

def calculate_wss(data, clusters, centroids, distance_func):
    wss = 0
    for i, point in enumerate(data):
        centroid = centroids[clusters[i]]
        wss += distance_func(point, centroid)**2
    return wss

def kmeans(data, k, distance_func, max_iters=100, threshold=1.0):
    centroids = init_centroids(data, k)
    prev_wss = float('inf')
    
    for _ in range(max_iters):
        clusters = assign_clusters(data, centroids, distance_func)
        new_centroids = update_centroids(data, clusters, k)
        wss = calculate_wss(data, clusters, new_centroids, distance_func)
        if abs(prev_wss - wss) < threshold:
            break
        prev_wss = wss
        centroids = new_centroids
    
    return clusters, centroids, wss

def elbow_method(data, max_k, distance_func):
    wcss = []
    for k in range(1, max_k + 1):
        _, _, wss = kmeans(data, k, distance_func)
        wcss.append(wss)
    
    return wcss

def find_best_centroids(data, k, distance_func, n_runs):
    best_centroids = None
    best_wss = float('inf')
    for _ in range(n_runs):
        clusters, centroids, wss = kmeans(data, k, distance_func)
        if wss < best_wss:
            best_wss = wss
            best_centroids = centroids
            best_clusters = clusters
    return best_clusters, best_centroids, best_wss

def find_elbow_point(wcss):
    first_derivative = np.diff(wcss)
    second_derivative = np.diff(first_derivative)
    elbow_point = np.argmin(second_derivative) + 2 
    return elbow_point

df = pd.read_csv('d:/Maria_iti/day 12/Countryclusters.csv')
data = df[['latitude', 'longitude']].values

max_k = 10 
n_runs = 10

wcss_manhattan = elbow_method(data, max_k, manhattan_distance)
wcss_euclidean = elbow_method(data, max_k, euclidean_distance)

plt.figure(figsize=(10, 6))

plt.plot(range(1, max_k + 1), wcss_manhattan, 'o-', label='Manhattan Distance', color='blue')
plt.plot(range(1, max_k + 1), wcss_euclidean, 'o-', label='Euclidean Distance', color='green')

plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.legend()
plt.grid(True)
plt.show()

best_k_manhattan = find_elbow_point(wcss_manhattan)
best_k_euclidean = find_elbow_point(wcss_euclidean)

print(f"Best number of clusters (Manhattan Distance): {best_k_manhattan}")
print(f"Best number of clusters (Euclidean Distance): {best_k_euclidean}")

clusters_manhattan, centroids_manhattan, wss_manhattan = find_best_centroids(data, best_k_manhattan, manhattan_distance, n_runs)
clusters_euclidean, centroids_euclidean, wss_euclidean = find_best_centroids(data, best_k_euclidean, euclidean_distance, n_runs)

print("Best Clusters with Manhattan Distance:")
print(clusters_manhattan)
print("Best Centroids with Manhattan Distance:")
print(centroids_manhattan)
print("Best WSS with Manhattan Distance:", wss_manhattan)

print("\nBest Clusters with Euclidean Distance:")
print(clusters_euclidean)
print("Best Centroids with Euclidean Distance:")
print(centroids_euclidean)
print("Best WSS with Euclidean Distance:", wss_euclidean)

cluster_countries_manhattan = {i: [] for i in range(best_k_manhattan)}
cluster_countries_euclidean = {i: [] for i in range(best_k_euclidean)}

for i, cluster in enumerate(clusters_manhattan):
    cluster_countries_manhattan[cluster].append(df['name'].iloc[i])

for i, cluster in enumerate(clusters_euclidean):
    cluster_countries_euclidean[cluster].append(df['name'].iloc[i])

print("\nCountries in each cluster (Manhattan Distance):")
for cluster, countries in cluster_countries_manhattan.items():
    print(f"Cluster {cluster + 1}: {countries}")

print("\nCountries in each cluster (Euclidean Distance):")
for cluster, countries in cluster_countries_euclidean.items():
    print(f"Cluster {cluster + 1}: {countries}")

def plot_clusters(data, clusters, centroids, title):
    plt.figure(figsize=(10, 6))
    unique_clusters = np.unique(clusters)
    colors = plt.cm.get_cmap('tab10', len(unique_clusters))
    for cluster in unique_clusters:
        cluster_points = data[np.array(clusters) == cluster]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=colors(cluster), label=f'Cluster {cluster + 1}')
    for i, centroid in enumerate(centroids):
        plt.scatter(centroid[0], centroid[1], color=colors(i), s=200, marker='X', edgecolor='black')
    
    plt.title(title)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_clusters(data, clusters_manhattan, centroids_manhattan, 'Best K-Means Clustering with Manhattan Distance')
plot_clusters(data, clusters_euclidean, centroids_euclidean, 'Best K-Means Clustering with Euclidean Distance')
