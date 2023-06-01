from ClasePersona import Persona

class Investigador(Persona):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_inv, tipo_inv):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.__area_inv = area_inv
        self.__tipo_inv = tipo_inv

    def toJSON(self):
        d = super().toJSON()
        d['__atributos__']['area_inv'] = self.__area_inv
        d['__atributos__']['tipo_inv'] = self.__tipo_inv

        return d


