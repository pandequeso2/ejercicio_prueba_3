#Funciones Principales: 
import time, os, msvcrt,csv


pedidos=[]
precio_5k=12500
precio_15k=25500
comunas=('Santiago','Colina','Pirque')

def registrar_pedido():
    print('Registrar pedido: ')
    print('CLIENTE: ')
    rut=int(input('Ingrese su rut(sin puntos ni digito verificador): '))
    nombre=input('Ingrese su nombre: ')
    direccion=input('Ingrese su dirección: ')
    comuna = int(input("*Ingrese número comuna(1: Santiago, 2:Colina, 3:Pirque): "))
    cantidad_5k=0
    cantidad_15k=0
    while True:
        print('Cilindros: ')
        print('1. Cantidad de 5 kilos ')
        print('2. Cantidad de 15 kilos ')
        print('3. Terminar pedido ')
        opc=input('Ingrese una opción: ')
        if opc=='1':
            cantidad=int(input('Ingrese su cantidad: '))
            cantidad_5k+=cantidad
        elif opc=='2':
            cantidad=int(input('Ingrese la cantidad: '))
            cantidad_15k+=cantidad
        elif opc=='3':
            break
        else:
            print('ERROR, Ingrese una de las 3 opciones: ')
    total=cantidad_5k*precio_5k+cantidad_15k*precio_15k
    pedido=[rut,nombre,direccion,comuna,cantidad_5k,cantidad_15k,total]
    pedidos.append(pedido)
    time.sleep(1)
    print('Cliente agregado...')        
def listar_pedido():
    if not pedidos:
        print('La lista esta vacia, ve a la opcion 1 primero...')
    else:
        print('Listar pedidos: ')
        for p in pedidos:
            print(f'Rut: {p[0]}')
            print(f'Nombre: {p[1]}')
            print(f'Dirección: {p[2]}')
            print(f'Comuna: {p[3]}')
            print(f'Cantidad de cilindros de 5 kilos: {p[4]}')
            print(f'Cantidad de cilinsros de 15 kilos: {p[5]}')
            print(f'Total a pagar: ${p[6]}')
            print()
            msvcrt.getch()
def buscar_rut():
    if not pedidos:
        print('La lista esta vacia, ve a la opción 1 primero...')
    else:
        print('Buscar por rut: ')
        rut_buscar=int(input('Ingrese su rut a buscar: '))
        tiene_pedido=False
        for p in pedidos:
            if rut_buscar==p[0]:
                tiene_pedido=True
                print(f'Rut: {p[0]}')
                print(f'Nombre: {p[1]}')
                print(f'Dirección: {p[2]}')
                print(f'Comuna: {p[3]}')
                print(f'Cantidad de cilindros de 5 kilos: {p[4]}')
                print(f'Cantidad de cilinsros de 15 kilos: {p[5]}')
                print(f'Total a pagar: ${p[6]}')
                print()
                print('Presione una teclapara continuar...')
                msvcrt.getch()
            if not tiene_pedido:
                print('No existe rut....')
def imprimir_hoja():
    if not pedidos:
        print('La lista esta vacia, ve a la opción 1 primero...')
    else:
        print('Imprimir Hoja: ')
        comuna = int(input("*Ingrese número comuna(1: Santiago, 2:Colina, 3:Pirque): "))
        nombre_archivo=input('Ingrese el nombre de su archivo: ')+'.csv'
        try: 
            with open(nombre_archivo,'x',newline=' ') as archivo:
                escritor=csv.writer(archivo)
                for p in pedidos:
                    if p[3]==comunas[comuna-1]:
                        escritor.writerow(p)
            print('Archivo creado con exito...')            
        except:
            print('Error,el nombre de el archivo ya esta en uso...')
def salir():
    print('Adioos....')
    exit()