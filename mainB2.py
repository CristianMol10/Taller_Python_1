import random

def lista(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.random()
      return lista

print("Ingrese el numero deseado de numeros aleatorios")
n=int(input())

aleatorios=lista(n)
print("sus numeros aleatorios son: \n", aleatorios)