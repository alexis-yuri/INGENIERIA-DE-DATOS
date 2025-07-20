# 
# EJERCICIO 03
# 
# ALEXIS YURI M.
#
"""
Crear un programa en Python que reciba el nombre, edad y país de residencia de una persona.
El sistema debe imprimir un mensaje personalizado y, adicionalmente, informar si esa
persona puede acceder a un beneficio que sólo está disponible para mayores de 18 años
que vivan en Argentina, Chile o Colombia.
"""
#
#
# Se solicitan los datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su país de residencia: ").lower()

# Se valida la edad mayor o igual a 18 años.
es_mayor_de_edad = edad >= 18

# Se valida que resida en uno de los paises de la lista.
pais_valido = pais in ["argentina", "chile", "colombia"]

# Se evalua que se cumplan las 2 condiciones anteriores.
acceso_beneficio = es_mayor_de_edad and pais_valido

# Se imprime un mensaje personalizado.
if acceso_beneficio:
    print(f"Hola, {nombre}, puedes acceder al beneficio.")
else:
    print(f"Hola, {nombre}, no puedes acceder al beneficio.")

