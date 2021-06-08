def Funcion_Amiga(self):
    print("Funcion Amiga")
class Coche():
    def __init__(self): #Constructor 
        print("Constructor")
    def arrancar(self): #Funcion no es lo mismo que metodo, metodo pertenece a la clase la funcion no pertenece a nada
        print("Arrancar")
        Funcion_Amiga(self)
    
class Galleta:
    chocolate = False
    def __init__(self):
        print(self)
    def saludar(self):
        print("Hola, soy una galleta muy sabrosa")
        print(self)

galleta = Galleta()
galleta.saludar()

miCoche=Coche() 
miCoche.arrancar()
