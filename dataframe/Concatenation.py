import atexit
import pandas as pd
import numpy as np

#arrays
array1 = np.arange(9).reshape(3,3)
array1 = np.concatenate([array1, array1])
print(array1)
print("\n")
array1 = np.concatenate([array1, array1], axis=1)
print(array1)
print("\n")

#series
serie1 = pd.Series([1,2,3], index=['a','b','c'])
serie2 = pd.Series([4,5,6], index=['d','e','f'])
serie = pd.concat([serie1, serie2], keys=['serie1', 'serie2'])
print(serie)

#dataframes
dataframe1 = pd.DataFrame(np.random.rand(3,3), columns=['a','b','c'])
dataframe2 = pd.DataFrame(np.random.rand(2,3), columns=['a','b','c'])
dataframe = pd.concat([dataframe1, dataframe2])
print(dataframe)
dataframe = pd.concat([dataframe1, dataframe2], ignore_index=True)
print(dataframe)