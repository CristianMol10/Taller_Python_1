import numpy as np

def RotacionX(Angulo):
    
    #Función para calcular la matriz de rotación en el eje X dado un ángulo en radianes.
    
    AnguloCos = np.cos(Angulo)
    AnguloSin = np.sin(Angulo)
    RotacionMatrix = np.array([[1, 0, 0],
                                [0, AnguloCos, -AnguloSin],
                                [0, AnguloSin, AnguloCos]])
    return RotacionMatrix

def RotacionY(Angulo):

    #Función para calcular la matriz de rotación en el eje Y dado un ángulo en radianes.
    
    AnguloCos = np.cos(Angulo)
    AnguloSin = np.sin(Angulo)
    RotacionMatrix = np.array([[AnguloCos, 0, AnguloSin],
                                [0, 1, 0],
                                [-AnguloSin, 0, AnguloCos]])
    return RotacionMatrix

def RotacionZ(Angulo):
    
    #Función para calcular la matriz de rotación en el eje Z dado un ángulo en radianes.

    AnguloCos = np.cos(Angulo)
    AnguloSin = np.sin(Angulo)
    RotacionMatrix = np.array([[AnguloCos, -AnguloSin, 0],
                                [AnguloSin, AnguloCos, 0],
                                [0, 0, 1]])
    return RotacionMatrix

# Definir ángulo de rotación en radianes
Angulo = np.pi / 4  # Por ejemplo, rotación de 45 grados

    # Realizar rotación en el eje X
RotacionX = RotacionX(Angulo)
print("Matriz de rotación en el eje X:")
print(RotacionX)

# Realizar rotación en el eje Y
RotacionY = RotacionY(Angulo)
print("\nMatriz de rotación en el eje Y:")
print(RotacionY)

# Realizar rotación en el eje Z
RotacionZ = RotacionZ(Angulo)
print("\nMatriz de rotación en el eje Z:")
print(RotacionZ)
    