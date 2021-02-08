# TODO: crear una función que reciba dos rutas (paths), y que mueva los archivos de la primera a la segunda
# Dicha función debe poder ejecutarse dos veces sin problemas
# Para resolver el ejercicio deberá investigar sobre las librerías "glob" y "os"

import glob
import os
import shutil


origen = r'C:\Users\Federico\Desktop\Python RPA Calyx'
destino = r'C:\Users\Federico\Desktop\Python RPA Calyx\test'


def mover_archivo(origen, destino):

    archivos_en_directorio = os.listdir(origen)
    archivos_filtrados = []
    cantidad_archivos = 0

    for archivo in archivos_en_directorio:

        try:

            if archivo.endswith('.py'):  # Filtro por extension
                archivos_filtrados.append(archivo)
                src = os.path.join(origen, archivo)
                dst = os.path.join(destino, archivo)
                shutil.move(src, dst)
                cantidad_archivos += 1
                print("Se movio correctamente el archivo : ", archivo)

        except Exception as e:  # Esta excepcion es arrojada si no filtro por extension
            print("El directorio contiene una carpeta : \n "+str(e))
            print("Los demas archivos ya se han movido")


mover_archivo(origen, destino)


# for archivo in archivos_en_directorio:

#     try:

#         src = os.path.join(origen, archivo)
#         dst = os.path.join(destino, archivo)
#         shutil.move(src, dst)
#         print("Se movio correctamente el archivo : ", archivo)

#     except Exception as e:

#         print("El directorio contiene una carpeta : \n "+str(e))
#         print("Los demas archivos ya se han movido")

# https://docs.python.org/es/3/library/shutil.html
