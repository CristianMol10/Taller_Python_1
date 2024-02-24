import math
print("seleccione la opcion para calcular el volumen de:")
opcion = int(input(print(f" 1. prisma\n 2. piramide\n 3. cono truncado\n 4. cilindro\n")))

if opcion == 1:
  print("a seleccionado la opcion volumen de un prisma, por favor seleccione el tipo de prisma:")
  prisma = int(input(print(f" 1.triangular\n 2.rectangular\n 3.trapezoidal\n 4.romboidal\n 5.pentagonal\n 6.hexagonal\n 7.octagonal\n")))
  if prisma == 1:
    print("a seleccionado un prisma triangular")
    altura = int(input("ingresa el valor en cm de la altura del prisma \n"))
    base = int(input("ingresa el valor en cm de la base del prisma \n"))
    largo = int(input("ingresa el largo en cm del prisma \n"))
    volumen = ((altura*base)/2)*largo
    print("el volumen del prisma triangular es: ", volumen,"cm")

  if prisma == 2:
    print("a seleccionado un prisma rectangular")
    altura = int(input("ingresa el valor de la altura en cm del prisma \n"))
    ancho = int(input("ingresa el valor de la base en cm del prisma \n"))
    largo = int(input("ingresa el largo en cm del prisma \n"))
    volumen = altura*ancho*largo
    print("el volumen del prisma rectangular es: ", volumen, "cm")
    
  if prisma == 3:
    print("a seleccionado un prisma trapezoidal")
    basemay = float(input("ingresa el valor de la base mayor en cm del prisma \n"))
    basemen = float(input("ingresa el valor de la base menor en cm del prisma \n"))
    altura = float(input("ingresa la altura en cm del prisma \n"))
    largo = float(input("ingresa el largo en cm del prisma \n"))
    volumen = ((basemay+basemen)/2)*altura*largo
    print("el volumen del prisma trapezoidal es: ", volumen, "cm")

  if prisma == 4:
    print("a seleccionado un prisma romboidal")
    diagonalmay = float(input("ingresa el valor de la diagonal mayor del rombo base en cm del prisma \n"))
    diagonalmen = float(input("ingresa el valor de la diagonal menor del rombo base en cm del prisma \n"))
    largo = float(input("ingresa el largo en cm del prisma \n"))
    volumen = ((diagonalmay*diagonalmen)/2)*largo
    print("el volumen del prisma romboidal es: ", volumen, "cm")

  if prisma == 5:
    print("a seleccionado un prisma pentagonal")
    ladop = float(input("ingresa el valor del lado del pentagono base en cm del prisma \n"))
    apotema = float(input("ingresa el valor de la apotema del pentagono base en cm del prisma \n"))
    largo = float(input("ingresa el largo en cm del prisma \n"))
    volumen = ((5*ladop*apotema)/2)*largo
    print("el volumen del prisma pentagonal es: ", volumen, "cm")

  if prisma == 6:
    print("a seleccionado un prisma hexagonal")
    ladoh = float(input("ingresa el valor del lado del hexagono base en cm del prisma \n"))
    apotema = float(input("ingresa el valor de la apotema del hexagono base en cm del prisma \n"))
    largo = float(input("ingresa el largo en cm del prisma \n"))
    volumen = 3*ladoh*apotema*largo
    print("el volumen del prisma hexagonal es: ", volumen, "cm")
    
  if prisma == 7:
    print("a seleccionado un prisma octagonal")
    ladoo = float(input("ingresa el valor del lado del octagono base en cm del prisma \n"))
    apotema = float(input("ingresa el valor de la apotema del octagono base en cm del prisma \n"))
    largo = float(input("ingresa el largo en cm del prisma \n"))
    volumen = 4*ladoo*apotema*largo
    print("el volumen del prisma octagonal es: ", volumen, "cm")    

if opcion == 2:
  print("a seleccionado la opcion volumen de una piramide:")
  lado1 = float(input("ingresa el valor en cm del primer lado \n"))
  lado2 = float(input("ingresa el valor en cm del segundo lado \n"))
  altura = float(input("ingresa el valor en cm de la altura \n"))
  volumen=lado1*lado2*altura/3
  print("el volumen de la piramide es: ", volumen, "cm")

if opcion == 3:
  print("a seleccionado la opcion volumen de un cono truncado:")
  radio1 = float(input("ingresa el valor en cm del primer radio \n"))
  radio2 = float(input("ingresa el valor en cm del segundo radio \n"))
  altura = float(input("ingresa el valor en cm de la altura \n"))
  volumen=math.pi*altura*(radio1**2+radio2**2+radio1*radio2)
  print("el volumen del cono truncado es: ", volumen%.2, "cm")

if opcion == 4:
  print("a seleccionado la opcion volumen de un cilindro:")
  radio = float(input("ingresa el valor en cm del radio \n"))
  altura = float(input("ingresa el valor en cm de la altura \n"))
  volumen = math.pi*radio**2*altura
  print("el volumen del cilindro es: ", volumen, "cm")

if opcion < 1 or opcion > 4:
  print("seleccion invalida")