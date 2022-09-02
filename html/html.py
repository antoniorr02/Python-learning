import pandas as pd
import lxml

url='https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

dataframe = pd.io.html.read_html(url)
dataframe_futbol = dataframe[0]
dataframe_futbol = dataframe_futbol.drop('Notas',axis=1)
print(dataframe_futbol)