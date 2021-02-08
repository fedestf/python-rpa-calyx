# Ejercicio 1

numeros = [1, 2, 3, 4, 5]
numerosLetras = [
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco"
]

# TODO: Crear un diccionario donde el key:value corresponda a la palabra y su correspondiente número

dic_numeros = {}

for numero in numeros:
    dic_numeros[numero] = numerosLetras[numero-1]

print(dic_numeros)

# Ejercicio 2

palabras = ["python", "rpa", "calyx", "curso",
            "jupyter", "windows", "lionel hutz"]
# TODO: Crear un diccionario donde el key:value corresponda a la palabra y
# el value sea el texto "La palabra PALABRA posee: X letras"
# Ejemplo: {"python": "La palabra python posee: 6 letras"}
# HACERLO EN CÓDIGO NO MANUALMENTE

dic_palabras = {}

for palabra in range(0, len(palabras)):
    dic_palabras[palabras[palabra]] = (
        'La palabra tiene {} letras'.format(len(palabras[palabra])))  # usar metodo replace para quitar espacios

print(dic_palabras)

# Ejercicio 3

numeros_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# TODO: Iterar la lista y obtener una tupla que contenga los elementos cada 2 saltos
# Hacerlo desde el íncide 0 y el índice 1
# Ejemplo: la tupla quedaría (1, 3, 5, 7, 9)

# hacer con range asi no carga dos veces en memoria
num_tupla_impar = tuple(numeros_10[0::2])
num_tupla_par = tuple(numeros_10[0::2])
print(num_tupla_impar, num_tupla_par)

# Ejercicio 4

diccionario = {
    "acciones": {
        "longitud": len,
        "list": list,
        "set": set,
        "tuple": tuple,
    },
    "datos": {
        "longitud": "Probando diccionarios",
        "list": {1, 2, 3, 4, 5},
        "set": [1, 2, 3, 4, 5],
        "tuple": [1, 2, 3, 4, 5]
    }
}

# TODO: Ejecutar cada acción con su correspondiente dato y agregarlo a una lista vacía
# Ejemplo: acciones->mostrar debería ejecutar datos->mostrar. Esto imprimirá en pantalla "Probando diccionarios" y
# lo agregará a una lista
lista_resultado = []

for key in diccionario["acciones"]:  # Accedo a las keys del diccionario acciones
    # con las keys del diccionario acciones paso el valor de los datos que tienen la misma key
    lista_resultado.append(

        diccionario["acciones"][key](diccionario["datos"][key])
    )


print(lista_resultado)
