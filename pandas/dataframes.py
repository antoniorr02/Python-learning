import pandas as pd
import webbrowser

website = 'https://github.com/antoniorr02/Python-learning'
webbrowser.open(website)

#Problems with dataframe management, so I commented all.
#dataframe_ej = pd.read_clipboard()
#print(dataframe_ej)
#dataframe_ej.columns
#dataframe_ej.loc[5]
#dataframe_ej['nombre_columna']
#dataframe_ej.head(4)
#dataframe_ej.tail(5)

asignaturas = ["matematicas", "lengua", "historia"]
notas = [8,5,9]
diccionario = {'Asignaturas':asignaturas, 'Notas':notas}
dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)