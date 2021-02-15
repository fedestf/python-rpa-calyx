import logging
from settings import RUTA
import os
from datetime import date


carpeta_debug = os.path.join(RUTA, "Debug")

if not os.path.exists(carpeta_debug):
    os.makedirs(carpeta_debug)

ruta = os.path.join(carpeta_debug,
                    date.today().strftime("%d-%m-%Y") + ".txt")

logger_debug = logging.getLogger("test_debug")
file_hand = logging.FileHandler(ruta)
format_hand = logging.Formatter(
    '%(levelname)s : %(asctime)s.%(msecs)03d -  [%(funcName)s]- %(message)s', "%d-%m-%Y %H:%M:%S")
file_hand.setFormatter(format_hand)  # Reutilizo el formatter
logger_debug.addHandler(file_hand)
logger_debug.setLevel(logging.DEBUG)
