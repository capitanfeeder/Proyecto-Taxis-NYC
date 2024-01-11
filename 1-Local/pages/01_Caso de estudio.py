import streamlit as st

# Título de la página
st.title("Estudio de Caso: Taxis en New York City")

# Separador visual
st.markdown('***')

# Imagen de presentación
st.image("https://camo.githubusercontent.com/b2961f7a7f8e8533211b2485a26762b733a3a33f2bfc9397a3a49c032e1783a8/68747470733a2f2f63616e616c632e636f6d2e61722f77702d636f6e74656e742f75706c6f6164732f323032332f30342f696d6167652d3434392e706e67", use_column_width=True)


st.write("""
Al implementarse una unidad de negocio nueva, la empresa Transport & Co, desea realizar un análisis preliminar del movimiento de los taxis en la ciudad de Nueva York. Esto les proporcionará un marco de referencia para tomar decisiones fundamentadas.  
""")

# Texto de los objetivos
st.write("""
El análisis se centra en los siguientes objetivos:

* **Analizar la rentabilidad al expandirse al mercado de taxis.**
* **Identificar la relación entre el transporte motorizado y la contaminación ambiental en la ciudad de Nueva York.**
* **Evaluar la viabilidad de incorporar vehículos eléctricos a la flota de transporte de pasajeros.**
""")