# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Exploración de archivos CSV.

Usa Pandas para cargar un archivo .csv, inspecciona su contenido y exporta
una versión modificada del archivo, aplicando algunas transformaciones básicas.

Paso a Paso:
- Importa la librería Pandas.
- Cargá un archivo CSV con pd.read_csv('archivo.csv').
- Visualiza las primeras filas con df.head() y revisá estructura general con df.info().
- Renombrar las columnas manualmente si no hay encabezado (header=None, names=[]).
- Detecta valores nulos con df.isnull().sum() y reemplazalos si es necesario.
- Exporta el DataFrame modificado a un nuevo archivo CSV (df.to_csv('nuevo_archivo.csv', index=False)).

"""

#Paso a Paso

# Se importa librería Pandas como pd
import pandas as pd

# Se carga el archivo CSV.
df = pd.read_csv('archivo.csv')

# Se visualizan las primeras filas y revisa la estructura general del dataframe.
print("Primeras filas del archivo:")
print(df.head())

print("\nInformación general del DataFrame:")
print(df.info())

# Se renombran las columnas del archivo sin encabezado.
# df = pd.read_csv('archivo.csv', header=None, names=['columna1', 'columna2', 'columna3'])

# Se detectan valores nulos por cada columna del dataframe.
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Se reemplazan valores nulos.
df.fillna(0, inplace=True)

# Se exporta el dataFrame modificado a un nuevo archivo CSV.
df.to_csv('nuevo_archivo.csv', index=False)
