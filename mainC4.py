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