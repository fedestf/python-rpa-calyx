# TODO: crear una función que cree una carpeta cuyo nombre sea la fecha del día con el formato YYYY-MM-DD
# Ejemplo: 2021-01-31

import os
import datetime
from datetime import date

# nombre_carpeta = os.path.join(fecha.today())
# directorio = os.path.join(
#    r'C:\Users\fedestf\Desktop', str(date.today()))


def crear_carpeta():

    directorio = os.path.join(
        r'C:\Users\fedestf\Desktop', str(date.today()))

    if not os.path.exists(directorio):
        os.makedirs(directorio)


# if directorio in r'C:\Users\fedestf\Desktop':
#    print("la carpeta ya existe")
