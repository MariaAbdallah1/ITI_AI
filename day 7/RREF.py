
import numpy as np
import sympy as sp

A = np.array([
    [0, 1, 2, 1],
    [1, 2, -1, 2],
    [0, -5, 3, -5]
])
b = np.array([-3, 5, -11])

augmented_matrix = np.column_stack((A, b))
sp.pprint(augmented_matrix)

augmented_matrix_sympy = sp.Matrix(augmented_matrix)
rref_matrix, pivot_columns = augmented_matrix_sympy.rref()

# Print the RREF matrix
print("RREF of the augmented matrix:")
sp.pprint(rref_matrix)
print(pivot_columns)
num_vars = A.shape[1]  
rank_A = sp.Matrix(A).rank()
rank_augmented = rref_matrix.rank()

print(f"Rank of A: {rank_A}")
print(f"Rank of [A|b]: {rank_augmented}")
if rank_A < rank_augmented:
    print("The system has no solution.")
elif rank_A == rank_augmented and rank_A == num_vars:
    print("The system has exactly one solution.")
elif rank_A == rank_augmented and rank_A < num_vars:
    print("The system has infinitely many solutions.")
else:
    print("Unexpected case.")