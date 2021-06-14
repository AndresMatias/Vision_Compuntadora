import cv2
import numpy as np
guardar=False #Bandera para indicar si se puede o no guardar
ix,iy=-1,-1
subimg=0
def draw(event,x,y,flags,param):
	global ix,iy,subimg,guardar
	if event==cv2.EVENT_LBUTTONDOWN: #Clic izq 
		ix,iy=x,y #Coordenadas iniciales del mouse
	elif event==cv2.EVENT_LBUTTONUP: #Suelto Boton
		fx,fy=x,y
		cv2.rectangle(img,(ix,iy),(fx,fy),(0,255,0),2)
		print("ix:{0},iy:{1},fx:{2},fy:{3}".format(ix,iy,fx,fy))
		#Correcion de coordenadas para manejar bien las posciones de la submatriz  	
		if (ix < fx) and (iy < fy) :	 	
			 subimg=img[iy:fy,ix:fx] #Fallo en la seleccion de la matriz
			 guardar=not guardar
		if (ix < fx) and (iy > fy) :
			subimg=img[fy:iy,ix:fx]
			guardar=not guardar
		if (ix > fx) and (iy < fy) :
			subimg=img[iy:fy,fx:ix]
			guardar=not guardar
		if (ix > fx) and (iy > fy) :
			subimg=img[fy:iy,fx:ix]
			guardar=not guardar
		if (ix == fx) and (iy == fy) :
			print("No hay imagen que guardar")	

print("Nota: El rectangulo aparece una vez que se arrastro y solto el clic del mouse")	 
img=cv2.imread('hojas.jpg',1)
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen',draw)
while(1):
	cv2.imshow('imagen',img)
	k=cv2.waitKey (1)&0xFF
	if k==ord('g') and guardar==True: #Guardar
		cv2.imwrite('Resultado.jpg',subimg)
		print("Imagen Guardada")
		guardar=False	
	elif k==ord('r'): #Restaurar
		img=cv2.imread('hojas.jpg',1)
		print("Imagen Restaurada")
	elif k==27: #Salir
		break
cv2.destroyAllWindows ( )