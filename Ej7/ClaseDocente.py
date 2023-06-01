from ClasePersona import Persona

class Docente(Persona):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    
    def toJSON(self): #Corregir
        d = super().toJSON()
        d['__atributos__']['carrera'] = self.__carrera
        d['__atributos__']['cargo'] = self.__cargo
        d['__atributos__']['catedra'] = self.__catedra

        return d

