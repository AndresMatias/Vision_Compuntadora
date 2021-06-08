import cv2
import numpy as np
from math import sin,cos,radians

def transformacionEuclidiana(src,h,w):
	dst=np.float32([[0,0],[h,0],[0,w/2],[h,w/2]]) #Puntos de salida
	matriz=cv2.getPerspectiveTransform(src,dst)
	return matriz

imgIn=cv2.imread('gato.jpeg',1) #Leo la imagen de entrada
(h,w)=imgIn.shape[:2] #Tamaño de imagen de entrada
punto=np.float32([[84, 69],[513, 77],[113, 358],[542, 366]])
M=transformacionEuclidiana(punto,h,w) #Genero la matriz para trasformar
imgOut=cv2.warpPerspective(imgIn,M,(h,w)) #Imagen de salida de la trasformacion
cv2.imwrite('ResultadoA.jpg',imgOut)
print("Imagen Guardada")