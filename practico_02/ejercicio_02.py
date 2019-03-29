# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.


import math

class Circulo:

    def __init__(self, radio):
        self.r=radio

    def area(self):
        return round(math.pi*(self.r)**2)

    def perimetro(self):
        return round(2*(self.r)*math.pi)


c = Circulo(10)

assert c.area() == 314
assert c.perimetro() == 63
