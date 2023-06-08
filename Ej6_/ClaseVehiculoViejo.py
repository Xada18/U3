from ClaseVehiculo import Vehiculo
import datetime 

class VehiculoViejo (Vehiculo):
    __marca = ""
    __patente = ""
    __año = 0
    __kilometraje = 0

    def __init__(self, modelo, puertas, color, precio_base, marca, patente, año, kilometraje):
        super().__init__(modelo, puertas, color, precio_base)
        self.__marca = marca
        self.__patente = patente
        self.__año = año
        self.__kilometraje = kilometraje
    
    def __str__(self):
        return self.__marca + " " + super().__str__() + f", Patente: {self.__patente}, Año: {self.__año}, Kilometraje: {self.__kilometraje}"
    
    def getPatente(self):
        return self.__patente
        
    def toJSON(self):
        d = super().toJSON()
        d['__atributos__']['__marca__'] = self.__marca
        d['__atributos__']['__patente__'] = self.__patente
        d['__atributos__']['__año__'] = self.__año
        d['__atributos__']['__kilometraje__'] = self.__kilometraje
        
        return d

    def calcularPrecio(self):
        precio = super().calcularPrecio()
        
        año_actual = datetime.datetime.now().year
        precio += self.getPrecioBase() * 0.01 * (año_actual - int(self.__año))
        if self.__kilometraje > 100000:
            precio -= self.getPrecioBase() * 0.02

        return precio



    
    

    
    