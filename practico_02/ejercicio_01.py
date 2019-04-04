# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura

    def area(self):
        area = self.base*self.altura
        print(area)
        return area

a=Rectangulo(2, 5)
a.area()

assert(a.area() == 10)
