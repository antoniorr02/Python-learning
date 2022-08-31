import pickle

frutas = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}

print("Introduzca el nomnbre del fichero")
nombre = input()

fichero = open(nombre, "wb")

pickle.dump(frutas, fichero)

fichero.close()

fichero = open(nombre, "rb")

texto = pickle.load(fichero)

print(texto)
print(texto.values())

fichero.close()