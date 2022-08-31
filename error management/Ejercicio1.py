from importlib.abc import SourceLoader


def operacion(num1, num2, num3):
    try:
        solucion = num1 / (num2 - num3)
        print(f"La solución es: {solucion}")
    except: 
        print("Se ha producido un error en la operacion")
    else:
        print("La operacion se completo correctamente")
    finally:
        print("Final de prueba de gestion de errores\n")

operacion(5,4,2)
operacion(6,3,3)