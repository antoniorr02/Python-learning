import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

vuelos = sns.load_dataset('flights')
print(vuelos.head())
vuelos = vuelos.pivot('month', 'year', 'passengers')
print(vuelos)

sns.heatmap(vuelos, annot=True, fmt='d')
mpl.pyplot.show()

valor_central = vuelos.loc['May'][1956]

sns.heatmap(vuelos, center=valor_central, annot=True, fmt='d')
mpl.pyplot.show()

sns.heatmap(vuelos, center=valor_central, annot=True, fmt='d', cbar_kws={'orientation':'horizontal'})
mpl.pyplot.show()