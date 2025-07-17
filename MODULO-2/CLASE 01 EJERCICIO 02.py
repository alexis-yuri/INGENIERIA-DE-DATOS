# 
# EJERCICIO 02
# 
# ALEXIS YURI M.
#
"""Práctica con Python

Paso a paso:
1. Abre tu entorno de trabajo preferido (VS Code, Jupyter, Colab, etc.).
2. Crea un nuevo archivo o celda de código.
3. Escribe un programa que:
    - Solicite al usuario su nombre y edad.
    - Use una estructura condicional (if) para verificar si es mayor o menor de edad.
    - Imprima un mensaje de saludo que incluya el nombre y la condición (mayor o menor).
4. Pruébalo con diferentes edades para verificar que funcione correctamente.
5. (Opcional) Agrega una función llamada es_mayor() que reciba la edad y retorne True o False.
"""

#
# Se solicita al usuario su nombre.
nombre = input("Ingrese su nombre: ")

# Se solicita al usuario su edad (y se convierte a entero).
edad = int(input("Ingrese su edad: "))

# Se verifica si la edad es negativa.
if edad < 0:
    print("La edad no puede ser negativa, vuelva a intentarlo.")
else:
    # Se verifica si usuario es mayor o menor de edad.
    if edad >= 18:
        condicion = "mayor de edad"
    else:
        condicion = "menor de edad"

    # Se imprime un mensaje.
    print(f"¡Hola, {nombre} eres {condicion}.")
