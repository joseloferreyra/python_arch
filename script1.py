import csv

# Función para leer datos desde un archivo CSV
def leer_datos_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            # Convertir la edad a un entero
            fila['Edad'] = int(fila['Edad'])
            datos.append(fila)
    return datos

# Función para imprimir todos los datos
def imprimir_datos(datos):
    for fila in datos:
        print(f"Nombre: {fila['Nombre']}, Apellido: {fila['Apellido']}, Edad: {fila['Edad']}, Departamento: {fila['Departamento']}")

# Función para filtrar por departamento
def filtrar_por_departamento(datos, departamento):
    filtrados = [fila for fila in datos if fila['Departamento'] == departamento]
    return filtrados

# Función para encontrar el empleado más joven
def encontrar_empleado_mas_joven(datos):
    return min(datos, key=lambda x: x['Edad'])

# Función para calcular la edad promedio
def edad_promedio(datos):
    total_edades = sum(empleado['Edad'] for empleado in datos)
    return total_edades / len(datos)

# Función para encontrar empleados por apellido
def encontrar_empleados_por_apellido(datos, apellido):
    return [empleado for empleado in datos if empleado['Apellido'].lower() == apellido.lower()]

# Nombre del archivo CSV
nombre_archivo = 'empleados.csv'

# Leer datos del archivo CSV
datos = leer_datos_csv(nombre_archivo)

# Imprimir todos los datos
print("Todos los empleados:")
imprimir_datos(datos)

# Filtrar empleados del departamento IT
print("\nEmpleados en IT:")
empleados_it = filtrar_por_departamento(datos, 'IT')
imprimir_datos(empleados_it)

# Encontrar el empleado más joven
empleado_mas_joven = encontrar_empleado_mas_joven(datos)
print(f"\nEl empleado más joven es: {empleado_mas_joven['Nombre']} {empleado_mas_joven['Apellido']}, Edad: {empleado_mas_joven['Edad']}")

# Calcular la edad promedio
promedio_edad = edad_promedio(datos)
print(f"La edad promedio de los empleados es: {promedio_edad:.2f}")

# Buscar empleados por apellido
apellido_busqueda = "Garcia"
empleados_encontrados = encontrar_empleados_por_apellido(datos, apellido_busqueda)
print(f"\nEmpleados con el apellido {apellido_busqueda}:")
imprimir_datos(empleados_encontrados)