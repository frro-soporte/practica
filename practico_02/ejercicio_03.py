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


import random


class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.n = nombre
        self.e = edad
        self.s = sexo
        self.p = peso
        self.a = altura
        self.d = self.generar_dni()

    def es_mayor_edad(self):
        if self.e >= 18:
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        dni = random.randint(1000000, 50000000)
        return dni

    def print_data(self):
        print("Nombre:", self.n)
        print("DNI:", self.d)
        print("Edad:", self.e)
        print("Sexo:", self.s)
        print("Peso:", self.p,"Kg")
        print("Altura:", self.a,"m")


p = Persona("Fulanito", 19, 'H', 64.3, 1.72)
assert p.es_mayor_edad() is True
p.print_data()
