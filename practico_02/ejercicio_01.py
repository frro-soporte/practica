''' Implementar la clase Rectangulo que contiene una base y una altura, y el método area.'''


class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        a = self.base*self.altura
        return a



algo = Rectangulo (5,6)

assert (algo.area()==30)

