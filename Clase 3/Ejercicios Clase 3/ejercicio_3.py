# TODO: crear una función que dado un patrón busque todos los archivos que cumplan dicho patrón y los elimine
# Dicha función debe poder ejecutarse dos veces sin problemas
# Para resolver el ejercicio deberá investigar sobre las librerías "glob" y "os"
import glob
import os as file
from os import remove

# al poner el *.extension hago referencia a todos los archivos con determinada extension
# Poniendo *.* traigo todos los archivos sin diferenciar extension
ruta = r'C:\Users\Federico\Documents\GitHub\python-rpa-calyx\Clase 3\Ejercicios Clase 3\*.txt'

# Traigo una lista con la cantidad de archivos con extension .py en el directorio definido en ruta
lista_txt = glob.glob(ruta)

for txt in lista_txt:
    try:
        file.remove(txt)
    except:
        # Preguntar porque no entra a la excepcion en la segunda vuelta
        print("Los archivos no existen")

print(lista_txt)
