from errno import EKEYEXPIRED
from traceback import print_tb
import pandas as pd
import numpy as np

lista_valores = [1,2,3]
lista_indices = ['a','b','c']
serie = pd.Series(lista_valores,index=lista_indices)
print(serie)
print(serie.index)
print(serie.index[0])

lista_notas = [[6,7,8],[4,5,6],[9,6,8]]
lista_asignaturas = ["Mates", "Literatura", "Historia"]
lista_nombres = ["Dani", "Marta", "Antonio"]
dataframe = pd.DataFrame(lista_notas, index=lista_asignaturas, columns=lista_nombres)
print(dataframe)
print(dataframe.index)
print("\n")

#Delete elements in series:
ejemplo = pd.Series(np.arange(4), index=['a','b','c','d'])
ejemplo = ejemplo.drop('c')
print(ejemplo)
print("\n")

#Select elements in series:
ejemplo = ejemplo * 2
print(ejemplo)
print("\n")
print(ejemplo["a"])
print(ejemplo[2])
print(ejemplo[0:2])
print(ejemplo["a":"b"])
print(ejemplo[ejemplo > 3])
ejemplo[ejemplo > 3] = 8
print(ejemplo)
print("\n")

#Delete elements in dataframes:
valores = np.arange(9).reshape(3,3)
indices = ['a','b','c']
columnas = ["col1","col2","col3"]
dataframe = pd.DataFrame(valores, index=indices, columns=columnas)
dataframe = dataframe.drop('b')
print(dataframe)
dataframe = dataframe.drop('col2', axis=1)
print(dataframe)
print("\n")

#Select elements in dataframes
elementos_dataframe = np.arange(25).reshape(5,5)
rows = ['i1','i2','i3','i4','i5']
cols = ['col1','col2','col3','col4','col5']
dataframe = pd.DataFrame(elementos_dataframe, index=rows, columns=cols)
print(f"{dataframe}\n")
print(dataframe['col2'])
print(dataframe['col2']['i2'])
print(dataframe[['col2','col4']])
print(dataframe[dataframe['col2'] > 15])
print("\n")
print(dataframe > 20)
print(dataframe.loc['i1'])#Busqueda por indice
print(dataframe.loc['i2']['col4'])