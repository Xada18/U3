from ClaseFacultad import Facultad
import csv

# -*- coding: utf-8 -*-

class ManejaFacultades:
    __facultades= None

    def __init__(self):
        self.__facultades = []

    def cargaFacultades(self, file):
        with open(file, 'r', encoding='utf-8') as archivo:
            archivo = open(file,"r")
            reader = csv.reader(archivo, delimiter=",",)

            fcodigo = "a"
            i = -1

            for line in reader:

                if fcodigo == line[0]:
                    
                    ccodigo = line[1]
                    cnombre = line[2]
                    titulo = line[3]
                    duracion = line[4]
                    fecha = line[5]

                    self.__facultades[i].crearCarrera(ccodigo, cnombre, titulo, duracion, fecha)
                    
                else:

                    fcodigo = line[0]
                    fnombre = line[1]
                    direccion = line[2]
                    localidad = line[3]
                    telefono = line[4]
                    
                    facultad = Facultad(fcodigo, fnombre, direccion, localidad, telefono)
                    self.__facultades.append(facultad)
                    i += 1
                
    
    def mostrarFacultades(self):
        for facultad in self.__facultades:
            print(facultad)
            carreras = facultad.getCarreras()
            for carrera in carreras:
                print(carrera)
            print("")

    def getFacultad(self, codigo):
        facultad = None
        i = 0
        while i < len(self.__facultades) and facultad == None:
            if self.__facultades[i].getCodigo() == codigo:
                facultad = self.__facultades[i]
            else:
                i+=1
        
        return facultad

    def getCarrera(self, nombre):
        i = 0
        j = 0

        while i < len(self.__facultades) and carrera == None:
            carreras = self.__facultades[i].getCarreras()
            while j < len(carreras) and carrera == None:
                if carreras[j].getNombre == nombre:
                    carrera = carreras[j]
                else:
                    j+=1
            i+=1
        
        return carrera

    def mostrarFacultadporCarrera(self, nombre):
        ban = False

        i = 0
        while not ban and i < len(self.__facultades):
            facultad = self.__facultades[i]
            carreras = facultad.getCarreras()
            j = 0
            while not ban and j < len(carreras):
                if carreras[j].getNombre() == nombre:
                    print(f"{facultad.getCodigo()}{carreras[j].getCodigo()}, {facultad.getNombre()}, {facultad.getLocalidad()}")
                    ban = True
                else:
                    j+=1
            i+=1
        