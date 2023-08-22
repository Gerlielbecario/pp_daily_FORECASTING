#Librerias

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

##############

path = 'apcp_sfc_2013031600_c00.grib2'

#Open file
ds = xr.open_dataset(path)

#Extraigo los datos de la variable Total Precipitation
var = ds.tp

#Un step o paso del pronostico
tiempo_0 = ds.step[1]
tiempo_1 = ds.step[3]
tiempo_2 = ds.step[5]
tiempo_3 = ds.step[7]


pp_0 = var.sel(step = tiempo_0) #Pronostico de lluvia acumulada de 00 a 06 UTC
pp_1 = var.sel(step = tiempo_1) #acumulado de lluvia de 06 a 12UTC
pp_2 = var.sel(step = tiempo_2) #acumulado de lluvia de 12 a 18UTC
pp_3 = var.sel(step = tiempo_3) #acumulado de lluvia de 18UTC a 00UTC

#Acumulado de lluvia para 1 dia 
pp = pp_0 + pp_1 + pp_2 + pp_3 

#Dimensiones de mi array
#
# print(pp.shape)  

#Latitudes de mi archivo
lat = ds.latitude
lon = ds.longitude

##Generamos un codigo que almacena estos datos

np.savez('pp_daily',pp_daily= pp,latitudes=lat,longitudes=lon)