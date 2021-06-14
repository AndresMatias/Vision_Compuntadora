import cv2
import numpy as np
from math import sin,cos,radians

puntos=[] #Lista que contendra los tres puntos escogidos para mapear, cada posicion de la lista, sera una tupla de las coordenadas x e y

def transformacionAfin(img):
	(h,w)=img.shape[:2] #Tamaño de imagen de entrada
	src=np.float32([[0, 0], [img.shape[1] - 1, 0], [0, img.shape[0] - 1]]) 
	dst= np.float32([[puntos[0]], [puntos[1]], [puntos[2]]])#Puntos de salida
	matriz=cv2.getAffineTransform(src,dst)
	imgOut=cv2.warpAffine(img,matriz,(h,w)) #Imagen de salida de la trasformacion
	return imgOut

def draw(event,x,y,flags,param):
	global ix,iy,subimg,guardar
	if event==cv2.EVENT_LBUTTONDOWN: #Clic izq 
		ix,iy=x,y #Coordenadas iniciales del mouse
		if len(puntos)!=3:
			puntos.append([x,y])
			cv2.circle(imgAux, (x, y), 7, (255,0,0), 2)
		else:
			print("Ya no puede escoger mas puntos para mapear")		
		if len(puntos)==3:
			guardar=True

def incrustado(img1,img2):
	(h,w)=img1.shape[:2] 

	img2=cv2.resize(img2,(h,w))

	#Primero obtenga el roi de la imagen original
	rows,cols,channels = img2.shape
	roi = img1[0:rows, 0:cols ]
	 
	#Imagen original convertida a valor gris
	img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

	#Binarizar el valor gris para obtener la máscara del área de ROI
	ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
	
	#Máscara invertida del área de la máscara
	mask_inv = cv2.bitwise_not(mask)

	#img2_fg =transformacionAfin(img2_fg) #Genero la matriz para trasformar

	mask_inv =transformacionAfin(mask_inv) #Genero la matriz para trasformar
	mask =transformacionAfin(mask) #Genero la matriz para trasformar


	#Fondo de pantalla de máscara
	img1_bg = cv2.bitwise_and(roi,roi,mask = mask)

	 
	#Máscara en primer plano
	img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)

	 
	#Superposición de imagen de fondo frontal
	dst = cv2.add(img1_bg,img2_fg)
	img1[0:rows, 0:cols ] = dst
	 
	return img1	


print("Intrucciones:\nEscoja 3 puntos y presione e para guardar\nPresione r para reiniciar la imagen\nPresione Esc para salir")	

imgIn=cv2.imread('hojas.jpg',1) #Leo la imagen de entrada
imgAux= imgIn.copy() #Img Auxiliar
logo = cv2.imread('logo.png',1) 

 
(h,w)=imgIn.shape[:2] #Tamaño de imagen de entrada
guardar=False #Bandera para indicar si se puede o no guardar
ix,iy=-1,-1
subimg=0
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen',draw) #Metodo de mouse



while(1):
	cv2.imshow('imagen',imgAux)
	k = cv2.waitKey(1) & 0xFF
	if k==ord('e') and guardar==True: #Aplico Transformacion euclidiana y guardo imagen
		imgOut=incrustado(imgIn,logo)
		cv2.imwrite('ResultadoB.jpg',imgOut)
		#Creo una segunda ventana y muestro el resultado
		cv2.namedWindow('imagen2')
		cv2.imshow('imagen2',imgOut)
		print("Imagen Guardada")
		for i in range(0,len(puntos)): puntos.pop() #Elimino todos los puntos
		guardar=False
	elif k==ord('r'): #Restaurar
		imgIn=cv2.imread('hojas.jpg',1)
		imgAux= imgIn.copy() #Img Auxiliar
		for i in range(0,len(puntos)): puntos.pop() #Elimino todos los puntos
		print("Imagen Restaurada")
	elif k==27: #Salir
		break				
cv2.destroyAllWindows()