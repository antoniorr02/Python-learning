import numpy

lista = numpy.arange(0,31)

principio = lista[0:10]

final = lista[20:30]

print(f"{lista}\n{principio}\n{final}")

for elemento in final:
    print(elemento)