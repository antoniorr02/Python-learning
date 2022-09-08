lado = input("¿Hacia que lado desea avanzar? ")
if (lado.lower() != 'derecha'):
    print("Mala eleccion, perdiste")
    exit()

accion = input("¿Prefiere nadar o esperar? ")
if (accion.lower() != 'esperar'):
    print("Mala eleccion, perdiste")
    exit()

color = input("Elija un color entre: verde, rojo y azul ")
if (color.lower() != 'verde'):
    print("Mala eleccion, perdiste")
    exit()

print("Has ganado")