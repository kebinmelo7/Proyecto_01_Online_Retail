import pandas as pd
import matplotlib.pyplot as plt


# Cargar datos

# Trabajamos con el archivo que ya pasó por el proceso de limpieza.

ruta = "data/processed/online_retail_clean.csv"
df = pd.read_csv(ruta)

print("Dataset cargado correctamente")
print(f"Registros: {len(df):,}")
print(f"Columnas: {df.shape[1]}")


# Resumen general

# Revisamos las principales cifras del dataset para tener una primera visión del negocio.

print("\nResumen general:")
print(f"Ventas totales: {df['TotalPrice'].sum():,.2f}")
print(f"Unidades vendidas: {df['Quantity'].sum():,}")
print(f"Facturas: {df['InvoiceNo'].nunique():,}")
print(f"Productos: {df['StockCode'].nunique():,}")
print(f"Clientes identificados: {df['CustomerID'].nunique():,}")
print(f"Países: {df['Country'].nunique():,}")


# Fechas

# Convertimos la fecha para poder analizar la evolución de las ventas.

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nPeriodo analizado:")
print(f"Inicio: {df['InvoiceDate'].min()}")
print(f"Fin: {df['InvoiceDate'].max()}")


# Ventas por mes

# Agrupamos las ventas para observar cómo evolucionó el negocio durante el periodo.

df["Mes"] = df["InvoiceDate"].dt.to_period("M")

ventas_mensuales = (
    df.groupby("Mes")["TotalPrice"]
    .sum()
    .reset_index()
)

ventas_mensuales["Mes"] = ventas_mensuales["Mes"].astype(str)

print("\nVentas por mes:")
print(ventas_mensuales)


# Evolución de las ventas

# Visualizamos el comportamiento de las ventas durante el periodo analizado.

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
plt.grid(True)
plt.tight_layout()

plt.show()


# Ventas por país

# Comparamos cuánto dinero genera cada país dentro del dataset.

ventas_pais = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

print("\nVentas por país:")
print(ventas_pais.head(15))


# Principales mercados

# Mostramos los países que concentran el mayor valor de ventas.

top_paises = ventas_pais.head(10)

plt.figure(figsize=(12, 6))

plt.bar(
    top_paises["Country"],
    top_paises["TotalPrice"]
)

plt.title("Top 10 países por ventas")
plt.xlabel("País")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# Productos comerciales

# Excluimos códigos especiales para analizar únicamente los productos vendidos.

codigos_especiales = ["POST", "DOT", "M"]

df_productos = df[
    ~df["StockCode"].isin(codigos_especiales)
]


# Productos con mayor valor de ventas

# Identificamos los productos que generan mayor valor económico.

ventas_producto_real = (
    df_productos.groupby(["StockCode", "Description"])["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

print("\nTop 10 productos comerciales:")

for _, producto in ventas_producto_real.head(10).iterrows():
    print(
        f"{producto['StockCode']} | "
        f"{producto['Description']} | "
        f"${producto['TotalPrice']:,.2f}"
    )


# Productos más vendidos por cantidad

# Identificamos los productos que concentran el mayor número de unidades vendidas.

cantidad_producto = (
    df_productos.groupby(["StockCode", "Description"])["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

print("\nTop 10 productos por unidades vendidas:")

for _, producto in cantidad_producto.head(10).iterrows():
    print(
        f"{producto['StockCode']} | "
        f"{producto['Description']} | "
        f"{producto['Quantity']:,} unidades"
    )


# Comparación de productos

# Combinamos unidades vendidas e ingresos para comparar el comportamiento de los productos.

comparacion_productos = (
    df_productos.groupby(["StockCode", "Description"])
    .agg(
        Unidades=("Quantity", "sum"),
        Ventas=("TotalPrice", "sum")
    )
    .sort_values("Ventas", ascending=False)
    .reset_index()
)

print("\nComparación de productos:")

for _, producto in comparacion_productos.head(10).iterrows():
    print(
        f"{producto['StockCode']} | "
        f"{producto['Description']} | "
        f"{producto['Unidades']:,} unidades | "
        f"${producto['Ventas']:,.2f}"
    )


# Ticket promedio

# Calculamos el valor promedio de las facturas para conocer el tamaño habitual de una compra.

ventas_factura = (
    df.groupby("InvoiceNo")["TotalPrice"]
    .sum()
)

ticket_promedio = ventas_factura.mean()

print("\nTicket promedio:")
print(f"${ticket_promedio:,.2f}")


# Ticket promedio de ventas positivas

# Comparamos el ticket general con las facturas que representan ventas positivas.

ventas_factura_positiva = ventas_factura[
    ventas_factura > 0
]

ticket_promedio_positivo = ventas_factura_positiva.mean()

print("\nTicket promedio de ventas positivas:")
print(f"${ticket_promedio_positivo:,.2f}")


# Impacto de las devoluciones

# Medimos cuánto representan las transacciones negativas frente al valor de las ventas positivas.

valor_ventas = df.loc[
    df["TotalPrice"] > 0,
    "TotalPrice"
].sum()

valor_devoluciones = abs(
    df.loc[
        df["TotalPrice"] < 0,
        "TotalPrice"
    ].sum()
)

porcentaje_devoluciones = (
    valor_devoluciones / valor_ventas * 100
)

print("\nImpacto de las devoluciones:")
print(f"Ventas positivas: ${valor_ventas:,.2f}")
print(f"Valor de devoluciones: ${valor_devoluciones:,.2f}")
print(f"Devoluciones sobre ventas: {porcentaje_devoluciones:.2f}%")

# Ventas por cliente

# Identificamos los clientes que generan mayor valor de ventas.

ventas_cliente = (
    df.dropna(subset=["CustomerID"])
    .groupby("CustomerID")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

print("\nTop 10 clientes por ventas:")

for _, cliente in ventas_cliente.head(10).iterrows():
    print(
        f"Cliente {cliente['CustomerID']:.0f} | "
        f"${cliente['TotalPrice']:,.2f}"
    )

# Concentración de ventas por cliente

# Medimos cuánto representan los principales clientes dentro de las ventas identificadas.

ventas_clientes_identificados = (
    df.dropna(subset=["CustomerID"])
    .groupby("CustomerID")["TotalPrice"]
    .sum()
)

top_10_clientes = (
    ventas_clientes_identificados
    .sort_values(ascending=False)
    .head(10)
    .sum()
)

total_ventas_clientes = ventas_clientes_identificados.sum()

porcentaje_top_10 = (
    top_10_clientes / total_ventas_clientes * 100
)

print("\nConcentración de ventas:")
print(f"Ventas de clientes identificados: ${total_ventas_clientes:,.2f}")
print(f"Ventas de los 10 principales: ${top_10_clientes:,.2f}")
print(f"Participación del Top 10: {porcentaje_top_10:.2f}%")