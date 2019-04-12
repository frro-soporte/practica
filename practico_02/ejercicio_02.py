# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
from math import pi

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        self.area = round(((pi * self.radio)**2),2) 
        return self.area

    def perimetro(self):
        self.perimetro = round(2*pi*self.radio,2)
        return self.perimetro

c = Circulo(2)
print(c.area(), '\n', c.perimetro())

assert c.area == 39.48
assert c.perimetro == 12.57
