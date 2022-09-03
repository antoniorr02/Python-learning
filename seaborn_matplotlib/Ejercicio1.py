import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datos = np.random.randn(1000)

plt.hist(datos)
plt.show()

sns.boxplot(datos)
plt.show()