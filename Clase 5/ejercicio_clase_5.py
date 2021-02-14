# Generar a partir del archivo "vgsales.csv" dos dataframes,
# uno deberá contener a los juegos cuyo género sea de Acción
# y el otro a los del género Sandbox. En ambos deben quedar
# solamente las columnas: title, genre, publisher, console.
import pandas as pd
from logger import logger_debug
from openpyxl import *

df = pd.read_csv(
    r'C:\Users\Federico\Documents\GitHub\python-rpa-calyx\Clase 5\vgsales.csv')


df_accion = df[df["genre"] == "Action"][[
    "title", "genre", "publisher", "console"]]

df_sandbox = df[df["genre"] == "Sandbox"][[
    "title", "genre", "publisher", "console"]]


# Luego se debe obtener un tercer dataframe, a partir de los
# dos anteriores, que contenga aquellos juegos que esten presentes
# en PC (o alguna PS si no hay ocurrencias). Dicho dataframe
# debe ser guardado en formato excel.

df3 = df_accion.query('console=="PC" or console=="PS"')[
    ["title", "console", "genre", "publisher"]]
df4 = df_sandbox.query('console=="PC" or console=="PS"')[
    ["title", "console", "genre", "publisher"]]

df5 = pd.concat([df3, df4])
df5.to_excel(
    r'C:\Users\Federico\Documents\GitHub\python-rpa-calyx\Clase 5\test.xlsx', index=False)


# Una vez generado el excel, se deberá leer el mismo y loguear
# la información disponible en cada fila.

wb = load_workbook(
    r'C:\Users\Federico\Documents\GitHub\python-rpa-calyx\Clase 5\test.xlsx')

sheet = wb['Sheet1']

for col in sheet.iter_cols():
    for row in sheet.iter_rows():
        print(row[0].value)
    # logger_debug.debug("{}".format(row[0].value))
