# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

import math

class Circulo:


    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area = math.pi*self.radio*self.radio
        print(area)
        return area

    def perimetro(self):
        perimetro = math.pi*self.radio
        print(perimetro)
        return perimetro

a=Circulo(5)
a.area()
a.perimetro()
