import streamlit as st

# Título de la página
st.title("Indicadores Clave de Desempeño (KPIs)")

# Separador visual
st.markdown('***')

# Imagen de presentación
st.image("Datasets/4-Extras/KPI.png", use_column_width=True)


st.write("""
Teniendo en cuenta los datos observados en un primer momento podemos recomendar los siguientes indicadores de desempeño para alcanzados los mismos, maximizar las oportunidades de éxito.  
""")

# Texto de los objetivos
st.write("""
## Indicadores de Desempeño Recomendados

1. **Ingreso promedio por hora:** 
   - Fórmula: Ingreso total / Duración total de los viajes
   - Proporciona una idea de la rentabilidad de los taxis por hora.

2. **Ingreso promedio por milla:** 
   - Fórmula: Ingreso total / Distancia total de los viajes
   - Proporciona una idea de la rentabilidad de los taxis por milla.

3. **Ingreso promedio por viaje:** 
   - Fórmula: Ingreso total / Cantidad total de viajes
   - Proporciona una idea de la rentabilidad de los taxis por viaje.

4. **Ingreso promedio por Borough:** 
   - Fórmula: Ingreso total en el Borough elegido / Cantidad de viajes en el Borough elegido
   - Proporciona una idea de la rentabilidad de los taxis por Borough.
""")