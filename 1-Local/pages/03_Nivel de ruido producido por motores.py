import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

sound_quality = pd.read_parquet('Datasets/3-Normalizados/sound_quality.parquet')

# Título de la página
st.title("Niveles de ruido producido por motores en New York City")

# Separador visual
st.markdown('***')

# Realizamos el conteo de frecuencia
counts = sound_quality['Engine Sound'].value_counts()

# Definimos el orden de las categorías
categories_order = ['Low', 'Medium', 'High']

# Reordenamos los resultados de acuerdo al orden definido
counts = counts.reindex(categories_order)

# Creamos el gráfico de barras con Plotly
fig = px.bar(x=counts.index, y=counts.values, color=counts.index,
             labels={'x': 'Nivel de Sonido', 'y': 'Frecuencia'},
             title='Distribución de Niveles de Sonido',
             template='plotly_white')

# Añadimos etiquetas de conteo encima de las barras con fuente en negrita y flecha
for i, count in enumerate(counts):
    fig.add_annotation(
        x=counts.index[i],
        y=count + 1,
        text=str(count),
        showarrow=True,
        arrowhead=5,
        ax=0,
        ay=-40,
        font=dict(size=12, color='black', family='Arial')  # Configuramos la fuente en negrita
    )

# Añadimos bordes a las columnas
fig.update_traces(marker_line=dict(color='black', width=1.5))

# Ajustamos el diseño del gráfico
fig.update_layout(
    xaxis_title='Nivel de Sonido',
    yaxis_title='Frecuencia',
)

# Mostramos el gráfico con Streamlit
st.plotly_chart(fig)

st.write("""
**Referencia:** _Low_ = 10 a 49 db, _Medium_ = 50 a 74 db, _High_ = 75 a 120 db.
""")


# Título de la página
st.title("Concentración sonora en New York City")

# Separador visual
st.markdown('***')

# Cargamos el GeoJSON
with open('Datasets/4-Extras/NYC Taxi Zones.geojson') as fd:
    geojson = json.load(fd)

# Creamos el mapa con Plotly
fig = go.Figure(go.Scattermapbox(
    mode='markers',
    lon=sound_quality['Longitude'],
    lat=sound_quality['Latitude'],
    marker=dict(
        size=10,
        color='red',
    ),
    text=sound_quality['Engine Sound'],
))

# Configuramos diseño del mapa
fig.update_layout(
    mapbox=dict(
        style="carto-positron",
        zoom=10,
        center=dict(lat=sound_quality['Latitude'].mean(), lon=sound_quality['Longitude'].mean()),
    ),
    height=600,
    title='Mapa de Sonidos de Motores en Nueva York',
    paper_bgcolor='#FFFFFF',  # Color de fondo elegante (azul oscuro)
    font_color='white',  # Color del texto en blanco
)

# Mostramos el mapa con Streamlit
st.plotly_chart(fig)

# Título de la página
st.title("Frecuencia de sonidos registrados por hora del día")

# Separador visual
st.markdown('***')

# Crear un DataFrame para contar la frecuencia por hora
hour_counts = sound_quality['Hour'].value_counts().sort_index().reset_index()
hour_counts.columns = ['Hour', 'Frequency']

# Crear el gráfico de barras con Plotly Express
fig = px.bar(hour_counts, x='Hour', y='Frequency', 
             labels={'Frequency': 'Frecuencia', 'Hour': 'Hora del Día'},
             title='Frecuencia de Sonidos Registrados por Hora del Día',
             template='plotly_white')

# Añadir bordes a las barras
fig.update_traces(marker_line_color='black', marker_line_width=1.5)

# Añadir etiquetas encima de las barras con flecha
for i, row in hour_counts.iterrows():
    fig.add_annotation(
        x=row['Hour'],
        y=row['Frequency'],
        text=str(row['Frequency']),
        showarrow=True,
        arrowhead=5,
        ax=0,
        ay=-30
    )

# Configurar el diseño del gráfico
fig.update_layout(
    xaxis=dict(tickmode='array', tickvals=list(range(24)), ticktext=[f"{i:02}:00" for i in range(24)]),
)

# Mostrar el gráfico con Streamlit
st.plotly_chart(fig)