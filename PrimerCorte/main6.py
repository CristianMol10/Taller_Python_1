import math

"""
Para calcular la fuerza de avance y retroceso de un cilindro neumático de doble efecto, se necesitan los siguientes datos:

Diámetro del vástago (d): Es el diámetro de la parte del cilindro que se mueve.
Presión de aire (P): Es la presión del aire que se suministra al cilindro.
Área efectiva del vástago (A): Es el área del vástago del cilindro.
Área efectiva del émbolo (A_e): Es el área del émbolo del cilindro.

F_avance = P * A_e
F_retroceso = P * (A_e - A)

"""

diametro_embolo = 20  # mm
diametro_vastago = 10  # mm
presion = 6  # bar

# Cálculo del área efectiva del émbolo
area_embolo = ((diametro_embolo / 2)**2 * math.pi) / 100  # cm^2

# Cálculo del área efectiva del vástago
area_vastago = ((diametro_vastago / 2)**2) *math.pi / 100  # cm^2

fuerza_avance = presion * area_embolo

fuerza_retroceso = presion * (area_embolo - area_vastago)

print(f"Fuerza de avance: {round(fuerza_avance,2)} Pascales")
print(f"Fuerza de retroceso: {round(fuerza_retroceso,2)} Pascales")
