from termios import N_MOUSE
import numpy
import pandas

clases = ["clase1", "clase2", "clase3"]
n_clase1 = numpy.random.randint(0,10)
n_clase2 = numpy.random.randint(0,10)
n_clase3 = numpy.random.randint(0,10)
#alumnos = numpy.random.randint(0,10,3) // Es equivalente, da 3 valores (ultimo parametro)

serie = pandas.Series([n_clase1,n_clase2,n_clase3], index=clases)
print(serie)
print(f"El numero de alumnos de la clase 2 es: {serie['clase2']}")