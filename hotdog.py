import os 
from random import randint
import csv

pedidos=[]
comunas =["coronel","concepcion","lota"]

def registrar_pedidos():
    cant_aleman=0
    cant_pobre=0
    cant_atomico=0
    id=randint(1,10000)
    nombre_completo=input("ingresa tu nombre completo : ")
    try:
        nombre, apellido=nombre_completo.split()
    except ValueError:
        print("Formato incorrecto. Debe ingresar nombre y apellido separados por espacio.")
        return
    print(f"comunas disponibles para delivery: {comunas} ")
    comuna=input("ingrese su comuna\n")
    if comuna not in comunas:
        print("comuna no disponible")
        return
    direccion=input("ingrese su dirreccion:...\n")
    try:
        while True:
            print("Cual de los siguentes Hot Dog desea comprar")
            print("1.Aleman")
            print("2.A lo pobre")
            print("3.Atomico")
            op_completo=int(input("Ingrese su opcion a elegir.."))
            if op_completo==1:
                cant_aleman=int(input("cuantos Aleman desea comprar?.."))
            elif op_completo==2:
                cant_pobre=int(input("cuantos A o pobre desea comprar?.."))
            elif op_completo==3:
                cant_atomico=int(input("cuantos Atomico desea comprar?.."))
            else:
                print("opcion no validad....intente otra vez")
                continue
            volver=input(print("desea volver al menu de completos? (si/no)"))
            if volver.lower()=="si":
                continue
            else:
                print("saliendo del menu de completos...")
                break
    except ValueError:
        print("debe ingresar un numero")
        return
    input("Presiona Enter para regresar al menú...")

    
    pedido={
        "ID":id,
        "cliente":nombre_completo,
        "direccion":direccion,
        "sector":comuna,
        "aleman":cant_aleman,
        "alo_pobre":cant_pobre,
        "atomico":cant_atomico
    }
    pedidos.append(pedido)
    print(f"\n{id}: Este es su numero para mostrar el detalle de su pedido")


def listar_pedidos():
    if not pedidos:
        print("no hay pedidos disponibles")
        return registrar_pedidos()
    else:
        for pedido in pedidos:
            print(f"ID:{pedido['ID']}, Cliente:{pedido['cliente']}, Direccion:{pedido['direccion']}, Sector:{pedido['sector']}"
                  f"Aleman:{pedido['aleman']}, Alo pobre:{pedido['alo_pobre']}, Atomico:{pedido['atomico']}")
            print("se listaron todos los pedidos :) ")

    input("Presiona Enter para regresar al menú...")


def imprimir_hoja_ruta():
    print(f"Por cuál de estas comunas {comunas} desea imprimir:")
    comuna = input("Ingrese su comuna: ")
    
    if comuna not in comunas:
        print("Comuna no disponible. Intente otra vez.")
        return
    else:
        with open(f"hoja_ruta_{comuna}.csv", "w", newline="") as planilla:
            ruta = csv.writer(planilla)
            ruta.writerow(["ID", "Clientes", "Direccion", "Sector", "Aleman", "Alo pobre", "Atomico"])
            for pedido in pedidos:
                if pedido['sector'] == comuna:
                    ruta.writerow([pedido['ID'], pedido['cliente'], pedido['direccion'], pedido['sector'], pedido['aleman'], pedido['alo_pobre'], pedido['atomico']])
        print(f"El archivo se ha generado correctamente como 'hoja_ruta_{comuna}.csv'.")
    input("Presiona Enter para regresar al menú...")


def buscar_pedido():
    try:
        buscar_id = int(input("Ingrese el número de su pedido para buscarlo:\n"))
        encontrado = False
        
        for pedido in pedidos:
            if pedido['ID'] == buscar_id:
                print(f"ID: {pedido['ID']}, Cliente: {pedido['cliente']}, Dirección: {pedido['direccion']}, Sector: {pedido['sector']}, "
                      f"Alemán: {pedido['aleman']}, A lo pobre: {pedido['alo_pobre']}, Atómico: {pedido['atomico']}")
                encontrado = True
                break
        
        if not encontrado:
            print("Pedido no encontrado.")
    
    except ValueError:
        print("Debe ingresar un número válido para buscar el pedido.")
    input("Presiona Enter para regresar al menú...")





def menu():
    while True:
        os.system("clear")
        print("Bienvenidos a completos a domicilio")
        print("1.Registrar pedido\n2.Listar todos los pedidos\n3.Imprimir hoja de ruta\n4.Buscar un pedido por ID\n5.Salir del programa\n")

        opcion = input("Ingrese su opción: ").strip()
        os.system("clear")  
        if opcion == "1":
            registrar_pedidos()
        elif opcion == "2":
            listar_pedidos()
        elif opcion == "3":
            imprimir_hoja_ruta()
        elif opcion == "4":
            buscar_pedido()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Su opción no es válida.... Intente nuevamente")
            input("Presiona Enter para continuar...")  

if __name__=="__main__":
    menu()


            

