import re
from typing import Reversible


cadena = "Esto es un texto de ejemplo"
longitud = len(cadena)
print(f"La logitud del string es: {longitud}")

strlongitud = str(longitud)
mayuscula = cadena.upper()
print(mayuscula)

resultado = mayuscula + " tiene longitud de " + strlongitud
print(resultado)