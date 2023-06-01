class Vehiculo:
    __modelo = "" 
    __puertas = 0 
    __color = ""
    __precio_base = 0
    __precio = 0

    def __init__(self, modelo, puertas, color, precio_base):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__precio_base = precio_base

    def getModelo(self):
        return self.__modelo
    
    def getPuertas(self):
        return self.__puertas
    
    def getColor(self):
        return self.__color
    
    def getPrecioBase(self):
        return self.__precio_base
    
    def getPrecio(self):
        return self.__precio
    
    def actualizarPrecio(self, precio_base, precio):
        self.__precio_base = precio_base
        self.__precio = precio