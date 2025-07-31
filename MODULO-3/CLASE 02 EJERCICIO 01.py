# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Primer acercamiento al análisis exploratorio con Pandas.

Carga un archivo CSV con Pandas y explora su contenido utilizando métodos como head(), info() y
describe(). Luego extrae estadísticas clave de las columnas numéricas y verifica si hay valores nulos.

Paso a Paso:

- Importa la librería Pandas como pd.
- Lee el archivo data.csv con pd.read_csv('data.csv') y asignalo a una variable llamada df.
- Usa los métodos:
	- df.head() para ver los primeros registros.
	- df.info() para revisar estructura y tipos de datos.
	- df.describe() para ver estadísticas básicas.

- Aplica df.isnull().sum() para detectar alores nulos.
- Usa df.mean() , df.median() y df.std() para obtener medidas adicionales.
- Comparte una breve interpretación de lo que observaste.

"""

#Paso a Paso

# Se importa libreria Pandas como pd.
import pandas as pd

# 1. Se lee el archivo CSV
df = pd.read_csv('data.csv')

# 2. Se muestran los primeros 5 registros del Dataframe creado.
print("Primeros 5 registros:")
print(df.head())

# 3. Se revisa la estructura y los tipos de datos
print("\nInformación general del DataFrame:")
print(df.info())

# 4. Se generan estadísticas básicas de los registros.
print("\nEstadísticas descriptivas:")
print(df.describe())

# 5. Se verifica la existencia de valores nulos.
print("\nValores nulos por columna:")
print(df.isnull().sum())

# 6. Se obtienen valores de la media, mediana y desviación estándar de las columnas "Edad" y "Sueldo".
print("\nMedia de las columnas numéricas:")
print(df.mean(numeric_only=True))

print("\nMediana de las columnas numéricas:")
print(df.median(numeric_only=True))

print("\nDesviación estándar de las columnas numéricas:")
print(df.std(numeric_only=True))


# 7. Interpretación:

# El conjunto de datos del Dataframe tiene las siguientes características:
# - Tiene 3 columnas, "Edad", "Sueldo" y "Area".
# - Tiene tipos de datos numéricos(flotantes) y objetos (string).
# - La columna "Edad" y "Sueldo" tienen valores nulos.
# - Las medias y medianas nos permiten observar si hay sesgo en la distribución (cuando no son iguales).
#   En este caso hay desviación en la columna "Edad" y no la hay en la columna "Sueldo".
# - La desviación estándar indica la dispersión de los datos.


