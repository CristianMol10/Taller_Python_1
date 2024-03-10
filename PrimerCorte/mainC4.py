import matplotlib.pyplot as plt

def vector(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

  
    ax.quiver(0, 0, 0, x, y, z, color='k', arrow_length_ratio=0.5)

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def main():
    print("Ingrese las coordenadas del vector:")
    x = float(input("Componente X: "))
    y = float(input("Componente Y: "))
    z = float(input("Componente Z: "))

    vector(x, y, z)

main()
