
# MODULO 06 - EJERCICIO 05-B
# ALEXIS YURI M.


# Se importan las librerías
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, roc_curve, auc, precision_score, recall_score, accuracy_score


# MODELO REGRESION LINEAL (Consumo de Energía).

# Se carga el dataset.
reg_df = pd.read_csv("regresion_dataset_consumo_energia.csv")

# Se definen variable caracteristica (X_reg) y objetivo (y_reg).
X_reg = reg_df.drop("Consumo_kWh", axis=1)
y_reg = reg_df["Consumo_kWh"]

# Se realiza preprocesamiento OneHot para la variable categórica "Tipo_dia".
preprocessor_reg = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop="first"), ["Tipo_dia"])
    ],
    remainder="passthrough"
)

# Se realiza división del dataset entre entrenamiento y test.
X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Se entrena el modelo de regresion lineal.
reg_model = Pipeline(steps=[
    ("preprocessor", preprocessor_reg),
    ("regressor", LinearRegression())
])

reg_model.fit(X_train, y_train)


# Se realizan predicciones usando el modelo de regresión.
y_pred_reg = reg_model.predict(X_test)

# Se calculan las métricas para un modelo de regresión lineal.
mae = mean_absolute_error(y_test, y_pred_reg)
mse = mean_squared_error(y_test, y_pred_reg)
rmse = mean_squared_error(y_test, y_pred_reg, squared=False)
r2 = r2_score(y_test, y_pred_reg)

print("=== METRICAS REGRESION ===")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")

# Se despliega Gráfico de datos Reales vs Predicciónes
plt.scatter(y_test, y_pred_reg, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2)
plt.xlabel("Valores Reales")
plt.ylabel("Predicciones")
plt.title("Regresión Lineal - Consumo de Energía")
plt.show()




# MODELO CLASIFICACION (Fraude Tarjetas).

# Se carga el dataset.
clf_df = pd.read_csv("clasificacion_dataset_fraude_tarjetas.csv", encoding="latin-1")

# Se definen variable caracteristica (X_clf) y objetivo (y_clf).
X_clf = clf_df.drop("Fraude", axis=1)
y_clf = clf_df["Fraude"]

# Se separan columnas categóricas y numéricas.
cat_cols = X_clf.select_dtypes(include=["object"]).columns.tolist()
num_cols = X_clf.select_dtypes(exclude=["object"]).columns.tolist()

# # Se realizan preprocesamientos OneHot y StandardScaler.
preprocessor_clf = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
    ]
)

# Se realiza división del dataset entre entrenamiento y test.
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_clf, y_clf, test_size=0.3, random_state=42, stratify=y_clf)

# Se entrena el modelo de clasificación.
clf_model = Pipeline(steps=[
    ("preprocessor", preprocessor_clf),
    ("classifier", KNeighborsClassifier(n_neighbors=7))
])

clf_model.fit(X_train_c, y_train_c)
y_pred_clf = clf_model.predict(X_test_c)
y_proba_clf = clf_model.predict_proba(X_test_c)[:, 1]

# Se calculan las métricas para un modelo de clasificación.
accuracy = accuracy_score(y_test_c, y_pred_clf)
precision = precision_score(y_test_c, y_pred_clf)
recall = recall_score(y_test_c, y_pred_clf)

tn, fp, fn, tp = confusion_matrix(y_test_c, y_pred_clf).ravel()
specificity = tn / (tn + fp)

fpr, tpr, thresholds = roc_curve(y_test_c, y_proba_clf)
roc_auc = auc(fpr, tpr)

print("\n=== METRICAS CLASIFICACION ===")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precisión: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"Especificidad: {specificity:.4f}")
print(f"AUC: {roc_auc:.4f}")
print("\n")

# 7. Matriz de confusión
ConfusionMatrixDisplay.from_estimator(clf_model, X_test_c, y_test_c, cmap="Blues")
plt.title("Matriz de Confusión - Fraude")
plt.show()

# 8. Curva ROC
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0,1], [0,1], "r--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Curva ROC - Fraude")
plt.legend()
plt.show()