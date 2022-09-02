import pandas as pd
import numpy as np

valores = [[1,2],[1,2],[5,6],[5,8]]
indices = list('nmop')
columnas = ['valor1','valor2']
dataframe = pd.DataFrame(valores, index=indices, columns=columnas)
print(dataframe)

new_index = dataframe.index.map(str.upper)
dataframe.index = new_index
print(dataframe)

dataframe = dataframe   .rename(index=str.lower)
print(dataframe)

nuevos = {'n':'a', 'm':'b', 'o':'c', 'p':'d'}
dataframe = dataframe.rename(index=nuevos)
print(dataframe)
print("\n")

nuevo = {'a':'xd'}
dataframe.rename(index=nuevo, inplace=True)
print(dataframe)