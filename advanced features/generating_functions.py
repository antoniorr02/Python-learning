range(0,11)

def pares(maximo):
    for numero in range(maximo):
        if (numero % 2 == 0):
            yield numero

maximo = 11
for numero in pares(maximo):
    print(numero)