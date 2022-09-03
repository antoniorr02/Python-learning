import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datos = np.random.randint(0,500,100)

plt.boxplot(datos)
plt.show()

sns.boxplot(datos)
plt.show()