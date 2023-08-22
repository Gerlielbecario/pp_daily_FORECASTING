#Un codigo que al leer un archivo .grib puede extraer los tiempos 
#pertenecientes al mismo dia 

#Librerias

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os 

#####################

#Archivo .grib que deseamos leer
file = "apcp_sfc_2009102400_c00.grib2"

#Carpeta donde se encuentra el archivo
folder = '/home/fernando.huaranca/datos/DATOS_REFORECAST/apcp_sfc'

#Ruta del archivo
path = os.path.join(folder,file)
print(path)

##########

#Tiempos de interes 
#times_forecast = [1,3,5,7]

ds = xr.open_dataset(path)
print(ds)