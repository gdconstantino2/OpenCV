import numpy as np
import cv2

# Inicializa a webcam
webcam = cv2.VideoCapture(0)
  
while True:
    ret, frame = webcam.read()
    height, width, _ = frame.shape
    
    if not ret:
        break

    # Converte para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Faixa de rosa no HSV
    lower_pink = np.array([140, 50, 50])  # Limite inferior
    upper_pink = np.array([170, 255, 255])  # Limite superior


    # Criar máscara para a cor rosa
    mask = cv2.inRange(hsv, lower_pink, upper_pink)

    # Suavizar a imagem para melhorar a detecção de círculos
    blurred = cv2.GaussianBlur(mask, (9, 9), 2)

    rect_width = width // 5  
    x_center_start = (width // 2) - (rect_width // 2)
    x_center_end = (width // 2) + (rect_width // 2)

    # Detectar círculos usando a Transformada de Hough
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                               param1=50, param2=30, minRadius=5, maxRadius=200)


    cv2.rectangle(frame, (x_center_start, 0), (x_center_end, height), (0, 255, 0), 2)

    if circles is not None:
        circles = np.uint16(np.around(circles))  # Arredondar os valores
        for i in circles[0, :]:
            
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 0, 0), 2)  # Contorno do círculo
            
            if (i[0]< x_center_start):
                print("vire para a esquerda")

            elif (i[0] > x_center_end):
                print("vire para a direita")

            else:
                print("está no meio da tela")

    # Mostrar as imagens
    cv2.imshow('frame', frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

# Liberar recursos
webcam.release()
cv2.destroyAllWindows()
