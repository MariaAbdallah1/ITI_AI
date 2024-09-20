Norms
import numpy as np
#Norm1
# a1=np.array([2,3])
# l1_norm = np.sum(np.abs(a1))
# print("L1 norm of vector a1:", l1_norm)
# print(np.linalg.norm(a1, ord=1))

# a2=np.array([4,5])
# N1=((np.abs(a1[0]-a2[0]))+(np.abs(a1[1]-a2[1])))
# print("The manhatten disctance between a1 and a2:", N1)
# from scipy.spatial.distance import cityblock
# print("The manhatten disctance between a1 and a2:", cityblock(a1, a2)) 

# Y = np.array([3.0, -0.5, 2.0, 7.0])
# Y_hat = np.array([2.5, 0.0, 2.0, 8.0])
# print(Y-Y_hat)
# print("Mean Absolute Error:", np.mean(np.abs(Y - Y_hat)))
# from sklearn.metrics import mean_absolute_error
# print("Mean Absolute Error:", mean_absolute_error(Y , Y_hat))

#Norm2
a1 = np.array([2, 3])
l2_norm = np.sqrt(np.sum(np.square(a1)))
print("L2 norm of vector a1:", l2_norm)
print("L2 norm of vector a1 (using numpy.linalg.norm):", np.linalg.norm(a1, ord=2))

a2 = np.array([4, 5])
N2 = np.sqrt(np.sum(np.square(a1 - a2)))
print("The Euclidean distance between a1 and a2:", N2)
from scipy.spatial.distance import euclidean
print("The Euclidean distance between a1 and a2 :", euclidean(a1, a2))

Y = np.array([3.0, -0.5, 2.0, 7.0])
Y_hat = np.array([2.5, 0.0, 2.0, 8.0])
print(Y - Y_hat)
rmse = np.sqrt(np.mean(np.square(Y - Y_hat)))
print("Root Mean Square Error:", rmse)
from sklearn.metrics import mean_squared_error
rmse_sklearn = np.sqrt(mean_squared_error(Y, Y_hat))
print("Root Mean Square Error:", rmse_sklearn)

#MaxNorm
a = np.array([3, -5, 7, 2])
max_norm_manual = np.max(np.abs(a))
print("Max Norm (manual calculation):", max_norm_manual)
max_norm_numpy = np.linalg.norm(a, ord=np.inf)
print("Max Norm (using numpy.linalg.norm):", max_norm_numpy)

a1 = np.array([2, 3])
a2 = np.array([4, 5])
print("Chebyshev Distance:", np.max(np.abs(a1 - a2)))
from scipy.spatial.distance import chebyshev
print("Chebyshev Distance:", chebyshev(a1, a2))