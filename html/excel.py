import pandas as pd

fichero_excel = pd.ExcelFile('./poblacion.xlsx')
dataframe = fichero_excel.parse('Hoja 1')
print(dataframe)
print(dataframe['Ciudad más poblada'][3])

fichero_csv = pd.read_csv('./poblacion.csv')
print(fichero_csv['Ciudad más poblada'][1])