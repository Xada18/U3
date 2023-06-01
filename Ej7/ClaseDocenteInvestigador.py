from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_inv, tipo_inv, categoria_inv, importe_extra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_inv, tipo_inv)
        self.__categoria_inv = categoria_inv
        self.__importe_extra = importe_extra

    def toJSON(self):
        d = super().toJSON()
        d['__atributos__']['categoria_inv'] = self.__categoria_inv
        d['__atributos__']['importe_extra'] = self.__importe_extra

        return d