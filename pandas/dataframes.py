#It works with poblacion.xlsx
import pandas as pd
import webbrowser

website = 'https://github.com/antoniorr02/Python-learning'
webbrowser.open(website)

#To use read_clipboard() you will need to install xclip.
dataframe_ej = pd.read_clipboard()
print(dataframe_ej)
dataframe_ej.columns
dataframe_ej.loc[2]
dataframe_ej['Superficie']
dataframe_ej.head(2)
dataframe_ej.tail(2)

asignaturas = ["matematicas", "lengua", "historia"]
notas = [8,5,9]
diccionario = {'Asignaturas':asignaturas, 'Notas':notas}
dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)