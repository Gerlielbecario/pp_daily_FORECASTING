import os
import gzip

folder_path = '/home/fernando.huaranca/datos/Datos_GSMAP/daily_G_v8'  # Ruta de la carpeta actual

print("Verificando la validez de los archivos Gzip en la carpeta:", folder_path)

invalid_gzips = []

for id,filename in os.listdir(folder_path):
    print(filename)

    if filename.endswith(".gz"):
        file_path = os.path.join(folder_path, filename)
        try:
            with gzip.open(file_path, "rb") as f:
                f.read(1)
        except gzip.BadGzipFile:
            invalid_gzips.append(filename)

if invalid_gzips:
    print("Archivos Gzip no válidos:")
    for filename in invalid_gzips:
        print(filename)
else:
    print("Todos los archivos Gzip son válidos.")
