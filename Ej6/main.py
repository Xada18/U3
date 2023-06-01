from ClaseObjectEncoder import ObjectEncoder
from ClaseListaVehiculos import ListaVehiculos


if __name__ == '__main__':

    jsonF = ObjectEncoder()
    vehiculos = ListaVehiculos()

    diccionario = jsonF.leerJSONArchivo('vehiculos.json')
    vehiculos = jsonF.decodificarDiccionario(diccionario)
    vehiculos.mostrarVehiculos()


    ban = True
    while ban:
        print("Menu")
        print("1 - Insertar un vehiculo en una posicion determinada de la Lista")
        print("2 - Agregar un vehículo a la Lista")
        print("3 - Dada una posicion, mostrar por pantalla qué tipo de objeto se encuentra almacenado en la posición ingresada")
        print("4 - Dada una patente, modificar el precio base, y luego mostrar el precio de venta")
        print("5 - Mostrar todos los datos, incluido el importe de venta, del vehículo más económico")
        print("6 - Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta")
        print("7 - Almacenar los objetos de la Lista en el archivo vehiculos.json")
        print("0 - Salir")

        op = input("Ingrese una opcion: ")

        if op == "0":
            ban = False

        elif op == "1":
            tipo = input("Ingrese el tipo de vehiculo (N: Nuevo, V: Viejo): ")
            vehiculo = vehiculos.crearVehiculo(tipo)

            if vehiculo == None:
                print("")
            else:
                pos = int(input("Ingrese la posicion: "))
                if pos > 0:
                    vehiculos.insertarVehiculoporPosicion(vehiculo, pos)
                    vehiculos.mostrarVehiculos()
                else:
                    print("Posicion no valida")
                            
        elif op == "2":
            tipo = input("Ingrese el tipo de vehiculo (N: Nuevo, V: Viejo): ")
            vehiculo = vehiculos.crearVehiculo(tipo)

            if vehiculo == None:
                print("")
            else:
                vehiculos.agregarVehiculoalFinal(vehiculo)
                vehiculos.mostrarVehiculos()
            
        elif op == "3":
            pos = int(input("Ingrese la posicion: "))
            if pos > 0:
                vehiculos.mostrarObjetoporPosicion(pos)
            else:
                print("Posicion no valida")

        elif op== "4":
            patente = input("Ingrese una patente: ")
            vehiculo = vehiculos.getVehiculoporPatente(patente)
            
            if vehiculo == None:
                print("Vehiculo no encontrado")
            else:
                precio_base = float(input("Ingrese nuevo precio base: "))
                vehiculo.calcularPrecio(precio_base)
                print(vehiculo)

        elif op == "5":
            vehiculos.getVehiculoMasEconomico()

        elif op == "6":
            vehiculos.mostrarVehiculos()

        elif op == "7":
            diccionario = vehiculos.toJSON()
            jsonF.guardarJSONArchivo(diccionario, 'nuevo.json')
        
        else:
            print("Opcion no valida")

        print("")
