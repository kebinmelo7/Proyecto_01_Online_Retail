import pandas as pd
import streamlit as st
import plotly.express as px


# Configuramos la página principal del dashboard
st.set_page_config(
    page_title="Online Retail | Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Un poco de estilo para que el dashboard tenga una apariencia más limpia
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f8fa;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    .dashboard-title {
        font-size: 2.7rem;
        font-weight: 700;
        color: #172033;
        margin-bottom: 0.2rem;
    }

    .dashboard-subtitle {
        font-size: 1.05rem;
        color: #687386;
        margin-bottom: 2rem;
    }

    .section-title {
        font-size: 1.45rem;
        font-weight: 650;
        color: #172033;
        margin-top: 1rem;
        margin-bottom: 0.2rem;
    }

    .section-description {
        color: #687386;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }

    .metric-card {
        background-color: white;
        border: 1px solid #e7eaf0;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }

    .metric-label {
        color: #687386;
        font-size: 0.9rem;
        margin-bottom: 5px;
    }

    .metric-value {
        color: #172033;
        font-size: 1.65rem;
        font-weight: 700;
    }

    .metric-description {
        color: #8a94a6;
        font-size: 0.78rem;
        margin-top: 4px;
    }

    .insight-box {
        background-color: white;
        border-left: 4px solid #315efb;
        border-radius: 10px;
        padding: 16px 18px;
        margin-top: 12px;
        margin-bottom: 18px;
    }

    .footer {
        text-align: center;
        color: #8a94a6;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #e7eaf0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


@st.cache_data
def cargar_datos():
    # Cargamos el archivo que ya pasó por el proceso de limpieza
    ruta = "data/processed/online_retail_clean.csv"

    datos = pd.read_csv(ruta)

    # La fecha se convierte para poder trabajar con meses y periodos
    datos["InvoiceDate"] = pd.to_datetime(datos["InvoiceDate"])

    # Conservamos los clientes como valores enteros, pero permitiendo datos vacíos
    datos["CustomerID"] = datos["CustomerID"].astype("Int64")

    return datos


df = cargar_datos()


# Encabezado principal
st.markdown(
    '<div class="dashboard-title">Online Retail Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="dashboard-subtitle">
    Dashboard de análisis comercial sobre ventas, productos,
    clientes y mercados del dataset Online Retail.
    </div>
    """,
    unsafe_allow_html=True
)


# Los filtros permiten explorar diferentes partes del dataset
st.sidebar.title("Filtros")

st.sidebar.write(
    "Utiliza estos filtros para explorar el comportamiento del negocio."
)


fecha_min = df["InvoiceDate"].min().date()
fecha_max = df["InvoiceDate"].max().date()


rango_fechas = st.sidebar.date_input(
    "Periodo",
    value=(fecha_min, fecha_max),
    min_value=fecha_min,
    max_value=fecha_max
)


paises = sorted(
    df["Country"]
    .dropna()
    .unique()
)


paises_seleccionados = st.sidebar.multiselect(
    "País",
    options=paises,
    default=paises
)


# Trabajamos sobre una copia para no modificar el dataset original
df_filtrado = df.copy()


if len(rango_fechas) == 2:

    fecha_inicio = pd.Timestamp(rango_fechas[0])

    # Sumamos un día para incluir todos los registros de la fecha final
    fecha_fin = (
        pd.Timestamp(rango_fechas[1])
        + pd.Timedelta(days=1)
    )

    df_filtrado = df_filtrado[
        (df_filtrado["InvoiceDate"] >= fecha_inicio)
        &
        (df_filtrado["InvoiceDate"] < fecha_fin)
    ]


if paises_seleccionados:

    df_filtrado = df_filtrado[
        df_filtrado["Country"].isin(
            paises_seleccionados
        )
    ]


# Calculamos los principales indicadores del periodo seleccionado
ventas_totales = df_filtrado["TotalPrice"].sum()
unidades_vendidas = df_filtrado["Quantity"].sum()
facturas = df_filtrado["InvoiceNo"].nunique()
clientes = df_filtrado["CustomerID"].nunique()


# Separamos las ventas positivas de las devoluciones
ventas_positivas = df_filtrado.loc[
    df_filtrado["TotalPrice"] > 0,
    "TotalPrice"
].sum()


devoluciones = abs(
    df_filtrado.loc[
        df_filtrado["TotalPrice"] < 0,
        "TotalPrice"
    ].sum()
)


if ventas_positivas > 0:

    porcentaje_devoluciones = (
        devoluciones / ventas_positivas
    ) * 100

else:

    porcentaje_devoluciones = 0


# Agrupamos por factura para conocer el valor promedio de cada compra
ventas_factura = (
    df_filtrado
    .groupby("InvoiceNo")["TotalPrice"]
    .sum()
)


ticket_promedio = ventas_factura.mean()


# También calculamos el ticket considerando únicamente facturas positivas
ventas_factura_positiva = ventas_factura[
    ventas_factura > 0
]


ticket_promedio_positivo = (
    ventas_factura_positiva.mean()
)


# Resumen principal
st.markdown(
    '<div class="section-title">Resumen del negocio</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-description">
    Principales indicadores del periodo y filtros seleccionados.
    </div>
    """,
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Ventas totales</div>
            <div class="metric-value">
                ${ventas_totales / 1_000_000:.2f} M
            </div>
            <div class="metric-description">
                Valor neto registrado
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Unidades</div>
            <div class="metric-value">
                {unidades_vendidas / 1_000_000:.2f} M
            </div>
            <div class="metric-description">
                Unidades registradas
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Facturas</div>
            <div class="metric-value">
                {facturas:,}
            </div>
            <div class="metric-description">
                Transacciones únicas
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Clientes</div>
            <div class="metric-value">
                {clientes:,}
            </div>
            <div class="metric-description">
                Clientes identificados
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# Indicadores complementarios
col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Ticket promedio",
        f"${ticket_promedio:,.2f}"
    )


with col2:

    st.metric(
        "Ticket promedio positivo",
        f"${ticket_promedio_positivo:,.2f}"
    )


with col3:

    st.metric(
        "Devoluciones sobre ventas",
        f"{porcentaje_devoluciones:.2f}%"
    )


# Mostramos las fechas que realmente están siendo utilizadas
st.markdown(
    '<div class="section-title">Periodo analizado</div>',
    unsafe_allow_html=True
)


if not df_filtrado.empty:

    st.write(
        f"Desde **{df_filtrado['InvoiceDate'].min():%d/%m/%Y %H:%M}** "
        f"hasta **{df_filtrado['InvoiceDate'].max():%d/%m/%Y %H:%M}**"
    )

else:

    st.warning(
        "No existen registros para los filtros seleccionados."
    )


# Organizamos el análisis en tres secciones principales
tab1, tab2, tab3 = st.tabs(
    [
        "Resumen",
        "Productos",
        "Clientes"
    ]
)


with tab1:

    st.markdown(
        '<div class="section-title">Evolución mensual de las ventas</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-description">
        Comportamiento de las ventas durante el periodo seleccionado.
        </div>
        """,
        unsafe_allow_html=True
    )


    # Agrupamos las ventas por mes para observar su evolución
    df_filtrado["Mes"] = (
        df_filtrado["InvoiceDate"]
        .dt.to_period("M")
        .astype(str)
    )


    ventas_mensuales = (
        df_filtrado
        .groupby("Mes")["TotalPrice"]
        .sum()
        .reset_index()
    )


    fig_mensual = px.line(
        ventas_mensuales,
        x="Mes",
        y="TotalPrice",
        markers=True,
        template="plotly_white"
    )


    fig_mensual.update_traces(
        line=dict(width=3)
    )


    fig_mensual.update_layout(
        xaxis_title="Mes",
        yaxis_title="Ventas",
        hovermode="x unified",
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )


    st.plotly_chart(
        fig_mensual,
        use_container_width=True
    )


    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            '<div class="section-title">Principales mercados</div>',
            unsafe_allow_html=True
        )


        # Tomamos los diez países con mayor valor de ventas
        ventas_pais = (
            df_filtrado
            .groupby("Country")["TotalPrice"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )


        ventas_pais = ventas_pais.sort_values(
            "TotalPrice"
        )


        fig_paises = px.bar(
            ventas_pais,
            x="TotalPrice",
            y="Country",
            orientation="h",
            template="plotly_white"
        )


        fig_paises.update_layout(
            xaxis_title="Ventas",
            yaxis_title="",
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            )
        )


        st.plotly_chart(
            fig_paises,
            use_container_width=True
        )


    with col2:

        st.markdown(
            '<div class="section-title">Lectura del mercado</div>',
            unsafe_allow_html=True
        )


        if not ventas_pais.empty:

            # Identificamos el mercado que genera más ingresos
            pais_principal = (
                ventas_pais
                .sort_values(
                    "TotalPrice",
                    ascending=False
                )
                .iloc[0]
            )


            st.markdown(
                f"""
                <div class="insight-box">
                    <strong>{pais_principal['Country']}</strong>
                    es el mercado con mayor valor de ventas
                    dentro del periodo seleccionado, con
                    <strong>
                    ${pais_principal['TotalPrice']:,.2f}
                    </strong>.
                    <br><br>
                    La distribución muestra una concentración
                    importante de las ventas en los principales
                    mercados.
                </div>
                """,
                unsafe_allow_html=True
            )


        st.markdown(
            '<div class="section-title">Devoluciones</div>',
            unsafe_allow_html=True
        )


        st.write(
            f"Ventas positivas: **${ventas_positivas:,.2f}**"
        )


        st.write(
            f"Valor de devoluciones: **${devoluciones:,.2f}**"
        )


        st.write(
            f"Impacto sobre ventas: "
            f"**{porcentaje_devoluciones:.2f}%**"
        )


with tab2:

    st.markdown(
        '<div class="section-title">Análisis de productos</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-description">
        Comparación de productos según ingresos y unidades.
        Los códigos POST, DOT y M corresponden a conceptos
        especiales y se excluyen del análisis comercial.
        </div>
        """,
        unsafe_allow_html=True
    )


    # Estos códigos corresponden a servicios, portes o ajustes,
    # por eso no los tenemos en cuenta al comparar productos comerciales
    codigos_especiales = [
        "POST",
        "DOT",
        "M"
    ]


    df_productos = df_filtrado[
        ~df_filtrado["StockCode"].isin(
            codigos_especiales
        )
    ]


    # Calculamos los productos que generan mayor valor de ventas
    ventas_producto = (
        df_productos
        .groupby(
            ["StockCode", "Description"],
            dropna=False
        )["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )


    ventas_producto["Producto"] = (
        ventas_producto["StockCode"].astype(str)
        + " | "
        + ventas_producto["Description"].fillna(
            "Sin descripción"
        )
    )


    fig_productos = px.bar(
        ventas_producto.sort_values("TotalPrice"),
        x="TotalPrice",
        y="Producto",
        orientation="h",
        template="plotly_white"
    )


    fig_productos.update_layout(
        xaxis_title="Ventas",
        yaxis_title="",
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )


    st.plotly_chart(
        fig_productos,
        use_container_width=True
    )


    st.markdown(
        '<div class="section-title">Productos con mayor volumen</div>',
        unsafe_allow_html=True
    )


    # Ahora miramos los productos desde el punto de vista de las unidades
    cantidad_producto = (
        df_productos
        .groupby(
            ["StockCode", "Description"],
            dropna=False
        )["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )


    cantidad_producto["Producto"] = (
        cantidad_producto["StockCode"].astype(str)
        + " | "
        + cantidad_producto["Description"].fillna(
            "Sin descripción"
        )
    )


    fig_cantidad = px.bar(
        cantidad_producto.sort_values("Quantity"),
        x="Quantity",
        y="Producto",
        orientation="h",
        template="plotly_white"
    )


    fig_cantidad.update_layout(
        xaxis_title="Unidades",
        yaxis_title="",
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )


    st.plotly_chart(
        fig_cantidad,
        use_container_width=True
    )


    st.markdown(
        """
        <div class="insight-box">
        <strong>Insight:</strong>
        el producto con mayor facturación no necesariamente
        es el producto con mayor volumen de unidades.
        Esta diferencia permite distinguir entre productos
        de alto valor y productos de alta rotación.
        </div>
        """,
        unsafe_allow_html=True
    )


with tab3:

    st.markdown(
        '<div class="section-title">Análisis de clientes</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-description">
        Identificación de los clientes con mayor valor de compras.
        </div>
        """,
        unsafe_allow_html=True
    )


    # Nos quedamos únicamente con los clientes que tienen identificación
    df_clientes = df_filtrado.dropna(
        subset=["CustomerID"]
    )


    # Sumamos las compras de cada cliente y ordenamos de mayor a menor
    ventas_cliente = (
        df_clientes
        .groupby("CustomerID")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )


    ventas_cliente["Cliente"] = (
        ventas_cliente["CustomerID"]
        .astype(str)
    )


    fig_clientes = px.bar(
        ventas_cliente.sort_values("TotalPrice"),
        x="TotalPrice",
        y="Cliente",
        orientation="h",
        template="plotly_white"
    )


    fig_clientes.update_layout(
        xaxis_title="Ventas",
        yaxis_title="Cliente",
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )


    st.plotly_chart(
        fig_clientes,
        use_container_width=True
    )


    # Calculamos cuánto generan todos los clientes identificados
    ventas_clientes_identificados = (
        df_clientes["TotalPrice"].sum()
    )


    # Sumamos las ventas de los diez clientes principales
    top_10_clientes = (
        ventas_cliente["TotalPrice"].sum()
    )


    if ventas_clientes_identificados != 0:

        # Medimos el peso que tienen los diez principales clientes
        participacion_top10 = (
            top_10_clientes
            / ventas_clientes_identificados
            * 100
        )

    else:

        participacion_top10 = 0


    st.markdown(
        '<div class="section-title">Concentración de ventas</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Ventas de clientes identificados",
            f"${ventas_clientes_identificados:,.2f}"
        )


    with col2:

        st.metric(
            "Ventas Top 10",
            f"${top_10_clientes:,.2f}"
        )


    with col3:

        st.metric(
            "Participación Top 10",
            f"{participacion_top10:.2f}%"
        )


    st.markdown(
        f"""
        <div class="insight-box">
        Los 10 principales clientes representan
        <strong>{participacion_top10:.2f}%</strong>
        de las ventas realizadas por clientes identificados.
        Esto permite observar el peso de los clientes de alto valor
        dentro del negocio.
        </div>
        """,
        unsafe_allow_html=True
    )


# Pie de página del dashboard
st.markdown(
    """
    <div class="footer">
        Online Retail Analysis · Proyecto de análisis de datos
        <br>
        Python · Pandas · Streamlit · Plotly
    </div>
    """,
    unsafe_allow_html=True
)