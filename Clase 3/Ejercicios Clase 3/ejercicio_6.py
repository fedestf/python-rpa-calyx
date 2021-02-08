# TODO: crear una función que reciba la función dummy (y sus parámetros) e imprima por pantalla
# El tiepmo que demoró en ejecutar dicha función
# Para resolver el ejercicio deberá utilizar la librería "time"

import time


def dummy(time_to_sleep):

    for i in range(10):
        # por cada iteración el script "duerme" durante
        # el tiempo indicado en "time_to_sleep"
        time.sleep(time_to_sleep)


def funcion_dormir(tiempo):

    print(dummy(tiempo))


funcion_dormir(10)
