import pandas as pd
import numpy as np

valores = np.random.randint(0,100,50)
print(valores)
print("\n")
dataframe = pd.DataFrame(valores.reshape(5,10))
print(dataframe)
print("\n")
print(dataframe[dataframe>50])