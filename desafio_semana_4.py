# Desarrollado por el equipo 7 'project_code'.
# Integrantes: Daniel Saucedo, Paula Ledesma, José Giménez.

import os
import datetime
from time import sleep

año_actual = datetime.date.today().year

reglas_de_validacion = {
'zona': ['A', 'B', 'C'], 
'estado': ['Disponible', 'Reservado', 'Vendido'],
'condiciones_min':
{
'año': 2000,
'metros': 60,
'habitaciones': 2
}
}

ESTADOS = {
    'disponible': 'Disponible',
    'reservado': 'Reservado',
    'vendido': 'Vendido'
    }

inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
    ]
inmuebles_eliminados = []

def pantalla_logo():
    os.system('cls')
    print("""

                          ^
             _______     ^^^
            |xxxxxxx|  _^^^^^_
            |xxxxxxx| | [][]  |     Sistema de Gestión Inmobiliario 
         ______xxxxx| |[][][] |                  v 1.0
        |++++++|xxxx| | [][][]|      
        |++++++|xxxx| |[][][] |             
        |++++++|_________ [][]|
        |++++++|=|=|=|=|=| [] |       Realizado por: project_code
        |++++++|=|=|=|=|=|[][]|                (c) 2023
________|++HH++|  _HHHH__|   _________   _________  _________-
         _______________   ______________      ______________
__________________  ___________    __________________    ____________

    """)
    sleep(3)

def menu_principal():
    # Imprime en pantalla el menú principal de la aplicacion.
    os.system('cls')
    print('''
                        Sistema de Gestión Inmobiliario
                          -----  Menú principal  -----  

                    Opciones:

                    1 - Agregar, editar o eliminar inmueble
                    2 - Cambiar estado de inmueble
                    3 - Buscar inmueble por presupuesto

                    4 - Salir
    ''')

def pantalla_cambios_guardados():
    os.system('cls')
    print('''
                        Sistema de Gestión Inmobiliario
                        -----  Agregar inmueble  -----

                
                              CAMBIOS GUARDADOS!
    ''')
    sleep(2)

def menu_agregar_editar_eliminar():
# se puede usar  una funcion para printar el menu de agregar con un while true y asi tambien con las demas funciones
    while True:
        os.system('cls')
        print('''
                        Sistema de Gestión Inmobiliario
                    -----  Agregar, editar o eliminar  -----  

                  Opciones:  
                  1 - Listar inmuebles
                  2 - Agregar inmueble
                  3 - Editar inmueble
                  4 - Eliminar inmueble  

                  5 - Volver
        ''')
        seleccion=input('Seleccion: ')

        while seleccion not in ['1','2','3','4','5']:
            menu_principal()
            seleccion=input('Opcion incorrecta! \nSeleccion: ')
        
        if seleccion == '1':
            listar_inmuebles()
        elif seleccion == '2':
            menu_agregar_inmueble()
        elif seleccion == '3':
            menu_editar_inmueble()
        elif seleccion == '4':
            menu_eliminar_inmueble()
        elif seleccion == '5':
            break

def menu_agregar_inmueble():
    while True:
        os.system('cls')
        print('''
                      Sistema de Gestión Inmobiliario
                      -----  Agregar inmueble  -----
        
        Condiciones generales: 

        Sólo se admiten zonas A, B o C.
        Inmuebles en estado Disponible, Reservado o Vendido.
        No se opera con inmuebles:
            - Anteriores al año 2000,
            - Menores de 60 metros cuadrados.
            - Menores de 2 habitaciones.
        ''')
        while True:
            # Años
            while True:
                año = input('Ingrese el año: ')
                if validar_digito(año):
                    año = int(año)
                    if validar_año(año):
                        break
                    else:
                        print ('No se aceptan años anteriores al 2000.')
                else:
                    print ('Valor ingresado no válido.')
            # Metros
            while True:
                metros = input('Ingrese los metros: ')
                if validar_digito(metros):
                    metros = int(metros)
                    if validar_metros(metros):
                        break
                    else:
                        print ('No se aceptan menos de 60 metros cuadrados.')
                else:
                    print ('Valor ingresado no válido.')
            # Habitaciones
            while True:
                habitaciones = input('Ingrese cantidad de habitaciones: ')
                if validar_digito(habitaciones):
                    habitaciones = int(habitaciones)
                    if validar_habitaciones(habitaciones):
                        break
                    else:
                        print ('No se aceptan menos de 2 habitaciones.')
                else:
                    print ('Valor ingresado no válido.')
            # Garaje
            while True:
                garaje = input('Posee garaje? (1 - SI / 2 - NO): ')
                if garaje in ['1', '2']:
                    if garaje == '1':
                        garaje = True
                        break
                    else:
                        garaje = False
                        break
                else:
                    print ('Valor ingresado no válido.')
            # Zona
            while True:
                zona = input('Ingrese la zona (A, B, C): ')
                zona = zona.upper()
                if validar_zona(zona):
                    break   
                else:
                    print ('Valor ingresado no válido.')
            # Estado
            while True:
                estado = input('Ingrese estado (1 - Disponible / 2 - Reservado / 3 - Vendido): ')
                if estado in ['1', '2', '3']:
                    if estado == '1':
                        estado = 'Disponible'
                    elif estado == '2':
                        estado = 'Reservado'
                    else:
                        estado = 'Vendido'
                    break
                else:
                    print ('Valor ingresado no válido.')
            # Conf
            os.system('cls')
            print(f'''
                      Sistema de Gestión Inmobiliario
                      -----  Agregar inmueble  -----
        
            Los datos ingresados son: 

            Año __________ {año}
            Metros ------- {metros}
            Habitaciones - {habitaciones}
            Garaje ------- {garaje}
            Zona --------- {zona}
            Estado ------- {estado}

            Guardar cambios? (1 - CONFIRMAR / 2 - CANCELAR)
            ''')
            seleccion = input('Seleccion: ')
            while seleccion not in ['1','2']:
                seleccion=input('Opcion incorrecta! \nSeleccion: ')
            
            if seleccion == '1':
                agregar_inmueble(año=año,metros=metros,habitaciones=habitaciones,garaje=garaje,zona=zona,estado=estado)
                pantalla_cambios_guardados()
                break
            else:
                break
        break

def menu_eliminar_inmueble():
    while True:
        os.system('cls')
        print('''
                      Sistema de Gestión Inmobiliario
                      -----  Eliminar inmueble  -----
                
            Seleccione un inmueble a eliminar ingresando su número.
            El mismo se puede visualizar en el apartado "Listar inmuebles".
        ''')
        seleccion = input('Selección (para cancelar presione ENTER sin ingresar opciones): ')
        if seleccion == '':
            break
        else:
            if validar_digito(seleccion):
                seleccion = int(seleccion)
                if seleccion <= len(inmuebles) and seleccion > 0:
                    os.system('cls')
                    print(f'''
                      Sistema de Gestión Inmobiliario
                      -----  Eliminar inmueble  -----
                    
                                ATENCION!
    Inmueble a eliminar:
    Número {seleccion} - {inmuebles[seleccion-1]}
                ''')
                    continuar = input('Desea continuar? (1 = CONFIRMAR / 2 - CANCELAR): ')
                    while continuar not in ['1', '2']:
                        continuar=input('Valor ingresado no válido. Selección: ')
                    if continuar == '1':
                        eliminar_inmueble(seleccion-1)
                        pantalla_cambios_guardados()
                        break
                    else:
                        break
                else:
                    print('El valor ingresado no pertenece a un inmueble.')
                    input('Presione ENTER para continuar...')
            else:
                print('Valor ingresado no válido.')
                input('Presione ENTER para continuar...')

def menu_editar_inmueble():
    while True:
        os.system('cls')
        print('''
                      Sistema de Gestión Inmobiliario
                       -----  Editar inmueble  -----
                
        Seleccione un inmueble a editar ingresando su número.
        El mismo se puede visualizar en el apartado "Listar inmuebles".
        ''')
        seleccion = input('Selección (para cancelar presione ENTER sin ingresar opciones): ')
        if seleccion == '':
            break
        else:
            if validar_digito(seleccion):
                seleccion = int(seleccion)
                if seleccion <= len(inmuebles) and seleccion > 0:
                    # Bucle del menu de edicion
                    while True:
                        os.system('cls')
                        print(f'''
                      Sistema de Gestión Inmobiliario
                       -----  Editar inmueble  -----
                    
        Inmueble seleccionado:    
        Numero {seleccion} - {inmuebles[seleccion-1]}
                            
                    Seleccione un campo a editar: 
                    
                    1 - Año
                    2 - Metros
                    3 - Habitaciones
                    4 - Garaje
                    5 - Zona

                    6 - Volver
                    ''')
                        seleccion_menu = input('Seleccion: ')
                        while seleccion_menu not in ['1', '2','3','4','5','6']:
                            seleccion_menu=input('Valor ingresado no válido. Selección: ')
                        if seleccion_menu == '1':
                            # Se pide al usuario el nuevo valor de Año.
                            while True:
                                año = input('Ingrese el año: ')
                                if validar_digito(año):
                                    año = int(año)
                                    if validar_año(año):
                                        inmuebles[seleccion-1]['año'] = año
                                        pantalla_cambios_guardados()
                                        break
                                    else:
                                        print ('No se aceptan años anteriores al 2000.')
                                else:
                                    print ('Valor ingresado no válido.')
                        elif seleccion_menu == '2':
                            # Se pide al usuario el nuevo valor de Metros.
                            while True:
                                metros = input('Ingrese los metros: ')
                                if validar_digito(metros):
                                    metros = int(metros)
                                    if validar_metros(metros):
                                        inmuebles[seleccion-1]['metros'] = metros
                                        pantalla_cambios_guardados()
                                        break
                                    else:
                                        print ('No se aceptan menos de 60 metros cuadrados.')
                                else:
                                    print ('Valor ingresado no válido.')
                        elif seleccion_menu == '3':
                            # Se pide al usuario el nuevo valor de Habitaciones.
                            while True:
                                habitaciones = input('Ingrese cantidad de habitaciones: ')
                                if validar_digito(habitaciones):
                                    habitaciones = int(habitaciones)
                                    if validar_habitaciones(habitaciones):
                                        inmuebles[seleccion-1]['habitaciones'] = habitaciones
                                        pantalla_cambios_guardados()
                                        break
                                    else:
                                        print ('No se aceptan menos de 2 habitaciones.')
                                else:
                                    print ('Valor ingresado no válido.')
                        elif seleccion_menu == '4':
                            # Se pide al usuario el nuevo valor de Garaje.
                            while True:
                                garaje = input('Posee garaje? (1 - SI / 2 - NO): ')
                                if garaje in ['1', '2']:
                                    if garaje == '1':
                                        inmuebles[seleccion-1]['garaje'] = True
                                        pantalla_cambios_guardados()
                                        break
                                    else:
                                        inmuebles[seleccion-1]['garaje'] = False
                                        pantalla_cambios_guardados()
                                        break
                                else:
                                    print ('Valor ingresado no válido.')
                        elif seleccion_menu == '5':
                            # Se pide al usuario el nuevo valor de Zona.
                            while True:
                                zona = input('Ingrese la zona (A, B, C): ')
                                zona = zona.upper()
                                if validar_zona(zona):
                                    inmuebles[seleccion-1]['zona'] = zona
                                    pantalla_cambios_guardados()
                                    break   
                                else:
                                    print ('Valor ingresado no válido.')
                        else:
                            # Se cierra el bucle de edicion y vuelve al menu anterior.
                            break
                else:
                    print('El valor ingresado no pertenece a un inmueble.')
            else:
                print('Valor ingresado no válido.')

def menu_cambiar_estado_inmueble():
    while True:
        os.system('cls')
        print('''
                      Sistema de Gestión Inmobiliario
                   -----  Cambiar estado inmueble  -----
                
            Seleccione un inmueble a editar ingresando su número.
            El mismo se puede visualizar en el apartado "Listar inmuebles".
        ''')
        seleccion = input('Selección (para cancelar presione ENTER sin ingresar opciones): ')
        if seleccion == '':
            break
        else:
            if validar_digito(seleccion):
                seleccion = int(seleccion)
                if seleccion <= len(inmuebles) and seleccion > 0:
                    # Bucle del menu de cambio de estado.
                    while True:
                        os.system('cls')
                        print(f'''
                      Sistema de Gestión Inmobiliario
                   -----  Cambiar estado inmueble  -----
                    
        Inmueble seleccionado:    
        Numero {seleccion} - {inmuebles[seleccion-1]}
                            
                 Seleccione nuevo estado: 
                 
                 1 - Disponible
                 2 - Reservado
                 3 - Vendido 

                 4 - Volver
                    ''')
                        seleccion_menu = input('Seleccion: ')
                        while seleccion_menu not in ['1', '2','3','4',]:
                            seleccion_menu=input('Valor ingresado no válido. Selección: ')
                        if seleccion_menu == '1':
                            # Se cambia estado a Disponible.
                            cambiar_estado_inmueble('Disponible',seleccion-1,inmuebles)
                            pantalla_cambios_guardados()
                            break
                        elif seleccion_menu == '2':
                            # Se cambia estado a Reservado.
                            cambiar_estado_inmueble('Reservado',seleccion-1,inmuebles)
                            pantalla_cambios_guardados()
                        elif seleccion_menu == '3':
                            # Se cambia estado a Reservado.
                            cambiar_estado_inmueble('Vendido',seleccion-1,inmuebles)
                            pantalla_cambios_guardados()
                        else:
                            # Se cierra el bucle de edicion y vuelve al menu anterior.
                            break
                else:
                    print('El valor ingresado no pertenece a un inmueble.')
            else:
                print('Valor ingresado no válido.')

def menu_buscador():
    os.system('cls')
    print('''
                      Sistema de Gestión Inmobiliario
                    -----  Buscar por presupuesto  -----
    
      Ingrese un monto y el sistema le devolverá una lista de
      inmuebles de igual o menor costo. 
    ''')
    while True:
        ingreso = input('Valor en pesos (para cancelar presione ENTER sin ingresar opciones): $ ')
        if ingreso == '':
            break
        else:
            if validar_digito(ingreso):
                ingreso = float(ingreso)
                if ingreso > 0:
                    os.system('cls')
                    if busqueda_por_precio(ingreso, inmuebles):
                        print(f'''
                      Sistema de Gestión Inmobiliario
                   -----  Buscar por presupuesto  -----
    
                           Lista de resultados:
                       Valor ingresado: ${ingreso}
    ''')
                        
                        for inmueble in busqueda_por_precio(ingreso, inmuebles):
                            print(f'{inmuebles.index(inmueble)+1} - {inmueble}')
                        input('\nPresione ENTER para continuar...')
                        break
                    else:
                        print('''
                      Sistema de Gestión Inmobiliario
                    -----  Buscar por presupuesto  -----
    
                       No se encontraron resultados.
    ''')
                        input('Presione ENTER para continuar...')
                        break
                else:
                    print('El valor ingresado no es válido')
            else:
                print('El valor ingresado no es válido')

def listar_inmuebles():
    os.system('cls')
    print('''
                      Sistema de Gestión Inmobiliario
                    -----  Listado de inmuebles  -----  
    ''')
    for inmueble in inmuebles:
        print(f'{inmuebles.index(inmueble)+1} - {inmueble}\n')
    input('Presione ENTER para continuar...')

def agregar_inmueble(**kwargs):
    inmuebles.append(dict(kwargs))

def eliminar_inmueble(inmueble):
    inmuebles_eliminados = inmuebles.pop(inmueble)

def busqueda_por_precio(precio, inmuebles):
    resultado = []
    for inmueble in inmuebles:
        if calcular_precio(inmueble) <= precio:
            inmueble['precio']=calcular_precio(inmueble)
            resultado.append(dict(inmueble))
    return resultado

def calcular_precio(inmueble):
    # Recibe un diccionario con las propiedades de un inmueble y devuelve el precio del mismo.
    precio = (inmueble['metros']*100+inmueble['habitaciones']* 500 + inmueble['garaje']*1500)*(1-(año_actual-inmueble['año'])/100)
    if inmueble['zona'] == 'A':
        return precio
    elif inmueble['zona'] == 'B':
        return precio * 1.5
    elif inmueble['zona'] == 'C':
        return precio * 2

def cambiar_estado_inmueble (estado, seleccion, inmuebles):
    inmuebles[seleccion]['estado'] = estado

def validar_zona(zona):
    if zona in reglas_de_validacion['zona']:
        return True
    else: 
        return False

def validar_estado(estado):
    if estado in reglas_de_validacion['estado']:
        return True
    else:
        return False

def validar_digito(valor):
    if valor.isdigit():
        return True
    else: 
        return False

def validar_año(año):
    if año >= 2000:
        return True
    else:
        return False

def validar_metros(metros):
    if metros >= 60:
        return True
    else:
        return False

def validar_habitaciones(habitaciones):
   if habitaciones >= 2:
      return True
   else:
      return False

pantalla_logo()
while True:
    menu_principal()
    seleccion=input('Seleccion: ')

    while seleccion not in ['1','2','3','4']:
        menu_principal()
        seleccion=input('Opcion incorrecta! \nSeleccion: ')

    if seleccion == '1':
        menu_agregar_editar_eliminar()
    elif seleccion == '2':
        menu_cambiar_estado_inmueble()
    elif seleccion == '3':
        menu_buscador()
    elif seleccion == '4':
        pantalla_logo()
        os.system('cls')
        break
        
