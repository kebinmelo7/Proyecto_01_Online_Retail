import pandas as pd


# Cargar datos

# Trabajamos sobre una copia del dataset original para mantener intacta la fuente.

ruta = "data/raw/Online Retail.xlsx"
df = pd.read_excel(ruta)

print("Dataset cargado correctamente")
print(f"Registros iniciales: {len(df):,}")

# Duplicados

# Eliminamos registros completamente repetidos para evitar contar
# la misma información más de una vez.

duplicados = df.duplicated().sum()

print(f"\nDuplicados encontrados: {duplicados:,}")

df = df.drop_duplicates()

print(f"Registros después de eliminar duplicados: {len(df):,}")

# Estado después de la limpieza

# Comprobamos nuevamente los principales valores faltantes.

print("\nValores faltantes después de eliminar duplicados:")
print(df.isnull().sum())

# Valor de la transacción

# Calculamos el valor de cada línea usando la cantidad y el precio unitario.

df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

print("\nTotalPrice creado correctamente")
print(df[["Quantity", "UnitPrice", "TotalPrice"]].head())

# Guardar datos procesados

# Guardamos el resultado para utilizarlo posteriormente en el análisis.

ruta_salida = "data/processed/online_retail_clean.csv"

df.to_csv(ruta_salida, index=False)

print("\nDataset procesado guardado correctamente")
print(f"Ubicación: {ruta_salida}")
print(f"Registros finales: {len(df):,}")
print(f"Columnas finales: {df.shape[1]}")

# Verificación final

# Comprobamos que los datos procesados quedaron correctamente.

print("\nVerificación final:")
print(f"Registros: {len(df):,}")
print(f"Columnas: {df.shape[1]}")
print(f"Duplicados: {df.duplicated().sum():,}")
print(f"Valores faltantes: {df.isnull().sum().sum():,}")