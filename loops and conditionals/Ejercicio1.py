diccionario = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}
print(f"La traducción de la palabra naranja es: {diccionario['naranja']}")
diccionario["pera"] = "pear"
for i,j in diccionario.items():
    print(f"{i} es inglés es {j}")