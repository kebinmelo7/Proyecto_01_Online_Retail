# 📊 Online Retail Analytics Dashboard

### Análisis de ventas, productos, clientes y mercados mediante Python y Business Intelligence

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white">
</p>

---

## 🚀 Sobre el proyecto

**Online Retail Analytics Dashboard** es un proyecto de análisis de datos desarrollado en Python a partir de un conjunto de datos de transacciones de comercio electrónico.

El proyecto cubre un flujo completo de trabajo, desde la exploración y limpieza de los datos hasta la transformación, análisis, generación de indicadores y construcción de un **dashboard interactivo desarrollado con Streamlit**.

El objetivo es transformar datos transaccionales en información útil para comprender el comportamiento de las ventas, identificar productos y clientes de alto valor y detectar patrones relevantes dentro del negocio.

---

## 🎯 Objetivos

El proyecto busca responder preguntas como:

- ¿Cómo evolucionaron las ventas durante el periodo analizado?
- ¿Cuáles son los principales mercados?
- ¿Qué productos generan mayores ingresos?
- ¿Qué productos tienen mayor volumen de unidades?
- ¿Cuáles son los clientes de mayor valor?
- ¿Cuál es el ticket promedio?
- ¿Qué impacto tienen las devoluciones?
- ¿Qué tan concentradas están las ventas en los principales clientes?

---

## 🔎 Preguntas de análisis

Durante el desarrollo del proyecto se buscó responder:

- ¿Cuánto dinero generan las ventas?
- ¿Cómo evolucionan las ventas mes a mes?
- ¿Qué países generan mayores ingresos?
- ¿Cuáles son los productos más importantes comercialmente?
- ¿Qué productos tienen mayor rotación?
- ¿Cuáles son los clientes de mayor valor?
- ¿Cuál es el valor promedio de una factura?
- ¿Qué impacto tienen las devoluciones?
- ¿Existe concentración de las ventas en determinados clientes?

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

## Dataset original

El dataset inicialmente contenía:

- **541,909 registros**
- **8 columnas**
- **5,268 registros duplicados**
- **1,454 registros sin Description**
- **135,080 registros sin CustomerID**
- **10,624 registros con Quantity negativa**
- **2,515 registros con UnitPrice igual a 0**

Los registros duplicados fueron eliminados para evitar que transacciones repetidas afectaran los resultados del análisis.

## Resultado después de eliminar duplicados

```text
Registros iniciales:        541,909
Registros duplicados:         5,268
Registros después limpieza: 536,641
Duplicados restantes:              0