import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pydeck as pdk

## Modelo de red neuronal
# Cargar el modelo
modelo = tf.keras.models.load_model("./redNeuronal/checkpoint.modelo.keras")
dataLimpia = pd.read_csv("./files/input/data.csv")


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
    st.title("Análisis de la Accidentalidad en Medellín entre los años 2015-2017🏙️🌄🚇")
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""  
### **Integrantes**  
- **Jerónimo Hoyos**  
- **Santiago Sosa**  
- **Brayan Cumbalaza**  
- **Manuel D. Echeverry**  
                 """)
    with col2:
        st.image("https://datosabiertos.metropol.gov.co/sites/default/files/2023-01/municipios_0.svg")

    with col3:
        st.image("https://datosabiertos.metropol.gov.co/themes/custom/theme_datosabiertos/images/logos/datos-abiertos-logo.svg",width=250)
        st.image("https://datosabiertos.metropol.gov.co/sites/default/files/2022-12/futuro-sostenible-logo.svg",width=230)

    st.markdown("""
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

    # Mostrar la gráfica en Streamlit
    st.title("Análisis descriptivo📊📈")
    st.markdown("---")
    st.image("dashboard/figures/horas.png")
    st.markdown("---")
    st.image("dashboard/figures/semana.png")
    st.markdown("---")
    st.image("dashboard/figures/mes.png")
    st.markdown("---")
    st.image("dashboard/figures/agosto.png")






elif menu == "Mapa":

    # Configuración de los hexagonos
    st.title("Los 100 lugares de Medellín con más accidentes 🗺️📌")
    st.markdown("---")
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
    st.markdown("---")
    st.subheader("Direcciones únicas con más accidentes")
    
    st.dataframe(data)

elif menu == "Modelo Predictivo":
    # Variables utilizadas
    features = ["CLASE", "DÍA DE LA SEMANA", "MES", "HORA24", "DISEÑO", "COMUNA"]

    # Inicializar transformaciones con los mismos parámetros usados en entrenamiento
    encoder = OneHotEncoder(drop="first", sparse_output=False)
    encoder.fit(dataLimpia[["CLASE", "DÍA DE LA SEMANA", "MES", "DISEÑO", "COMUNA"]])

    scaler = StandardScaler()
    scaler.fit(dataLimpia[["HORA24"]])

    st.title("Modelo Predictivo de Accidentes de la gravedad del accidente🧠")
    st.markdown("---")
    clase = st.selectbox(
        "Seleccione la clase de accidente", dataLimpia["CLASE"].unique()
    )
    dia_semana = st.selectbox(
        "Seleccione el día de la semana", dataLimpia["DÍA DE LA SEMANA"].unique()
    )
    mes = st.selectbox("Seleccione el mes", dataLimpia["MES"].unique())
    hora24 = st.selectbox(
        "Seleccione la hora (24h)", sorted(dataLimpia["HORA24"].unique())
    )
    diseno = st.selectbox("Seleccione el diseño", dataLimpia["DISEÑO"].unique())
    comuna = st.selectbox("Seleccione la comuna", dataLimpia["COMUNA"].unique())

    # Convertir entrada del usuario a DataFrame
    entrada_df = pd.DataFrame([[clase, dia_semana, mes, hora24, diseno, comuna]], 
                            columns=["CLASE", "DÍA DE LA SEMANA", "MES", "HORA24", "DISEÑO", "COMUNA"])

    # Aplicar transformaciones
    entrada_encoded = encoder.transform(entrada_df[["CLASE", "DÍA DE LA SEMANA", "MES", "DISEÑO", "COMUNA"]])
    entrada_scaled = scaler.transform(entrada_df[["HORA24"]])

    # Unir las características transformadas
    entrada_final = np.hstack((entrada_encoded, entrada_scaled)).astype(np.float32)

    # Predicción
    if st.button("Predecir"):
        prediccion = modelo.predict(entrada_final)
        clase_predicha = np.argmax(prediccion)  # Obtener la clase más probable
        
        # Diccionario para interpretar la salida
        clases_dict = {0: "Daños materiales", 1: "Heridos", 2: "Muertos"}
        
        st.subheader("Resultado de la Predicción:")
        st.write(f"⚠️ **Categoría predicha:** {clases_dict[clase_predicha]}")

        st.subheader("Probabilidades por clase:")
        for i, prob in enumerate(prediccion[0]):
            st.write(f"📌 **{clases_dict[i]}**: {prob:.2%}")


st.sidebar.write("---")
st.sidebar.write("Talento Tech")
st.sidebar.write("Universidad Nacional de Colombia")
st.sidebar.write("Sede Medellín")

st.markdown("---")

col1, col2 = st.columns([1, 2]) 
with col1:
    st.link_button("Repositorio", "https://github.com/BrayanCumbalazaVallejo/Project_BootCamp")
    st.image("https://img.icons8.com/?size=100&id=Mhl1TfJLdkh5&format=png&color=000000",width=110)
with col2:
    st.image("https://lh4.googleusercontent.com/proxy/WNtyuTbDjnnITJFxg1dlI63L0jfIMRf0CIKg75VavFd3ameUuokpEiXIZvafO0UbA3rGKkhjDZ2HFtRWcGiPIn7Syd37PqnCrQuXFNHguRRPYm__safRJi9Q",width=400)
