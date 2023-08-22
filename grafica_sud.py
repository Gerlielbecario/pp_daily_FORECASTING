#Un codigo muy simple y rudimentario que pueda graficar el contenido de 
#FORECAST GFS SUDAMERICA

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
paso = ds.step[34]



#Seleccionamos de nuestro array el paso y obtenemos una matriz 2x2 latitudexlongitude
pp = var.sel(step = paso)


##Seleccion area sudamerica

#Latitudes y longitudes (box)

lat_north = 12
lat_south = -55
lon_east = 340
lon_west = 260

#latitudes
lat_index = np.flatnonzero((ds.latitude.values <lat_north) & (ds.latitude.values > lat_south))

#longitudes
lon_index = np.flatnonzero((ds.longitude.values > lon_west) & (ds.longitude.values < lon_east))


#lat_north = 
#lat_south = 
#lon_west = 
#lon_east = 


suda = pp[lat_index,lon_index]
suda.shape


#grafico
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
suda.plot.pcolormesh(ax=ax, transform=ccrs.PlateCarree(), cmap='Blues', extend='both')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)

#plt.figure(figsize=(12, 6))
#pp.plot.pcolormesh()
#plt.colorbar(label='Precipitación (kg m^-2)')
#plt.title(f"Mapa de precipitación para el paso {paso}")
#plt.xlabel('Longitud')
#plt.ylabel('Latitud')

# Agrega el comando input para pausar la ejecución y ver la ventana emergente
#plt.savefig('pruebaone.png')
print(type(suda))