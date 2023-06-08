from ClaseNodo import Nodo
from zope.interface import implementer
from ClaseInterface import ILista
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoViejo import VehiculoViejo

@implementer(ILista)

class ManejadorVehiculos:
    __comienzo: Nodo
    __actual: Nodo
    __tope: int
    __indice: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0

    def __iter__(self):
        return self
    def __next__(self):

        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            vehiculo = self.__actual.getVehiculo()
            self.__actual = self.__actual.getSiguiente()
            
            return vehiculo
    
    def toJSON(self):

        d = dict(
            __class__=self.__class__.__name__,
            vehiculos = [vehiculo.toJSON() for vehiculo in self]
        )

        return d

    def mostrarVehiculos(self):
        for vehiculo in self:
            print(vehiculo)

    def crearVehiculo(self, tipo):
        if tipo == "N" or tipo == "n":
            print("Marca: Ford")
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
    
    def agregarVehiculo(self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    
    def insertarElemento(self, vehiculo, pos): #1
        if pos < 1 or pos > self.__tope + 1:
            raise Exception('Posicion no valida')
        
        else:
            nodo = Nodo(vehiculo)
            if pos == 1:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo = nodo

            else:
                aux = self.__comienzo
                for _ in range(pos - 2):
                    aux = aux.getSiguiente()

                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
            
            self.__actual = self.__comienzo
            self.__tope += 1
    def agregarElemento(self, vehiculo): #2
        nodo = Nodo(vehiculo)

        if self.__comienzo == None:
            self.__comienzo = nodo
            
        else:
            aux = self.__comienzo
            while aux.getSiguiente():
                aux = aux.getSiguiente()

            nodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(nodo)
        
        self.__actual = self.__comienzo
        self.__tope += 1
    def mostrarElemento(self, pos):
        if pos > self.__tope or pos < 1:
            raise Exception('Posicion no valida')
        else:
            aux = self.__comienzo
            i = 1
            while i < pos:
                aux = aux.getSiguiente()
                i += 1
            print(aux.getVehiculo())

    def getVehiculoporPosicion(self, pos):
        if pos > self.__tope or pos < 1:
            raise Exception('Posicion no valida')
        else:
            aux = self.__comienzo
            i = 1
            while i < pos:
                aux = aux.getSiguiente()
                i += 1
            vehiculo = aux.getVehiculo()

            return vehiculo
    def mostrarTipoVehiculo(self, vehiculo): #3
        if type(vehiculo) == VehiculoNuevo:
            print("El vehiculo en esta posicion es un vehiculo nuevo")
        elif type(vehiculo) == VehiculoViejo:
            print("El vehiculo en esta posicion es un vehiculo viejo")


    def getVehiculoporPatente(self, patente):
        vehiculo = None
        aux = self.__comienzo
        while vehiculo == None and aux:
            v = aux.getVehiculo()
            if type(v) == VehiculoViejo and patente == v.getPatente():
                vehiculo = v
            aux = aux.getSiguiente()
        return vehiculo
    def mostrarPrecio(self, vehiculo): #4
        precio = vehiculo.calcularPrecio()
        print("Precio de venta: " + str(precio))

    def getMenorPrecio(self):
        if self.__comienzo == None:
            print("Lista vacia")
            menor = None
        else:
            aux = self.__comienzo
            vehiculo = aux.getVehiculo()
            menor = vehiculo.calcularPrecio()
            aux = aux.getSiguiente()
            while aux:
                vehiculo = aux.getVehiculo()
                precio = vehiculo.calcularPrecio()
                if precio < menor:
                    menor = precio
                aux = aux.getSiguiente()

        return menor
    def getVehiculoMasEconomico(self): #5
        menor = self.getMenorPrecio()
        aux = self.__comienzo
        while aux:
            precio = aux.getVehiculo().calcularPrecio()
            if precio == menor:
                print(str(aux.getVehiculo()) + ", " + str(precio))
            aux = aux.getSiguiente()

    def mostrarDatos(self): #6
        for vehiculo in self:
            print(f"Modelo: {vehiculo.getModelo()}, Cantidad de puertas: {vehiculo.getPuertas()}, Precio: {vehiculo.calcularPrecio()}")






