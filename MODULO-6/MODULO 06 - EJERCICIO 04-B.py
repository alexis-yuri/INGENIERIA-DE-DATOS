
# MODULO 06 - EJERCICIO 04-B
# ALEXIS YURI M.


# Se importan las librerías.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Se Carga el dataset.
df = pd.read_csv("ejercicio_2. publicidad_vs_ventas.csv", sep=";")

# Se reemplazan las comas por puntos y se convierte a tipo numérico (float).
df["Inversion_Redes_USD"] = df["Inversion_Redes_USD"].astype(str).str.replace(",", ".").astype(float)
df["Ventas_Miles_Unidades"] = df["Ventas_Miles_Unidades"].astype(str).str.replace(",", ".").astype(float)

print("Vista previa del dataset:")
print(df.head())

# Se definen variable caracteristica (X) y objetivo (y).
X = df[["Inversion_Redes_USD"]]
y = df["Ventas_Miles_Unidades"]

# Se realiza división del dataset entre entrenamiento y test.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Se entrena el modelo de regresion lineal.
model = LinearRegression()
model.fit(X_train, y_train)

# Se obtienen los coeficientes y con ellos se construye el modelo de regresión lineal.
intercept = model.intercept_
coef = model.coef_[0]
print(f"\nModelo estimado: Ventas ≈ {intercept:.4f} + {coef:.6f} * Inversión")

# Se realizan predicciones de las ventas usando el modelo de regresión.
y_pred = model.predict(X_test)

# Se calculan las métricas para un modelo de regresión lineal.
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMétricas en test:")
print(f"MSE  = {mse:.4f}")
print(f"RMSE = {rmse:.4f}")
print(f"MAE  = {mae:.4f}")
print(f"R²   = {r2:.4f}")

# Se generan 2 Gráficos:
# Dispersión + recta de regresión (modelo lineal)
plt.figure(figsize=(7,5))
plt.scatter(X_test, y_test, color="blue", alpha=0.6, label="Datos reales")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Recta de regresión")
plt.xlabel("Inversión en Redes (USD)")
plt.ylabel("Ventas (Miles de Unidades)")
plt.title("Regresión Lineal: Publicidad vs Ventas")
plt.legend()
plt.show()

# Residuos vs predicciones
residuos = y_test - y_pred
plt.figure(figsize=(7,5))
plt.scatter(y_pred, residuos, alpha=0.6, color="purple")
plt.axhline(y=0, color="red", linestyle="--")
plt.xlabel("Predicciones")
plt.ylabel("Residuos")
plt.title("Residuos vs Predicciones")
plt.show()
