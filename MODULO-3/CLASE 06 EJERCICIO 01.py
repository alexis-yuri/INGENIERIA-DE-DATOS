# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Análisis de ventas por categoría.

Utiliza técnicas de agrupamiento y pivoteado con Pandas para construir un resumen tabular de ventas mensuales por categoría.

Paso a paso:

- Carga el archivo ventas_productos.csv (contiene columnas como fecha, categoría, producto, ventas).
- Convierte la columna fecha a tipo datetime y extrae el mes en una nueva columna.
- Agrupa por categoría y mes usando groupby() y calcula la suma de ventas.
- Pivotea el resultado para que las categorías estén en filas y los meses en columnas.
- Exporta el DataFrame pivotado como reporte_categorias.csv.

"""

#Paso a Paso

# Se importa librería Pandas como pd
import pandas as pd


# Se lee el archivo csv.
df = pd.read_csv("ventas_productos.csv")
print("Se muestran las 5 primeras filas del dataframe:")
print(df.head())

# Se convierte la columna fecha a tipo datetime y se crea una nueva columna 'mes'.
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month

# Se agrupa por categoría y mes, y se calcula la suma de las ventas.
agrupado = df.groupby(['categoría', 'mes'])['ventas'].sum().reset_index()
print("\nVentas agrupadas por categoría y mes:")
print(agrupado)

# Se pivotean los datos para que las categorías estén en filas y los meses en columnas.
pivoteado = agrupado.pivot(index='categoría', columns='mes', values='ventas').fillna(0)
print("\nTabla de ventas mensuales por categoría:")
print(pivoteado)

# Se exporta el nuevo dataframe a csv.
pivoteado.to_csv("reporte_categorias.csv", encoding='utf-8')
print("\nEl reporte de categorías ha sido exportado a csv correctamente.")
