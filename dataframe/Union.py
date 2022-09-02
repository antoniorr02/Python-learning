import pandas as pd

dataframe1 = pd.DataFrame({'c1':['1','2','3'], 'clave':['a','b','c']})
print(dataframe1)
dataframe2 = pd.DataFrame({'c2':['4','5','6'], 'clave':['b','c','e']})
print(dataframe2)
dataframe3 = pd.merge(dataframe1, dataframe2, on='clave') #En este caso on='clave' se podría omitir (unica columna en comun)
print(dataframe3)
dataframe4 = pd.merge(dataframe1, dataframe2, on='clave', how='left')
print(dataframe4)
dataframe4 = pd.merge(dataframe1, dataframe2, on='clave', how='right')
print(dataframe4)
dataframe4 = pd.merge(dataframe1, dataframe2, on='clave', how='outer')
print(dataframe4)