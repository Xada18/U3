from ClaseNodo import Nodo
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePersonalDeApoyo import PersonalDeApoyo
from ClaseDocenteInvestigador import DocenteInvestigador

class ManejadorPersonal:
    def __init__(self):
        self.__comienzo = None

    def agregarPersona(self, persona):
        nodo = Nodo(persona)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def mostrarPersonas(self):
        nodo = self.__comienzo
        i = 1
        while nodo:
            print(str(i) + " - " + str(nodo.getPersona()))
            i+=1
            nodo = nodo.getSiguiente()

    def toJSON(self):
        lista_personas = []
        nodo = self.__comienzo
        while nodo != None:
            lista_personas.append(nodo.getPersona())
            nodo = nodo.getSiguiente()

        d = dict(
            __class__=self.__class__.__name__,
            personas = [persona.toJSON() for persona in lista_personas]
        )

        return d
    


    def agregarElemento(self, persona):
        nodo = Nodo(persona)

        if self.__comienzo == None:
            self.__comienzo = nodo
        else:
            aux = self.__comienzo

            while aux.getSiguiente():
                aux = aux.getSiguiente()

            aux.setSiguiente(nodo)

    def insertarElemento(self, persona, pos):
        nodo = Nodo(persona)        
        if pos == 1:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
        else:
            aux = self.__comienzo
            actual = 1
            while aux.getSiguiente() and  actual < pos - 1 :
                aux = aux.getSiguiente()
                pos += 1

            if pos - 1 != actual:
                print("Posicion no valida")
            else:
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)

    def mostrarElemento(self, pos):
        aux = self.__comienzo
        
        while pos != 1 and aux:
            aux = aux.getSiguiente()
            pos -= 1
        if pos == 1:
            print("Posicion no valida")
        else:
            print(aux.getPersona())

    def registrarPersona(self):
        ban = True

        while ban:
            ban = False
            print("D - Docente")
            print("I - Investigador")
            print("PA - Personal de Apoyo")
            print("DI - Docente Investigador")

            p = input("Ingrese tipo de agente: ")
            if p not in ["D", "I", " PA", "DI"]:
                print("Tipo no valido")
                ban = True

            else:
                cuil =input()
                apellido = input()
                nombre = input() 
                sueldo_basico = input()
                antiguedad = input()

                if p == "D":
                    carrera = input()
                    cargo = input()
                    catedra = input()

                    persona = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)

                elif p == "I":
                    area = input()
                    tipo = input()

                    persona = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area, tipo)

                elif p == "PA":
                    categoria = input()

                    persona = PersonalDeApoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)

                elif p == "DI":
                    carrera = input()
                    cargo = input()
                    catedra = input()
                    area = input()
                    tipo = input()
                    categoria = input()
                    extra = input()

                    persona = DocenteInvestigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area, tipo, categoria, extra)
        
        return persona