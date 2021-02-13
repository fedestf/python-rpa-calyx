import logging
from settings import RUTA
import os
from datetime import date
from libreria_logging import debug_test, error_test

try:
    1+"sss"
    debug_test("Ejecutado correctamente")
except Exception as e:
    error_test(e)

try:
    1+2
    debug_test("VAPAI")
except Exception as e:
    error_test(e)
