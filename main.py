import numpy as np

vector1 = np.array([2, 2, 2])
vector2 = np.array([2, 2, 2])
#comentario random
suma_vectores = vector1+vector2
resta_vectores = vector1-vector2
producto_punto = np.dot(vector1, vector2)
producto_cruz = np.cross(vector1, vector2)
division_vectores = vector1/vector2

print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Suma:", suma_vectores)
print("Resta:", resta_vectores)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("División:", division_vectores)