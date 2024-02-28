import numpy as np
import matplotlib.pyplot as plt

# Definir los puntos para cada letra

def nombre_david():
    nombre1 = {
        'D': [(0, 0),(0, 2),(1, 1.5),(1,0.5),(0,0)],
        'A': [(1.5, 0), (2, 2), (2.5, 0),(2.25,1),(1.75,1)],
        'V': [(3, 2), (4, 0), (5,2)],
        'I': [(6, 0), (6, 2)],
        'DD': [(7,0),(7, 2),(8,1.5),(8,0.5),(7,0)]
    }

    # Crear una figura
    plt.figure()

    # Dibujar cada letra
    for letra, puntos in nombre1.items():
        x, y = zip(*puntos)
        plt.plot(x, y, 'o-', label=letra)

    # Ajustar los límites del gráfico
    plt.xlim(-1, 15)
    plt.ylim(-1, 3)

    # Añadir etiquetas y leyenda
    plt.title("Nombre")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def nombre_Juan():
    nombre1 = {
        'J': [(-0.5, 0),(0, 0),(0, 2),(-0.5,2),(0.5,2)],
        'U': [(1, 2), (1, 0), (2, 0),(2,2)],
        'A': [(3, 0), (4, 2), (5,0),(4.5,1),(3.5,1)],
        'N': [(6, 0), (6, 2),(8,0),(8,2)]
    }

    # Crear una figura
    plt.figure()

    # Dibujar cada letra
    for letra, puntos in nombre1.items():
        x, y = zip(*puntos)
        plt.plot(x, y, 'o-', label=letra)

    # Ajustar los límites del gráfico
    plt.xlim(-1, 15)
    plt.ylim(-1, 3)

    # Añadir etiquetas y leyenda
    plt.title("Nombre")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def nombre_Steven():
    nombre1 = {
        'S': [(1, 2),(0, 2),(0, 1),(1,1),(1,0),(0,0)],
        't': [(1.5,2), (2.5, 2), (2, 2),(2,0)],
        'e': [(4, 2), (3, 2), (3,0),(4,0),(3,0),(3,1),(4,1)],
        'v': [(4.5,2), (5.5, 0), (6.5, 2)],
        'ee': [(8, 2), (7, 2), (7,0),(8,0),(7,0),(7,1),(8,1)],
        'n': [(8.5,0),(8.5, 2), (10, 0), (10,2)]
    }

    # Crear una figura
    plt.figure()

    # Dibujar cada letra
    for letra, puntos in nombre1.items():
        x, y = zip(*puntos)
        plt.plot(x, y, 'o-', label=letra)

    # Ajustar los límites del gráfico
    plt.xlim(-1, 15)
    plt.ylim(-1, 3)

    # Añadir etiquetas y leyenda
    plt.title("Nombre")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def nombre_Hector():
    nombre1 = {
        'H': [(0, 0),(0, 2),(0, 1),(1,1),(1,0),(1,2)],
        'E': [(2.5, 2), (1.5, 2), (1.5,0),(2.5,0),(1.5,0),(1.5,1),(2.5,1)],
        'C': [(4, 2), (3, 2), (3,0),(4,0),(3,0)],
        'T': [(4.5,2), (5.5, 2), (6.5, 2),(5.5, 2),(5.5,0)],
        'O': [(8, 2), (7, 2), (7,0),(8,0),(8,2)],
        'R': [(8.5,0),(8.5, 2), (9.5, 2), (9.5,1),(8.5,1),(9.5,1),(10,0)]
    }

    # Crear una figura
    plt.figure()

    # Dibujar cada letra
    for letra, puntos in nombre1.items():
        x, y = zip(*puntos)
        plt.plot(x, y, 'o-', label=letra)

    # Ajustar los límites del gráfico
    plt.xlim(-1, 15)
    plt.ylim(-1, 3)

    # Añadir etiquetas y leyenda
    plt.title("Nombre")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def inicio():
    opcion = input("Seleccione el nombre que quiere imprimir:\n1. David\n2. Juan\n3. Steven\n4. Hector\n")

    if opcion == "1":
        nombre_david()
    elif opcion == "2":
        nombre_Juan()
    elif opcion == "3":
        nombre_Steven()
    elif opcion == "4":
        nombre_Hector()

while 1:
 inicio()
