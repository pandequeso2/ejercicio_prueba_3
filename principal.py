from funciones import *
import os,time,msvcrt
while True:
    os.system('cls')
    print("GAXPLOSIVE")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Buscar pedido por RUT")
    print("4. Imprimir hoja de ruta")
    print("5. Salir del programa")
    opc = input("Ingrese opción: ")
    os.system('cls')
    if opc=='1':
        registrar_pedido()
    elif opc=='2':
        listar_pedido()
    elif opc=='3':
        buscar_rut()
    elif opc=='4':
        imprimir_hoja()
    elif opc=='5':
        salir()
    else:
        print('Error, debe ingresar una de las opciónes.')
    time.sleep(2)    