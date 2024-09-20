import numpy as np
from scipy import linalg
from scipy.linalg import solve
A = np.array(
    [
        [1, 9, 2, 1, 1],
        [10, 1, 2, 1, 1],
        [1, 0, 5, 1, 1],
        [2, 1, 1, 2, 9],
        [2, 1, 2, 13, 2],
    ]
)
#A . Seta=B
#Seta=Inverse(A) . b
b = np.array([170, 180, 140, 180, 350]).reshape((-1, 1))
A_inv = linalg.inv(A)
# x = A_inv @ b
x=solve(A,b)
print(x)