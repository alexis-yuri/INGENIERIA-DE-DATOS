# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Explorando Matrices y operaciones básicas.

Crear una matríz 3x3 usando np.array a partir de listas de listas. Luego, aplica
operaciones matemáticas básicas (suma y multiplicación por un escalar), y
realiza una selección condicional de elementos mayores a 5.
Finalmente, analiza si el resultado de una asignación es una copia o una referencia.
"""

#Paso a Paso

# Se importa libreria Numpy como np.
import numpy as np

# Se crea una matriz de 3x3 con números del 1 al 9.
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("La matriz A:\n",A,"\n")

# Se suma 10 a cada elemento de la matriz A.
A_suma = A + 10
print("La matriz A sumada al escalar 10:\n",A_suma,"\n")

# Se multiplica la matriz A por 2.
A_doble = A * 2
print("La matriz A multiplicada por el escalar 2:\n",A_doble,"\n")


# Se extraen los elementos mayores a 5 usando selección condicional.
mayores_a_5 = A[A > 5]
print("Los elementos de la matriz A mayores a 5 son:\n", mayores_a_5)


# Se asigna A a B y luego se modifica un valor de B.
B = A
B[0, 0] = 999
print("\nMatriz B modificada (referencia):\n", B)
print("\nTambién cambió la matriz A:\n", A)


# Se restaura la matriz A original, luego se usa B=A.copy() y se repite la modificación.
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])  

B = A.copy()
B[0, 0] = 999
print("\nMatriz B (copia) modificada:\n", B)
print("\nLa matriz A no cambió:\n", A,"\n")
