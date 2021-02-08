# TODO: crear una función que cree una carpeta cuyo nombre sea la fecha del día con el formato YYYY-MM-DD
# Ejemplo: 2021-01-31

import os
import datetime
from datetime import date

# directorio_con_subdirectorios=r'C:\Users\fedestf\Desktop\asd1\asd2\asd3' prueba sobre subdirectorios
direccion = r'C:\Users\fedestf\Desktop'


def crear_carpeta(ruta):

    directorio = os.path.join(ruta, str(date.today()))

    if not os.path.exists(directorio):  # si no existe el directorio
        # Crea la carpeta o todos los sub directorios necesarios si no existe
        os.makedirs(directorio)


crear_carpeta(direccion)
