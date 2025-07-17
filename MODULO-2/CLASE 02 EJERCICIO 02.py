# 
# EJERCICIO 02
# 
# ALEXIS YURI M.
#
"""
Escriba un programa que reciba el nombre, la edad y el salario de una persona, y que luego muestre un mensaje 
con el siguiente formato:

"Hola, [nombre]. Tienes [edad] años y tu salario es $[salario]."

Asegúrate que el salario se muestre con dos decimales.
"""
#
#
# Se solicitan los datos al usuario.
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
salario = float(input("Ingresa tu salario: "))

# Se formatea e imprime el mensaje.
mensaje = f"Hola, {nombre}. Tienes {edad} años y tu salario es ${salario:.2f}."
print(mensaje)