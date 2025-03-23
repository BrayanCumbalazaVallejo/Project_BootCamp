# Análisis de la Accidentalidad en el Area Metropolitana entre los años 2015-2018 

**Jerónimo Hoyos Botero**  
**Manuel Danilo Echeverry Franco**  
**Santiago Sosa García**  
**Brayan Cumbalaza Vallejo**  

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