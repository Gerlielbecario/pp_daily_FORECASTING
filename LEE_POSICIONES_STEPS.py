#Este es un codigo que extrae las posiciones de los steps de interes para
#precipitacion diaria. 06, 12, 18 y 00utc. Devuelve una matriz que contiene
#las posiciones. Cada fila representa el dia 'fecha' y cada columna representa las
#horas mencionadas.

import numpy as np
import pandas as pd
import xarray as xr
import os


###############################

#Archivo .grib que deseamos leer
file = "apcp_sfc_2009102400_c00.grib2"

#Carpeta donde se encuentra el archivo
folder = '/home/fernando.huaranca/datos/DATOS_REFORECAST/apcp_sfc'

#Ruta del archivo
path = os.path.join(folder,file)
print(path)

##########

ds = xr.open_dataset(path)




##########################################################

# Crear un arreglo con las fechas y horas
fechas_horas = pd.to_datetime(ds.time.values + ds.step.values, origin='unix', unit='ns')

# Crear una Serie con las fechas y horas
fechas_series = pd.Series(fechas_horas)

# Encuentra las posiciones de las horas 00, 06, 12 y 18
horas_interes = [0, 6, 12, 18]

###### Crear un array para almacenar las posiciones por día y hora#####

n_col = 5 # 06 12 18 00utc y la fecha a la que pertenece

#ya que son la cantidad de step dividido por la cantidad de tiempos por dia
n_row = int(ds.step.shape[0]/8) 

posiciones_por_dia_hora = np.zeros((n_row, n_col), dtype=object)

# Inicializar índices para el array
indice_fila = 0
indice_columna = 0

# Iterar a través de las fechas y agregar las posiciones al array
for idx, fecha_hora in fechas_series.items():
    fecha_hora = fecha_hora - pd.Timedelta(hours=6)  # Resta 6 horas para ajustar al día anterior
    fecha_str = fecha_hora.strftime('%d-%m-%Y')
    hora = fecha_hora.hour
    if hora in horas_interes:
        posiciones_por_dia_hora[indice_fila, 0] = fecha_str
        posiciones_por_dia_hora[indice_fila, indice_columna + 1] = idx
        indice_columna += 1
        if indice_columna == 4:
            indice_columna = 0
            indice_fila += 1
print(posiciones_por_dia_hora)
