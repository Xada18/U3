

class Sabor:
    """
    __idSabor: str
    __ingredientes: str
    __nombreSabor: str
    __contador: int"""
    
    __idSabor = ""
    __ingredientes = ""
    __nombreSabor = ""
    __contador=0
    def __init__(self, id, ingredientes, nombre):
        self.__idSabor = id
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombre
        self.__contador = 0

    def __str__(self):
        #return f"{self.__idSabor}, {self.__ingredientes}, {self.__nombreSabor}"
        return self.__idSabor + self.__ingredientes + self.__nombreSabor
        

    def getIdSabor(self):
        return self.__idSabor
    
    def getIngredientes(self):
        return self.__ingredientes
    
    def getNombreSabor(self):
        return self.__nombreSabor
    
    def getContador(self):
        return self.__contador
    
    def contar(self):
        self.__contador += 1

    def __lt__(self, otro):
        return self.__contador < otro.__contador
    
    
    