# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        self.area = self.base * self.altura
        print(self.area)
        return self.area



x = Rectangulo(2,2)
x.area()

assert x.area == 4