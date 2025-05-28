import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv("vehicles_us.csv")

# Encabezado
st.title("Explorador de Vehículos Usados en EE.UU.")
st.write("Esta app permite visualizar datos con Plotly y generar un histograma al hacer clic en un botón.")

# Casilla para mostrar los datos
if st.checkbox("Mostrar datos"):
    st.subheader("Vista previa de los datos")
    st.write(df.head())

# Botón para mostrar histograma
if st.button("Generar histograma de precios"):
    st.subheader("Histograma de Precios")
    fig_hist = px.histogram(
        df,
        x="price",
        nbins=30,
        title="Distribución de Precios",
        labels={"price": "Precio"}
    )
    st.plotly_chart(fig_hist)

# Gráfico de dispersión fijo
st.subheader("Gráfico de Dispersión: Precio vs Año del Modelo")
fig_scatter = px.scatter(
    df,
    x="model_year",
    y="price",
    title="Relación entre Año del Modelo y Precio",
    labels={"model_year": "Año del Modelo", "price": "Precio"},
    opacity=0.5
)
st.plotly_chart(fig_scatter)
