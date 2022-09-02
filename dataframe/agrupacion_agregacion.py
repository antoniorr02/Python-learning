from traceback import print_tb
import pandas as pd
import numpy as np

lista_valores = {'clave1':['x','x','y','y','z'],'clave2':['a','b','a','b','a'], 'datos1':np.random.rand(5), 'datos2':np.random.rand(5)}
dataframe = pd.DataFrame(lista_valores)
print(dataframe)
print("\n")

grupo1 = dataframe['datos1'].groupby(dataframe['clave1'])
print(grupo1)
print("\n")
print(grupo1.mean())
print("\n")

print(dataframe.agg(['sum','min']))