import numpy as np

matriz1 = np.array([[1, 1, 1], [2, 2, 2]])
matriz2 = np.array([[9, 9, 9], [9, 9, 9]])

suma_matrices = matriz1 + matriz2
resta_matrices = matriz1 - matriz2
producto_punto = np.dot(matriz1, matriz2.T)
producto_cruz = np.cross(matriz1, matriz2)
division_matrices = matriz1.astype(float) / matriz2

print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)
print("\nSuma de matrices:")
print(suma_matrices)
print("\nResta de matrices:")
print(resta_matrices)
print("\nProducto punto de matrices:")
print(producto_punto)
print("\nProducto cruz de matrices:")
print(producto_cruz)
print("\nDivisión de matrices:")
print(division_matrices.round(2))
