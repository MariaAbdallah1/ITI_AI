import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import *

# Create some sample data points
x = np.array([0, 1, 2, 3, 5, 6, 7, 8, 9, 10])
y = np.array([0, 1, 4, 9, 16, 5, 67, 98, 24, 20])

x_interp = np.linspace(0, 14, 100)

# Linear Interpolation
y_linear = np.interp(x_interp, x, y)
# Quadratic Interpolation
p =  np.polyfit(x,y,2)
y_quadratic = np.polyval(p, x_interp)
# Cubic Spline Interpolation
cs = CubicSpline(x, y)
y_spline = cs(x_interp)

# Plotting
plt.scatter(x, y, label='Data Points')
plt.plot(x_interp, y_linear, label='Linear Interpolation')
plt.plot(x_interp, y_spline, label='Cubic Spline Interpolation')
# plt.plot(x_interp, y_quadratic, label='quadratic Interpolation (Degree 2)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Interpolation Techniques')
plt.show()