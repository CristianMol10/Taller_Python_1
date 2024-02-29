import cv2 #Importar Libreria

# Leer la imagen, las imagenes se deben descargar localmente
img = cv2.imread("d:\Downloads\Mazda.png")

# Aplicar desenfoque a la imagen
blur = cv2.blur(img, (6,6))

# Binarizar la imagen
imgCanny = cv2.Canny(blur, 10, 150)

# Encontrar contornos
contornos, _ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Inicializar una lista para almacenar las coordenadas de todos los contornos
coordenadas_contornos = []

# Iterar sobre todos los contornos encontrados
for contorno in contornos:
    # Obtener las coordenadas del rectángulo que encierra el contorno
    x, y, w, h = cv2.boundingRect(contorno)
    coordenadas_contornos.append((x, y, w, h))

# Mostrar las coordenadas de los contornos
print("Coordenadas de los contornos:")
for i, (x, y, w, h) in enumerate(coordenadas_contornos, 1):
    print(f"Contorno {i}: Coordenadas (X, Y): ({x}, {y}), Ancho: {w}, Altura: {h}")

# Dibujar contornos
cv2.drawContours(img, contornos, -1, (0,255,0), 10)

# Visualizar la  imagen
cv2.imshow("Bordes", imgCanny)
cv2.imshow("Contornos de la imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()