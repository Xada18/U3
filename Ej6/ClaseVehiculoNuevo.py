from ClaseVehiculo import Vehiculo

class VehiculoNuevo(Vehiculo):
    __marca = "Ford"
    __version = ""

    def __init__(self, modelo, puertas, color, precio_base, version):
        self.__version = version
        self.calcularPrecio(precio_base)
        super().__init__(modelo, puertas, color, precio_base)
    
    def calcularPrecio(self, pb):
        precio = pb + pb * 0.1 
        if self.__version == "Full":
            precio += pb * 0.02

        self.actualizarPrecio(pb, precio)
        
    
    def __str__(self):
        return self.__marca + " " + self.getModelo() + " " + self.__version + ", " + str(self.getPrecioBase()) + ", " + str(self.getPrecio())

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__, 
            __atributos__ = dict(
                modelo = self.getModelo(), 
                puertas = self.getPuertas(), 
                color = self.getColor(), 
                precio_base = self.getPrecioBase(),
                version = self.__version 
            )
        )
        
        return d
    
    