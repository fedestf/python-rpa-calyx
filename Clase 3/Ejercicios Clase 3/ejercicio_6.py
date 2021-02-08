# TODO: crear una función que reciba la función dummy (y sus parámetros) e imprima por pantalla
# El tiepmo que demoró en ejecutar dicha función
# Para resolver el ejercicio deberá utilizar la librería "time"

import time


def dummy(time_to_sleep):

    for i in range(10):

        time.sleep(time_to_sleep)


def calculo_tiempo_dummy(tiempo_dummy):  # hacer funcion con dos parametros

    tiempo_inicial = time.perf_counter()

    dummy(tiempo_dummy)

    tiempo_final = time.perf_counter()

    print(tiempo_final - tiempo_inicial)


calculo_tiempo_dummy(1)

# Utiliza *args para pasar de forma opcional a una función un número variable de argumentos posicionales.
# El parámetro *args recibe los argumentos como una tupla.
# Emplea **kwargs para pasar de forma opcional a una función un número variable de argumentos con nombre.
