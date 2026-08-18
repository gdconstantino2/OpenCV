import os

import cv2



#*********************************************LER IMAGEM*********************************************************
image_path = os.path.join('.', 'fotos', 'captura1.jpg')
img = cv2.imread(image_path)  


#*********************************************ESCREVER IMAGEM*********************************************************
cv2.imwrite(os.path.join('.', 'fotos', 'captura1_out.jpg'), img)


#*********************************************VISUALIZAR IMAGEM*********************************************************

cv2.imshow('image', img)
cv2.waitKey(0) #milisegundos


#*********************************************LER VÍDEO*********************************************************

video_path = os.path.join('.', 'videos', 'video1.mp4')
video = cv2.VideoCapture(video_path)


#*********************************************VISUALIZAR VÍDEO***************************************************

#ret = True

#while ret:
#   ret, frame = video.read()
#   cv2.imshow('frame', frame)
#   cv2.waitKey(10)
#video.release()
#cv2.destroyAllWindows()

#*********************************************LER WEBCAM***************************************************

webcam = cv2.VideoCapture(0)

#*********************************************VISUALIZAR WEBCAM***************************************************

while True:
    ret, frame = webcam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()

#*********************************************RESIZING***************************************************

img = cv2.imread(os.path.join('.', 'fotos', 'captura1.jpg'))

resized_img = cv2.resize(img, (960, 1280))
print(resized_img.shape)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)


#*********************************************CROP***************************************************
img = cv2.imread(os.path.join('.', 'fotos', 'captura1.jpg'))

cropped_img = img[20:640, 40:848]
print(cropped_img.shape)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
