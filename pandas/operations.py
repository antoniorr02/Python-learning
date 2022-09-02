import pandas as pd
import numpy as np

serie1 = pd.Series([0,1,2], index=['a','b','c'])
serie2 = pd.Series([3,4,5,6], index=['a','b','c','d'])
serie = serie1 + serie2
print(serie)
print("\n")

lista_valores = np.arange(4).reshape(2,2)
lista_indices = list('ab')
lista_columnas = list('12')
datadframe = pd.DataFrame(lista_valores, lista_indices, lista_columnas)

lista_valores2 = np.arange(9).reshape(3,3)
lista_indices2 = list('abc')
lista_columnas2 = list('123')
datadframe2 = pd.DataFrame(lista_valores2, lista_indices2, lista_columnas2)

datadframe3 = datadframe + datadframe2
print(datadframe3)
print("\n")

dataframe4 = datadframe.add(datadframe2, fill_value=0) #No está rellenando con 0s?
print(dataframe4)

combinacion_aleatoria = np.random.permutation(3)
print(combinacion_aleatoria)
dataframe4 = dataframe4.take(combinacion_aleatoria)
print(dataframe4)