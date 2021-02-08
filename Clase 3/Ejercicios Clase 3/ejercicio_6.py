# TODO: crear una función que reciba la función dummy (y sus parámetros) e imprima por pantalla
# El tiepmo que demoró en ejecutar dicha función
# Para resolver el ejercicio deberá utilizar la librería "time"
from datetime import datetime
import time


def dummy(time_to_sleep):

    for i in range(10):

        time.sleep(time_to_sleep)


def calculo_tiempo_dummy(tiempo_dummy):
    tiempo_inicial = datetime.now()

    dummy(tiempo_dummy)

    tiempo_final = datetime.now()

    print(tiempo_final - tiempo_inicial)


calculo_tiempo_dummy(1)
