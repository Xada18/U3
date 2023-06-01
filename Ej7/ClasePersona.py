
class Persona:
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo_basico = sueldo_basico
        self.__antiguedad = antiguedad

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__, 
            __atributos__ = dict(
                cuil = self.__cuil,
                apellido = self.__apellido,
                nombre = self.__nombre,
                sueldo_basico = self.__sueldo_basico,
                antiguedad = self.__antiguedad
            )
        )

        return d