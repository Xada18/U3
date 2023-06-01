
class Empleado:
    __dni = ""
    __nombre = ""
    __direccion = ""
    __telefono = ""

    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def __str__(self):
        return f"{self.__dni}, {self.__nombre}, {self.__direccion}, {self.__telefono}"
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono