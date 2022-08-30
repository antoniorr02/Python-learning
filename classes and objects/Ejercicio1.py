from select import select


class Coche:
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrarCaracteristicas(self):
        print(f"El coche es de la marca {self.marca} de color {self.color} de {self.combustible} con una cilindrada de {self.cilindrada}")

coche1 = Coche("Opel", "rojo", "gasolina", "1.6")
coche1.mostrarCaracteristicas()