import logging
from settings import RUTA
import os
from datetime import date

# logging.basicConfig(filename=r"C:\Users\fedestf\Documents\GitHub\python-rpa-calyx\Clase 6\logs.txt",
#                     format="'%(levelname)s : %(asctime)s - %(message)s'")


# Custom logger

# Creo subdirectorio (en caso de que no exista) a partir de la ruta de logs definida en settings
# carpeta_error = os.path.join(RUTA, "Error")

# # Declaro la ruta  y el nombre del archivo para pasarlo al file handler
# # Ahora mi ruta es carpeta
def error_test(error):

    carpeta_error = os.path.join(RUTA, "Error")
    if not os.path.exists(carpeta_error):
        os.makedirs(carpeta_error)

    ruta = os.path.join(carpeta_error, str(date.today()))
    logger_custom = logging.getLogger("test_custom")
    file_hand = logging.FileHandler(ruta)
    format_hand = logging.Formatter(
        '%(levelname)s : %(asctime)s - %(message)s')
    file_hand.setFormatter(format_hand)
    logger_custom.addHandler(file_hand)
    logger_custom.exception(error)


# ---------------------TEST DEBUG--------------------------------------


def debug_test(mensaje):
    carpeta_debug = os.path.join(RUTA, "Debug")

    if not os.path.exists(carpeta_debug):
        os.makedirs(carpeta_debug)

    ruta = os.path.join(carpeta_debug, str(date.today()))
    logger_custom = logging.getLogger("test_debug")
    file_hand = logging.FileHandler(ruta)
    format_hand = logging.Formatter(
        '%(levelname)s : %(asctime)s - %(message)s')
    file_hand.setFormatter(format_hand)
    logger_custom.addHandler(file_hand)
    logger_custom.setLevel(logging.DEBUG)
    logger_custom.debug(mensaje)


# logger_custom.info("INFO")
# logger_custom.debug("DEBUG")
# logger_custom.critical("CRITICAL")
# logger_custom.error("ERROR")
# logger_custom.warning("WARNING")
