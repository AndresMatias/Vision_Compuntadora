import cv2
import numpy as np

img1 = cv2.imread('1.png')
img2 = cv2.imread('4.png')


img2 = cv2.resize(img2,(100,100))
 
#Primero obtenga el roi de la imagen original
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
 
#Imagen original convertida a valor gris
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 
#Binarizar el valor gris para obtener la máscara del área de ROI
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('img2_fg',mask)
cv2.waitKey(0) 

 
 #Máscara invertida del área de la máscara
mask_inv = cv2.bitwise_not(mask)
 
 
#Fondo de pantalla de máscara
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
cv2.imshow('fondopantalla',img1_bg)
cv2.waitKey(0)
 
#Máscara en primer plano
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
cv2.imshow('img2_fg',img2_fg)
cv2.waitKey(0)
 
 # Superposición de imagen de fondo frontal
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
 
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
