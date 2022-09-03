import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

datos1 = np.random.randn(100)
sns.distplot(datos1, rug=False, hist=False)
mpl.pyplot.show()

argumentos_curva = {'color':'black', 'label':'Curva'}
argumentos_histograma = {'color':'grey', 'label':'Histograma'}

sns.distplot(datos1, bins=25, kde_kws=argumentos_curva, hist_kws=argumentos_histograma)
mpl.pyplot.show()

serie = pd.Series(datos1)
sns.distplot(serie, bins=25, color='green')
mpl.pyplot.show()