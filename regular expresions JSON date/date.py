from calendar import month
from datetime import datetime
from re import S

fechaYhora = datetime.now()

print(fechaYhora)

anio = fechaYhora.year
mes = fechaYhora.month
dia = fechaYhora.day

hora = fechaYhora.hour
minutos = fechaYhora.minute
segundos = fechaYhora.second
microsegundos = fechaYhora.microsecond

print(f"La hora es {hora}:{minutos}:{segundos}")