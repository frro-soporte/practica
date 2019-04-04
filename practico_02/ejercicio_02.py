# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

import math

class Circulo:


    def __init__(self, radio):
        self.r = radio

    def area(self):
        a = self.r

    def perimetro(self):
        per = (self.r * math.pi)/2
        return per

a = Circulo(5)
assert (a.perimetro() == 7.853981633974483)


