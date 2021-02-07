# TODO: crear una función que reciba dos rutas (paths), y que mueva los archivos de la primera a la segunda
# Dicha función debe poder ejecutarse dos veces sin problemas
# Para resolver el ejercicio deberá investigar sobre las librerías "glob" y "os"

import glob
import os
import shutil


ruta_analisis_extension = r'C:\Users\Federico\Desktop\Python RPA Calyx\*.py'
origen = r'C:\Users\Federico\Desktop\Python RPA Calyx'
destino = r'C:\Users\Federico\Desktop\Python RPA Calyx\test'
lista_txt = []  # glob.glob(ruta_analisis_extension)


test = os.path.splitext(origen)
print(test[0], test[1])

# for archivo in archivos_en_directorio:
#     lista_txt.append(archivo)

# for archivo in archivos_en_directorio:

#     try:
#         src = os.path.join(origen, archivo)
#         dst = os.path.join(destino, archivo)
#         shutil.copy2(src, dst)
#         print("Correcto")
#     except Exception as e:
#         print(e)
#         # print("Falló")
#         # print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

for txt in lista_txt:
    try:
        src = os.path.join(origen, txt)
        dst = os.path.join(destino, txt)
        shutil.copy(src, dst)
        print("Archivo ok")
    except:
        # Preguntar porque no entra a la excepcion en la segunda vuelta
        print("Los archivos no existen")
