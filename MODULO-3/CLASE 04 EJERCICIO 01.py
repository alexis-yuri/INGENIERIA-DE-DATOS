# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Carga y exportación de archivos CSV.

Utiliza Pandas para cargar un archivo CSV sin encabezados, renonmbrar las columnas, limpiar
datos nulos y exportar el resultado a un nuevo archivo .csv con delimitador personalizado.

Paso a paso:

- Abre tu entorno de trabajo preferido (VS Code, Jupyter, Colab, etc.).
- Importa Pandas (import pandas as pd).
- Lee el archivo datos.csv usando header=None y asigna nombres personalizados con names=['nombre', 'edad', 'ciudad'].
- Reemplaza valores nulos o símbolos como '?' usando na_values y fillna().
- Elimina filas duplicadas si las hubiera con drop_duplicates().
- Exporta el DataFrame limpio con to_csv(), usando sep=';' y encoding='utf-8'.

"""

#Paso a Paso

# Se importa librería Pandas como pd
import pandas as pd

# Se simula un archivo CSV sin encabezado
datos_crudos = [
    ["Juan", "25", "Santiago"],
    ["Ana", "?", "Valparaíso"],
    ["Carlos", "30", "Santiago"],
    ["Ana", "?", "Valparaíso"],
    ["Luis", "28", "?"]
]

# Se guarda como 'datos.csv' en el mismo directorio del script
pd.DataFrame(datos_crudos).to_csv("datos.csv", header=False, index=False)



# Se lee el archivo sin encabezado, se asigna nombres de columnas y define "?" como valor nulo.
df = pd.read_csv("datos.csv", header=None, names=["nombre", "edad", "ciudad"], na_values="?")

# Se muestra las primeras 5 filas.
print("Primeras 5 filas del dataframe:\n", df.head())

# Se reemplazan valores nulos para cada columna.
# Se usará la media sin decimales para reemplazar valores nulos de la edad.
media=int(df["edad"].mean())
df["nombre"].fillna("Desconocido", inplace=True)
df["edad"].fillna(media, inplace=True)
df["ciudad"].fillna("Desconocida", inplace=True)

# Se eliminan los duplicados.
df.drop_duplicates(inplace=True)

# Se exporta el dataframe limpio a un nuevo archivo CSV con delimitador punto y coma.
df.to_csv("datos_limpios.csv", sep=';', encoding='utf-8', index=False)

print("Archivo limpio exportado exitosamente.")