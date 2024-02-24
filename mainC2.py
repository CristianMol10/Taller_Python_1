import matplotlib.pyplot as plt
from scipy import signal
import control as ct

Frecuencia_Natural = float(input("Ingrese la frecuencia natural del sistema: "))
Coeficiente_De_Amortiguamiento = float(input("Ingrese el coeficiente de amortiguamiento del sistema: "))

def Sistema_Segundo_Orden(Frecuencia_Natural, Coeficiente_De_Amortiguamiento):
    num = [Frecuencia_Natural**2]
    den = [1, 2 * Coeficiente_De_Amortiguamiento * Frecuencia_Natural, Frecuencia_Natural**2]

    sys = signal.TransferFunction(num, den)
    print(sys)
    t, y_step = signal.step(sys)

    s = ct.TransferFunction.s
    G = (num[0])/(den[0]*s**2 + den[1]*s + den[2])
    print(G)

    if Coeficiente_De_Amortiguamiento < 1:
        system_type = "Subamortiguado"
    elif Coeficiente_De_Amortiguamiento == 1:
        system_type = "Críticamente amortiguado"
    else:
        system_type = "Sobreamortiguado"

    plt.figure(figsize=(6, 5))
    plt.plot(t, y_step, label='Respuesta al escalón', color='red')
    plt.title(f"Respuesta del sistema ({system_type})")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Respuesta")
    plt.legend()
    plt.grid(True)
    plt.show()

Sistema_Segundo_Orden(Frecuencia_Natural, Coeficiente_De_Amortiguamiento)
