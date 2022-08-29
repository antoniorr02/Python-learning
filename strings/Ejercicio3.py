from unicodedata import numeric


print("Introduce the first number")
dato1 = input()
print("Introduce the second number")
dato2 = input()
numero1 = int(dato1)
numero2 = int(dato2)
suma = numero1 + numero2
strSuma = str(suma)
resultado = "La suma es " + strSuma
print(resultado)