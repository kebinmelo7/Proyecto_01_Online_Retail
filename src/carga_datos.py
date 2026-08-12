import pandas as pd


# Cargar datos

# Se importa el dataset original para comenzar el análisis.

ruta = "data/raw/Online Retail.xlsx"
df = pd.read_excel(ruta)

print("Dataset cargado correctamente")
print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")


# Exploración inicial

# Revisamos la estructura, columnas y tipos de datos.

print("\nPrimeras 5 filas:")
print(df.head())

print("\nTipos de datos:")
print(df.dtypes)


# Valores faltantes

# Identificamos qué datos faltan y cuánto representan.

print("\nValores faltantes:")
print(df.isnull().sum())

print("\nPorcentaje de valores faltantes:")
print((df.isnull().sum() / len(df) * 100).round(2))


# CustomerID

# Revisamos los registros que no tienen identificador de cliente.

print("\nRegistros sin CustomerID:")
print(df[df["CustomerID"].isnull()].head())

print("\nEstadísticas de registros sin CustomerID:")
print(
    df[df["CustomerID"].isnull()][["Quantity", "UnitPrice"]].describe()
)


# Cantidades negativas

# Analizamos posibles devoluciones, cancelaciones o ajustes.

print("\nRegistros con Quantity negativa:")
print(df[df["Quantity"] < 0].head())

print("\nCantidad de registros con Quantity negativa:")
print((df["Quantity"] < 0).sum())

print("\nFacturas con Quantity negativa:")
print(
    df[df["Quantity"] < 0]["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
    .value_counts()
)

print("\nFacturas que empiezan por C:")
print(
    df["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
    .value_counts()
)

print("\nRegistros con Quantity negativa y sin C en InvoiceNo:")
print(
    df[
        (df["Quantity"] < 0) &
        (~df["InvoiceNo"].astype(str).str.startswith("C"))
    ].head(10)
)

print("\nEstadísticas de estos registros:")
print(
    df[
        (df["Quantity"] < 0) &
        (~df["InvoiceNo"].astype(str).str.startswith("C"))
    ][["Quantity", "UnitPrice"]].describe()
)


# Precios en cero

# Revisamos registros que no tienen un precio asociado.

print("\nRegistros con UnitPrice igual a 0:")
print((df["UnitPrice"] == 0).sum())

print("\nRegistros con UnitPrice = 0:")
print(
    df[df["UnitPrice"] == 0][
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "CustomerID",
            "Country"
        ]
    ].head(10)
)

print("\nRegistros con UnitPrice = 0 según Quantity:")
print(
    df[df["UnitPrice"] == 0]["Quantity"]
    .apply(lambda x: "Negativa" if x < 0 else "Positiva")
    .value_counts()
)


# StockCode

# Exploramos los códigos de productos y posibles códigos especiales.

print("\nStockCode más frecuentes:")
print(df["StockCode"].value_counts().head(20))

print("\nTipos de StockCode:")
print(
    df["StockCode"]
    .astype(str)
    .str.len()
    .value_counts()
    .sort_index()
)

print("\nStockCode que contienen letras:")
print(
    df[
        df["StockCode"]
        .astype(str)
        .str.contains(r"[A-Za-z]", regex=True)
    ]["StockCode"]
    .value_counts()
    .head(30)
)


# Códigos especiales

# Revisamos algunos códigos alfanuméricos para entender qué representan.

print("\nRegistros POST:")
print(
    df[df["StockCode"] == "POST"][
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "CustomerID",
            "Country"
        ]
    ].head(10)
)

print("\nRegistros DOT:")
print(
    df[df["StockCode"] == "DOT"][
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "CustomerID",
            "Country"
        ]
    ].head(10)
)

print("\nRegistros M:")
print(
    df[df["StockCode"] == "M"][
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "CustomerID",
            "Country"
        ]
    ].head(10)
)


# Descripción de códigos especiales

# Revisamos qué información tienen asociados algunos códigos para entender su función.

print("\nDescripción de códigos especiales:")
print(
    df[df["StockCode"].isin(["POST", "DOT", "M"])]
    [["StockCode", "Description"]]
    .drop_duplicates()
    .sort_values("StockCode")
)


# Facturas

# Revisamos la cantidad y distribución de los identificadores de factura.

print("\nCantidad de facturas únicas:")
print(df["InvoiceNo"].nunique())


# Distribución de facturas

# Revisamos cuántos registros contiene cada factura.

print("\nRegistros por factura:")
print(df["InvoiceNo"].value_counts().head(10))


# Productos

# Revisamos cuántos códigos de producto diferentes aparecen en los datos.

print("\nCantidad de StockCode únicos:")
print(df["StockCode"].nunique())


# Clientes

# Revisamos cuántos clientes diferentes están identificados en los datos.

print("\nCantidad de clientes únicos:")
print(df["CustomerID"].nunique())


# Periodo de ventas

# Revisamos las fechas mínima y máxima disponibles en el dataset.

print("\nPeriodo de los datos:")
print(f"Fecha inicial: {df['InvoiceDate'].min()}")
print(f"Fecha final: {df['InvoiceDate'].max()}")


# Países

# Revisamos los países presentes y la cantidad de registros por país.

print("\nCantidad de países:")
print(df["Country"].nunique())

print("\nRegistros por país:")
print(df["Country"].value_counts().head(15))


# Resumen de calidad

# Reunimos los principales problemas encontrados antes de limpiar los datos.

print("\nResumen de calidad de los datos:")

print(f"Registros totales: {len(df):,}")
print(f"Valores faltantes en Description: {df['Description'].isnull().sum():,}")
print(f"Valores faltantes en CustomerID: {df['CustomerID'].isnull().sum():,}")
print(f"Quantities negativas: {(df['Quantity'] < 0).sum():,}")
print(f"UnitPrice iguales a 0: {(df['UnitPrice'] == 0).sum():,}")
print(f"Facturas únicas: {df['InvoiceNo'].nunique():,}")
print(f"Productos/códigos únicos: {df['StockCode'].nunique():,}")
print(f"Clientes identificados: {df['CustomerID'].nunique():,}")
print(f"Países: {df['Country'].nunique():,}")


# Descripciones faltantes

# Revisamos si los registros sin descripción contienen información útil.

print("\nRegistros sin Description:")
print(
    df[df["Description"].isnull()][
        [
            "InvoiceNo",
            "StockCode",
            "Quantity",
            "UnitPrice",
            "CustomerID",
            "Country"
        ]
    ].head(10)
)


# Calidad de registros sin Description

# Comprobamos si tienen cantidad y precio disponibles para el análisis.

print("\nValores faltantes en registros sin Description:")
print(
    df[df["Description"].isnull()][
        ["Quantity", "UnitPrice", "CustomerID"]
    ].isnull().sum()
)


# Valor de las ventas

# Calculamos el valor de cada línea para conocer su impacto económico.

df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

print("\nValor total de las transacciones:")
print(df["TotalPrice"].sum())

print("\nValor asociado a cantidades negativas:")
print(df.loc[df["Quantity"] < 0, "TotalPrice"].sum())


# Duplicados

# Revisamos si existen registros completamente repetidos en el dataset.

print("\nRegistros duplicados:")
print(df.duplicated().sum())

# Impacto de los duplicados
# Revisamos qué porcentaje del dataset representan los registros repetidos.

duplicados = df.duplicated().sum()
porcentaje_duplicados = (duplicados / len(df)) * 100

print("\nImpacto de los duplicados:")
print(f"Registros duplicados: {duplicados:,}")
print(f"Porcentaje del dataset: {porcentaje_duplicados:.2f}%")