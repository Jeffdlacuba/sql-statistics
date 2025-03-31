import pandas as pd

# importar los archivos
df_company_trips = pd.read_csv("../datasets/moved_project_sql_result_01.csv")
# company_name: nombre de la empresa de taxis
# trips_amount: el número de viajes de cada compañía de taxis el 15 y 16 de noviembre de 2017.

df_location_averae_trips = pd.read_csv(
    "../datasets/moved_project_sql_result_04.csv")
# dropoff_location_name: barrios de Chicago donde finalizaron los viajes
# average_trips: el promedio de viajes que terminaron en cada barrio en noviembre de 2017.

df_ts_weather_duration = pd.read_csv(
    "../datasets/moved_project_sql_result_07.csv")
# start_ts: fecha y hora de la recogida
# weather_conditions: condiciones climáticas en el momento en el que comenzó el viaje
# duration_seconds: duración del viaje en segundos

# estudiar los datos que contienen
df_company_trips.info()
df_location_averae_trips.info()

# identificar los 10 principales barrios en términos de finalización del recorrido
df_location_averae_trips.head(10)

# hacer gráficos: empresas de taxis y número de viajes, los 10 barrios principales por número de finalizaciones


# Prueba la hipótesis:
# "La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos".
# Decide por tu cuenta dónde establecer el nivel de significación (alfa).

# Explica:
# cómo planteaste las hipótesis nula y alternativa
# qué criterio usaste para probar las hipótesis y por qué


# ¿Cómo será evaluado mi proyecto?
# Esto es lo que buscará el revisor del proyecto al evaluar tu proyecto:

# cómo recuperas los datos del sitio web
# cómo creas slices de datos
# cómo agrupas los datos
# si usas correctamente los diversos métodos para combinar datos
# cómo formulas las hipótesis
# qué criterios utilizas para probar las hipótesis y por qué
# a qué conclusiones llegas
# si dejas comentarios en cada paso
