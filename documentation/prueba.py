#Generate documentation in terminal --> pydoc <path>
#Generate documentation in html --> pydoc -w <path>

class Saludos():
    """
    Esta es la documentacion de la clase saludos
    Tendra dos funciones saludo y despedida
    y ambas necesitaran como parametro el nombre de una persona.
    """
    def saludo(nombre):
        """Sirve  para saludar a un nombre pasado como parametro"""
        print("Buenos dias " + nombre)
    
    def despedida(nombre):
        """Sirve  para decir adios a un nombre pasado como parametro"""
        print("Adios " + nombre)