from libreria_logging import debug_test, error_test

# try:
#     1+"sss"
#     debug_test("Ejecutado correctamente")
# except Exception as e:
#     error_test(e)

# try:
#     1+2
#     debug_test("VAPAI")
# except Exception as e:
#     error_test(e)


# def suma_prueba(num1, num2):
#     try:
#         resultado = num1 + num2
#         debug_test("asdadasd")
#         return resultado
#     except Exception as e:
#         error_test(e)


# print(suma_prueba(2, 2))
lista = [1, "GASasA", 2, "GASasA", 3, 4, 5, "GASasA"]

for elemento in lista:
    try:
        print(elemento+"KK")
        debug_test("Se ejecuto bien hasta {} ".format(elemento[0]))
    except Exception as e:
        error_test(e)
