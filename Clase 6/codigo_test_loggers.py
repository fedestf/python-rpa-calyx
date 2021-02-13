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


def suma_prueba(num1, num2):
    try:
        resultado = num1 + num2
        debug_test("asdadasd")
        return resultado
    except Exception as e:
        error_test(e)


suma_prueba(2, 2)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in lista:
#     try:
#         print(i+"s")
#         debug_test("Se ejecuto bien hasta {} ".format(i))
#     except Exception as e:
#         error_test(e)

# Preguntar porque empieza a escribir mas de una vez las cosas cuando deberia escribirla solamente una vez
