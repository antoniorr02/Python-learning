import pandas as pd
import numpy as np

#Las funciones que se utilizan aquí, son aplicables a los dataframes.

lista = ['1','2',np.nan, '4']
serie = pd.Series(lista, index=list('abcd'))
print(serie)
print(serie.isnull())
print(serie.dropna())
print(serie.fillna(0))