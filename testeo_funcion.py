##Este es un codigo que testea la funcion extrae_tiempos
#La utiliza para extraer matrices de sudamerica

from funcion_extrae_tiempos import extrae_tiempos

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os 
import pandas as pd
##############

#Archivo .grib que deseamos leer
file = "apcp_sfc_2009102400_c00.grib2"

#Carpeta donde se encuentra el archivo
folder = '/home/fernando.huaranca/datos/DATOS_REFORECAST/apcp_sfc'

#Ruta del archivo
path = os.path.join(folder,file)
print(path)

##########

ds = xr.open_dataset(path)

#################Seleccion de tiempos######

#Extrae indices de steps
idx_steps = extrae_tiempos(ds)

#Tiempos para el dia 1
one_day = idx_steps[0,1:]

var = ds.tp.values



######Obtener matriz de precipitacion acumulada por dia

row = ds.latitude.shape[0]
col = ds.longitude.shape[0]
pp = np.zeros([row,col])

    
for paso in one_day:

    #Matriz de pp global
    pp = np.round(var[paso,:,:] + pp,3)


###################################################3

##Seleccion area sudamerica

#Latitudes y longitudes (box)

lat_north = 15
lat_south = -65
lon_east = 330
lon_west = 260

#latitudes
lat_index = np.flatnonzero((ds.latitude.values <lat_north) & (ds.latitude.values > lat_south))

#longitudes
lon_index = np.flatnonzero((ds.longitude.values > lon_west) & (ds.longitude.values < lon_east))

#Selecciona seccion de sudamerica
suda = pp[lat_index[0]:lat_index[-1],lon_index[0]:lon_index[-1]]


lat = ds.latitude.values
lon = ds.longitude.values

lat = lat[lat_index]
lon = lon[lon_index]







######################PLOTEO############


#Se genera una figura en blanco con 10pulgadas de ancho y 10 de alto
fig = plt.figure(figsize=(10, 8))

#Se crea un eje de matplotlib en la figura y se especifica la proyeccion cartografica
#en este caso se usa cartopy para latitud y longitud
ax = plt.axes(projection=ccrs.PlateCarree())

#Utilizando el metodo pcolormersh se crea un mapa de colores.
#Transform especifica la proyeccion utilizada
pp_plot = ax.pcolormesh(lon,lat, suda, transform=ccrs.PlateCarree(), cmap='Blues', shading='auto')

#Se agregan caracteristicas geograficas a la trama
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':') #estilo de linea punteada

#Agrega lineas de cuadricula al mapa. Indica que se dibujen lineas de latitud y longitud
#dms = True muestra las etiquetas en grados minutos y segundos
ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)

#Agrega una barra de color que pertence a los valores de precipitacion
plt.colorbar(pp_plot, ax=ax, label='Precipitación')

#Titulo por encima
#plt.title('Mapa de Precipitación Diaria')
#plt.show() #muestra el grafico por pantalla
