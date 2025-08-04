# 
# EJERCICIO 02
# 
# ALEXIS YURI M.
#
"""
Integración de datos de usuarios y compras

Aplica merge() y groupby() en Pandas para analizar cuántas compras hizo cada tipo de usuario.

Paso a paso:

- Carga dos archivos: usuarios.csv (con columnas user_id, segmento, registro_fecha) y compras.csv (con user_id, compra_id, monto).
- Unir ambos datasets utilizando merge() por user_id.
- Agrupar por segmento y contar la cantidad de compras realizadas.
- Calcula también el monto total gastado por segmento usando .agg().
- Mostrar los resultados ordenados de mayor a menor cantidad de compras.

"""

#Paso a Paso

# Se importa librería Pandas como pd
import pandas as pd

# Se leen ambos archivos csv.
usuarios = pd.read_csv('usuarios6.csv')
compras = pd.read_csv('compras6.csv')

# Se unen ambos dataframes por 'user_id' usando merge.
datos_completos = pd.merge(usuarios, compras, on='user_id')

# Se muestran los datos del nuevo dataframe formado.
print("Se muestran las 5 primeras filas del nuevo dataframe:","\n")
print(datos_completos.head())

# Se agrupa por segmento y se cuenta la cantidad de compras realizadas
compras_por_segmento = datos_completos.groupby('segmento').agg(
    cantidad_compras=('compra_id', 'count'),
    monto_total=('monto', 'sum')
)

# Se muestran los resultados ordenados de mayor a menor (cantidad de compras).
compras_ordenadas = compras_por_segmento.sort_values(by='cantidad_compras', ascending=False)
print("\nCompras Ordenadas:")
print(compras_ordenadas)



