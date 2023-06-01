from ClaseNodo import Nodo
from ClaseVehiculoViejo import VehiculoViejo
from ClaseVehiculoNuevo import VehiculoNuevo
#from zope.interface import implementer

class ListaVehiculos:
    __comienzo = None

    def __init__(self):
        self.__comienzo = None

    def agregarVehiculo(self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def mostrarVehiculos(self):
        nodo = self.__comienzo
        i = 1
        while nodo:
            print(str(i) + " - " + str(nodo.getVehiculo()))
            i+=1
            nodo = nodo.getSiguiente()

    def toJSON(self):
        lista_vehiculos = []
        nodo = self.__comienzo
        while nodo != None:
            lista_vehiculos.append(nodo.getVehiculo())
            nodo = nodo.getSiguiente()

        d = dict(
            __class__=self.__class__.__name__,
            vehiculos = [vehiculo.toJSON() for vehiculo in lista_vehiculos]
        )

        return d

    def crearVehiculo(self, tipo):
        if tipo == "N" or tipo == "n":
            marca = input("Ingrese marca: ")
            modelo = input("Ingrese modelo: ")
            puertas = input("Ingrese cantidad de puertas: ")
            color = input("Ingrese color: ")
            precioBase = input("Ingrese precio base: ")
            version = input("Ingrese version: ")
            vehiculo = VehiculoNuevo(modelo, int(puertas), color, float(precioBase), version)
            
        elif tipo == "V" or tipo == "v":
            marca = input("Ingrese marca: ")
            modelo = input("Ingrese modelo: ")
            puertas = input("Ingrese cantidad de puertas: ")
            color = input("Ingrese color: ")
            precioBase = input("Ingrese precio base: ")
            patente = input("Ingrese patente: ")
            año = input("Ingrese año: ")
            kilometraje = input("Ingrese kilometraje: ")
            vehiculo = VehiculoViejo(modelo, int(puertas), color, float(precioBase), marca, patente, año, float(kilometraje))
            
        else: 
            print("Tipo no valido")
            vehiculo = None

        return vehiculo
   
    def insertarVehiculoporPosicion(self, vehiculo, posicion):
        ban = False
        aux = self.__comienzo
        anterior = None
        if posicion == 1:
            self.agregarVehiculo(vehiculo)
        else:
            while aux and posicion != 1:
                anterior = aux
                aux = aux.getSiguiente()
                posicion = posicion - 1
                if posicion == 1:
                    nodo = Nodo(vehiculo)
                    nodo.setSiguiente(aux)
                    anterior.setSiguiente(nodo)
                    ban = True
        
        if not ban:
            print("Posicion no valida")

    def agregarVehiculoalFinal(self, vehiculo):
        aux = self.__comienzo
        anterior = None

        if self.__comienzo == None:
            self.agregarVehiculo(vehiculo)
        else:
            while aux != None:
                anterior = aux
                aux = aux.getSiguiente()
            nodo = Nodo(vehiculo)
            nodo.setSiguiente(aux)
            anterior.setSiguiente(nodo)

    def mostrarObjetoporPosicion(self, posicion):
        aux = self.__comienzo
        ban = False
        while posicion != 0 and aux:
            posicion -= 1
            if posicion == 0:
                if type(aux.getVehiculo()) == VehiculoViejo:
                    print("Hay un vehiculo viejo en esta posicion")
                elif type(aux.getVehiculo()) == VehiculoNuevo:
                    print("Hay un vehiculo nuevo en esta posicion")
                ban = True
            aux = aux.getSiguiente()
        
        if ban == False:
            print("Posicion no valida")

    def getVehiculoporPatente(self, patente):
        vehiculo = None
        aux = self.__comienzo
        while vehiculo == None and aux:
            v = aux.getVehiculo()
            if type(v) == VehiculoViejo and patente == v.getPatente():
                vehiculo = v
            aux = aux.getSiguiente()

        return vehiculo
    
    def getMenorPrecio(self):
        aux = self.__comienzo
        if aux == None:
            print("Lista vacia")
        else:
            vehiculo = aux.getVehiculo()
            menor = vehiculo.getPrecio()
            aux = aux.getSiguiente()
            while aux:
                vehiculo = aux.getVehiculo()
                if vehiculo.getPrecio() < menor:
                    menor = vehiculo.getPrecio()
                aux = aux.getSiguiente()

        return menor
    
    def getVehiculoMasEconomico(self):
        menor = self.getMenorPrecio()
        aux = self.__comienzo
        while aux:
            if aux.getVehiculo().getPrecio() == menor:
                print(aux.getVehiculo())
            aux = aux.getSiguiente()
        