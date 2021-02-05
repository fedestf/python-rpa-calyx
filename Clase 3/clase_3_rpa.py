# Archivos
# Manera correcta de abrir un archivo with open(ruta, modo) as file:
with open("example_clase3.txt", "a+") as file:
    file.write("\n kkkkkkkkkkkk")

# Excepciones funciones: TRACBACK,raise,assert
# Dentro de un for siempre considerar si considero un try y un except


with open("example_clase3.txt", "r") as file:
    try:
        # Fuerzo pasando el "asd" y la excepcion me imprime "error"
        print(file.read(""))
    except Exception as e:
        # raise(e)  # lanza el error y termina la ejecucion del programa
        print("error")
# Funciones (googear Abstraccion y reusabilidad, modularidad)


def palabras_numeros(titulo, numero=1, palabra="Testing"):

    def mayuscula(titulo):

        print(titulo.upper())

    mayuscula(titulo)
    print(numero, palabra)


palabras_numeros(
    titulo="federico lopez",
    numero=2,
    palabra="Tamo chequeando"
)
