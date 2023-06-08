

class Vehiculo:
    __modelo = ""
    __puertas = 0 
    __color = ""
    __precio_base = 0

    def __init__(self, modelo, puertas, color, precio_base):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__precio_base = precio_base

    def __str__(self):
        return f"{self.__modelo}, Puertas: {self.__puertas}, Color: {self.__color}, Precio Base: {self.__precio_base}"

    def getModelo(self):
        return self.__modelo
    
    def getPuertas(self):
        return self.__puertas
    
    def getColor(self):
        return self.__color
    
    def getPrecioBase(self):
        return self.__precio_base
    
    def actualizarPrecioBase(self, precioBase):
        print("Precio base actual: " + str(self.__precio_base))
        self.__precio_base = precioBase
        print("Nuevo precio base: " + str(self.__precio_base))

    def calcularPrecio(self):
        precio = self.__precio_base
        return precio

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__, 
            __atributos__ = dict(
                modelo = self.__modelo, 
                puertas = self.__puertas, 
                color = self.__color, 
                precio_base = self.__precio_base
            )
        )
        
        return d