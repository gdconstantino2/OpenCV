import os
import cv2

img = cv2.imread(os.path.join('.', 'fotos', 'captura1.jpg'))  


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte cores de uma para outra

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.imshow('img_gray', img_gray)

cv2.waitKey(0)
