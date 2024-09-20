import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/Maria Abdallah/Downloads/Maria_iti/day 7/Breast_cancer_data.csv")
data = df.drop(columns=['diagnosis']).values
query_point = np.array([17.99, 10.38, 122.8, 1001.0, 0.1184])

def euclidean(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def manhattan(p1, p2):
    return np.sum(np.abs(p1 - p2))

def chebyshev(p1, p2):
    return np.max(np.abs(p1 - p2))

def nearest_points(data, query_point, distance_function, top_n=3):
    distances = [distance_function(point, query_point) for point in data]
    nearest_i = np.argsort(distances)[:top_n]
    nearest_points = [data[i] for i in nearest_i]
    return nearest_points

def format_point(point):
    return ' ,'.join([f' {x:.2f}' for x in point])

method = euclidean
method_name = "Euclidean"

nearest_points = nearest_points(data, query_point, method)

print(f"Nearest 3 points using {method_name} Norm:")
for i, point in enumerate(nearest_points):
    print(f"Point {i+1}: {format_point(point)}")
