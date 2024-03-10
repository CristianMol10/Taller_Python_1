#https://ceiv.com.mx/rtd-pt100/#:~:text=Un%20RTD%20Pt100%20forma%20parte,de%20la%20resistencia%20y%20viceversa.
"""
R = R₀(1 + α(T - T₀))
R: Resistencia del RTD a la temperatura T (Ω)
R₀: Resistencia del RTD a la temperatura de referencia T₀ (Ω) 0° = 100 Ω 
α: Coeficiente de temperatura de resistencia del platino (0.00385 °C⁻¹)
T: Temperatura del RTD (°C)
T₀: Temperatura de referencia (°C)

Ecuaciones de Callendar-Van Dusen:
Temperatura RTD ≥ 0°C: Rt = R0(1+At+Bt2)
Temperatura RTD < 0°C: Rt = R0[1+At+Bt2+C(t-100)t3]
"""
def calcular_resistencia(t):
    R0 = 100.0  # Resistencia a 0°C para PT100
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12 if t < 0 else 0 
    
    if t >= 0:
        Rt = R0 * (1 + A * t + B * t**2)
    else:
        Rt = R0 * (1 + A * t + B * t**2 + C * (t - 100) * t**3)
    
    return Rt

def main():
    temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
    resistencia = calcular_resistencia(temperatura)
    print(f"La resistencia de la RTD a {temperatura}°C es {resistencia} ohmios.")

main()
