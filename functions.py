import json
def menu():
    print('''==== MENÚ ====
    1. Mostrar información sobre las empresas.
    2. Mostrar total de empresas y empleados SOC en cada una de ellas.
    3. Filtrar por sector y país.
    4. Mostrar información a través de hostname.
    5. Filtrar información por herramienta.
    6. Salir.''')
    print()
    
def datos():
    with open('empresas.json') as archivo:
        datos=json.load(archivo)
    
    return datos
    
def listado(datos):
    for info in datos['empresas']:
        print('La empresa ', info['empresa']['nombre'], ' trabaja en el secto ', info['empresa']['sector'], ' en el país ', info['empresa']['sedes'][0]['pais'], ' ubicada en la ciudad ', info['empresa']['sedes'][0]['ciudad'])
      
        
def total_empresas_emp_soc(datos):
    total = len(datos['empresas'])
    print('Hay un total de ', total, ' empresas.')
    for emp in datos['empresas']:
        nombre = emp['empresa']['nombre']
        total_miembros = 0
        
        for sede in emp['empresa']['sedes']:
            for planta in sede['edificio']['plantas']:
                for depto in planta['departamentos']:
                    if depto['nombre'] == 'SOC':
                        for equipo in depto['equipos']:
                            total_miembros = total_miembros + len(equipo['miembros'])

    
        print('La empresa ', nombre, ' tiene ', total_miembros, 'trabajadores en el SOC')
        


