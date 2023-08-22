#Una funcion a la que se le entrega un valor de step y lo transforma en
#una fecha.
#Una funcion a la que se le entrega una fecha y puede transformarlo
#en un step
#NOFUINCA
#Librerias

import os 
import numpy as np
from datetime import datetime, timedelta
import xarray as xr
#####################

#Archivo .grib que deseamos leer
file = 'apcp_sfc_2013031600_c00.grib2'

#Carpeta donde se encuentra el archivo
folder = '/home/fernando.huaranca/test_forecast'

#Ruta del archivo
path = os.path.join(folder,file)
print(path)
ds = xr.open_dataset(path)
##########


def convertir_step_a_fecha(n_step):
    # Convertir el valor de step en nanosegundos a timedelta
    valor = np.timedelta64(ds.step[n_step].values)
    
    # Calcular la fecha correspondiente sumando el step_timedelta a la fecha de inicio
    fecha_inicio = ds.time.values
    fecha = fecha_inicio + valor
    
    # Formatear la fecha en el formato deseado
    fecha_formateada = fecha.astype(datetime).strftime("%H:%M %d/%m/%Y")
    
    return fecha_formateada

# Ejemplo de uso

ds.time.values+np.timedelta64(ds.step[0].values)
step_ejemplo = ds.tp.step.values[0]


fecha_formateada = convertir_step_a_fecha(step_ejemplo)
print("Fecha formateada:", fecha_formateada)
