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
file = "apcp_sfc_2000010100_c00.grib2"

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

#Extrae indices de steps
idx_steps = extrae_tiempos(ds)

#Extraigo latitudes y longitudes
lat = ds.tp.latitude.values
lon = ds.tp.longitude.values

#Cerramos dataset
ds.close()




##Seleccion area sudamerica

#Latitudes y longitudes (box)
lat_north = 12
lat_south = -55
lon_east = 340
lon_west = 260

#####LATITUDES
lat_index = np.flatnonzero((lat <lat_north) & (lat > lat_south))

lat = lat[lat_index]


#LONGITUDES
lon_index = np.flatnonzero((lon > lon_west) & (lon < lon_east))

lon = lon[lon_index]


#Tiempos para el dia N

row = lat.shape[0]
col = lon.shape[0]


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
        pp = np.round(var[tiempo,lat_index[0]:lat_index[-1]+1,lon_index[0]:lon_index[-1]+1] + pp,3)
        

    # Ruta completa del archivo donde guardar los datos
    out_path = f'/home/fernando.huaranca/test_forecast/testeo_erroneos/{name_file}.npz'

    # Guardar los arreglos en el archivo

    np.savez(out_path,pp_daily = pp, latitudes = lat,longitudes = lon,name = name_file)


