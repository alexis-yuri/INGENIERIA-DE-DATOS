# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Práctica con Python
Contexto:
Reconocer los elementos centrales del marco de trabajo Scrum para comprender cómo se estructura y funciona en un entorno ágil.
Consigna:
Construye un programa que simule una calculadora básica, pero cada operación (suma, resta, multiplicación y división) debe
estar definida como una función diferente. 
Luego, crea una función principal que le pregunte al usuario qué operación desea realizar y la ejecute.
(Nota: en esta versión solicitada no se usan funciones, se hace con if/elif/else)"""
#
#
# Se pide ingresar una operacion de la calculadora.
opcion = int(input("Ingrese la opción deseada (1) Suma / (2) Resta / (3) Multiplicación / (4) División: "))

# Se verifica que la opción esté en el rango entre 1 y 4.
if opcion < 1 or opcion > 4:
    print("Opción no válida. Debe ser un número entre 1 y 4.")
else:
    # Se solicitan los números solo si la opción es válida.
    numero1 = int(input("Ingrese el número 1: "))
    numero2 = int(input("Ingrese el número 2: "))

    # Se valida el segundo número en caso de seleccionar la opción "división".
    if opcion == 4 and numero2 == 0:
        print("El segundo número no puede ser cero.")
    else:
        if opcion == 1:
            resultado = numero1 + numero2
        elif opcion == 2:
            resultado = numero1 - numero2
        elif opcion == 3:
            resultado = numero1 * numero2
        elif opcion == 4:
            resultado = numero1 / numero2

        print("El resultado es:", resultado)