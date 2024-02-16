import math
print("seleccione la opcion para calcular el volumen de:")
opcion = int(input(print(f" 1. prisma\n 2. piramide\n 3. cono truncado\n 4. cilindro\n")))

if opcion == 1:
  print("a seleccionado la opcion volumen de un prisma, por favor seleccione el tipo de prisma:")
  prisma = int(input(print(f" 1. triangular\n 2. rectangular\n 3. trapezoidal\n 4. romboidal\n 5.pentagonal\n 6.hexagonal\n 7.octagonal\n")))
  if prisma == 1:
    print()
  if prisma == 2:
    print()
  if prisma == 3:
    print()
  if prisma == 4:
    print()
  if prisma == 5:
    print()
  if prisma == 6:
    print()
  if prisma == 7:
    print()

if opcion == 2:
  print("a seleccionado la opcion volumen de una piramide:")
  lado1 = float(input("ingresa el valor del primer lado \n"))
  lado2 = float(input("ingresa el valor del segundo lado \n"))
  altura = float(input("ingresa el valor de la altura \n"))
  volumen=lado1*lado2*altura/3
  print("el volumen de la piramide es: ", volumen)

if opcion == 3:
  print("a seleccionado la opcion volumen de un cono truncado:")
  radio1 = float(input("ingresa el valor del primer radio \n"))
  radio2 = float(input("ingresa el valor del segundo radio \n"))
  altura = float(input("ingresa el valor de la altura \n"))
  volumen=math.pi*altura*(radio1**2+radio2**2+radio1*radio2)
  print("el volumen del cono truncado es: ", volumen)

if opcion == 4:
  print("a seleccionado la opcion volumen de un cilindro:")
  radio = float(input("ingresa el valor del radio \n"))
  altura = float(input("ingresa el valor de la altura \n"))
  volumen = math.pi*radio**2*altura
  print("el volumen del cilindro es: ", volumen)

if opcion < 1 or opcion > 4:
  print("seleccion invalida")