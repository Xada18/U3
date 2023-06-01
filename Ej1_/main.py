from ClaseManejaFacultades import ManejaFacultades


if __name__ == '__main__':
    archivo = "Facultades.csv"
    listaFacultades = ManejaFacultades()
    listaFacultades.cargaFacultades(archivo)
    listaFacultades.mostrarFacultades()

    ban = True
    while ban:
        print("Menu")
        print("1 - Listar carreras de una facultad")
        print("2 - Informacion de una carrera")
        print("0 - Salir")

        op = input("Ingrese una opcion: ")

        if op == "0":
            ban = False

        elif op == "1":
            codigo = input("Ingrese el codigo de una facultad: ")
            facultad = listaFacultades.getFacultad(codigo)
            if facultad == None:
                print("Codigono valido")
            else:
                facultad.mostrarCarreras()

        elif op == "2":
            nombre = input("Ingrese el nombre de la carrera: ")
            listaFacultades.mostrarFacultadporCarrera(nombre)

        else:
            print("Opcion no valida")

        print("")
