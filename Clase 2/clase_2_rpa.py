numeros = [1, 2, 3, 4, 5]

numeros_dobles = []

for numero in numeros:
    numeros_dobles.append(numero*2)

print(numeros_dobles)

# Comprenhension list , poner primero la operacion en una lista
numeros_triples = [numero*3 for numero in numeros]
print(numeros_triples)

# Metodo insert
metodo_insert = [1, 2, 3, 4]

metodo_insert.insert(0, 0)  # inserta un 0 en la lista en la posicion 0

# Metodo pop devuelve el ultimo elemento y lo saca

# inverso de una lista[::-1]

print(numeros[::-1])

# Los sets no tienen objetos repetidos
