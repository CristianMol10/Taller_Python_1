import numpy as np

matriz1 = np.array([[1, 1, 1], [2, 2, 2])
matriz2 = np.array([[1, 1, 1], [2, 2, 2],)

suma_matrices = matriz1 + matriz2
resta_matrices = matriz1 - matriz2
producto_elemento_a_elemento = matriz1 * matriz2
producto_matricial = np.dot(matriz1, matriz2)

print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)
print("\nSuma:")
print(suma_matrices)
print("\nResta:")
print(resta_matrices)
print("\nProducto elemento a elemento:")
print(producto_elemento_a_elemento)
print("\nProducto matricial:")
print(producto_matricial)
