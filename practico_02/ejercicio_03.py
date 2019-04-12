# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.

from random import randrange

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        self.dni = randrange(10000000, 99999999)
        return self.dni

    def print_data(self):
        print(self.nombre, self.edad, self.sexo, self.dni, self.altura, self.peso)

x = Persona('juan', 21, 'M', 80, 180)
x.print_data()
x.es_mayor_edad()

assert x.nombre == 'juan'
assert x.edad == 21
assert x.sexo == 'M'
assert x.peso == 80
assert x.altura == 180
