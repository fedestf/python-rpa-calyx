# Generar a partir del archivo "vgsales.csv" dos dataframes,
# uno deberá contener a los juegos cuyo género sea de Acción
# y el otro a los del género Sandbox. En ambos deben quedar
# solamente las columnas: title, genre, publisher, console.
import pandas as pd

df = pd.read_csv(
    r'C:\Users\fedestf\Documents\GitHub\python-rpa-calyx\Clase 5\vgsales.csv')


df_accion = df[df["genre"] == "Action"][[
    "title", "genre", "publisher", "console"]]

df_sandbox = df[df["genre"] == "Sandbox"][[
    "title", "genre", "publisher", "console"]]


# Luego se debe obtener un tercer dataframe, a partir de los
# dos anteriores, que contenga aquellos juegos que esten presentes
# en PC (o alguna PS si no hay ocurrencias). Dicho dataframe
# debe ser guardado en formato excel.


df3 = df_accion.query('console=="PC" or console=="PS"')
df4 = df_sandbox.query('console=="PC" or console=="PS"')

print(df3["console"] == "PS")


# Una vez generado el excel, se deberá leer el mismo y loguear
# la información disponible en cada fila.
