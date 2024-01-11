import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

air_quality = pd.read_parquet('Datasets/3-Normalizados/air_quality.parquet')

# Título de la página
st.title("Polución por Borough en New York City")

# Separador visual
st.markdown('***')

# Creamos el DataFrame para el total general por 'Borough'
total_values = air_quality.groupby('Borough')['Data Value'].sum().reset_index()

# Redondeamos los valores a 2 decimales
total_values['Data Value'] = total_values['Data Value'].round(2)

# Creamos el gráfico de barras con Plotly
fig = px.bar(air_quality, x='Borough', y='Data Value', color='Pollutant',
             labels={'Data Value': 'Niveles de Contaminantes (mcg/m3 or ppb)'},
             title='Niveles de Contaminantes por Borough (2023)',
             template='plotly_white')

# Añadimos las etiquetas del total general encima de cada columna
for i, borough in enumerate(total_values['Borough']):
    fig.add_annotation(
        x=borough,
        y=total_values['Data Value'][i],
        text=f'Total: {total_values["Data Value"][i]}',
        showarrow=True,
        arrowhead=5,
        ax=0,
        ay=-40
    )

# Añadimos bordes a las columnas
fig.update_traces(marker_line=dict(color='black', width=1.5))

# Ajustamos el diseño del gráfico
fig.update_layout(
    xaxis=dict(tickangle=-45),
    legend_title='Contaminante',
    xaxis_title='Borough',
    yaxis_title='Niveles de Contaminantes (mcg/m3 or ppb)',
)

# Mostramos el gráfico con Streamlit
st.plotly_chart(fig)