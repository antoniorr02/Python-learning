print("Introducir calificaciones")
nota1 = input()
nota2 = input()
nota3 = input()
nota_media = (int(nota1) + int(nota2) + int(nota3))/3
if (nota_media >= 5): 
    nota_final = "aprobado"
else:
    nota_final = "suspenso"

print(f"La nota media es de: {nota_media} --> {nota_final}")