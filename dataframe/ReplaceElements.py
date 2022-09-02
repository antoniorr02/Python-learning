import pandas as pd

valores = [[1,2],[1,2],[5,6],[5,8]]
indices = list('nmop')
columnas = ['valor1','valor2']
dataframe = pd.DataFrame(valores, index=indices, columns=columnas)
print(dataframe)

dataframe = dataframe.replace(1,6)
print(dataframe)

dataframe = dataframe.replace({6:2, 5:4})
print(dataframe)