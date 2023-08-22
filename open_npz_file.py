#Codigo que abre un archivo de formato .npz. Muestra por pantalla la informacion que 
#contiene este tipo de archivos y luego lo plotea.


#Librerias

import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

#Directorio
path = 'pp_daily.npz'

#Cargamos el archivo
datos = np.load(path)

##Muetra por pantalla la informacion de cada dimension y su tamaño
print('Dentro del archivo se hallan los siguientes arrays: ')
for arreglo in datos.files:
    dimensiones = datos[arreglo].shape
    peso = datos[arreglo].nbytes
    peso_megas = peso/(1024**2)
    print(arreglo,dimensiones," tamaño en disco:",np.round(peso_megas,2),"MB")

#Extraigo dimensiones de mi archivo
pp = datos['pp_daily']
lat = datos['latitudes']
lon = datos['longitudes']

#Una vez abierto el archivo y extrayendo las dimensiones podemos plotearlo

############################################################################################
################### GRAFICADO ################################################################


#Se genera una figura en blanco con 10pulgadas de ancho y 10 de alto
fig = plt.figure(figsize=(10, 8))

#Se crea un eje de matplotlib en la figura y se especifica la proyeccion cartografica
#en este caso se usa cartopy para latitud y longitud
ax = plt.axes(projection=ccrs.PlateCarree())

#Utilizando el metodo pcolormersh se crea un mapa de colores.
#Transform especifica la proyeccion utilizada
pp_plot = ax.pcolormesh(lon, lat, pp, transform=ccrs.PlateCarree(), cmap='Blues', shading='auto')

#Se agregan caracteristicas geograficas a la trama
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':') #estilo de linea punteada

#Agrega lineas de cuadricula al mapa. Indica que se dibujen lineas de latitud y longitud
#dms = True muestra las etiquetas en grados minutos y segundos
ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)

#Agrega una barra de color que pertence a los valores de precipitacion
plt.colorbar(pp_plot, ax=ax, label='Precipitación')

#Titulo por encima
plt.title('Mapa de Precipitación Diaria')
plt.show() #muestra el grafico por pantalla
