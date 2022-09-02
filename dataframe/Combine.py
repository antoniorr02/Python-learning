import pandas as pd
import numpy as np

#series
serie1 = pd.Series([1,2,np.nan])
serie2 = pd.Series([4,5,6])
serie3 = serie1.combine_first(serie2)
print(serie3)

#dataframe
dataframe1 = pd.DataFrame([1,2,np.nan])
dataframe2 = pd.DataFrame([4,5,6])
dataframe3 = dataframe1.combine_first(dataframe2)
print(dataframe3)