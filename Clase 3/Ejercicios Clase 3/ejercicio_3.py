# TODO: crear una función que dado un patrón busque todos los archivos que cumplan dicho patrón y los elimine
# Dicha función debe poder ejecutarse dos veces sin problemas
# Para resolver el ejercicio deberá investigar sobre las librerías "glob" y "os"
import glob
import os as file
from os import remove

# al poner el *.extension hago referencia a todos los archivos con determinada extension
# Poniendo *.* traigo todos los archivos sin diferenciar extension


# Traigo una lista con la cantidad de archivos con extension .py en el directorio definido en ruta


def borrar_archivo_ejercicio_clase_3(extension):
    ruta = r'C:\Users\Federico\Documents\GitHub\python-rpa-calyx\Clase 3\Ejercicios Clase 3\*.txt'
    lista_txt = glob.glob(ruta)

    for txt in lista_txt:
        if txt.endswith(extension):
            try:
                file.remove(txt)
                print(f"El archivo {txt} ha sido eliminado")

            except:
                # Preguntar porque no entra a la excepcion en la segunda vuelta
                print("Los archivos no existen")


borrar_archivo_ejercicio_clase_3(".txt")
