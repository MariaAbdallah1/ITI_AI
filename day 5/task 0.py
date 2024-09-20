import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 1.0    # Thermal conductivity
L = 1.0    # Thickness of the wall
G = 0.5    # Heat generation rate
Tw = 50.0  # Heat at both surfaces of the wall

# Matrix dimensions
nx, ny = 20, 20
T = np.zeros((nx, ny))

# Compute temperature distribution
x = np.linspace(0, L, nx)
y = np.linspace(0, L, ny)
X, Y = np.meshgrid(x, y)

T = (G * L**2 / (2 * K)) * (1 - (X**2 / L**2)) + Tw

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, T, cmap='hot')

# Labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Temperature')
ax.set_title('Temperature Distribution Across the Wall')

plt.show()