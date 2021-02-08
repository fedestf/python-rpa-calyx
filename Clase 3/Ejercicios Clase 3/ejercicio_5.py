# TODO: crear una función que cree una carpeta cuyo nombre sea la fecha del día con el formato YYYY-MM-DD
# Ejemplo: 2021-01-31

import os
import datetime
from datetime import date

# nombre_carpeta = os.path.join(fecha.today())

direccion = r'C:\Users\fedestf\Desktop'


def crear_carpeta(ruta):

    directorio = os.path.join(ruta, str(date.today()))

    if not os.path.exists(directorio):
        # Crea todos los sub directorios necesarios si no existe
        os.makedirs(directorio)


crear_carpeta(direccion)
