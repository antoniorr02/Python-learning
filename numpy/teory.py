#Creacion de arrays (pip install numpy)
import numpy as np
array = np.array(([1,2,3],[4,5,6],[7,8,9]))
ejemplo = np.arange(15).reshape((3,5))
print(array)
print(ejemplo)
print(np.zeros(4))
print(np.ones(4))
print(np.arange(5))
print(np.arange(1,11))
print(np.arange(2,20,3))

lista = [1,2,3,4,5]
lista1 = [6,7,8,9,10]
array1 = np.array(lista)
print(array1)
array1 += 4 #Operaciones con arrays
print(f"\nArray tras operacion:\n {array1}\n")
print(f"Parte indexada de array1:\n {array1[1:3]}\n")
array_copia = array1.copy()

lista_doble = (lista,lista1)
array2 = np.array(lista_doble)
print(f"Array doble:\n {array2}")
print(f"Primera fila: {array2[0]}\nPrimer elemento: {array2[0][0]}")
print(array2.shape)
print(f"{array2.dtype} \n")

traspuesta = array2.T
print(f"La matriz traspuesta del array2 queda como:\n {traspuesta}\n")

#Entrada y salida con arrays
np.save('array1s', array1)
np.load('array1s.npy')

np.savez('arrays', x=array, y=array1)
recuperado = np.load('arrays.npz')
print(f"El primer array recuperado es:\n {recuperado['x']}")
print(f"El segundo array recuperado es:\n {recuperado['y']}\n")

np.savetxt('array.txt', array2, delimiter=',')
np.loadtxt('./array.txt', delimiter=',')

#Funciones con arrays

print(f"Raiz cuadrada de array: {np.sqrt(array)}\n")
print(np.random.rand(5)) 
print("\n")

operando1 = np.array(([1,2,3]))
operando2 = np.array(([2,3,4]))
print(f"Suma de arrays: {np.add(operando1, operando2)}")
print(f"Eleccion de elemento mayor: {np.maximum(operando1, operando2)}")