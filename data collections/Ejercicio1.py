lista = [1,2,5,25,33,75,21,56,89,43,13,62,24]
dato = input()
if (int(dato) in lista):
    print(f"Lista contains {int(dato)}")
else:
    print(f"Lista doesn't contain {int(dato)}")