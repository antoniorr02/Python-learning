import pandas as pd

precios = [42,55,48,23,5,21,88,34,26]
rango = [10,20,30,40,50,60,70,80,90,100]
precios_con_rangos = pd.cut(precios, rango)
print(precios_con_rangos)

print(pd.value_counts(precios_con_rangos))