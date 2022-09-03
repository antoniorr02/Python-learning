import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

propinas = sns.load_dataset('tips')
print(propinas.head(10))

mpl.pyplot.show() #¿Se podría evitar esta línea?

sns.lmplot(x='total_bill',y='tip',data=propinas)
mpl.pyplot.show() #No entiendo porque no se muestra este gráfico si no hago lo de la linea 9

sns.lmplot(x='total_bill',y='tip',data=propinas, fit_reg=False, scatter_kws={'marker':'o', 'color':'green'}, line_kws={'color':'blue'})
mpl.pyplot.show()

propinas['porcentaje'] = 100 * propinas['tip'] / propinas['total_bill']
print(propinas.head())
sns.lmplot(x='size',y='porcentaje',data=propinas)
mpl.pyplot.show()
sns.lmplot(x='size',y='porcentaje',data=propinas, hue='sex', markers=['x','o'])
mpl.pyplot.show()
sns.lmplot(x='size',y='porcentaje',data=propinas, hue='day')
mpl.pyplot.show()