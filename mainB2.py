import random
mayor = int(input('Ingrese el rango maximo de numeros\n'))
menor = int(input('Ingrese el rango minimo de numeros\n'))
cantidad = int(input('Ingresa el valor de numeros aleatorios\n'))
 
lista = [random.randint(menor, mayor) for _ in range(cantidad)]
print("sus numeros aleatorios son: \n", lista)