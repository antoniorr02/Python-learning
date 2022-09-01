#Series:
import pandas as pd
serie1 = pd.Series([3,5,7])
print(serie1)
print("\n")

asignaturas = ["matematicas", "lengua", "historia"]
notas_dani = [8,5,9]
serie_notas_dani = pd.Series(notas_dani, index=asignaturas)
serie_notas_dani.name = "Notas de Daniel"
serie_notas_dani.index.name = "Asignaturas de Daniel"
print(serie_notas_dani)
print(serie_notas_dani["historia"])
print(serie_notas_dani[serie_notas_dani >= 8])
print("\n")

diccionario = serie_notas_dani.to_dict()
print(diccionario)
print("\n")

serie = pd.Series(diccionario)
print(serie)
print("\n")

notas_antonio = [9,10,9]
serie_notas_antonio = pd.Series(notas_antonio, index=asignaturas)

notas_medias = (serie_notas_antonio + serie_notas_dani) / 2
print(f"Notas medias: {notas_medias}")