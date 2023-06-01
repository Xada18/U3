from ClaseEmpleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea = ""
    __fechainicio = ""
    __fechafin= ""
    __monto_viático = 0
    __costo_de_obra = 0
    __monto_seguro_de_vida = 0

    def __init__(self, dni, nombre, direccion, telefono, tarea, inicio, fin, viatico, obra, seguro):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fechainicio = inicio
        self.__fechafin= fin
        self.__monto_viático = float(viatico)
        self.__costo_de_obra = float(obra)
        self.__monto_seguro_de_vida = float(seguro)

    def __str__(self) -> str:
        return super().__str__() + f", {self.__tarea}, {self.__fechainicio}, {self.__fechafin}, {self.__monto_viático}, {self.__costo_de_obra}, {self.__monto_seguro_de_vida}"
    
    def getTarea(self):
        return self.__tarea
    
    def getFechaFin(self):
        return self.__fechafin
    
    def getCostodeObra(self):
        return self.__costo_de_obra
    
    def getViatico(self):
        return self.__monto_viático
    
    def getSeguro(self):
        return self.__monto_seguro_de_vida