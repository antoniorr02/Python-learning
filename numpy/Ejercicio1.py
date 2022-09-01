import numpy as np

def pares(inicio, fin):
    lista = []
    for i in range(inicio, fin):
        if(i%2 == 0):
            lista.append(i)
    array = np.array(lista)
    return array

# Otra resolucion
def pares2(inicio, fin):
    if (inicio % 2 == 0):
        array = np.arange(inicio, fin, 2)
    else:
        array = np.arange(inicio+1, fin, 2)
    return array

print(pares(10,20))
print(pares2(10,20))