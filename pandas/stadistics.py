import pandas as pd
import numpy as np

lista_valores = [[1,2,3],[4,5,6]]
lista_indices = ['a','b']
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=list('123'))
print(dataframe)
print("\n")
print(dataframe.sum())
print(dataframe.sum(axis=1))
print(dataframe.min()) #minimo valor en cada fila
print(dataframe.max())
print(dataframe.idxmin())
print(dataframe.describe())