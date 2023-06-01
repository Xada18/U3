

class Carrera:
    __codigo = ""
    __nombre = ""
    __titulo = ""
    __duracion = ""
    __fechainicio = ""

    def __init__(self, codigo, nombre, titulo, duracion, fecha):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__fechainicio = fecha

    def __str__(self):
        return f"{self.__codigo}, {self.__nombre}, {self.__titulo}, {self.__duracion}, {self.__fechainicio}"


    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getTitulo(self):
        return self.__titulo
    
    def getDuracion(self):
        return self.__duracion
    
    def getFechaInicio(self):
        return self.__fechainicio