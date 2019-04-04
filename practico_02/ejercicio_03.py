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

import random

class Persona:


    def __init__(self, nombre, edad, sexo, peso, altura):

        self.nom = nombre
        self.age = edad
        self.sex = sexo
        self.peso = peso
        self.alt = altura
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        if self.age >= 18:
            return True
        else:
            return False


    def generar_dni(self):
        return random.randint(00000000, 99999999)

    def print_data(self):
        print(' Nombre:' ,self.nom, '\n',
              'Edad>>', self.age, '\n',
              'Sexo>>', self.sex, '\n',
              'Peso>>', self.peso, '\n',
              'Altura>>', self.alt, '\n'
              ' DNI>>>', self.dni, '\n')


p = Persona('Juan', 23, 'Masculino', 66, 1.64)

p.print_data()
print('Es Mayor de esad: ', p.es_mayor_edad())

