media = lambda num1 , num2, num3: (num1 + num2 + num3)/3
print ("Introduzca 3 numeros para calcular su media")
num1 = input()
num2 = input()
num3 = input()
print(f"La media con la funcion lambda da: {media(int(num1),int(num2),int(num3))}")