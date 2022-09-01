from audioop import mul


def multiplicar(num):
    return num * 2

lista = [2,4,6]

mapeo = map(multiplicar, lista)
resultado = list(mapeo)
print(resultado)

lista_resultado = list(map(lambda numero: numero * 2, lista))
print(lista_resultado)