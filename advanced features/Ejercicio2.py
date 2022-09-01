from traceback import print_tb


numeros = [1,2,3,4,5,6,7,8,9,10]

def pares(numero):
    if(numero % 2 == 0):
        return True
    else:
        return False

filtrado = filter(pares, numeros)
print(list(filtrado))