import matplotlib.pyplot as plt
import pandas as pd
import re

def clean_data(data):
    data = data.dropna()
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].str.strip().str.lower()
    data = data.drop_duplicates()
    data['BARRIO'] = data['BARRIO'].str.replace('no. ', 'no.')
    return data

    #elimina las filas que tengan en la columna BARRIO los valores "sin información" o "n/r"
def delete_barrios_sin_info(data):
    data = data[(data['BARRIO'] != 'sin información') & (data['BARRIO'] != 'n/r')]
    # tambien de la columna "CLASE" se borran los valores "sin información"
    data = data[data['CLASE'] != 'sin información']
    return data


import matplotlib.pyplot as plt

def graficar_histogramas(data):
    columnas_excluir = {'COD_MUNICIPIO', 'FECHA', 'HORA', 'DIRECCIÓN', 'BARRIO'}
    columnas_a_graficar = [col for col in data.columns if col not in columnas_excluir]
    
    for columna in columnas_a_graficar:
        plt.figure(figsize=(8, 4))
        
        if data[columna].dtype == 'object' or data[columna].dtype.name == 'category':
            data[columna].value_counts().plot(kind='barh', color='skyblue', edgecolor='black')
            plt.xlabel("Frecuencia")
        else:
            plt.hist(data[columna].dropna(), bins=20, color='lightcoral', edgecolor='black', alpha=0.7, orientation='horizontal')
            plt.xlabel("Frecuencia")
        
        plt.title(f"Distribución de '{columna}'")
        plt.ylabel("Valores")
        plt.grid(axis='x', alpha=0.5)
        plt.show()




def convertir_hora(hora):
    hora = hora.strip().lower()
    if 'p' in hora:
        match = re.match(r'(\d+):\d+', hora)
        if match:
            hora_pm = int(match.group(1))
            if hora_pm < 12:
                hora_pm += 12
            return hora_pm

    else:
        match = re.match(r'(\d+):\d+', hora)
        if match:
            return int(match.group(1))

def convertir_mes(mes):
    meses = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre'
    }
    return meses.get(mes, 0)


def muertos_heridos_daños(muertos, heridos, daños, PALABRA):
    muertos = muertos / muertos.sum()
    heridos = heridos / heridos.sum()
    daños = daños / daños.sum()

    fig, ax = plt.subplots(figsize=(10, 6))

    width = 0.25
    x = range(len(muertos))

    ax.barh(x, muertos, height=width, color='red', label="Muertos")
    ax.barh([i + width for i in x], heridos, height=width, color='blue', label="Heridos")
    ax.barh([i + 2 * width for i in x], daños, height=width, color='green', label="Daños")

    ax.set_title(f"Muertos, Heridos y Daños por {PALABRA}")
    ax.set_xlabel("Porcentaje Normalizado")
    ax.set_ylabel(f"{PALABRA}")
    ax.set_yticks([i + width for i in x])
    ax.set_yticklabels(muertos.index)

    ax.legend()
    plt.show()
