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

def graficar_histogramas(data):
    """
    Genera histogramas para todas las columnas del DataFrame excepto:
    - COD_MUNICIPIO
    - FECHA
    - DIRECCIÓN
    """
    columnas_excluir = {'COD_MUNICIPIO', 'FECHA', 'HORA', 'DIRECCIÓN', 'BARRIO'}
    columnas_a_graficar = [col for col in data.columns if col not in columnas_excluir]
    
    for columna in columnas_a_graficar:
        plt.figure(figsize=(8, 4))
        
        if data[columna].dtype == 'object' or data[columna].dtype.name == 'category':
            data[columna] = data[columna].astype(str).str.lower().fillna("desconocido")  # Manejo de NaN
            data[columna].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
            plt.ylabel("Frecuencia")
        else:
            plt.hist(data[columna].dropna(), bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
            plt.ylabel("Frecuencia")
        
        plt.title(f"Distribución de '{columna}'")
        plt.xlabel("Valores")
        plt.xticks(rotation=45)
        plt.grid(axis='y', alpha=0.5)
        plt.show()

def convertir_hora(hora):
    hora = hora.strip().lower()

    # Caso para formato PM (si contiene 'p')
    if 'p' in hora:
        match = re.match(r'(\d+):\d+', hora)  # Solo hora y minutos
        if match:
            hora_pm = int(match.group(1))
            if hora_pm < 12:  # Si es menor a 12, sumamos 12
                hora_pm += 12
            return f'{hora_pm}:00'  # Solo devolvemos horas y minutos

    # Si no tiene 'p', asumimos que es formato 24 horas
    else:
        match = re.match(r'(\d+):\d+', hora)  # Solo hora y minutos
        if match:
            return f'{match.group(1)}:00'  # Devolvemos la hora en formato 24h