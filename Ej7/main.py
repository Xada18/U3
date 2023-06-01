from ClaseObjectEncoder import ObjectEncoder
from ClaseManejadorPersonal import ManejadorPersonal

if __name__ == '__main__':
    
    jsonF = ObjectEncoder()
    personal = ManejadorPersonal()





    ban = True
    while ban:
        print("Menu")
        print("1 - Insertar agentes a la colección.")
        print("2 - Agregar agentes a la colección.")
        print("3 - Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.")
        print("4 - Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
        print("5 - Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.")
        print("6 - Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
        print("7 - Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado,") 
        print("    listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría,") 
        print("    al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran")
        print("    los docentes investigadores de la categoría solicitada")
        print("8 - Almacenar los datos de todos los agentes en el archivo “personal.json”")
        print("0 - Salir")

        op = input("Ingrese una opcion: ")

        if op == "0":
            ban = False

        elif op == "1":
            persona = personal.registrarPersona()
            pos = int(input("Ingrese la posicion: "))
            personal.insertarElemento(persona, pos)

        elif op == "2":
            persona = personal.registrarPersona()
            personal.agregarElemento(persona)

        elif op == "3":
            pass

        elif op == "4":
            pass

        elif op == "5":
            pass

        elif op == "6":
            pass

        elif op == "7":
            pass

        elif op== "8":
            d = personal.toJSON()
            jsonF.guardarJSONArchivo(d, 'personal.json')
        
        else:
            print("Opcion no valida")

        print("")