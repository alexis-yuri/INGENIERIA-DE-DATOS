# 
# EJERCICIO 02
# 
# ALEXIS YURI M.
#
"""
Generación de datos y redimensionado.

Utiliza funciones de Numpy como np.arange(), np.linspace() y np.random.randit() para
generar distintos tipos de arreglos.
Luego, redimensionalos con reshape() y aplica funciones matemáticas a los mismos.
"""

#Paso a Paso

# Se importa libreria Numpy como np.
import numpy as np

# Se crea un arreglo con np.arange(1, 17) y se redimensiona a una matriz de 4x4
x = np.arange(1, 17).reshape(4, 4)

# Se genera un arreglo de 10 elementos equidistantes entre 0 y 100 usando np.linspace()
linspace_arr = np.linspace(0, 100, 10)


# Se crea una matriz aleatoria de 3x3 con enteros entre 1 y 20 usando np.random.randint()
random_matrix = np.random.randint(1, 21, size=(3, 3))


# Se aplican np.sqrt() y np.log() sobre las matrices.
sqrt_x = np.sqrt(x)
log_x = np.log(x)

sqrt_linspace = np.sqrt(linspace_arr)
log_linspace = np.log(linspace_arr + 1e-9)  # para evitar log(0) se suma un pequeño epsilon

sqrt_random = np.sqrt(random_matrix)
log_random = np.log(random_matrix)


# Se imprimen los resultados:
print("Paso 1 - Matriz 4x4 con np.arange:")
print(x)
print("\nRaíz cuadrada de la matriz:")
print(sqrt_x)
print("\nLogaritmo natural de la matriz:")
print(log_x)

print("\nPaso 2 - Arreglo equidistante entre 0 y 100:")
print(linspace_arr)
print("\nRaíz cuadrada del arreglo:")
print(sqrt_linspace)
print("\nLogaritmo natural del arreglo (evitando log(0)):")
print(log_linspace)

print("\nPaso 3 - Matriz aleatoria 3x3 entre 1 y 20:")
print(random_matrix)
print("\nRaíz cuadrada de la matriz:")
print(sqrt_random)
print("\nLogaritmo natural de la matriz:")
print(log_random,"\n")


# Qué diferencias notas en la forma de aplicar funciones sobre arreglos enteros vs flotantes?

# Las diferencias en NumPy tienen que ver principalmente con la precisión, el tipo de resultados
# obtenidos y el comportamiento de ciertas funciones.

# Usar arreglos flotantes es más seguro y preciso cuando se trabaja con funciones matemáticas
# complejas o que requieren valores no enteros.

# Algunas funciones matemáticas como np.sqrt() o np.log() requieren valores flotantes para devolver
# resultados válidos. Por eso si se aplican estas funciones a un arreglo entero, NumPy convierte
# internamente los datos a tipo flotante para evitar errores o pérdida de precisión.






