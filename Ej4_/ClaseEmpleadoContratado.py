from ClaseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __fecha_inicio = ""
    __fecha_fin = ""
    __horas = 0
    __valor_hora = 0

    def __init__(self, dni, nombre, direccion, telefono, inicio, fin, horas, valor):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_inicio = inicio
        self.__fecha_fin = fin
        self.__horas = int(horas)
        self.__valor_hora = float(valor)

    def __str__(self):
        return super().__str__() + f", {self.__fecha_inicio}, {self.__fecha_fin}, {self.__horas}, {self.__valor_hora}"
    
    def getHoras(self):
        return self.__horas
    
    def getValorHora(self):
        return self.__valor_hora

    def registrarHoras(self, horas):
        self.__horas += int(horas)