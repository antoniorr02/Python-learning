#It works with poblacion.xlsx
import pandas as pd

datos = pd.read_clipboard()
print(datos)
print("\n")
print(datos.columns)
print("\n")
print(datos.loc[0])
print("\n")
print(datos['Superficie'])
print("\n")
datos = pd.DataFrame(datos)
print(datos[['Continente','Población']])
print(datos.loc[0:3, ['Continente','Población']])
print("\n")
print(datos.head(3))
print("\n")
print(datos.tail(2))