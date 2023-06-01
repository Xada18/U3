from ClaseManejaHelados import ManejaHelados
from ClaseManejaSabores import ManejaSabores

if __name__ == '__main__':

    archivo = "sabores.csv"
    listaSabores = ManejaSabores()
    listaSabores.cargaSabores(archivo)
    listaHelados = ManejaHelados()

    ban = True
    while ban:
        print("Menu")
        print("1 - Registrar helado")
        print("2 - Helados mas vendidos")
        print("3 - Cantidad de gramos vendidos de un sabor")
        print("4 - Sabores de los helados segun el peso")
        print("5 - Importe total")
        print("0 - Salir")

        op = input("Ingrese una opcion: ")

        if op == "0":
            ban = False
        elif op == "1":
            gramos = input("Ingrese peso: ")
            precio = input("Ingrese precio: ")

            listaHelados.registroHelado(gramos, precio, listaSabores)
        
        elif op == "2":
            listaSabores.ordenar()
            listaSabores.mostrarMasVendidos()
            
        elif op == "3":
            sabor = input("Ingrese sabor: ")
            grvendidos = listaHelados.gramosVendidos(sabor)
            #print(f"Gramos vendidos: {grvendidos}")
            print(grvendidos)
            
        elif op == "4":
            gramos = input("Ingrese peso: ")
            listaHelados.pesoHelados(gramos)
        
        elif op == "5":
            #print(f"Importe total: {listaHelados.importeTotal()}")
            print(listaHelados.importeTotal())

        else:
            print("Opcion no valida")

        #listaHelados.mostrarHelados()
        print("")
