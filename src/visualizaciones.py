import pandas as pd
import matplotlib.pyplot as plt


# Cargar datos

# Trabajamos con el dataset limpio para construir las visualizaciones.

ruta = "data/processed/online_retail_clean.csv"
df = pd.read_csv(ruta)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


# Ventas por mes

# Agrupamos las ventas para observar su evolución durante el periodo analizado.

df["Mes"] = df["InvoiceDate"].dt.to_period("M")

ventas_mensuales = (
    df.groupby("Mes")["TotalPrice"]
    .sum()
    .reset_index()
)

ventas_mensuales["Mes"] = ventas_mensuales["Mes"].astype(str)


# Gráfico de ventas mensuales

# Representamos la evolución de las ventas a lo largo del tiempo.

plt.figure(figsize=(12, 6))

plt.plot(
    ventas_mensuales["Mes"],
    ventas_mensuales["TotalPrice"],
    marker="o"
)

plt.title("Evolución mensual de las ventas")
plt.xlabel("Mes")
plt.ylabel("Ventas")

plt.xticks(rotation=45)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()

# Ventas por país

# Identificamos los mercados que generan mayor valor de ventas.

ventas_pais = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)


# Gráfico de ventas por país

# Comparamos visualmente los principales mercados del negocio.

plt.figure(figsize=(10, 6))

plt.barh(
    ventas_pais.index,
    ventas_pais.values
)

plt.title("Top 10 países por ventas")
plt.xlabel("Ventas")
plt.ylabel("País")

plt.tight_layout()

plt.show()

# Ventas por producto

# Excluimos códigos especiales para mostrar únicamente productos comerciales.

codigos_especiales = ["POST", "DOT", "M"]

df_productos = df[
    ~df["StockCode"].isin(codigos_especiales)
]

ventas_producto = (
    df_productos
    .groupby(["StockCode", "Description"])["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)


# Gráfico de productos

# Mostramos los productos comerciales que generan mayor valor de ventas.

nombres_productos = ventas_producto.index.get_level_values("Description")

plt.figure(figsize=(12, 7))

plt.barh(
    nombres_productos,
    ventas_producto.values
)

plt.title("Top 10 productos por ventas")
plt.xlabel("Ventas")
plt.ylabel("Producto")

plt.tight_layout()

plt.show()

# Ventas por cliente

# Identificamos los clientes que generan mayor valor de ventas.

ventas_cliente = (
    df.dropna(subset=["CustomerID"])
    .groupby("CustomerID")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)


# Gráfico de clientes

# Mostramos los clientes con mayor valor de compras.

clientes = ventas_cliente.index.astype(str)

plt.figure(figsize=(10, 6))

plt.barh(
    clientes,
    ventas_cliente.values
)

plt.title("Top 10 clientes por ventas")
plt.xlabel("Ventas")
plt.ylabel("Cliente")

plt.tight_layout()

plt.show()