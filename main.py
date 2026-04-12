import os

from functions import *
from os import system

menu()

datos = datos()

opcion = 0

while opcion != 6:
    opcion = int(input('Ingrese una opción: '))
    
    os.system('clear')
    menu()

    if opcion == 1:
        listado(datos)
        
    elif opcion == 2:
        total_empresas_emp_soc(datos)
        
    elif opcion == 3:
        empresa_sector_pais(datos)
        
    elif opcion == 4:
        empresa_hostname(datos)
        
    elif opcion == 5:
        filtrar_herramienta(datos)
        
    elif opcion == 6:
        print('Saliendo del programa...')
        
    else:
        print('Opción no válida. Por favor, ingrese una opción del 1 al 6.')
