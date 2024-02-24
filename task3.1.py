from mpl_toolkits import mplot3d
import numpy as np
import math
import matplotlib.pyplot as plt
x_values = np.arange(-7.5,7.5,0.2)
y_values = x_values 
x_grid, y_grid = np.meshgrid(x_values, y_values) 
z_grid = np.sin(np.sqrt(x_grid**2+y_grid**2))/np.sqrt(x_grid**2+y_grid**2)

plt.axes(projection = '3d').plot_surface(x_grid, y_grid, z_grid)
plt.title('surface plot')