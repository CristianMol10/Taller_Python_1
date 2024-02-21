import numpy as np

x = 2
y = 2
z = 5

def recta_cilindricas(x, y, z):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta, float(z)

def recta_esfericas(x, y, z):
  p = np.sqrt(x**2 + y**2 + z**2)
  theta = np.arctan2(y, x)
  phi = np.arccos(z / p)
  return float(p), float(theta), float(phi)

r_cilindrica, theta_cilindrica, z_cilindrica = recta_cilindricas(x, y, z)
print("\nCoordenadas cilíndricas:")
print("r =", round(r_cilindrica, 2))
print("theta =", round(theta_cilindrica, 2))
print("z =", round(z_cilindrica, 2))

p_esferica, theta_esferica, phi_esferica = recta_esfericas(x, y, z)
print("\nCoordenadas esfericas:")
print("p =", round(p_esferica, 2))
print("theta =", round(theta_esferica, 2))
print("phi =", round(phi_esferica, 2),)