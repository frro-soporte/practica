# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return "('El area del rectangulo es '{0})".format(self.base * self.altura)


base = input('Ingresar base')
try:
    bas = int(base)
    altura = input('Ingresar altura')
    try:
        alt = int(altura)
        resultado = Rectangulo(bas,alt)
        area = resultado.area()
        print(area)
    except ValueError:
        print('No ingreso correctamente')

except ValueError:
    print('No ingreso correctamente')



