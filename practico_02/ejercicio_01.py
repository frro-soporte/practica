# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):

        self.base=base
        self.altura=base

        pass

    def area(self):
        return self.base*self.altura

        pass

re=Rectangulo(1.2,3)

print(re.area())