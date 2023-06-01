
class Helado:
    """
    __gramos: str
    __precio: str
    __sabores: list
    """
    __gramos = ""
    __precio = ""
    __sabores = []
    def __init__(self, gramos, precio):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabores = []

    def __str__(self):
        #return f"{self.__gramos} gr, {self.__precio} $"
        return self.__gramos + " " + self.__precio
    
    def mostrarSabores(self):
        for sabor in self.__sabores:
            print(sabor)

    def getGramos(self):
        return self.__gramos
    
    def getPrecio(self):
        return self.__precio
    
    def getSabores(self):
        return self.__sabores
    
    def sabores(self, sabor):
        self.__sabores.append(sabor)

    def getSabor(self, idSabor):
        sabor = None
        i = 0
        while i < len(self.__sabores) and sabor == None:
            if self.__sabores[i].getIdSabor() == idSabor:
                sabor = self.__sabores[i]
                sabor.contar()
            else:
                i+=1
        
        return sabor