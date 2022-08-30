minimo = 20
maximo = 500
dato = input()
numero = int(dato)
if (numero < minimo):
    print("low value")
else: 
    if(numero > maximo):
        print("high value")
    else:
        print("middle value")