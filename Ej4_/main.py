from ClaseManejadorEmpleados import ManejadorEmpleados
from ClaseEmpleadoContratado import EmpleadoContratado

if __name__ == '__main__':
    
    ListaEmpleados = ManejadorEmpleados()
    
    archivo = "planta.csv"
    ListaEmpleados.cargaEmpleados(archivo)
    
    archivo = "contratados.csv"
    ListaEmpleados.cargaEmpleados(archivo)

    archivo = "externos.csv"
    ListaEmpleados.cargaEmpleados(archivo)

    ListaEmpleados.mostrarEmpleados()



    ban = True
    while ban:
        print("Menu")
        print("1 - Registrar horas")
        print("2 - Total de tarea")
        print("3 - Ayuda Económica")
        print("4 - Calcular sueldo")
        print("0 - Salir")

        op = input("Ingrese una opcion: ")

        if op == "0":
            ban = False

        elif op == "1":
            dni = input("Ingrese DNI: ")
            empleado = ListaEmpleados.getEmpleado(dni)
            if empleado == None:
                print("Empleado no encontrado")
            elif type(empleado) != EmpleadoContratado:
                print("El empleado no es un empleado contratado")
            else:
                horas = input("Ingrese cantidad de horas trabjadas hoy: ")
                empleado.registrarHoras(horas)

        elif op == "2":
            tarea = input("Ingrese tarea: ")
            fecha = input("Ingrese fecha actual: ")
            ListaEmpleados.getTareas(tarea, fecha)

        elif op == "3":
            ListaEmpleados.ayudaEconomica()

        elif op== "4":
            ListaEmpleados.sueldoEmpleados()
        
        else:
            print("Opcion no valida")

        print("")
