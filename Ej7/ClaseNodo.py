class Nodo:
    __persona = None
    __siguiente = None

    def __init__(self, persona):
        self.__persona = persona
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getPersona(self):
        return self.__persona