#Este es un codigo al que se le ingresa un archivo y devuelve
#matrices en formato .npz que almacenan la precipitacion diaria 
#del archivo


#########Librerias##################
from funcion_extrae_tiempos import extrae_tiempos

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os 
import pandas as pd

#Archivo .grib que deseamos leer
file = "apcp_sfc_2009102400_c00.grib2"

#Carpeta donde se encuentra el archivo
folder = '/home/fernando.huaranca/datos/DATOS_REFORECAST/apcp_sfc'

#Ruta del archivo
path = os.path.join(folder,file)
print(path)

###########################################################

#Abrimos el dataset
ds = xr.open_dataset(path)

#Extraigo el array de Total Precipitation
var = ds.tp.values

#Seleccion de tiempos

#################Seleccion de tiempos######

#Extrae indices de steps
idx_steps = extrae_tiempos(ds)

#Tiempos para el dia N


row = ds.latitude.shape[0]
col = ds.longitude.shape[0]




for dia in range(idx_steps.shape[0]):

    #Inicializo matriz de pp acumulada
    pp = np.zeros([row,col])

    #Selecciono los indices de steps del dia N
    DiaN = idx_steps[dia,1:]

    
    name_file = f'{idx_steps[dia, 0]}' 

    print(f'Leyendo archivo {name_file}')

    #Genero una matriz que almacena la precipitacion acumulada
    #por dia
    for tiempo in DiaN:
        pp += np.round(var[tiempo,:,:],3)
        

    # Ruta completa del archivo donde guardar los datos
    out_path = f'/home/fernando.huaranca/test_forecast/output_matrices/{name_file}.npz'

    # Guardar los arreglos en el archivo

    np.savez(out_path,pp_daily = pp)






