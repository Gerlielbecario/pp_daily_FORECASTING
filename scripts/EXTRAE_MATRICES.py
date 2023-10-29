#Este es un codigo al que se le ingresa una lista de archivos y devuelve
#matrices en formato .npz que almacenan la precipitacion diaria 
#del los archivos


#########Librerias##################
from funcion_extrae_tiempos import extrae_tiempos

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os 
import pandas as pd


#------CARGAR ARCHIVOS------------------

#Carpeta donde se encuentra el archivo
folder = '/home/fernando.huaranca/datos/DATOS_REFORECAST/apcp_sfc'

FileS = os.listdir(folder)



print('Lista de archivos cargada')



#-------LIMITES PARA EL SUSBSET-----------

#Region de sudamerica

ini_lon=260.0
end_lon=330.0
ini_lat=-65.0
end_lat=15.0

#Lista para almacenar archivos erroneos

fallidos = []

#Porcentaje
i = 0
total = len(FileS)




#-------BUCLE PARA PROCESAR CADA ARCHIVO-----------------------


for file in FileS:


    #Ruta del archivo
    path = os.path.join(folder,file)

    print('Leyendo archivo: ',file)

    i = i + 1 
    porcentaje = (i/total) * 100


    try:

        #Abrimos el dataset
        ds = xr.open_dataset(path)

        print('Comienza la extraccion de variables')

        #Extraigo el array de Total Precipitation
        var = ds.tp.values

        #Extrae indices de steps
        idx_steps = extrae_tiempos(ds)

        #Extraigo latitudes y longitudes

        lat = ds.tp.latitude.values
        lon = ds.tp.longitude.values

        #Cerramos dataset
        ds.close()

        print('Se extrajo correctamente las variables del file: ',file)

        #----SUBSET
        
        #latitudes
        lat_index = np.flatnonzero((lat <end_lat) & (lat > ini_lat))
        lat = lat[lat_index]

        #longitudes
        lon_index = np.flatnonzero((lon > ini_lon) & (lon < end_lon))

        lon = lon[lon_index]
        
        #Tiempos para el dia N  
        row = lat.shape[0]
        col = lon.shape[0]

        print('Comienza la creacion de las 10 matrices de pp acumulada para:',file)
        
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
            
            print('Matrices del file ',file,' generadas correctamente')

            # Ruta completa del archivo donde guardar los datos
            out_path = f'/home/fernando.huaranca/test_forecast/output_matrices/{name_file}.npz'


            # Guardar los arreglos en el archivo

            np.savez(out_path,pp_daily = pp, latitudes = lat,longitudes = lon,name = name_file)

            print('Finalizado')

    except Exception as e:
        print(f'Error al procesar el archivo {file}: {str(e)}')
        fallidos.append(file)
        # Aquí puedes almacenar el nombre del archivo con errores en un registro si es necesario.

    print('SE HA COMPLETADO UN: ',porcentaje,'%')
    

print('Proceso finalizado')

print('Lista de Archivos fallidos')
print('Cantidad: ',len(fallidos))
print(fallidos)