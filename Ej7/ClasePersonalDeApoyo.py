from ClasePersona import Persona

class PersonalDeApoyo(Persona):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.__categoria = categoria

    def toJSON(self):
        d = super().toJSON()
        d['__atributos__']['categoria'] = self.__categoria

        return d
    