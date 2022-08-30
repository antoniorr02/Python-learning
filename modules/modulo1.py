class Coche:
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrarCaracteristicas(self):
        print(f"El coche es de la marca {self.marca} de color {self.color} de {self.combustible} con una cilindrada de {self.cilindrada}")

media = lambda num1 , num2, num3: (num1 + num2 + num3)/3