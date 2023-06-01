from ClaseHelado import Helado

class ManejaHelados:
    __helados=[]

    def __init__(self):
        self.__helados = []

    def getHelados(self):
        return self.__helados
    
    def registroSabor(self, idSabor, sabores, helado):
        while idSabor != "0":
            sabor = sabores.getSabor(idSabor)
            if sabor == None:
                print("Sabor no encontrado")
            else:
                helado.sabores(sabor)
            idSabor = input("Ingrese sabor: ")

    def registroHelado(self, gramos, precio, sabores):
        helado = Helado(gramos, precio)
        idSabor = input("Ingrese sabor: ")
        self.registroSabor(idSabor, sabores, helado)

        self.__helados.append(helado)

    def mostrarHelados(self):
        for helado in self.__helados:
            print(helado)
            helado.mostrarSabores()

    def gramosVendidos(self, sabor):
        pesototal = 0
        i = 0
        for helado in self.__helados:
            gramos = None
            while i < len(helado.getSabores()) and gramos == None:
                if helado.getSabores()[i].getIdSabor() == sabor:
                    gramos = helado.getGramos()
                    peso = float(gramos)/len(helado.getSabores())
                    pesototal += peso 
                else:
                    i += 1
        
        return pesototal
    
    def pesoHelados(self, gramos):
        for helado in self.__helados:
            if helado.getGramos() == gramos:
                helado.mostrarSabores()
                print("")

    def importeTotal(self):
        importe = 0
        for helado in self.__helados:
            importe += float(helado.getPrecio())

        return importe