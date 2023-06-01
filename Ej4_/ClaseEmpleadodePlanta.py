from ClaseEmpleado import Empleado

class EmpleadodePlanta(Empleado):
    __sueldo_basico = 0
    __antiguedad = 0

    
    def __init__(self, dni, nombre, direccion, telefono, basico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldo_basico = float(basico)
        self.__antiguedad = int(antiguedad)

    def __str__(self):
        return super().__str__() + f", {self.__sueldo_basico}, {self.__antiguedad}"
    
    def getSueldoBasico(self):
        return self.__sueldo_basico
    
    def getAntiguedad(self):
        return self.__antiguedad

