# 
# EJERCICIO 02
# 
# ALEXIS YURI M.
#
"""
Escribe un programa que recorra un diccionario de empleados con nombre y edad y:
- Imprima solo los empleados mayores de 30 años.
- Genere una lista con los nombres de quienes tienen menos de 30 años.
- Indique cuantos empleados hay en total.

Paso a Paso:
- Cree un diccionario con al menos 5 empleados.
- Usa un for y .items() para recorrer cada empleado.
- Aplica una condición para filtrar según edad.
- Guarda en una lista los nombres que cumplan con el criterio y cuenta los empleados.
"""
# 
# Se crea un diccionario con nombre y edad de 5 empleados.
empleados = {
    'emp1': {'nombre': 'Hugo', 'edad': 20},
    'emp2': {'nombre': 'Paco', 'edad': 25},
    'emp3': {'nombre': 'Luis', 'edad': 35},
    'emp4': {'nombre': 'Maria', 'edad': 40},
    'emp5': {'nombre': 'Luisa', 'edad': 45}
}

# Se crea una lista vacía para guardar los nombres de empleados menores de 30 años.
menores_de_30 = []

# Contador del total de empleados inicializado en 0.
total_empleados = 0

# Se usa un ciclo for para recorrer el diccionario y condición para filtrar por edad.
# Se imprime nombre y edad de empleados mayores de 30 años. Los menores se almacenan en una lista.
for emp_id, datos in empleados.items():
    total_empleados += 1
    nombre = datos['nombre']
    edad = datos['edad']

    if edad > 30:
        print(f"{nombre} tiene {edad} años.")
    elif edad < 30:
        menores_de_30.append(nombre)

# Se imprime lista con empleados menores de 30 años y total de empleados.
print(f"\nLista de empleados menores de 30 años: {menores_de_30}")
print(f"Cantidad total de empleados: {total_empleados}")

