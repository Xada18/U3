
from ClaseEmpleadodePlanta import EmpleadodePlanta
from ClaseEmpleadoContratado import EmpleadoContratado
from ClaseEmpleadoExterno import EmpleadoExterno
import numpy as np
import csv

class ManejadorEmpleados:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __empleados = None

    def __init__(self, dimension=0, incremento=5):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__empleados = np.empty(dimension, dtype=object)
    
    def agregarEmpleado(self, empleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad] = empleado
        self.__cantidad += 1

    def cargaEmpleados(self, file):
        archivo = open(file, "r")
        reader = csv.reader(archivo, delimiter=",")
        
        for line in reader:
            if len(line) == 6:
                empleado = EmpleadodePlanta(line[0], line[1], line[2], line[3], line[4], line[5])
            elif len(line) == 8:
                empleado = EmpleadoContratado(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
            elif len(line) == 10:
                empleado = EmpleadoExterno(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])

            self.agregarEmpleado(empleado)
        
        archivo.close()

    def mostrarEmpleados(self):
        for i in range(self.__cantidad):
            print(self.__empleados[i])

    def getEmpleado(self, dni):
        empleado = None
        i = 0
        while empleado == None and i < self.__cantidad:
            if dni == self.__empleados[i].getDNI():
                empleado = self.__empleados[i]
            else:
                i+=1

        return empleado
    
    def getTareas(self, tarea, fecha):
        for empleado in self.__empleados:
            
            if type(empleado) == EmpleadoExterno and empleado.getTarea() == tarea:
                f1 = empleado.getFechaFin().split("/")
                f2 = fecha.split("/")
                fechafin = f1[2] + f1[1] + f1[0]
                fechaactual = f2[2] + f2[1] + f2[0]
                if fechaactual > fechafin:
                    print(f"Costo de la obra: {empleado.getCostodeObra()}")

    
    def calcularSueldo(self, empleado):
        if isinstance(empleado, EmpleadodePlanta):
            sueldo = empleado.getSueldoBasico() + empleado.getSueldoBasico() * 0.01 * empleado.getAntiguedad()
        elif isinstance(empleado, EmpleadoContratado):
            sueldo = empleado.getHoras() * empleado.getValorHora()
        elif isinstance(empleado,EmpleadoExterno):
            sueldo = empleado.getCostodeObra() - empleado.getViatico() - empleado.getSeguro()
        
        return sueldo
    
    def ayudaEconomica(self):
        for empleado in self.__empleados:
            sueldo = self.calcularSueldo(empleado)
            if sueldo < 150000:
                print(f"{empleado.getNombre()}, {empleado.getDireccion()}, {empleado.getDNI()}")
    
    def sueldoEmpleados(self):
        for empleado in self.__empleados:
            sueldo = self.calcularSueldo(empleado)
            print(f"{empleado.getNombre()}, {empleado.getTelefono()}, {sueldo}")