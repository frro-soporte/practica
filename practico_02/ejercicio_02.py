# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
from math import  pi

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return (pi * self.radio ** 2  )

    def perimetro(self):
        return (self.radio * 2 * pi)

cir = Circulo(5)
print(cir.area())
print(cir.perimetro())