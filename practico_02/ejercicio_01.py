# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):

        self.base=base
        self.altura=altura

        pass

    def area(self):
        return self.base*self.altura

        pass

re=Rectangulo(4,2)

print('El area del rectangulo es:',re.area())
assert re.area()==8
