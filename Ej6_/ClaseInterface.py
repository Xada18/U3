from zope.interface import Interface

class ILista (Interface):
    def insertarElemento(vehiculo, pos):    #La interface esta bien, no se encarga de la escepciones?
        pass

    def agregarElemento(vehiculo):
        pass

    def mostraElemento(pos):
        pass

    