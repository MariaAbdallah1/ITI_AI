import numpy as np
data = np.array([
    [51, 92, 14, 71, 60],
    [20, 82, 86, 74, 70],
    [10, 84, 70, 33, 61],
    [75, 98, 56, 83, 41],
    [56, 92, 48, 37, 80],
    [28, 46, 93, 54, 22],
    [62, 99, 74, 50, 20],
    [21, 84, 77, 96, 19],
    [63, 29, 71, 48, 88],
    [17, 11, 94, 22, 48],
    [93, 66, 58, 54, 10],
    [71, 96, 87, 35, 99],
    [50, 82, 12, 73, 31],
    [83, 64, 50, 72, 19],
    [96, 53, 19, 60, 90],
    [25, 68, 42, 55, 94],
    [47, 81, 99, 72, 63],
    [52, 35, 40, 91, 12],
    [64, 58, 36, 22, 78],
    [89, 46, 68, 94, 21]
])
query_point = np.array([63, 45, 76, 32, 14])

def euclidean(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def manhattan(p1, p2):
    return np.sum(np.abs(p1 - p2))

def chebyshev(p1, p2):
    return np.max(np.abs(p1 - p2))

def nearest_point(data, query_point):
    min_euclidean = float('inf')
    min_manhattan = float('inf')
    min_chebyshev = float('inf')

    for point in data:
        dist_euclidean = euclidean(point, query_point)
        if dist_euclidean < min_euclidean:
            min_euclidean = dist_euclidean
            nearest_euclidean = point

        dist_manhattan = manhattan(point, query_point)
        if dist_manhattan < min_manhattan:
            min_manhattan = dist_manhattan
            nearest_manhattan = point

        dist_chebyshev = chebyshev(point, query_point)
        if dist_chebyshev < min_chebyshev:
            min_chebyshev = dist_chebyshev
            nearest_chebyshev = point

    return nearest_euclidean, nearest_manhattan, nearest_chebyshev

nearest_euclidean, nearest_manhattan, nearest_chebyshev = nearest_point(data, query_point)

print("Nearest point using Euclidean Norm:", nearest_euclidean)
print("Nearest point using Manhattan Norm:", nearest_manhattan)
print("Nearest point using Chebyshev Norm:", nearest_chebyshev)
