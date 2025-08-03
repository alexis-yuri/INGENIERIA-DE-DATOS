# 
# EJERCICIO 02
# 
# ALEXIS YURI M.
#
"""
Transformación y enriquecimiento de datos de RRHH.

Aplica transformaciones avanzadas a un dataset de empleados (empleados.csv) para crear
nuevas variables y preparar los datos para análisis.

Paso a paso:

- Agrupa los empleados por área y calcula el promedio de antigüedad y edad.
- Discretiza la edad en categorías:
    Joven (≤30)
    Medio (31–45)
    Senior (46+)
- Crea una nueva columna con apply() para clasificar empleados según su permanencia 
  (Antigüedad > 5 años = “Estable”).
- Exporta el nuevo DataFrame limpio con to_csv().

"""

#Paso a Paso

# Se importa librería Pandas como pd
import pandas as pd


# Se carga el archivo csv.
df = pd.read_csv('empleados.csv')


# Se calcula el promedio de 'edad' y 'antigüedad' por cada área.
promedios = df.groupby('área')[['edad', 'antigüedad']].mean().reset_index()

print("Promedios de 'edad' y 'antigüedad' por área:\n", promedios, "\n")


# Se define una función para clasificar los empleados por edad.
def categorizar_edad(edad):
    if edad <= 30:
        return 'Joven'
    elif 31 <= edad <= 45:
        return 'Medio'
    else:
        return 'Senior'


# Se agrega al dataframe una nueva columna llamada 'categoria_edad'.
df['categoria_edad'] = df['edad'].apply(categorizar_edad)


# Se usa apply para agregar una nueva columna 'permanencia'
df['permanencia'] = df['antigüedad'].apply(lambda x: 'Estable' if x > 5 else 'No Estable')


# Se exporta el nuevo dataframe a un nuevo archivo csv.
df.to_csv('empleados_transformado.csv', index=False)

print("Nuevo dataset:\n", df)






