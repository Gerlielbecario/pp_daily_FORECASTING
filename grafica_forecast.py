#Un codigo muy simple y rudimentario que pueda graficar el contenido de 
#FORECAST GFS

#Librerias

import xarray as xr
import matplotlib.pyplot as plt

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

#lat_north = 
#lat_south = 
#lon_west = 
#lon_east = 



#plt.figure(figsize=(12, 6))
pp.plot.pcolormesh()
#plt.colorbar(label='Precipitación (kg m^-2)')
#plt.title(f"Mapa de precipitación para el paso {paso}")
#plt.xlabel('Longitud')
#plt.ylabel('Latitud')

# Agrega el comando input para pausar la ejecución y ver la ventana emergente
plt.savefig('pp.png')

