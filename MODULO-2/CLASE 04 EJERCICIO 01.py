# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Escribe un programa que reciba una lista de calificaciones (números entre 0 y 100) y realice lo siguinte:
- Calcule el promedio general.
- Cuente cuantos estudiantes aprobaron (nota >=60).
- Genere una nueva lista sólo con las notas aprobadas.

Paso a Paso:
- Define una lista con al menos 8 calificaciones.
- Usa un for para recorrer las calificaciones y calcular el total acumulado.
- Suma una condición (if) para contar los aprobados y guardar sus notas en otra lista.
- Calcula el promedio al final y muestralo junto con la cantidad de aprobados y su lista.
"""
# Se desarrolla el programa de forma modular.
# Se define la función para calcular el promedio de notas.
def calcular_promedio(lista):
    return sum(lista) / len(lista)

# Se define la función usando ciclo for para contar cuántos aprobaron (nota >= 60).
def contar_aprobados(lista):
    return len([nota for nota in lista if nota >= 60])

# Se define la función usando ciclo for para generar una nueva lista con las notas >= 60.
def obtener_aprobados(lista):
    return [nota for nota in lista if nota >= 60]

# Se define la función principal del programa de Análisis de Calificaciones.
# Se define una lista con al menos 8 calificaciones entre 0 y 100.
def analizar_calificaciones():
    calificaciones = [54, 81, 60, 50, 77, 67, 58, 96]
  
    promedio = calcular_promedio(calificaciones)
    aprobados = obtener_aprobados(calificaciones)
    cantidad_aprobados = contar_aprobados(calificaciones)

    print(f"\nLista de calificaciones: {calificaciones}")
    print(f"Promedio general: {promedio:.2f}")
    print(f"Cantidad de aprobados: {cantidad_aprobados}")
    print(f"Lista de notas aprobadas: {aprobados}")

# Ejecución del programa
analizar_calificaciones()