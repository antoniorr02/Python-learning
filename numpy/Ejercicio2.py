import numpy

lista1 = [10,11,12,13,14,15,16,17,18,19]
lista2 = [50,51,52,53,54,55,56,57,58,59]
lista = (lista1, lista2)

matriz = numpy.array(lista)
print(f"{matriz}\n")
matriz2 = matriz * 2
print(matriz2)