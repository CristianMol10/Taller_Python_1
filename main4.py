#https://ceiv.com.mx/rtd-pt100/#:~:text=Un%20RTD%20Pt100%20forma%20parte,de%20la%20resistencia%20y%20viceversa.

"""
R = R₀(1 + α(T - T₀))

R: Resistencia del RTD a la temperatura T (Ω)
R₀: Resistencia del RTD a la temperatura de referencia T₀ (Ω) 0° = 100 Ω 
α: Coeficiente de temperatura de resistencia del platino (0.00385 °C⁻¹)
T: Temperatura del RTD (°C)
T₀: Temperatura de referencia (°C)

"""
def resistencia_PT100(B):
  A = 0.00385
  Ro = 100.0

  R = Ro * (1 + A * (B - 0))
  return float(R)

B = 50
print("La resistencia para la temperatura", B ,"°C es:", round(resistencia_PT100(B),2), "Ω")
