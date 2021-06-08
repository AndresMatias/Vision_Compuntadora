import cv2
import numpy as np
from math import sin,cos,radians

def transformacionEuclidiana(angulo,tx,ty):
	#tx: Traslacion en x
	#ty: Traslacion en y
	matriz=np.array([[cos(radians(angulo)),sin(radians(angulo)),tx],[-sin(radians(angulo)),cos(radians(angulo)),ty]]) #Transformacion euclidiana
	return matriz


imgIn=cv2.imread('hojas.jpg',1)

(h,w)=(imgIn.shape[0],imgIn.shape[1]) #Tamaño de imagen de salida
M=transformacionEuclidiana(90,0,w)
imgOut=cv2.warpAffine(imgIn,M,(h,w)) #Imagen de salida

cv2.imwrite('ResultadoA.jpg',imgOut)
