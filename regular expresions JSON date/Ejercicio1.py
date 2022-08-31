import re

def buscar(texto, palabra):
    resultado = re.search(palabra, texto)
    if (resultado):
        print(f"La palabra se encuentra entre las posiciones {resultado.span()}")
        print(f"La palabra se encuentra entre las posiciones {resultado.start()} y {resultado.end()}")

    else:
        print("Palabra no encontrada")

texto = "Esto es una frase de pruebas para hacer busquedas"
palabra = "frase"

buscar(texto, palabra)