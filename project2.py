import cv2
import os
import numpy as np

# Carregar o classificador Haar Cascade treinado
cascade = cv2.CascadeClassifier(os.path.join('.', 'azul', 'cascade.xml'))

# Iniciar a webcam
webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    
    if not ret:
        break

    # Converter para tons de cinza para o Haar Cascade
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar objetos com Haar Cascade
    detections = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=8, minSize=(30, 30))

    # Converter para HSV para filtragem de cor
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir intervalo de cor azul (ajuste os valores se necessário)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Criar máscara azul
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Verificar quais detecções realmente são azuis
    for (x, y, w, h) in detections:
        roi_mask = mask[y:y+h, x:x+w]  # Recortar a região detectada na máscara azul
        
        # Verificar se há azul suficiente na região detectada
        blue_pixels = cv2.countNonZero(roi_mask)
        total_pixels = w * h
        blue_ratio = blue_pixels / total_pixels  # Porcentagem de azul na área

        if blue_ratio > 0.3:  # Ajuste o limite conforme necessário
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(frame, 'AZUL', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2, cv2.LINE_AA)

    # Mostrar a imagem original e a máscara azul
    cv2.imshow('Detecção de Azul com Haar Cascade', frame)
    cv2.imshow('Máscara Azul', mask)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
