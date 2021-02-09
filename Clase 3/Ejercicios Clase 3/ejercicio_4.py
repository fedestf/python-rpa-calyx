# TODO: crear una función que reciba dos rutas (paths), y que mueva los archivos de la primera a la segunda
# Dicha función debe poder ejecutarse dos veces sin problemas
# Para resolver el ejercicio deberá investigar sobre las librerías "glob" y "os"

import glob
import os
import shutil


origen = r'C:\Users\Federico\Desktop\Origen'
destino = r'C:\Users\Federico\Desktop\Destino'


def mover_archivo(origen, destino):

    archivos_en_directorio = os.listdir(origen)

    for archivo in archivos_en_directorio:

        try:

            if archivo.endswith('.py'):  # Filtro por extension

                src = os.path.join(origen, archivo)
                dst = os.path.join(destino, archivo)
                shutil.move(src, dst)
                print("Se movio correctamente el archivo : ", archivo)

        # Esta excepcion es arrojada si no filtro por extension (sucedia cuando habia una carpeta de por medio)
        except Exception as e:

            print("Error : \n "+str(e))
            print("Los demas archivos ya se han movido")


mover_archivo(origen, destino)


# https://docs.python.org/es/3/library/shutil.html
