import moduloficheros

print("Introduzca el nomnbre del fichero")
nombre = input()
fichero = moduloficheros.Fichero(nombre)

texto = "Hola mundo!\n"

fichero.grabarFichero(texto)
fichero.incluirFichero(texto)
print(fichero.leerFichero())