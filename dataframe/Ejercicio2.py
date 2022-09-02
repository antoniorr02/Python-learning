import pandas as pd
import numpy as np

array1 = np.random.randint(0,100,9)
array2 = np.random.randint(0,100,9)
array1 = array1.reshape(3,3)
array2 = array2.reshape(3,3)
print(array1)
print(array2)

dataframe1 = pd.DataFrame(array1)
dataframe2 = pd.DataFrame(array2)
dataframe3 = pd.concat([dataframe1,dataframe2], ignore_index=True)
print(dataframe3)