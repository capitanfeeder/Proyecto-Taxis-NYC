import streamlit as st

# Título de la página
st.title('Presentación del Grupo N° 5')

# Separador visual
st.markdown('***')

# Sección para cada integrante del proyecto
st.header('María Inés Hiriart (Uruguay)')
# Imagen del integrante 1
image_int_1 = 'Datasets/4-Extras/Ines.png'  
st.image(image_int_1, width=700, caption='Data Analyst - Experta en Análisis de Datos')

st.write("""
María Inés es una apasionada analista de datos de Uruguay. Con experiencia en la interpretación y 
análisis de grandes conjuntos de datos, aporta una perspectiva única al equipo.
""")

# Separador visual
st.markdown('***')

st.header('Santiago Ituyán (Colombia)')
image_int_2 = 'Datasets/4-Extras/Santiago.png' 
st.image(image_int_2, width=700, caption='Data Analyst - Data Scientist')

st.write("""
Santiago, desde Colombia, es un científico de datos y analista apasionado. Su habilidad para 
convertir datos en ideas accionables es un activo clave para nuestro proyecto.
""")

# Separador visual
st.markdown('***')

st.header('Jordi Segarra (México)')
image_int_3 = 'Datasets/4-Extras/Jordi.png' 
st.image(image_int_3, width=700, caption='Data Scientist - Especialista en Machine Learning')

st.write("""
Jordi, con raíces en México, es nuestro experto en Machine Learning. Su experiencia y habilidades 
contribuyen a la creación de modelos predictivos avanzados.
""")

# Separador visual
st.markdown('***')

st.header('Leopoldo Farah (Argentina)')
image_int_4 = 'Datasets/4-Extras/Leopoldo.png' 
st.image(image_int_4, width=700, caption='Data Engineer (Líder de Proyecto)')

st.write("""
Leopoldo lidera nuestro proyecto como Data Engineer desde Argentina. Con sólidos conocimientos en 
ingeniería de datos, garantiza el flujo eficiente de información.
""")

# Separador visual
st.markdown('***')

st.header('Gabriel Sosa (Argentina)')
image_int_5 = 'Datasets/4-Extras/Gabriel.jpg' 
st.image(image_int_5, width=700, caption='Data Engineer - Especialista en Desarrollo de Software')

st.write("""
Gabriel, también desde Argentina, es nuestro experto en desarrollo de software. Su habilidad para 
crear soluciones eficientes impulsa el éxito de nuestro proyecto.
""")

# Separador visual
st.markdown('***')

# Sección para el stack tecnológico
st.header('Stack Tecnológico')
st.write("""
1. **Lenguaje de Programación:** Python
2. **Frameworks:** Streamlit, FastAPI
3. **Base de Datos:** AWS Athena, AWS S3
4. **Frontend:** Streamlit
5. **Backend:** FastAPI, Servicios AWS
6. **Contenedores y Orquestación:** Docker, Servicios AWS
7. **Gestión de Dependencias:** Pip (Python)
8. **Control de Versiones:** Git (GitHub)
9. **Despliegue:** AWS Elastic Beanstalk, Render, Railway
10. **Seguridad:** HTTPS, Autenticación y Autorización
11. **Monitoreo y Registro:** AWS Cloudwatch
12. **Herramientas Adicionales:** Git, Power BI, xgboost, Plotly, Pandas, Numpy, Scikit-Learn, GeoPandas, Shapely, Tkinter, Pyinstaller
""")

# Separador visual
st.markdown('***')

# Título de la sección
st.title("Tratamiento de los datos")

# Tratamiento de los datos
st.image("Datasets/4-Extras/vidato_datagnius.jpg", use_column_width=True)

# Separador visual
st.markdown('***')

# Título de la sección
st.title("Metodología de trabajo")

st.write("""
En **datagnius** implementamos la metodología Scrum para mejorar la agilidad en el desarrollo de proyectos, facilitando la 
adaptabilidad a cambios y optimizando la entrega continua de productos de alta calidad mediante una gestión 
eficiente de equipos multifuncionales y ciclos de desarrollo iterativos. Además, con ella promovemos una comunicación 
transparente y colaborativa, maximizando la satisfacción del cliente y la eficiencia operativa.
""")

# Imagen de la empresa
st.image("Datasets/4-Extras/Gantt.png", use_column_width=True)

# Separador visual
st.markdown('***')

# Hipervínculo al repositorio de GitHub
st.markdown('[Repositorio en GitHub](https://github.com/capitanfeeder/Proyecto-Taxis-NYC)')
