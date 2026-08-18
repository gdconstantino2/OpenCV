import os

import cv2


img = cv2.imread(os.path.join('.', 'fotos', 'captura1.jpg'))  


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converte cores de uma para outra


cv2.imshow('img', img)
cv2.imshow('img_rgb', img_rgb)
cv2.waitKey(0)