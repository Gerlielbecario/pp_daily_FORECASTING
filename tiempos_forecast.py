#Un codigo muy simple y rudimentario que explique que informacion de tiempos tiene
#cada archivo

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

#Tiempo inicial de nuestro pronostico
#print('Tiempo inicial de nuestro pronostico')
print('Tiempo inicial: ',ds.time.values.astype(str))
#print('.........')


#print('Tiempo final de nuestro pronostico')


###Para ir sumando los step

#print('Tiempo posterior',ds.time.values+np.timedelta64(ds.step[0].values))


#tengo pronosticos cada 3 hs y tengo 10 dias de informacion

#tiempo_inicial = ds.time.values
#print(ds.step[0].values.astype(str)
for i in range(80):
    print('Tiempo',str(i),ds.time.values+np.timedelta64(ds.step[i].values))

