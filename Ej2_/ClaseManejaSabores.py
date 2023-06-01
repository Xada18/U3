from ClaseSabor import Sabor
import csv

class ManejaSabores:
    #__sabores: list
    __sabores = []

    def __init__(self):
        self.__sabores = []

    def getSabores(self):
        return self.__sabores
    

    def cargaSabores(self, file):
        archivo = open(file, "r")
        reader = csv.reader(archivo, delimiter=";")

        for line in reader:
            sabor = Sabor(line[0], line[1], line[2])
            self.__sabores.append(sabor)

        archivo.close()


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
    
    def ordenar(self):
        self.__sabores.sort(reverse=True)

    def mostrarMasVendidos(self):
        i = 0
        for i in range(5):
            print(self.__sabores[i].getIdSabor())

