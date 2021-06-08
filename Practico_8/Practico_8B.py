import cv2
import numpy as np
from math import sin,cos,radians

puntos=[] #Lista que contendra los tres puntos escogidos para mapear, cada posicion de la lista, sera una tupla de las coordenadas x e y

def transformacionEuclidiana(src,h,w):
	#(h,w)=scr.shape[:2] #Tamaño de imagen de entrada
	dst=np.float32([[0,0],[h,0],[0,w/2],[h,w/2]]) #Puntos de salida
	matriz=cv2.getPerspectiveTransform(src,dst)
	return matriz

def draw(event,x,y,flags,param):
	global ix,iy,imgIn,guardar
	if event==cv2.EVENT_LBUTTONDOWN: #Clic izq 
		ix,iy=x,y #Coordenadas iniciales del mouse
		if len(puntos)!=4:
			puntos.append([x,y])
			cv2.circle(imgIn, (x, y), 7, (255,0,0), 2)
		else:
			print("Ya no puede escoger mas puntos para mapear")		
		if len(puntos)==4:
			guardar=True
			
imgIn=cv2.imread('gato.jpeg',1) #Leo la imagen de entrada
(h,w)=imgIn.shape[:2] #Tamaño de imagen de entrada
guardar=False #Bandera para indicar si se puede o no guardar
ix,iy=-1,-1
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen',draw) #Metodo de mouse

while(1):
	cv2.imshow('imagen',imgIn)
	k=cv2.waitKey (1)&0xFF
	if k==ord('h') and guardar==True: #Aplico Transformacion euclidiana y guardo imagen
		punto=np.float32([[puntos[0][0],puntos[0][1]],
						[puntos[1][0],puntos[1][1]],
						[puntos[2][0],puntos[2][1]],
						[puntos[3][0],puntos[3][1]]])
		M=transformacionEuclidiana(punto,h,w) #Genero la matriz para trasformar
		imgOut=cv2.warpPerspective(imgIn,M,(h,w)) #Imagen de salida de la trasformacion
		cv2.imwrite('ResultadoB.jpg',imgOut)
		print("Imagen Guardada")
		for i in range(0,len(puntos)): puntos.pop() #Elimino todos los puntos
		guardar=False
	elif k==ord('r'): #Restaurar
		imgIn=cv2.imread('hojas.jpg',1)
		print("Imagen Restaurada")
	elif k==27: #Salir
		break				
cv2.destroyAllWindows()