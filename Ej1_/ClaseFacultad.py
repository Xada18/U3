from ClaseCarrera import Carrera


class Facultad:
    __codigo = ""
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = ""
    __carreras = None

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []
    
    def crearCarrera(self, codigo, nombre, fecha, duracion, titulo):
        carrera = Carrera(codigo, nombre, fecha, duracion, titulo)
        self.__carreras.append(carrera)

    def getCodigo(self):
        return self.__codigo

    def getCarreras(self):
        return self.__carreras
    
    def getNombre(self):
        return self.__nombre
    
    def getLocalidad(self):
        return self.__localidad

    def __str__(self):
        return f"{self.__codigo}, {self.__nombre}, {self.__direccion}, {self.__localidad}, {self.__telefono}"
    
    def mostrarCarreras(self):
        print(f"Facultad: {self.__nombre}")
        print("Carreras y su duracion:")
        for carrera in self.__carreras:
            print(f"{carrera.getNombre()}, {carrera.getDuracion()}")