import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x=input(print("ingrese el valor de la cordenada X"))
y=input(print("ingrese el valor de la cordenada Y"))
z=input(print("ingrese el valor de la cordenada Z"))

ax1 = fig.add_subplot(111,projection='3d')

vector1 = np.array([x, y, z])
ax1.plot_wireframe(x, y, z)

plt.figure(figsize=(5, 5))
plt.title("sistema cordenado XYZ")
plt.grid(True)
plt.show()