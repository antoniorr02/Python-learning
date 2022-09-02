import pandas as pd
import numpy as np

lista_valores = range(4)
lista_indices = list('CABD')
serie = pd.Series(lista_valores, index=lista_indices)
serie = serie.sort_index()
print(serie)
serie = serie.sort_values()
print(serie)
print(serie.rank())

serie2 = pd.Series(np.random.rand(10))
print(serie2)
print(serie2.rank())