# json_project


# Descripción

Este proyecto consiste en una aplicación en Python que permite gestionar y consultar información sobre empresas, sus sedes, empleados y herramientas utilizadas en entornos SOC (Security Operations Center), a partir de un archivo JSON.

# El sistema permite realizar diferentes consultas como:

Listado de empresas
Número de empleados SOC
Filtros por sector y país
Búsqueda por hostname
Filtrado por herramientas (ej: Wazuh, TheHive


# Estructura del archivo.json

El archivo empresas.json contiene una estructura jerárquica compleja que representa empresas con múltiples niveles organizativos.

{
  "nombre": "Jorge Molina",
  "rol": "Analista",
  "habilidades": {
    "soar": ["TheHive"],
    "forense": {
      "memoria": true,
      "disco": true
    }
  }
}

Las habilidades pueden ser listas o diccionarios, como ejemplo tenemos:
soar -> lista
forense -> diccionario


# Funciones del programa

1. Muestra el menú de opciones disponibles al usuario.

2. Carga el archivo JSON y devuelve los datos. (excepciones archivo no encontrado y json mal foramado, que se repetirá en todas las demás funciones)

3. Muestra información básica de cada empresa: nombre, sector, pais y ciudad.

4. Mostrar numero total de empresas y cuenta cuántos empleados trabajan en el departamento SOC.

5. Filtrar empresas por sector y pais (valida datos introducidos).

6. Busca información de una empresa a partir de un hostname.
Devuelve:

Empresa
Sector
Ubicación
Edificio

Valida:

Que el hostname no esté vacío
Que exista en el sistema

7. Permite buscar una herramienta (ej: Wazuh, TheHive) y muestra:
Permite buscar una herramienta (ej: Wazuh, TheHive) y muestra:

Empresas donde se usa
Miembros que la utilizan
Roles
Tipo de habilidad (ej: siem, soar)
Estadísticas (totales y porcentaje)

Tiene en cuenta que:

Solo analiza habilidades que son listas
Evita duplicados


# Problemas encontrados
Durante el desarrollo se identificaron varios problemas:
-Estructura muy anidad.
-Requiere múltiples bucles anidados.

Duplicidad de datos
-Empresas repetidas.
-Roles repetidos
-Solución: comprobaciones antes de añadir a listas


# Decisiones tomadas
Uso de try/except
-Para evitar que el programa se rompa por: errores de estructura o datos incorrectos

Validación de tipos
-Evita errores al recorrer datos no iterables

Uso de listas para resultados
-Permite controlar duplicados
