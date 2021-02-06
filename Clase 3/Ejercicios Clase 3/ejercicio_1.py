# TODO: crear una función que reciba al menos dos parámetros: nombre del archivo a crear y una listas de fechas
# Las fechas deberán tener el formato YYYY-MM-DD, y deberán ser strings. Ejemplo: ["2021-01-31"]
# La función deberá crear el archivo con el nombre indicado y agregar el nombre del mes de cada fecha en cada línea
# Ejemplo: ["2021-01-31"] deberá escribir "Enero" en el archivo
# Para resolver el ejercicio deberá investigar sobre la librería "datetime", standard de Python

# TODO: modificar la función anterior para que utilice el archivo si ya existe, en vez de crearlo de nuevo.

from datetime import date

fechas = []
# Ruta del archivo de salida
ruta_y_nombre = r"C:\Users\Federico\Documents\GitHub\python-rpa-calyx\Clase 3\Ejercicios Clase 3\salida_ejercicio_1.txt"


def carga_lista_fechas(año, mes, dia):

    fechas.append(date(año, mes, dia))


carga_lista_fechas(1995, 7, 9)
carga_lista_fechas(1999, 8, 9)
carga_lista_fechas(2002, 12, 9)


def paso_a_mes(mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses[mes-1]


def archivo_fecha(nombre_archivo, lista_fechas):
    with open(nombre_archivo, "a+") as file:
        for fecha in lista_fechas:  # Recorro la lista llamando a la funcion paso a mes pasandole el valor en numero de cada mes
            file.write(paso_a_mes(fecha.month)+'\n')


archivo_fecha(ruta_y_nombre, fechas)
