from operator import truediv


def positivo(num):
    if (num >= 0):
        return True
    else:
        return False

numeros = [4,-2,8,-3,-5,-7,1,9]
filtro = filter(positivo, numeros)
resultado = list(filtro)
print(resultado)