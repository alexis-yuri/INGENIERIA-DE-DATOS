# 
# EJERCICIO 02
# 
# ALEXIS YURI M.
#
"""
Lectura desde Excel y extracción de tablas web.

Lee un archivo de Excel desde tu equipo y extrae una tabla HTML desde una página
web utilizando Pandas. Explora ambos conjuntos de datos y guarda una copia en
archivos locales.

Paso a Paso:

- Asegurate de tener instalada la librería openpyxl para poder leer archivos .xlsx.
- Lee un archivo Excel con pd.read_excel('archivo.xlsx').
	- Si hay múltiples hojas prueba cargarlas usando sheet_name-.
- Busca una URL que contenga una tabla HTML simple (o usa una proporcionada por el docente).
- Utiliza pd.read_html('url') para importar tabla (recuerda que devuelve una lista de Dataframes).
- Explora los datos con head() y describe().
- Exporta ambos conjuntos de datos como nuevos archivoa .xlsx y csv.

"""

#Paso a Paso

# Se importa la librería Pandas con el alias pd
import pandas as pd


# Se lee el archivo Excel.
df_excel = pd.read_excel('valores.xlsx')


# Se exploran los datos del dataframe con head() y describe().
print("Primeras 5 filas del dataframe 1:")
print(df_excel.head())

print("\nResumen estadístico del dataframe 1:")
print(df_excel.describe())


# Se guardan los datos leídos en un nuevo archivo Excel
df_excel.to_excel('valores_nuevos.xlsx', index=False)

#---------------------------------------------------------

# URL del ejemplo con tabla UF (del SII)
url = 'https://www.sii.cl/valores_y_fechas/uf/uf2025.htm'

# Se leen las tablas HTML
tablas = pd.read_html(url, decimal=",", thousands=".")

# Se usa la primera tabla.
df_html = tablas[0]

# Se exploran los datos del dataframe con head() y describe().
print("\nPrimeras 5 filas del dataframe 2:")
print(df_html.head())

print("\nResumen estadístico del dataframe 2:")
print(df_html.describe())

# Se guardan los datos leídos desde la web en un archivo CSV.
df_html.to_csv('tabla_uf_2025.csv', index=False)


