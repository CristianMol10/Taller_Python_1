import numpy as np
import matplotlib.pyplot as plt

temperatures = np.linspace(-200, 200)

plt.figure(figsize=(5, 5))
plt.plot(temperatures, temperatures)
plt.title('Sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Temperatura del sensor (°C)')
plt.grid(True)
plt.show()