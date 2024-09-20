import matplotlib.pyplot as plt
import numpy as np

v1 = np.array([3,2])
v2 = np.array([1,1])
v3 = v1+v2 #(Addition)
# print(v3)
# v3=v1-v2 #(Subtraction)
# print(v3)
scalar=3
# v3=v2*scalar
# Visualize the v1, v2, and v3
fig, axes = plt.subplots(1, 3)
axes[0].quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1)
axes[1].quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1)
axes[2].quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1)
axes[0].set_xlim([-1, 10])
axes[0].set_ylim([-1, 6])
axes[1].set_xlim([-1, 10])
axes[1].set_ylim([-1, 6])
axes[2].set_xlim([-1, 10])
axes[2].set_ylim([-1, 6])
plt.show()