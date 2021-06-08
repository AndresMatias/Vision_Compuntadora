import cv2
import numpy as np
from math import sin,cos,radians

puntos=[] #Lista que contendra los tres puntos escogidos para mapear, cada posicion de la lista, sera una tupla de las coordenadas x e y

def transformacionEuclidiana(src):
	#(h,w)=scr.shape[:2] #Tamaño de imagen de entrada
	dst=np.float32([[src[0][0]+100, src[0][1]+100],
		[src[1][0]+200, src[1][1]+200],
		[src[2][0]+100, src[2][1]+100]]) #Puntos de salida
	matriz=cv2.getAffineTransform(src,dst)
	return matriz

imgIn=cv2.imread('hojas.jpg',1) #Leo la imagen de entrada
(h,w)=imgIn.shape[:2] #Tamaño de imagen de entrada
punto=np.float32([[100,100],[150,100],[250,250]])
M=transformacionEuclidiana(punto) #Genero la matriz para trasformar
imgOut=cv2.warpAffine(imgIn,M,(h,w)) #Imagen de salida de la trasformacion
cv2.imwrite('ResultadoA.jpg',imgOut)
print("Imagen Guardada")