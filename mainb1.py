corriente = float(input("Ingrese la corriente del circuito: "))

voltaje = float(input("Ingrese el voltaje del circuito: "))

potenciacalculada = round(corriente * voltaje,2)

print("La potencia calculada es: " + str(potenciacalculada) + "W")