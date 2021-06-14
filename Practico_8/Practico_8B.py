import cv2
import numpy as np
from math import sin,cos,radians

puntos=[] #Lista que contendra los tres puntos escogidos para mapear, cada posicion de la lista, sera una tupla de las coordenadas x e y

def determinarRecta(punto1,punto2):
    #Calculo de pendiente m
    deltaY=punto1[1]-punto2[1]
    deltaX=punto1[0]-punto2[0]
    if deltaX==0 and deltaY==0: #Recta y perpendicular al eje x
        #mismo punto
        m="M"
        b=punto1 #en M indico que ambos puntos son iguales
        pass
    elif deltaX==0: #Recta y perpendicular al eje x
        m="X"
        b=punto1[0] #Utlizo b para indicar cual es punto donde hay una recta perpendicular y m indico que el eje X es el fijo

    elif deltaY==0: #Recta x perpendicular al eje y
        m="Y"
        b=punto1[1] #Utlizo a b para indicar cual es punto donde hay una recta perpendicular y con m indico que el eje Y es el fijo
    else:
        m=deltaY/deltaX
        b=punto1[1]-(punto1[0]*m)
    #Calculo de termino independitente b=y-x*m
    return m,b

def DeterminarPuntosNoColinelaes(puntos):
    #Varaibles Auxiliares
    Ba1=False
    cont1=0
    cont2=0
    cont3=0
    #Nro de puntos
    N=len(puntos)
    #Numero rectas por puntos
    Np=N-1 
    #Nro minimo de rectas
    Nmin=(Np*N)/2
    #Lista de rectas
    Rectas=[]
    #Calculo de rectas minimas, y=x*m+b
    for i in range(0,Np):   
        for j in range(i,Np):
        		#Estos dos for estan contruidos de forma que permite calcular las rectas entre los puntos sin repetir la misma recta dos veces para dos puntos
            #print("p1: {0}, p2: {1},  j:{2}, i: {3},  j+1: {4}".format(puntos[i],puntos[j+1],j,i,j+1))
            m,b=determinarRecta(puntos[i],puntos[j+1])
            #print("Y=X*{0}+{1}\n".format(m,b))
            Rectas.append([m,b])

    #For para determinar colinealidad(Recordar de ninguna recta entre dos puntos se repite)
    for i in range(0,len(Rectas)):
        for j in range(0,len(Rectas)):
            a=Rectas[i][0]
            b=Rectas[j][0]
            if a==b=="M" and j!=i and cont1<2:
                cont1=cont1+1
            elif a==b=="X" and j!=i and cont2<2:
                cont2=cont2+1
            elif a==b=="Y" and j!=i and cont3<2:
                cont3=cont3+1
            elif a==b and Rectas[i][1]==Rectas[j][1] and j!=i and Ba1==False and (a!="M" and a!="X" and a!="Y"): #Si dos rectas tienen misma pendiente y termino independinte significa que hay tres puntos colineales
                print("Rectas iguales")
                Ba1=True
            if cont1>1 or cont2>1 or cont3>1 or Ba1==True:
                return False
    return True

def transformacionEuclidiana(src,h,w):
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
			bandera=DeterminarPuntosNoColinelaes(puntos)
			if bandera==True:
				guardar=True
			else:
				print("Elementos Colineales elija otros puntos")
				for i in range(0,len(puntos)):puntos.pop()

			

print("Intrucciones:\nEscoja 4 puntos y presione h para guardar\nPresione r para reiniciar la imagen\nPresione Esc para salir")			
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
		imgIn=cv2.imread('gato.jpeg',1)
		for i in range(0,len(puntos)):puntos.pop() #Borro lista de puntos
		print("Imagen Restaurada")
	elif k==27: #Salir
		break				
cv2.destroyAllWindows()