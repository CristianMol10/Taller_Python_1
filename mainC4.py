"""
import numpy as np
import matplotlib.pyplot as plt

x=input(print("ingrese el valor de la cordenada X"))
y=input(print("ingrese el valor de la cordenada Y"))
z=input(print("ingrese el valor de la cordenada Z"))

vector1 = np.array([x, y, z])

plt.figure(figsize=(5, 5))
plt.title("sistema cordenado XYZ")
plt.grid(True)
plt.show()
"""
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax1 = fig.add_subplot(111,projection='3d')
x = (0,20)
y = (0,20)
z = (0,20)

ax1.plot_wireframe(x, y, z)

plt.show()