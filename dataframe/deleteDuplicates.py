import pandas as pd

valores = [[1,2],[1,2],[5,6],[5,8]]
indices = list('nmop')
columnas = ['valor1','valor2']
dataframe = pd.DataFrame(valores, index=indices, columns=columnas)
print(dataframe)

dataframe = dataframe.drop_duplicates()
print(dataframe)

dataframe2 = dataframe.drop_duplicates(['valor1'], keep='last')#si quitamos keep se quedaria o en lugar de p
print(dataframe2)