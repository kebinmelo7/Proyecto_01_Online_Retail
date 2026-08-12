# 📊 Online Retail Analytics Dashboard

### Análisis de ventas, productos, clientes y mercados mediante Python y Business Intelligence

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white">
</p>

---

## 🚀 Sobre el proyecto

**Online Retail Analytics Dashboard** es un proyecto de análisis de datos desarrollado en Python a partir del dataset **Online Retail**, compuesto por transacciones de un negocio de comercio electrónico.

El proyecto implementa un flujo completo de análisis de datos, desde la exploración y limpieza de la información hasta el análisis exploratorio, generación de visualizaciones e implementación de un dashboard interactivo mediante Streamlit.

El objetivo es transformar datos transaccionales en información útil para comprender el comportamiento de las ventas, identificar productos y clientes de alto valor, analizar los principales mercados y detectar patrones relevantes para la toma de decisiones.

---

## 🎯 Objetivos del análisis

El proyecto busca responder preguntas de negocio como:

- ¿Cómo evolucionan las ventas durante el periodo analizado?
- ¿Cuáles son los principales mercados?
- ¿Qué productos generan mayores ingresos?
- ¿Qué productos presentan mayor volumen de unidades vendidas?
- ¿Cuáles son los clientes de mayor valor?
- ¿Cuál es el valor promedio de las compras?
- ¿Qué impacto tienen las devoluciones?
- ¿Existe concentración de las ventas en determinados clientes?

---

## 🔎 Preguntas de negocio

El análisis se estructura alrededor de las siguientes preguntas:

1. ¿Cuánto dinero generan las ventas?
2. ¿Cómo evolucionan las ventas mes a mes?
3. ¿Qué países generan mayores ingresos?
4. ¿Cuáles son los productos más importantes comercialmente?
5. ¿Qué productos tienen mayor rotación?
6. ¿Cuáles son los clientes de mayor valor?
7. ¿Cuál es el valor promedio de una factura?
8. ¿Qué impacto tienen las devoluciones?
9. ¿Existe concentración de las ventas en determinados clientes?

---

# 📂 Dataset

El proyecto utiliza el dataset **Online Retail**, compuesto por registros de transacciones realizadas en un entorno de comercio electrónico.

### Principales variables

| Variable | Descripción |
|---|---|
| `InvoiceNo` | Número de factura |
| `StockCode` | Código del producto |
| `Description` | Descripción del producto |
| `Quantity` | Cantidad de unidades |
| `InvoiceDate` | Fecha y hora de la transacción |
| `UnitPrice` | Precio unitario |
| `CustomerID` | Identificador del cliente |
| `Country` | País del cliente |

---

# 🧹 Limpieza y preparación de datos

Antes de realizar el análisis se llevó a cabo una etapa de exploración y limpieza de los datos.

Se revisaron diferentes aspectos relacionados con la calidad de la información:

- Valores faltantes.
- Registros duplicados.
- Cantidades negativas.
- Precios unitarios iguales a cero.
- Códigos especiales.
- Fechas.
- Identificadores de clientes.
- Consistencia de los registros.

### Dataset original

El dataset inicialmente contenía:

- **541,909 registros**
- **8 columnas**
- **5,268 registros duplicados**
- **1,454 registros sin `Description`**
- **135,080 registros sin `CustomerID`**
- **10,624 registros con `Quantity` negativa**
- **2,515 registros con `UnitPrice` igual a 0**

Los registros duplicados fueron eliminados para evitar que transacciones repetidas afectaran los resultados del análisis.

### Resultado después de eliminar duplicados

```text
Registros iniciales:         541,909
Registros duplicados:          5,268
Registros después limpieza:  536,641
Duplicados restantes:              0           0