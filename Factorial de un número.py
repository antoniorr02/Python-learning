
from unittest import result


def factorial(valor):
	producto=1
	for valor in range(1,valor+1):
		producto*=valor
	return(producto)

print("Introduzca el numero al que calcular el factorial")
valor = input()
print(f"Resultado funcion: {factorial(int(valor))}")
