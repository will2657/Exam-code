import matplotlib.pyplot as plt
import numpy as np
import random 
x_values = np.linspace(0,150,15)
y_values = [1,0.87,0.12,0.45,0,0.25,0.63,0.89,0.21,0.71,0.12,0.78,0.33,0.45,0.31]
y2_values=np.random.rand(15)
colors=np.random.randint(100, size=(15))
sizes = 10 * np.random.randint(100, size=(15))
plt.scatter(x_values, y_values,  c='red')
plt.scatter(x_values, y2_values,s=sizes, c=colors, cmap='viridis')
plt.title('Random Scatter')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()