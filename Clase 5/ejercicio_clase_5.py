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

df_consola = df[df["console"] == "PC"][["console", "title",
                                        "genre", "publisher"]]
df_ps = df[df["console"] == "PS"][["console", "title",
                                   "genre", "publisher"]]

# traigo los que estan en ambos
df_test = df_accion.merge(df_sandbox, on="title")
#df_test = df_accion.merge(df_sandbox, on=["console"]["pc"])

df_test.to_excel(
    r'C:\Users\fedestf\Documents\GitHub\python-rpa-calyx\Clase 5\test.xlsx', index=False)

print(df_test)

# result = pd.merge(user_usage,
#                  user_device[['use_id', 'platform', 'device']],
#                  on='use_id')


# print(df)


# Luego se debe obtener un tercer dataframe, a partir de los
# dos anteriores, que contenga aquellos juegos que esten presentes
# en PC (o alguna PS si no hay ocurrencias). Dicho dataframe
# debe ser guardado en formato excel.


# Una vez generado el excel, se deberá leer el mismo y loguear
# la información disponible en cada fila.
