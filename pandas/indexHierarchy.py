from traceback import print_tb
import pandas as pd
import numpy as np

lista_valores = np.random.rand(6)
lista_indices = [[1,1,1,2,2,2],['a','b','c','a','b','c']]
series = pd.Series(lista_valores, index=lista_indices)
print(series)
print(series[1])
print(series[1]['b'])

dataframe = series.unstack()
print(dataframe)

dataframeTOserie = dataframe.stack()
print(dataframeTOserie)