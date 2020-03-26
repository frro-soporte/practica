# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base*self.altura)

assert Rectangulo(4,5).area() == 20
