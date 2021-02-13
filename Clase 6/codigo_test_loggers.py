from libreria_logging import logger_error, logger_debug

try:
    1+"sss"
    logger_debug.debug("Ejecucion correcta")

except Exception as e:
    logger_error.exception(e)

try:
    resultado = 123+3
    logger_debug.debug("{}+{} = {}".format(123, 3, resultado))

except Exception as e:
    logger_error.exception(e)


def suma_prueba(num1, num2):
    try:
        resultado = num1 + num2
        logger_debug.debug("{}+{} = {} ".format(num1, num2, resultado))
        return resultado
    except Exception as e:
        logger_error.exception(e)


suma_prueba(2, 2)

lista = [1, 2, 3, 4, "k", 6, "7", 8, 9, 10]


def contar_hasta_10(lista):

    for i in lista:
        try:
            print(i+1)
            logger_debug.debug("Se ejecuto bien en la posicion {} ".format(i))
        except Exception as e:
            logger_error.exception(e)


contar_hasta_10(lista)
