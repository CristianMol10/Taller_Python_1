print("seleccione la opcion del tipo de robot al cual quiere conocer la informacion:")
opcion = str(input())
a = str("cilindrico")
b = str("cartesiano")
c = str("esferico")

if opcion == a:
    print("Robot Cilindrico")
    print("Este tipo de Robots consta de una articulacion rotacional y dos articulaciones prismaticas, cuyos ejes son coincidentes con los ejes cartesianos \nes un robot cuyos ejes forman un sistema de cordenadas cilindricas")

if opcion == b:
    print("Robot Cartesiano")
    print("Este tipo de Robots tiene 3 articulaciones prismaticas en su brazo, Empleado para trabajos de Pick and Place")

if opcion == c:
    print("Robot Esferico")
    print("Este tipo de robot tiene en sus primeras dos articulaciones rotacionales con sus ejes perpendiculares, y una tercera de tipo primsatico con su eje perpendicular a las dos primeras")
