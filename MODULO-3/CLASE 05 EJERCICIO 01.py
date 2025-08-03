# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Limpieza de datos de un e-commerce.

Usa Pandas para limpiar el archivo ventas_ecommerce.csv, aplicando técnicas de detección de duplicados,
reemplazo de valores erróneos y normalización de formatos..

Paso a paso:

- Carga el dataset con pd.read_csv().
- Detecta y elimina filas duplicadas.
- Identifica columnas con valores nulos y decidí si deben eliminarse o imputarse.
- Reemplaza valores incorrectos en la columna Método de pago (ej: “tarjeta”, “efetivo”) usando replace().
- Asegurate de que las fechas estén en formato datetime y los precios en float.

"""

#Paso a Paso

# Se importa librería Pandas como pd
import pandas as pd

# Se lee el arhivo csv.
df = pd.read_csv('ventas_ecommerce.csv')
print("Primeras 5 filas del dataframe:")
print(df.head())

# Se eliminan filas duplicadas.
duplicados = df.duplicated().sum()
print(f"Filas duplicadas: {duplicados}")
df = df.drop_duplicates()

# Se identifican los valores nulos.
print("\nCantidad de valores nulos por columna:")
print(df.isnull().sum())

# Se eliminan filas con valores nulos en columnas definidas 'precio' y 'fecha'.
df = df.dropna(subset=['precio', 'fecha'])

# Se imputan valores nulos en la columna 'metodo_pago'.
df['metodo_pago'].fillna('desconocido', inplace=True)

# Se reemplazan valores incorrectos en la columna 'metodo_pago'.
print("\nValores únicos en columna 'metodo_pago' antes del reemplazo:")
print(df['metodo_pago'].unique())

df['metodo_pago'] = df['metodo_pago'].replace({
    'tarjeta ': 'tarjeta',
    'Tarjeta': 'tarjeta',
    'efetivo': 'efectivo'
})

print("\nValores únicos en columna 'metodo_pago' después del reemplazo:")
print(df['metodo_pago'].unique())

# Se asegura formato correcto de fecha (datetime) y precios (float).
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
df['precio'] = df['precio'].astype(float)

# Se exporta el dataframe limpio.
df.to_csv('ventas_ecommerce_limpio.csv', index=False)

# Se mostra información general del dataframe limpio.
print("\nInformación del DataFrame limpio:\n")
print(df.info())
