import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Configurar el título de la aplicación Streamlit
st.header('Visualización de Datos de Anuncios de Venta de Coches')

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

# Lógica a ejecutar cuando se hace clic en el botón
if scatter_button:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    scatter_fig = go.Figure(data=go.Scatter(
        x=car_data['cylinders'],
        y=car_data['price'],
        mode='markers',
        marker=dict(size=5, color='rgba(152, 0, 0, .8)',
                    line=dict(width=1, color='DarkSlateGrey'))
    ))

    # Añadir un título y etiquetas a los ejes
    scatter_fig.update_layout(
        title='Gráfico de Dispersión: Año del carro vs Precio',
        xaxis_title='Año de fabricación',
        yaxis_title='Precio'
    )
