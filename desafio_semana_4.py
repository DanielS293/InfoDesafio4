import os

def menu_principal():
    os.system('cls')
    print('''
                    Sistema de Gestion Inmobiliario
                      -----  Menú principal  -----  

                Opciones:
                1 - Agregar, editar o eliminar inmueble
                2 - Cambiar estado de inmueble
                3 - Buscar inmueble

                4 - Salir
    ''')



ESTADOS = {
    'disponible': 'Disponible',
    'reservado': 'Reservado',
    'vendido': 'Vendido'
    }


inmuebles= [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
    ]


while True:
    menu_principal()
    seleccion=input('Seleccion: ')

    while seleccion not in ['1','2','3','4']:
        menu_principal()
        seleccion=input('Opcion incorrecta! \nSeleccion: ')

    if seleccion == '1':
        # Enlazar funcion de agregar, eliminar o editar
        agregar_eliminar_editar()
    elif seleccion == '2':
        # Enlazar funcion de cambiar estado
        cambiar_estado()
    elif seleccion == '3':
        # Enlazar funcion de buscador
        buscador()
    elif seleccion == '4':
        os.system('cls')
        break
