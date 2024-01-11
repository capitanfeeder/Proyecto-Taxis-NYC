import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# Título de la página
st.title("Taxis en New York City")

# Separador visual
st.markdown('***')

# Título de la sección
st.header("Recuento de viajes por hora y dia de la semana")

# Leer los datos de los viajes
trips = pd.read_parquet('Datasets/3-Normalizados/taxis_2023.parquet',
                        columns=['pickup_datetime', 'dropoff_datetime', 'trip_distance', 'PULocationID', 'DOLocationID',])

# Leer datos de la zona de taxis
taxi_zone = pd.read_parquet('Datasets/3-Normalizados/taxi_zones.parquet', columns=['LocationID', 'Zone'])
taxi_zone.set_index(['LocationID'], inplace=True)

# Cargar GeoJSON para el mapa
with open('Datasets/4-Extras/NYC Taxi Zones.geojson') as fd:
    geojson = json.load(fd)

# Agregar columnas para el día de la semana y la hora de recogida
trips['PU_dayofweek'] = trips['pickup_datetime'].dt.dayofweek
trips['PU_hour'] = trips['pickup_datetime'].dt.hour

# Agrupar por día de la semana y hora y contar la frecuencia
gb_time = trips.groupby(by=['PU_dayofweek', 'PU_hour'], as_index=False).agg(count=('PU_dayofweek', 'count'))

# Crear el gráfico de barras con Plotly Express
fig = px.bar(
    gb_time,
    x='PU_hour',
    y='count',
    color='PU_dayofweek',
    color_continuous_scale='sunset_r',
)

# Configuración de etiquetas
fig.update_layout(
    title='Recuento de viajes por hora y día de la semana',
    xaxis_title='Hora del día',
    yaxis_title='Recuento de viajes',
    coloraxis_colorbar_title='Día de la semana',
)

# Mostrar el gráfico con Streamlit
st.plotly_chart(fig)


# Título de la sección
st.header("Recuento de viajes por pickup")

# Leer los datos de los viajes
trips = pd.read_parquet('Datasets/3-Normalizados/taxis_2023.parquet',
                        columns=['pickup_datetime', 'dropoff_datetime', 'trip_distance', 'PULocationID', 'DOLocationID',])

# Leer datos de la zona de taxis
taxi_zone = pd.read_parquet('Datasets/3-Normalizados/taxi_zones.parquet', columns=['LocationID', 'Zone'])
taxi_zone.set_index(['LocationID'], inplace=True)

# Cargar GeoJSON para el mapa
with open('Datasets/4-Extras/NYC Taxi Zones.geojson') as fd:
    geojson = json.load(fd)

# Agrupar por ubicación de recogida y contar la frecuencia
gb_pu_location = trips.groupby(['PULocationID'], as_index=False).agg(count=('PULocationID', 'count'))

# Configuración del gráfico de mapa de coropletas
fig = go.Figure(
    go.Choroplethmapbox(
        geojson=geojson,
        featureidkey='properties.location_id',
        locations=gb_pu_location['PULocationID'],
        z=gb_pu_location['count'],
        colorscale="Viridis",
        marker_opacity=0.7,
        marker_line_width=0.1
    )
)

# Configuración del diseño del mapa
fig.update_layout(
    title='Recuento de viajes por ubicación de recogida',
    mapbox_style="carto-positron",
    mapbox_zoom=9,
    mapbox_center={"lat": 40.7158, "lon": -73.9805},
    height=600,
    margin={"r":0,"t":40,"l":0,"b":0},
)

# Etiquetas adicionales
fig.update_layout(
    annotations=[
        dict(
            x=0.5,
            y=-0.1,
            showarrow=False,
            text="Fuente: Datos de viajes",
            xref="paper",
            yref="paper",
        )
    ]
)

# Mostrar el gráfico con Streamlit
st.plotly_chart(fig)


# Título de la sección
st.header("Recuento de viajes por dropoff")

# Leer los datos de los viajes
trips = pd.read_parquet('Datasets/3-Normalizados/taxis_2023.parquet',
                        columns=['pickup_datetime', 'dropoff_datetime', 'trip_distance', 'PULocationID', 'DOLocationID',])

# Leer datos de la zona de taxis
taxi_zone = pd.read_parquet('Datasets/3-Normalizados/taxi_zones.parquet', columns=['LocationID', 'Zone'])
taxi_zone.set_index(['LocationID'], inplace=True)

# Cargar GeoJSON para el mapa
with open('Datasets/4-Extras/NYC Taxi Zones.geojson') as fd:
    geojson = json.load(fd)

# Agrupar por ubicación de destino y contar la frecuencia
gb_do_location = trips.groupby(['DOLocationID'], as_index=False).agg(count=('DOLocationID', 'count'))

# Configuración del gráfico de mapa de coropletas
fig = go.Figure(
    go.Choroplethmapbox(
        geojson=geojson,
        featureidkey='properties.location_id',
        locations=gb_do_location['DOLocationID'],
        z=gb_do_location['count'],
        colorscale="Viridis",
        marker_opacity=0.7,
        marker_line_width=0.1
    )
)

# Configuración del diseño del mapa
fig.update_layout(
    title='Recuento de viajes por ubicación de destino',
    mapbox_style="carto-positron",
    mapbox_zoom=9,
    mapbox_center={"lat": 40.7158, "lon": -73.9805},
    height=600,
    margin={"r": 0, "t": 40, "l": 0, "b": 0},
)

# Etiquetas adicionales
fig.update_layout(
    annotations=[
        dict(
            x=0.5,
            y=-0.1,
            showarrow=False,
            text="Fuente: Datos de viajes",
            xref="paper",
            yref="paper",
        )
    ]
)

# Mostrar el gráfico con Streamlit
st.plotly_chart(fig)