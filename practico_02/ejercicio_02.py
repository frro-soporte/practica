# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area = round(math.pi * pow(self.radio,2),2)
        return area

    def perimetro(self):
        perimetro = round(2*math.pi*self.radio,2)
        return perimetro


circulo =Circulo(2)

assert(circulo.area())== 12.57;
assert(circulo.perimetro())==12.57;