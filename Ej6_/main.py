from ClaseObjectEncoder import ObjectEncoder
from ClaseManejadorVehiculos import ManejadorVehiculos


if __name__ == '__main__':

    jsonF = ObjectEncoder()
    vehiculos = ManejadorVehiculos()


    ban = True
    while ban:
        print("Menu")
        print("0 - Cargar archivo vehiculos.json")
        print("1 - Insertar un vehiculo en una posicion determinada de la Lista")
        print("2 - Agregar un vehículo a la Lista")
        print("3 - Dada una posicion, mostrar por pantalla qué tipo de objeto se encuentra almacenado en la posición ingresada")
        print("4 - Dada una patente, modificar el precio base, y luego mostrar el precio de venta")
        print("5 - Mostrar todos los datos, incluido el importe de venta, del vehículo más económico")
        print("6 - Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta")
        print("7 - Almacenar los objetos de la Lista en el archivo vehiculos.json")
        print("X - Salir")
        print("")
        op = input("Ingrese una opcion: ")

        if op == "0":
            diccionario = jsonF.leerJSONArchivo('vehiculos.json')
            vehiculos = jsonF.decodificarDiccionario(diccionario)
            vehiculos.mostrarVehiculos()


        elif op == "1":
            tipo = input("Ingrese el tipo de vehiculo (N: Nuevo, V: Viejo): ")
            vehiculo = vehiculos.crearVehiculo(tipo)
            
            if vehiculo:
                pos = int(input("Ingrese la posicion: "))
                try:
                    vehiculos.insertarElemento(vehiculo, pos)
                except Exception as e:
                    print("Error, " + str(e))
                    
                            
        elif op == "2":
            tipo = input("Ingrese el tipo de vehiculo (N: Nuevo, V: Viejo): ")
            vehiculo = vehiculos.crearVehiculo(tipo)

            if vehiculo:
                vehiculos.agregarElemento(vehiculo)
            

        elif op == "3":
            pos = int(input("Ingrese la posicion: "))
            try:
                vehiculo = vehiculos.getVehiculoporPosicion(pos)
                vehiculos.mostrarTipoVehiculo(vehiculo)

            except Exception as e:
                print("Error, " + str(e))
            

        elif op== "4":
            patente = input("Ingrese una patente: ")
            vehiculo = vehiculos.getVehiculoporPatente(patente)
            
            if vehiculo == None:
                print("Vehiculo no encontrado")
            else:
                precio_base = float(input("Ingrese nuevo precio base: "))
                vehiculo.actualizarPrecioBase(precio_base)
                vehiculos.mostrarPrecio(vehiculo)


        elif op == "5":
            vehiculos.getVehiculoMasEconomico()


        elif op == "6":
            vehiculos.mostrarDatos()


        elif op == "7":
            diccionario = vehiculos.toJSON()
            jsonF.guardarJSONArchivo(diccionario, 'nuevo.json')             


        elif op == "X" or op == "x":
            ban = False


        else:
            print("Opcion no valida")


        print("")
