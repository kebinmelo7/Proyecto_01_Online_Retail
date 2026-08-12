# 📊 Online Retail Analytics Dashboard

### Transformando datos transaccionales en decisiones de negocio

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Git-GitHub-F05032?style=for-the-badge&logo=git&logoColor=white">
</p>

<p align="center">
  <a href="https://proyecto01onlineretail-ka2sk4agcqxz762kkbeflu.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_VER_DASHBOARD_EN_VIVO-Streamlit-FF4B4B?style=for-the-badge">
  </a>
</p>

---

## 🚀 Dashboard en vivo

### 👉 [Abrir Online Retail Analytics Dashboard](https://proyecto01onlineretail-ka2sk4agcqxz762kkbeflu.streamlit.app/)

Explora directamente el dashboard interactivo desarrollado con **Python, Pandas, Plotly y Streamlit**.

El dashboard permite analizar:

- 💰 Ventas
- 📦 Productos
- 👥 Clientes
- 🌎 Mercados
- 🔄 Devoluciones
- 📈 Evolución temporal
- 🎯 Concentración de ventas

---

# 📌 Sobre el proyecto

**Online Retail Analytics Dashboard** es un proyecto de análisis de datos desarrollado en Python a partir del dataset **Online Retail**, compuesto por transacciones de comercio electrónico.

El proyecto fue diseñado para simular un escenario real de análisis comercial, donde los datos transaccionales deben convertirse en información útil para comprender el comportamiento del negocio.

El flujo de trabajo abarca desde la **exploración y limpieza de datos** hasta el **análisis exploratorio, generación de indicadores, visualización y construcción de un dashboard interactivo**.

> **Objetivo:** transformar datos transaccionales en insights accionables que permitan comprender ventas, productos, clientes y mercados.

---

# 🎯 Problema de negocio

Los datos transaccionales por sí solos no permiten tomar decisiones fácilmente.

Por esta razón, este proyecto busca responder preguntas relevantes para un negocio de comercio electrónico:

- ¿Cómo evolucionan las ventas a través del tiempo?
- ¿Qué mercados generan mayor facturación?
- ¿Qué productos generan mayores ingresos?
- ¿Qué productos presentan mayor volumen de unidades?
- ¿Quiénes son los clientes de mayor valor?
- ¿Cuál es el ticket promedio?
- ¿Qué impacto tienen las devoluciones?
- ¿Existe concentración de ingresos en determinados clientes?
- ¿Qué diferencia existe entre productos de alto valor y productos de alta rotación?

---

# 📊 Principales indicadores

El dashboard permite consultar dinámicamente indicadores como:

| KPI | Descripción |
|---|---|
| 💰 Ventas totales | Valor neto de las transacciones |
| 📦 Unidades | Total de unidades registradas |
| 🧾 Facturas | Número de transacciones únicas |
| 👥 Clientes | Clientes identificados |
| 🎟️ Ticket promedio | Valor promedio por factura |
| 💵 Ticket positivo | Promedio considerando únicamente facturas positivas |
| 🔄 Devoluciones | Impacto de devoluciones sobre las ventas |

Los indicadores se recalculan automáticamente según los filtros seleccionados.

---

# 🔎 Análisis realizado

## 💰 Análisis de ventas

Se estudió la evolución temporal de las ventas para identificar cambios en el comportamiento comercial.

Se analizaron:

- Ventas totales
- Evolución mensual
- Número de facturas
- Unidades vendidas
- Ticket promedio
- Devoluciones

---

## 🌎 Análisis de mercados

Se analizaron los ingresos generados por país para identificar los principales mercados.

El dashboard permite observar:

- Países con mayor facturación
- Concentración de ventas
- Distribución geográfica del negocio
- Diferencias entre mercados

---

## 📦 Análisis de productos

Los productos fueron analizados desde dos perspectivas diferentes:

### Ingresos

¿Qué productos generan mayor facturación?

### Volumen

¿Qué productos presentan mayor cantidad de unidades vendidas?

Esta comparación permite diferenciar entre:

> **Productos de alto valor comercial**

y

> **Productos de alta rotación**

Además, se excluyeron códigos especiales como:

```text
POST
DOT
M