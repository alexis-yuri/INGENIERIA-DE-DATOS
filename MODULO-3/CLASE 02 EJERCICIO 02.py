# 
# EJERCICIO 02
# 
# ALEXIS YURI M.
#
"""
Práctica con Python

Paso a Paso:

- Abre tu entorno de trabajo preferido (VS Code, Jupiter etc.).
- Crea un nuevo archivo o celda de código.
- Escribe un programa que:
	- Solicite al usuario su nombre y edad.
	- Use una estructura condicional IF para verificar si es mayor o menor de edad.
	- Imprima un mensaje de saludo que incluya el nombre y la condición (mayor o menor).

- Pruébalo con diferentes edades para verifiar que funiona correctamente.
- Agrega una función llamada es_mayor() que reciba la edad y retorne True or False.

"""

#Paso a Paso

# Se define una función que recibe la edad y determina si la persona es mayor de edad.
def es_mayor(edad):
    return edad >= 18

# Se solicita nombre y edad del usuario.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# Usando una estructura IF y la función es_mayor() se verifica si usuario es mayor o menor de edad.
if es_mayor(edad):
    condicion = "mayor de edad"
else:
    condicion = "menor de edad"

# Se muestra mensaje de saludo que incluye nombre y condición.
print(f"Hola, {nombre}, eres {condicion}.")


