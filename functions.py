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
    try:
        with open('empresas.json') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print("Error: El archivo 'empresas.json' no existe.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON está mal formado.")
    except Exception as e:
        print("Error inesperado:", e)


def listado(datos):
    try:
        for info in datos['empresas']:
            print('La empresa ', info['empresa']['nombre'], 
                  ' trabaja en el sector ', info['empresa']['sector'], 
                  ' en el país ', info['empresa']['sedes'][0]['pais'], 
                  ' ubicada en la ciudad ', info['empresa']['sedes'][0]['ciudad'])
    except KeyError:
        print("Error: Faltan datos en la estructura del JSON.")
    except TypeError:
        print("Error: Los datos no tienen el formato esperado.")


def total_empresas_emp_soc(datos):
    try:
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
                                total_miembros += len(equipo['miembros'])

            print('La empresa ', nombre, ' tiene ', total_miembros, ' trabajadores en el SOC')
    
    except KeyError:
        print("Error: Falta alguna clave en los datos.")
    except TypeError:
        print("Error: Estructura de datos incorrecta.")


def empresa_sector_pais(datos):
    try:
        sector = input('Ingrese el sector: ')
        pais = input('Ingrese el país: ')
        
        if sector.isdigit() or pais.isdigit():
            raise ValueError("El sector y el país deben ser texto, no números.")
        
        for emp in datos['empresas']:
            empresa = emp['empresa']['nombre']
            sector_emp = emp['empresa']['sector']
            pais_emp = emp['empresa']['sedes'][0]['pais']
            
            if sector_emp == sector and pais_emp == pais:
                print('La empresa ', empresa, ' trabaja en el sector ', sector, ' en el país ', pais)
    
    except ValueError as e:
        print("Error:", e)
    except KeyError:
        print("Error: Datos incompletos en el JSON.")
    except TypeError:
        print("Error: Problema en el formato de los datos.")


def empresa_hostname(datos):
    try:
        hostname = input('Ingrese el hostname: ').strip()
        
        if not hostname:
            raise ValueError("El hostname no puede estar vacío.")
        
        encontrado = False
        
        for emp in datos['empresas']:
            if 'infraestructura' in emp and 'servidores' in emp['infraestructura'] and 'wazuh' in emp['infraestructura']['servidores']:
                wazuh = emp['infraestructura']['servidores']['wazuh']
                
                if 'managers' in wazuh:
                    for manager in wazuh['managers']:
                        if manager['hostname'] == hostname:
                            empresa = emp['empresa']
                            sede = empresa['sedes'][0]
                            
                            print('- La empresa a la que pertenece:', empresa['nombre'])
                            print('- El sector:', empresa['sector'])
                            print('- El país:', sede['pais'])
                            print('- La ciudad:', sede['ciudad'])
                            print('- El nombre del edificio principal:', sede['edificio']['nombre'])
                            
                            encontrado = True 
        
        if not encontrado:
            raise ValueError("El hostname introducido no existe.")
    
    except ValueError as e:
        print("Error:", e)
    except KeyError:
        print("Error: Falta información en la infraestructura.")
    except TypeError:
        print("Error: Formato de datos incorrecto.")


def filtrar_herramienta(datos):
    try:
        herramienta = input('Ingrese la herramienta: ')
        
        empresas_encontradas = []
        miembros_encontrados = []
        roles = []
        tipos_habilidad = []
        
        total_empresas = len(datos['empresas'])
        
        for emp in datos['empresas']:
            nombre_empresa = emp['empresa']['nombre']
            
            for sede in emp['empresa']['sedes']:
                for planta in sede['edificio']['plantas']:
                    for depto in planta['departamentos']:
                        for equipo in depto['equipos']:
                            for miembro in equipo['miembros']:
                                
                                habilidades = miembro['habilidades']
                                
                                for tipo in habilidades:
                                    if isinstance(habilidades[tipo], list):
                                        if herramienta in habilidades[tipo]:
                                            
                                            if nombre_empresa not in empresas_encontradas:
                                                empresas_encontradas.append(nombre_empresa)
                                            
                                            miembros_encontrados.append({
                                                'nombre': miembro['nombre'],
                                                'rol': miembro['rol'],
                                                'empresa': nombre_empresa
                                            })
                                            
                                            if miembro['rol'] not in roles:
                                                roles.append(miembro['rol'])
                                            
                                            if tipo not in tipos_habilidad:
                                                tipos_habilidad.append(tipo)
        
        print('\n--- RESULTADOS ---\n')
        
        print('Empresas donde aparece:')
        for e in empresas_encontradas:
            print('- ', e)
        
        print('\nMiembros que la utilizan:')
        for m in miembros_encontrados:
            print('- ', m['nombre'], '(', m['rol'], ') -', m['empresa'])
        
        print('\nRoles:')
        for r in roles:
            print('- ', r)
        
        print('\nTipo de habilidad:')
        for t in tipos_habilidad:
            print('- ', t)
        
        print('\nTotal empresas que la usan:', len(empresas_encontradas))
        print('Total miembros que la usan:', len(miembros_encontrados))
        
        if total_empresas > 0:
            porcentaje = (len(empresas_encontradas) / total_empresas) * 100
            print('Porcentaje respecto al total de empresas:', round(porcentaje, 2), '%')
    
    except KeyError:
        print("Error: Alguna clave no existe en los datos.")
    except TypeError:
        print("Error: Problema con el tipo de datos.")
