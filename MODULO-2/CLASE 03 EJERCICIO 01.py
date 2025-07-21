# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Crear un programa en Python que reciba el nombre, edad y país de residencia de una persona.
El sistema debe imprimir un mensaje personalizado y, adicionalmente, informar si esa
persona puede acceder a un beneficio que sólo está disponible para mayores de 18 años
que vivan en Argentina, Chile o Colombia.

Divide el programa de la actividad anterior en dos archivos: uno que contenga todas las funciones
(tu propio módulo) y otro que sea el programa principal desde donde se importa y se ejecuta la
lógica del menú. 
"""
#
# Se solicitan los datos de nombre, edad y país usando la función capturar_datos().
def capturar_datos():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    pais = input("Ingrese su país de residencia: ").lower()
    return nombre, edad, pais

# Se verifica que la edad sea mayor o igual a 18 años y que el país esté en la lista.
def validar_datos(edad, pais):
    es_mayor_de_edad = edad >= 18
    pais_valido = pais in ["argentina", "chile", "colombia"]
    return es_mayor_de_edad and pais_valido

#  Se muestra mensaje personalizado según la validación de los datos.
def mostrar_mensaje(nombre, acceso_beneficio):
    if acceso_beneficio:
        print(f"Hola, {nombre}, puedes acceder al beneficio.")
    else:
        print(f"Hola, {nombre}, no puedes acceder al beneficio.")

# Se define la función principal que invoca las funciones anteriores.
def main():
    nombre, edad, pais = capturar_datos()
    acceso_beneficio = validar_datos(edad, pais)
    mostrar_mensaje(nombre, acceso_beneficio)

# Se ejecuta la función principal.
if __name__ == "__main__":
    main()
