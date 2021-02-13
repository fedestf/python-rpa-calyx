import logging
from settings import RUTA
import os
# logging.basicConfig(filename=r"C:\Users\fedestf\Documents\GitHub\python-rpa-calyx\Clase 6\logs.txt",
#                     format="'%(levelname)s : %(asctime)s - %(message)s'")

# variable_prueba = 123456

# try:
#     "andrea"+variable_prueba
# except Exception as e:
#     logging.exception("Eso no se puede resolver")

# Custom logger
ruta = os.path.join(RUTA, "test_custom.txt")
logger_custom = logging.getLogger("test_custom")
file_hand = logging.FileHandler(ruta)
format_hand = logging.Formatter('%(asctime)s - %(message)s')
file_hand.setFormatter(format_hand)
logger_custom.addHandler(file_hand)

logger_custom.error("TESTEANDO ANDO")
