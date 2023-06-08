from ClaseVehiculo import Vehiculo

class VehiculoNuevo(Vehiculo):
    __marca = "Ford"
    __version = ""

    def __init__(self, modelo, puertas, color, precio_base, version):
        super().__init__(modelo, puertas, color, precio_base)
        self.__marca = "Ford"
        self.__version = version

    def __str__(self):
        return self.__marca + " " + super().__str__() + ", Version: " + self.__version

    def toJSON(self):
        d = super().toJSON()
        d['__atributos__']['__version__'] = self.__version 
        
        return d
    
    def calcularPrecio(self):
        precio = super().calcularPrecio()
        precio += self.getPrecioBase() * 0.1 
        if self.__version == "Full":
            precio += self.getPrecioBase() * 0.02

        return precio       
    



    
    