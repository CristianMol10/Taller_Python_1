import numpy as np
import matplotlib.pyplot as plt

'''
 Carga  // V(t)=V(1−e− RC)
 Descarga // V(t)=V*e− RC)

'''


Voltaje = float(input("Ingrese el voltaje inicial (V): "))
Resistencia = float(input("Ingrese la resistencia (Ω): "))
Capacitancia = float(input("Ingrese la capacitancia (μF): "))

tiempo = np.linspace(0, 20000, 1000)

def carga_descarga_RC(Voltaje, Capacitancia, Resistencia, tiempo):
    
    tau = Resistencia * Capacitancia
    carga = Voltaje * (1 - np.exp(-tiempo / tau))
    descarga = Voltaje * np.exp(-tiempo / tau)

    return carga, descarga

carga, descarga = carga_descarga_RC(Voltaje, Capacitancia, Resistencia, tiempo)


plt.figure(figsize=(6, 4))
plt.plot(tiempo, carga, label='Carga')
plt.plot(tiempo, descarga, label='Descarga')
plt.title('Carga y descarga de un capacitor en un circuito RC')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)
plt.show()
