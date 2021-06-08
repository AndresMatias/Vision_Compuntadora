import cv2
import numpy as np
from math import sin,cos,radians

def transformacionEuclidiana(angulo,tx,ty,s):
	#tx: Traslacion en x
	#ty: Traslacion en y
	matriz=np.array([[s*cos(radians(angulo)),s*sin(radians(angulo)),tx],[s*(-sin(radians(angulo))),s*cos(radians(angulo)),ty]]) #Transformacion euclidiana
	return matriz


imgIn=cv2.imread('hojas.jpg',1)

(h,w)=(imgIn.shape[0],imgIn.shape[1]) #Tamaño de imagen de salida
M=transformacionEuclidiana(90,0,w,0.5)
imgOut=cv2.warpAffine(imgIn,M,(h,w)) #Imagen de salida

cv2.imwrite('ResultadoA.jpg',imgOut)
