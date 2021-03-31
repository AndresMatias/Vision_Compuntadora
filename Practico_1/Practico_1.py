import random
def adivinar(intentos): #Funcion adivinar
	intentos_max=3
	if intentos<=intentos_max:
		nro1=int(input('Ingrese un numero entero para adivinar: '))
		nro2=random.randint(0, 100); #Numero a adivinar
		print(str(nro1))
		if nro1==nro2 :
			print("Adivinaste en el intento "+str(intentos))
			return(10)
		else:
			print("Fallaste, tenes "+str(intentos_max-intentos) +" intentos")
			return(0)
	else:
		print("Usaste todos los intentos")	
		return(10)
#-----------Fin de Funcion-----------------

for i in range(1,4):
	if adivinar(i) == 10:
		break
else:
	print("Fin del Programa")