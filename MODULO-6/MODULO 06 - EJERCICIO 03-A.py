
# MODULO 06 - EJERCICIO 03-A 
# diagnóstico y transformación de datos crudos
#
# ALEXIS YURI M.


# Se importan las librerías
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


# Se carga el dataset.
df = pd.read_csv("dataset_vivero.csv", encoding="latin-1", sep=";")

print("\n")
print("Forma inicial:", df.shape)
print("\nPrimeras 5 filas:")
print(df.head())


# Se buscan valores nulos y duplicados.
print("\nValores nulos por columna:\n", df.isna().sum())
print("\nFilas duplicadas:", df.duplicated().sum())


# Se revisan que tipos de datos tienen las columnas.
print("\nTipos de datos iniciales:\n", df.dtypes)


# Se convierten a numéricas las columnas guardadas como texto. 
def to_num_series(s: pd.Series) -> pd.Series:
    cleaned = s.astype(str).str.replace(",", ".", regex=False)   
    cleaned = cleaned.str.replace(r"[^0-9\.\-]", "", regex=True) 
    cleaned = cleaned.replace("", np.nan)
    return pd.to_numeric(cleaned, errors="coerce")

df_clean = df.copy()

for c in df_clean.select_dtypes(include=["object"]).columns:
    conv = to_num_series(df_clean[c])
    if conv.notna().mean() >= 0.8:   # convertir si ≥80% de valores son numéricos válidos
        df_clean[c] = conv

print("\nTipos de datos después de conversión:\n", df_clean.dtypes)


# Se identifican columnas numéricas y categóricas.
num_cols = df_clean.select_dtypes(include=["number"]).columns.tolist()
cat_cols = df_clean.select_dtypes(exclude=["number"]).columns.tolist()


# Se excluye del análisis la columna "PlantaID" 
id_cols = [c for c in df_clean.columns if "id" in c.lower()]
num_cols = [c for c in num_cols if c not in id_cols]
cat_cols = [c for c in cat_cols if c not in id_cols]

print("\nColumnas numéricas:", num_cols)
print("Columnas categóricas:", cat_cols)
print("Columnas identificadoras:", id_cols)


# Se imputan valores faltantes
df_imp = df_clean.copy()

# En columnas numéricas se imputa la media o mediana según sesgo.
for c in num_cols:
    strat = "median" if abs(df_imp[c].skew()) > 1 else "mean"
    df_imp[c] = SimpleImputer(strategy=strat).fit_transform(df_imp[[c]])

# En columnas categóricas se imputa la moda.
if cat_cols:
    df_imp[cat_cols] = SimpleImputer(strategy="most_frequent").fit_transform(df_imp[cat_cols])


# Se usa codificación One-Hot en columnas categoricas (para convertirlas en binarias).
if cat_cols:
    df_ohe = pd.get_dummies(df_imp[cat_cols], 
                            prefix=cat_cols, 
                            prefix_sep="=", 
                            drop_first=False, 
                            dtype="uint8")
else:
    df_ohe = pd.DataFrame(index=df_imp.index)

print("\nColumnas después del One-Hot Encoding:", df_ohe.shape[1])


# Se realiza escalamiento con StandardScaler.
if num_cols:
    scaler = StandardScaler()
    df_scaled_num = pd.DataFrame(scaler.fit_transform(df_imp[num_cols]),
                                 columns=num_cols, index=df_imp.index)
else:
    df_scaled_num = pd.DataFrame(index=df_imp.index)


# Se concatenan las "columnas" resultantes en un nuevo dataset.
if id_cols:
    df_final = pd.concat([df_imp[id_cols], df_scaled_num, df_ohe], axis=1)
else:
    df_final = pd.concat([df_scaled_num, df_ohe], axis=1)

print("\nForma final:", df_final.shape)
print("Primeras 5 filas:", df_final.head())


# Se exporta a un archivo CSV el nuevo dataset transformado.
df_final.to_csv("dataset_vivero_procesado.csv", index=False)
print("\n Dataset procesado guardado como dataset_vivero_procesado.csv")
