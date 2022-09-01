#python3 doctest.py -v --> Pruebas desde documentacion

def sumar(num1, num2):
    """
    Funcion que suma dos numeros pasados por parametro

    >>> sumar(4,3)
    7

    >>> sumar(8,5)
    11

    """
    return num1 + num2

print(sumar(5,6))

import doctest
doctest.testmod()