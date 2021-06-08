import cv2
import numpy as np
from math import sin,cos,radians

def transformacionEuclidiana(angulo,tx,ty,s):
	#tx: Traslacion en x
	#ty: Traslacion en y
	matriz=np.array([[s*cos(radians(angulo)),s*sin(radians(angulo)),tx],[s*(-sin(radians(angulo))),s*cos(radians(angulo)),ty]]) #Transformacion euclidiana
	return matriz

def draw(event,x,y,flags,param):
	global ix,iy,subimg,guardar
	if event==cv2.EVENT_LBUTTONDOWN: #Clic izq 
		ix,iy=x,y #Coordenadas iniciales del mouse
	elif event==cv2.EVENT_LBUTTONUP: #Suelto Boton
		fx,fy=x,y
		cv2.rectangle(imgIn,(ix,iy),(fx,fy),(0,255,0),2)
		print("ix:{0},iy:{1},fx:{2},fy:{3}".format(ix,iy,fx,fy))  	
		if (ix < fx) and (iy < fy) :	 	
			 subimg=imgIn[iy:fy,ix:fx] #Fallo en la seleccion de la matriz
			 guardar=not guardar
		if (ix < fx) and (iy > fy) :
			subimg=imgIn[fy:iy,ix:fx]
			guardar=not guardar
		if (ix > fx) and (iy < fy) :
			subimg=imgIn[iy:fy,fx:ix]
			guardar=not guardar
		if (ix > fx) and (iy > fy) :
			subimg=imgIn[fy:iy,fx:ix]
			guardar=not guardar
		if (ix == fx) and (iy == fy) :
			print("No hay imagen que guardar")

imgIn=cv2.imread('hojas.jpg',1) #Leo la imagen de entrada
guardar=False #Bandera para indicar si se puede o no guardar
ix,iy=-1,-1
subimg=0
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen',draw) #Metodo de mouse
while(1):
	cv2.imshow('imagen',imgIn)
	k=cv2.waitKey (1)&0xFF
	if k==ord('e') and guardar==True: #Aplico Transformacion euclidiana y guardo imagen
		(h,w)=(subimg.shape[0],subimg.shape[1]) #Tamaño de imagen de salida
		M=transformacionEuclidiana(90,0,w,0.5) #Genero la matriz para trasformar
		imgOut=cv2.warpAffine(subimg,M,(h,w)) #Imagen de salida de la trasformacion
		cv2.imwrite('ResultadoB.jpg',imgOut)
		print("Imagen Guardada")
		guardar=False
	elif k==ord('r'): #Restaurar
		imgIn=cv2.imread('hojas.jpg',1)
		print("Imagen Restaurada")
	elif k==27: #Salir
		break
cv2.destroyAllWindows ( )
