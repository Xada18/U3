from ClaseVehiculo import Vehiculo

class VehiculoViejo (Vehiculo):
    __marca = ""
    __patente = ""
    __año = ""
    __kilometraje = 0
    __año_actual = "2023"

    def __init__(self, modelo, puertas, color, precio_base, marca, patente, año, kilometraje):
        self.__marca = marca
        self.__patente = patente
        self.__año = año
        self.__kilometraje = kilometraje
        self.calcularPrecio(precio_base)
        super().__init__(modelo, puertas, color, precio_base)

    def calcularPrecio(self, pb):
        precio = pb - pb * 0.01 * (int(self.__año_actual) - int(self.__año))
        if self.__kilometraje > 100000:
            precio -= pb * 0.02
        
        self.actualizarPrecio(pb, precio)

    def actualizarAñoActual(self):
        añoActual = input("Ingrese año actual: ")
        self.__año_actual = añoActual

    def __str__(self):
        return self.__marca + " " + self.getModelo() + ", " + self.__patente + ", " + str(self.getPrecioBase()) + ", " + str(self.getPrecio())
    
    def getPatente(self):
        return self.__patente
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__, 
            __atributos__ = dict(
                modelo = self.getModelo(), 
                puertas = self.getPuertas(), 
                color = self.getColor(), 
                precio_base = self.getPrecioBase(),
                marca = self.__marca,
                patente = self.__patente,
                año = self.__año,
                kilometraje = self.__kilometraje
            )
        )
        
        return d