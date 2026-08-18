import cv2
import numpy as np
import os

# Carregar a imagem
imagem = cv2.imread(os.path.join('.', 'azul', 'turquesa.jpg'))

# Converter para HSV
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Definir faixa de cor azul em HSV
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

# Criar máscara para a cor azul
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Contar pixels azuis
total_pixels = imagem.shape[0] * imagem.shape[1]
blue_pixels = cv2.countNonZero(mask)  # Conta quantos pixels são azuis

# Calcular porcentagem
porcentagem_azul = (blue_pixels / total_pixels) * 100

print(f"Porcentagem de azul: {porcentagem_azul:.2f}%")
