#Use: pip install seaborn

import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

datos1 = np.random.randn(100)
print(mpl.pyplot.hist(datos1, density=True))
#mpl.pyplot.show() // Si descomento esto no saldrían juntos los histogramas que arroja la linea 13
print(mpl.pyplot.hist(datos1, color='green', alpha=0.6, bins=20, density=True))
mpl.pyplot.show()

print(sns.distplot(datos1, color='red'))
mpl.pyplot.show()

datos2 = np.random.randn(1000)
datos3 = np.random.randn(1000)
sns.jointplot(datos2,datos3)
mpl.pyplot.show()

sns.jointplot(datos2,datos3, kind='hex')
mpl.pyplot.show()