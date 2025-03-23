import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pydeck as pdk

# Configuración datos
data = pd.read_csv("./files/input/coordenadas.csv")
data['lat'] = data['lat'].str.replace(',', '.').astype(float)
data['lon'] = data['lon'].str.replace(',', '.').astype(float)

# Barra lateral
st.sidebar.title("Accidentalidad Medellín")

# Opciones del menú

menu = st.sidebar.radio(
    "Selecciona una opción:",
    ["Presentación", "Gráficas", "Mapa", "Modelo Predictivo"]
)

# Contenido de cada opción
if menu == "Presentación":
    st.title("Análisis de la Accidentalidad en el Area Metropolitana entre los años 2015-2018🏙️🌄🚇")

    st.markdown("""
---              
### **Integrantes**  
- **Jerónimo Hoyos**  
- **Santiago Sosa**  
- **Brayan Cumbalaza**  
- **Manuel D. Echeverry**  

---

## **Introducción**  
En este trabajo final realizaremos un análisis del conjunto de datos [Accidentalidad Valle de Aburrá](https://datosabiertos.metropol.gov.co/dataset/f2c142b3-b5c1-4c62-9902-797f04aee252), obtenido del banco de datos abiertos del **Área Metropolitana del Valle de Aburrá**.

Este dataset contiene información sobre los accidentes registrados por las Secretarías de Movilidad y Transporte durante los años **2015**, **2016**, **2017** y **2018** en algunos municipios del Valle de Aburrá.  

---

## **Descripción del Dataset**  
El conjunto de datos está compuesto por **11 columnas**:  

- 📍 **`cod_municipio`**: Código del municipio.  
- 🏙️ **`municipio`**: Nombre del municipio.  
- 📅 **`fecha`**: Fecha del evento o suceso.  
- 🕒 **`hora`**: Hora del evento o suceso.  
- 📆 **`dia_semana`**: Día de la semana.  
- 🚨 **`clase`**: Tipo o categoría del evento.  
- 📌 **`direccion`**: Dirección del lugar del evento.  
- ⚠️ **`gravedad_asociada`**: Nivel de gravedad asociado.  
- 🏡 **`barrio`**: Nombre del barrio.  
- 🔢 **`comuna`**: Número o nombre de la comuna.  
- 🛣️ **`diseno`**: Diseño asociado al evento o suceso.  

---

## **Objetivo del Análisis**  
Este análisis tiene como objetivo identificar patrones y factores de riesgo en la accidentalidad, con el fin de proveer información para generar soluciones efectivas basadas en los hallazgos obtenidos. Para ello, se emplearán diversas herramientas visuales como gráficas de calor, gráficos de barras y mapas interactivos, utilizando herramientas como Streamlit, Google Maps, Pandas, Seaborn y NumPy.  
""")
    
elif menu == "Gráficas":
    st.title("Acá iría el análisis explotario de datos")

elif menu == "Mapa":

# Configuración de los hexagonos
    st.title("Los 100 lugares de Medellín con más accidentes")
    hexagonos = pdk.Layer(
    "HexagonLayer",
    data=data,
    get_position=["lon", "lat"],
    get_elevation="num_accidentes", 
    radius=50,
    elevation_scale=5, #Diferencia escala 
    elevation_range=[10, 350], #Límites 
    extruded=True, #Volumen
    )

# Configuración de la vista inicial
    view_state = pdk.ViewState(
    latitude=data['lat'].mean(), #Centrar posición
    longitude=data['lon'].mean(), 
    zoom=12,
    pitch=50, #Inclinación
    )

# Mostrar el mapa
    st.pydeck_chart(pdk.Deck(layers=[hexagonos], initial_view_state=view_state))

# Mostrar tabla
    st.subheader("Direcciones únicas con más accidentes")
    st.dataframe(data)

elif menu == "Modelo Predictivo":
    st.title("Acá iría modelo predictivo")

st.sidebar.write("---")
st.sidebar.write("Talento Tech")
st.sidebar.write("Universidad Nacional de Colombia")
st.sidebar.write("Sede Medellín")